###### This script just deletes old files in a directory
import os
import glob
photosPath = '~/Photos'
numberOfPhotosToKeep = 60


files = filter(os.path.isfile, glob.glob(photosPath + "*"))
files.sort(key=lambda x: os.path.getmtime(x))
if len(files) > numberOfPhotosToKeep:
    for inum,i in enumerate(files):
        if inum > len(files)-numberOfPhotosToKeep:
            break
        else:
            os.remove(i)


