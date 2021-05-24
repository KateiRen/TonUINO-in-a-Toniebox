import sys
import os
import shutil

def isValidMP3Folder(name):
    #name = name[:2] # DFPlayer
    if len(str(name))>2:
        print("Folder name should be a two digit number")
        return False
    try:
        number = int(name)
        return True
    except:
        print("Folder name could not be matched to a two digit number")
        return False

def isValidMP3File(name):
    if name[-4:] != ".mp3":
        return False
    name = name[:3] # if naming with appended song title is used
    try:
        number = int(name)
        return True
    except:
        return False


def prepareFolder(destinationPath):
    # find biggest numbered mp3 folder name
    number  = 0
    for entry in os.scandir(destinationPath):
        if entry.is_dir() and isValidMP3Folder(entry.name):
            if int(entry.name) > number:
                number = int(entry.name)
    if number == 0:
        print("\nNo msic folder (two digit number) found.")    
    else:
        print("\nHighest music folder found: {0:02d}".format(number))
    number += 1

    # create new folder
    destinationDirectory = destinationPath+"/"+"{0:02d}".format(number)
    os.mkdir(destinationDirectory)
    print("Created new folder: " + destinationDirectory + "\n")
    return destinationDirectory


def getName(item):
    return item.name.upper() # alles in Großbuchtstaben wandeln


def transferFiles(sourcePath, destinationDirectory):
    # collect mp3 files and sort
    mp3files = []
    for mp3 in os.scandir(sourcePath):
        if mp3.name[-4:] == ".mp3":
            mp3files.append(mp3)        

    mp3files.sort(key = getName)

    # copy mp3 files and rename as three digit number
    number = 1 # start with 001.mp3
    for mp3 in mp3files:
        shutil.copy(sourcePath + "/" + mp3.name, destinationDirectory + "/{0:03d}.mp3".format(number))
        print("Copied " + sourcePath + "/" + mp3.name)
        print("To " + destinationDirectory + "/{0:03d}.mp3".format(number)+"\n")
        number += 1    


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: transfer.py <source folder of mp3 files> <destination path of the SD card>")
    else:
        transferFiles(sys.argv[1], prepareFolder(sys.argv[2]))
