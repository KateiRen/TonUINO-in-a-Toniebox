# TonUINO-in-a-Toniebox

A little description of how I married [TonUINO](https://www.tonuino.de/) with [Toniebox](https://tonies.de/toniebox/)

## Some words on the project itself

[https://kateiren.github.io/TonUINO-in-a-Toniebox/](https://kateiren.github.io/TonUINO-in-a-Toniebox/)

## Get used with the minimalistic SD Card file naming

The DFMini Player has some restrictions on how to name folders (two digit numbers from 01 to 99) and audio files (001.mp3 to 255.mp3). Therefore moving files to the SD card means creating the next numbered folder as well as renaming every single audio file to be transferred.

To ease the process I created two simple Python scripts:
- [transfer.py](https://github.com/KateiRen/TonUINO-in-a-Toniebox/blob/main/src/transfer.py) - copy a folder of MP3 files to the SD card and take care of all renaming
- [listContent.py](https://github.com/KateiRen/TonUINO-in-a-Toniebox/blob/main/src/listContent.py) - use embedded MP3 tags to display meaningful information for the SD card content, optionally create a csv file

 Or as an alternative - Jupyter Notebooks:
- [Transfer mp3 folder.ipynb](https://github.com/KateiRen/TonUINO-in-a-Toniebox/blob/main/src/Transfer%20mp3%20folder.ipynb)
- tbd

## Print your RFID labels

After countless less-than-ideal prints I created this template using [Inkscape](https://inkscape.org/).

A small guidance is included in the file itself. Make sure to open with [Inkscape](https://inkscape.org/) and not your browser.
