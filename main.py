from getAndExportData import getAndExportData
from runStatisticsOnTagging import runStatisticsOnTagging
import sys

def main(url):
    contin = True
    tags = {}
    exportData = getAndExportData("Villaneve")

    while contin: 
        tags = exportData.pullTagsFromPage(url, tags)
        url = exportData.incrementPage(url)
        contin = exportData.doesPageContainFics(url)

    print(f"Found tags: {tags}")

    stats = runStatisticsOnTagging()

    stats.topTenPie(stats.sortedKeyList(tags), stats.sortedValueList(tags))

if __name__ == "__main__":
    main(sys.argv[1])
        