# TonUINO-in-a-Toniebox

A little description of how I married [TonUINO](https://www.tonuino.de/) with [Toniebox](https://tonies.de/toniebox/)

## Some words on the project

[https://kateiren.github.io/TonUINO-in-a-Toniebox/](https://kateiren.github.io/TonUINO-in-a-Toniebox/)

## Some code to help get going with the minimalistic SD Card file naming

The DFMini Player has some restrictions on how to name folders (two digit numbers from 01 to 99) and audio files (001.mp3 to 255.mp3). Therefore moving files to the SD card means creating the next numbered folder as well as renaming every single audio file to be transferred.

To ease the process I created a simple script and Jupyter Notebook:
- [transfer.py](https://github.com/KateiRen/TonUINO-in-a-Toniebox/blob/main/src/transfer.py)
- [Transfer mp3 folder.ipynb](https://github.com/KateiRen/TonUINO-in-a-Toniebox/blob/main/src/Transfer%20mp3%20folder.ipynb)
