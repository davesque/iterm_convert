from collections import OrderedDict
from decimal import Decimal

from lxml import etree
import yaml


def convert_to_byte(v):
    return int(round(255 * Decimal(v)))


def convert_to_hex(v):
    return hex(v)[2:]


def scheme_color_to_hex(v):
    return '{0}{1}{2}'.format(
        convert_to_hex(v['Red Component']),
        convert_to_hex(v['Green Component']),
        convert_to_hex(v['Blue Component']),
    )


def read_iterm_color_scheme(f):
    tree = etree.HTML(f.read())

    colour_name_els = tree.cssselect('plist > dict > key')

    entries = {}

    for colour_name_el in colour_name_els:
        entries[colour_name_el.text] = {}

        colour_value_els = colour_name_el.getnext().cssselect('key')

        for colour_value_el in colour_value_els:
            value = convert_to_byte(colour_value_el.getnext().text)
            entries[colour_name_el.text][colour_value_el.text] = value

    return entries


def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict, **kwargs):
    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))

    OrderedLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)

    return yaml.load(stream, OrderedLoader, **kwargs)


def ordered_dump(data, stream=None, Dumper=yaml.Dumper, **kwargs):
    class OrderedDumper(Dumper):
        pass

    def dict_representer(dumper, data):
        return dumper.represent_mapping(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, data.items())

    OrderedDumper.add_representer(OrderedDict, dict_representer)

    return yaml.dump(data, stream, OrderedDumper, **kwargs)
