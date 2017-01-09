import sys

from .utils import read_iterm_color_scheme


KEY_MAP = {
    'Ansi 0 Color': [6],
    'Ansi 1 Color': [8],
    'Ansi 2 Color': [10],
    'Ansi 3 Color': [12],
    'Ansi 4 Color': [14],
    'Ansi 5 Color': [16],
    'Ansi 6 Color': [18],
    'Ansi 7 Color': [20],
    'Ansi 8 Color': [7],
    'Ansi 9 Color': [9],
    'Ansi 10 Color': [11],
    'Ansi 11 Color': [13],
    'Ansi 12 Color': [15],
    'Ansi 13 Color': [17],
    'Ansi 14 Color': [19],
    'Ansi 15 Color': [21],
    'Background Color': [2, 3],
    'Bold Color': [1],
    'Cursor Color': [5],
    'Cursor Text Color': [4],
    'Foreground Color': [0],
}


def main(in_file, out_file):
    scheme = read_iterm_color_scheme(in_file)

    out_file.write('Windows Registry Editor Version 5.00\n\n')
    out_file.write('[HKEY_CURRENT_USER\SOFTWARE\SimonTatham\PuTTY\Sessions\<session name>]\n')

    for k, v in scheme.items():
        numbers = KEY_MAP.get(k, None)

        if numbers:
            for n in numbers:
                out_file.write('"Colour{n}"="{r},{g},{b}"\n'.format(
                    n=n,
                    r=v['Red Component'],
                    g=v['Green Component'],
                    b=v['Blue Component'],
                ))


if __name__ == '__main__':
    main(sys.stdin, sys.stdout)
