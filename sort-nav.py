import ruamel.yaml
from ruamel.yaml import CommentedMap, CommentedSeq


def get_nav_item(root_nav, name: str) -> CommentedMap:
    for elem in root_nav:
        key, path = next(iter(elem.items()))
        if name == key:
            return elem
    raise KeyError(f'Could not find {name}')


def sort_nav_items(nav: CommentedMap):
    # The first item might be a plain string (section index)
    # in which case we simply remove and insert it back again
    items: CommentedSeq = next(iter(nav.values()))
    if len(items) == 0:
        return items
    section_index = None
    if isinstance(items[0], str):
        section_index = items.pop(0)
    items.sort(key=lambda x: next(iter(x.keys())))
    if section_index is not None:
        items.insert(0, section_index)
    return items


def main():
    nav_to_be_sorted = ['Features', 'Platforms', 'Mixer specifics']

    yaml = ruamel.yaml.YAML()
    yaml.indent(mapping=2, sequence=4, offset=2)
    yaml.preserve_quotes = True
    with open('mkdocs.yml') as f:
        mkdocs = yaml.load(f)
    root_nav = mkdocs['nav']
    for nav_name in nav_to_be_sorted:
        nav = get_nav_item(root_nav, nav_name)
        sort_nav_items(nav)

    with open('mkdocs.yml', 'w') as f:
        yaml.dump(mkdocs, f)


if __name__ == '__main__':
    main()
