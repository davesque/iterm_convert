# iTerm-convert

Tools for converting iTerm XML color schemes to color scheme formats for the
following terminal emulators:

* Alacritty
* PuTTY
* Windows console

## Example usage

```bash
python setup.py install

python -m iterm_convert.alacritty < hybrid.itermcolors > alacritty.yml

python -m iterm_convert.putty < hybrid.itermcolors > hybrid-putty.reg

python -m iterm_convert.windows_console < hybrid.itermcolors > hybrid-console.reg
```
