from decimal import Decimal
import sys

from lxml import etree


def convert_to_byte(v):
    return int(round(255 * Decimal(v)))


def convert_to_hex(v):
    return hex(v)[2:]


KEY_MAP = {
  'Ansi 0 Color': ['ColorTable00'],
  'Ansi 1 Color': ['ColorTable04'],
  'Ansi 2 Color': ['ColorTable02'],
  'Ansi 3 Color': ['ColorTable06'],
  'Ansi 4 Color': ['ColorTable01'],
  'Ansi 5 Color': ['ColorTable05'],
  'Ansi 6 Color': ['ColorTable03'],
  'Ansi 7 Color': ['ColorTable07'],
  'Ansi 8 Color': ['ColorTable08'],
  'Ansi 9 Color': ['ColorTable12'],
  'Ansi 10 Color': ['ColorTable10'],
  'Ansi 11 Color': ['ColorTable14'],
  'Ansi 12 Color': ['ColorTable09'],
  'Ansi 13 Color': ['ColorTable13'],
  'Ansi 14 Color': ['ColorTable11'],
  'Ansi 15 Color': ['ColorTable15'],
  # 'Background Color': ['ColorTable02','ColorTable03'],
  # 'Bold Color': ['ColorTable01'],
  # 'Cursor Color': ['ColorTable05'],
  # 'Cursor Text Color': ['ColorTable04'],
  # 'Foreground Color': ['ColorTable00'],
}


def main(in_file, out_file):
    tree = etree.HTML(in_file.read())

    colour_name_els = tree.cssselect('plist > dict > key')

    entries = {}

    for colour_name_el in colour_name_els:
        entries[colour_name_el.text] = {}

        colour_value_els = colour_name_el.getnext().cssselect('key')

        for colour_value_el in colour_value_els:
            value = convert_to_byte(colour_value_el.getnext().text)
            entries[colour_name_el.text][colour_value_el.text] = value

    out_file.write('Windows Registry Editor Version 5.00\n\n')
    out_file.write('[HKEY_CURRENT_USER\Console]\n')

    for iterm_key, v in entries.items():
        console_keys = KEY_MAP.get(iterm_key, None)

        if console_keys:
            for key in console_keys:
                out_file.write('"{key}"=dword:{b}{g}{r}\n'.format(
                    key=key,
                    r=convert_to_hex(v['Red Component']),
                    g=convert_to_hex(v['Green Component']),
                    b=convert_to_hex(v['Blue Component']),
                ))


if __name__ == '__main__':
    main(sys.stdin, sys.stdout)
