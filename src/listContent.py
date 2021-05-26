import sys
import os
import eyed3
import csv
from transfer import isValidMP3Folder # same routines as used in the transfer script
from transfer import isValidMP3File   # same routines as used in the transfer script


def listMetaData(mp3Path, writer = False):
    for entry in os.scandir(mp3Path):
        if entry.is_dir() and isValidMP3Folder(entry.name):
            for song in os.scandir(mp3Path+"/"+entry.name):
                if isValidMP3File(song.name):
                    audiofile = eyed3.load(mp3Path+"/"+entry.name+"/"+song.name)
                    print(mp3Path + "/" + entry.name + "/" + song.name + ": " + audiofile.tag.title + ", " + audiofile.tag.artist + ", " + audiofile.tag.album) 
                    if writer:
                        writer.writerow([mp3Path + "/" + entry.name + "/" + song.name , audiofile.tag.title, audiofile.tag.artist, audiofile.tag.album])


if __name__ == "__main__":
    if len(sys.argv) == 1 or len(sys.argv) > 3: # Wrong number of arguments
        print("\nUsage:")
        print("listContent.py <path of the SD card>")
        print("- or -")
        print("listContent.py <path of the SD card> <filename of the output csv>")

    elif len(sys.argv) == 2: # just list content
        listMetaData(sys.argv[1])

    else: # list content and write to csv file
        with open(sys.argv[2], "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["File", "Song Title", "Artist", "Album"])
            listMetaData(sys.argv[1], writer)