from .FindFiles import FindFiles
import pandas as pd

class FileFinderUsage():
    """
    this is a class with Usage Examples for the FileFinder Module
    Use it for reference
    """
    def __init__(self):
        self.ff = FindFiles()

    def findHorizontalArtworks(self):
        """
        finds artworks with size 3840x2160px in a searchpath, copies them to a destination folder and prints the name
        and resolution of these files to the console
        :return:
        """
        searchpath = "G:\\Digitale Distribution\\10_PLATTFORMEN\\00_Grafik\\*\\*\\"
        destination = 'G:\\Digitale Distribution\\10_PLATTFORMEN\\00_Grafik\\__iTunes_Querartworks\\'

        pathlist = self.ff.findFiles(searchpath=searchpath, searchstring="*3840x2160*", filetype="png")

        self.ff.copyfiles2folder(pathlist, destination)

        for file in pathlist:
            width, height = self.ff.get_image_size(file)
            print(file + ": Resolution: " + str(width) + "x" + str(height))


    def findZipFiles(self):
        """
        finds zip-Files, saves the paths, filesizes and lastModifiedDates to a csv file
        :return:
        """
        fileList = self.ff.findFiles(searchpath="G:\\Digitale Distribution\\10_PLATTFORMEN\\00_Grafik\\*\\",
                                      filetype="zip")
        filesizes = []
        lastModifiedDate = []
        sizeOfAllFiles = 0
        
        for file in fileList:
            filesizes.append(self.ff.getFileSize(file))
            lastModifiedDate.append(self.ff.getLastModifiedDate(file))

        df = pd.DataFrame(data={"path": fileList, "filesize": filesizes, "lastModifiedDate": lastModifiedDate})
        df.to_csv("./filesizes.csv", sep=',', index=True)

        print("Number of zip-files: " + len(filesizes))
        for filesize in filesizes:
            sizeOfAllFiles += filesize
            print(sizeOfAllFiles)


if __name__ == '__main__':
    ff = FileFinderUsage()
    ff.findHorizontalArtworks()
    ff.findZipFiles()
