import glob
import os
from shutil import copy2
from PIL import Image


class FindFiles():
    def findFiles(self, searchpath:str, searchstring="*", filetype="*"):
        """
        find files of a specific filetype in the given searchpath
        :param searchpath: str path where the program should look for files
        :param searchstring: specify a searchstring want to look for ("*3840x2160*", "*clean"...)
        :param filetype: specify a type you want to look for ("zip"/"jpg"...)
        :return: list of filepaths
        """
        return glob.glob(searchpath + searchstring + "." + filetype,recursive=False)


    def convert_bytes(self, num):
        """
        this function will convert bytes to MB.... GB... etc
        """
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0

    def getFileSize(self, file_path):
        """
        this function will return the file size
        """
        if os.path.isfile(file_path):
            file_info = os.stat(file_path)
            return file_info.st_size

    def getLastModifiedDate(self, path):
        """
        this function returns the Last Modified date for the given filepath
        """
        return os.stat(path)[8]

    def copyfiles2folder(self, files:[], destination:str):
        """
        copies all given files to another folder
        :param files: list of files you want to copy
        :param destination: folder as string where you want the files copied to
        :return:
        """
        for file in files:
            print('copying ' + file)
            copy2(file, destination)

    def get_image_size(self, path)->(int, int):
        """
        returns the width and height of a given image
        """
        with Image.open(path) as img:
            width, height = img.size
        return width, height