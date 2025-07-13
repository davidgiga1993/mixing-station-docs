"""
Generates the "compatible mixer" table
"""

import json
import logging
import re
from typing import Generator, Dict

log = logging.getLogger('mkdocs')


class Versions:
    path = r"versions.json"

    def __init__(self):
        self._data = {}
        with open(self.path) as f:
            self._data = json.load(f)

    def get_all_mixer_series(self) -> Generator[any, None, None]:
        # Sort by manu name
        manus = self._data["manufacturers"]
        manus.sort(key=lambda manu: manu["name"])
        for manu in manus:
            series = manu["series"]
            # Sort series by name
            series.sort(key=lambda manu: manu["name"])
            yield series, manu

    def get_mixer_series(self, console_id: int):
        for manu in self._data["manufacturers"]:
            for series in manu["series"]:
                if series["consoleId"] != console_id:
                    continue
                return series, manu

        return None


TAG_FIRMWARE = "mixer_fw"
TAG_SERIES = "mixer_series"
TAG_MIXER_TABLE = "mixer_table"
TAG_NOTES = "notes"


class MixerGenerator:
    headers = ["Model", "Supported Firmware"]

    def __init__(self):
        self.versions: Versions = Versions()
        self.notes: Dict[int, str] = {}

    def process(self, markdown: str) -> str:
        notes_pattern = r"\{" + TAG_NOTES + r":(\d+):.+?}(.+)"
        for match in re.findall(notes_pattern, markdown):
            console_id = int(match[0])
            note = match[1]
            self.notes[console_id] = note
        markdown = re.sub(notes_pattern, "", markdown)

        for unused in self.find_tags(TAG_MIXER_TABLE, markdown):
            content = "| Mixers | Supported Firmware | Notes\n| --- | --- | --- |\n"
            for all_series, manu in self.versions.get_all_mixer_series():
                for series in all_series:
                    console_id = series["consoleId"]
                    content += "| " + self.get_series_content(console_id)
                    content += " | " + self.get_firmware_content(console_id);
                    content += " | " + self.notes.get(console_id, "") + " |\n"
            markdown = self.replace_tag(TAG_MIXER_TABLE, unused, markdown, content)

        for console_id in self.find_tags(TAG_SERIES, markdown):
            content = self.get_series_content(console_id)
            markdown = self.replace_tag(TAG_SERIES, console_id, markdown, content)

        for console_id in self.find_tags(TAG_FIRMWARE, markdown):
            content = self.get_firmware_content(console_id)
            markdown = self.replace_tag(TAG_FIRMWARE, console_id, markdown, content)
        return markdown

    def find_tags(self, tag: str, text: str) -> Generator[int, None, None]:
        matches = re.findall(r'\{' + tag + r':(\d+)}', text)
        for match in matches:
            console_id = int(match)
            yield console_id

    def replace_tag(self, tag: str, console_id: int, text: str, new_content: str) -> str:
        return text.replace("{" + tag + ":" + str(console_id) + "}", new_content)

    def get_series_content(self, console_id: int) -> str:
        series, manu = self.versions.get_mixer_series(console_id)
        return manu["name"] + " " + series["name"]

    def get_firmware_content(self, console_id: int) -> str:
        content = ""
        series, manu = self.versions.get_mixer_series(console_id)
        for console in series["consoles"]:
            oldest = "V" + console["oldest"]
            newest = "V" + console["newest"]
            if oldest == newest:
                firmware = newest
            else:
                firmware = oldest + "-" + newest

            for model in console["models"]:
                content += f"{model}: `{firmware}`<br>"
        return content


generator = MixerGenerator()


def on_page_markdown(markdown, **kwargs):
    return generator.process(markdown)
