import sys

from .utils import ordered_load, ordered_dump, read_iterm_color_scheme, scheme_color_to_hex


KEY_MAP = {
    'colors.normal.black': 'Ansi 0 Color',
    'colors.normal.red': 'Ansi 1 Color',
    'colors.normal.green': 'Ansi 2 Color',
    'colors.normal.yellow': 'Ansi 3 Color',
    'colors.normal.blue': 'Ansi 4 Color',
    'colors.normal.magenta': 'Ansi 5 Color',
    'colors.normal.cyan': 'Ansi 6 Color',
    'colors.normal.white': 'Ansi 7 Color',
    'colors.bright.black': 'Ansi 8 Color',
    'colors.bright.red': 'Ansi 9 Color',
    'colors.bright.green': 'Ansi 10 Color',
    'colors.bright.yellow': 'Ansi 11 Color',
    'colors.bright.blue': 'Ansi 12 Color',
    'colors.bright.magenta': 'Ansi 13 Color',
    'colors.bright.cyan': 'Ansi 14 Color',
    'colors.bright.white': 'Ansi 15 Color',
    'colors.primary.background': 'Background Color',
    'colors.primary.foreground': 'Foreground Color',
}


TEMPLATE = """
colors:
  primary:
    background: '0x000000'
    foreground: '0x000000'

  normal:
    black:   '0x000000'
    red:     '0x000000'
    green:   '0x000000'
    yellow:  '0x000000'
    blue:    '0x000000'
    magenta: '0x000000'
    cyan:    '0x000000'
    white:   '0x000000'

  bright:
    black:   '0x000000'
    red:     '0x000000'
    green:   '0x000000'
    yellow:  '0x000000'
    blue:    '0x000000'
    magenta: '0x000000'
    cyan:    '0x000000'
    white:   '0x000000'
"""


def main(in_file, out_file):
    scheme = read_iterm_color_scheme(in_file)

    obj = ordered_load(TEMPLATE)

    for category in obj['colors'].keys():
        for color in obj['colors'][category].keys():
            key = KEY_MAP['colors.{0}.{1}'.format(category, color)]
            hex_value = scheme_color_to_hex(scheme[key])

            obj['colors'][category][color] = '0x{0}'.format(hex_value)

    ordered_dump(obj, out_file, default_flow_style=False)


if __name__ == '__main__':
    main(sys.stdin, sys.stdout)
