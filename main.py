from getAndExportData import getAndExportData
import sys

def main(url):
    contin = True
    tags = {}
    exportData = getAndExportData("Villaneve")
    print(exportData.doesPageContainFics(url))

    while contin: 
        tags = exportData.pullTagsFromPage(url, tags)
        url = exportData.incrementPage(url)
        contin = exportData.doesPageContainFics(url)
        print (contin)

    #insert math part here

if __name__ == "__main__":
    main(sys.argv[1])
        