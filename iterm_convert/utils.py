from decimal import Decimal

from lxml import etree


def convert_to_byte(v):
    return int(round(255 * Decimal(v)))


def convert_to_hex(v):
    return hex(v)[2:]


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
