# fcrawler

## Installation

You can use pip:

``` console
~$ pip3 install fcrawler
```

This is a Python based application that can be used to copy files of a given file type from a folder directory.

## Option 1 - Copy files from a directory to another

![Option 1](https://i.imgur.com/vr0JxTy.gif)

This creates subfolders in the destination folder as the original folder subfolders.

(This only creates sub-folders containing the files you have entered)

## Option 2 - Copy files from a directory to another (without creating subfolders)

![Option 2](https://i.imgur.com/CrDDpNX.gif)

This will copy files from the original folder to the destination folder without creating subfolders. If it contains a large number of files, the destination folder may be cluttered.

## Option 3 - Copy files using a filelist

You can use a file list file to copy files. The list must be a txt file type.

Example - filelist.txt

``` txt
C:\testing\source\file.mp4
C:\testing\source\file2.mp4
C:\testing\source\file3.mp4
C:\testing\source\subfolder1\file4.mp4
C:\testing\source\subfolder1\file5.mp4
C:\testing\source\subfolder2\file6.mp4
```

## Option 4 - Create filelist
If you want to make a list of files, use this method. Then you can use that file from the 3rd option.

This will help you to skip unnecessary files. But how?

You can open and edit the text file. Just remove the unnecessary file paths from the text file. then use it.
