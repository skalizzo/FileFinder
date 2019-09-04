from .FindFiles import FindFiles
import pandas as pd

class FileFinderUsage():
    def __init__(self):
        self.ff = FindFiles()

    def findHorizontalArtworks(self):
        #print(PIL.PILLOW_VERSION)
        #Einstellungsvariablen
        searchpath = "G:\\Digitale Distribution\\10_PLATTFORMEN\\00_Grafik\\*\\*\\"
        destination = 'G:/Digitale Distribution/10_PLATTFORMEN/00_Grafik/__iTunes_Querartworks/'

        #Files suchen
        pfadliste = self.ff.findFiles(searchpath=searchpath, searchstring="*3840x2160*", filetype="png")

        #Files in einenOrdner kopieren
        self.ff.copyfiles2folder(pfadliste, destination)

        #Auflösung von Bildern ausgeben
        for file in pfadliste:
            width, height = self.ff.get_image_size(file)
            print(file + ": Auflösung: " + str(width) + "x" + str(height))


    def findZipFiles(self):
        fileList = self.ff.findFiles(searchpath="G:\\Digitale Distribution\\10_PLATTFORMEN\\00_Grafik\\*\\",
                                      filetype="zip")
        filesizes = []
        sizeOfAllFiles = 0
        lastModifiedDate = []

        for file in fileList:
            filesizes.append(self.ff.getFileSize(file))
            lastModifiedDate.append(self.ff.getLastModifiedDate(file))

        df = pd.DataFrame(data={"path": fileList, "filesize": filesizes, "lastModifiedDate": lastModifiedDate})
        df.to_csv("./filesizes.csv", sep=',', index=True)

        print("Anzahl zip-Dateien: " + len(filesizes))
        for filesize in filesizes:
            sizeOfAllFiles += filesize
            print(sizeOfAllFiles)


if __name__ == '__main__':
    ff = FileFinderUsage()
    ff.findHorizontalArtworks()
    ff.findZipFiles()
