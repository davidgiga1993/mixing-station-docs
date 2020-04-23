# Settings
This page explains how the app stores settings.

There are 4 different settings categories: Globa, Series, Session and user settings.

## Global settings
These settings apply to the whole app. On android these settigns apply to all app instances.

- Update branch
- UI scale
- Network interface settings

## Console model settings
These settings apply to the currently selected mixer series.

- Restricted access config
- Last IP address and mix access


## Session settings
These settings are saved when starting / closing the app and are stored for each mixer model separatly.

- All app UI / UX related configuration
- Mutegroup names

## User settings
These settings are only saved if `Autosave` is enabled or the user saves the settings manualy.

- [Layer](../layers.md)
- [Layouts](../custom-layouts.md)
- [Midi](../usb-midi.md)

To manualy save the settings open:
```
Menu -> Setup -> App -> Folder icon
```
or
```
Menu -> Setup -> Layer -> Folder icon
```
or
```
Menu -> Setup -> Layout -> Folder icon
```

![Settings-Manager](../img/settings-manager.png)

Use the scope buttons to select which settings should be saved or loaded.
Press and hold an entry to open a context menu.

### Export / Import settings
You can export `User settings` by opening the context menu and selecting `Share`.
Depending on the platform, multiple share options are available.
For importing you can use the arrow menu button or select the file you want to import in a file explorer and open it with mixing station.
