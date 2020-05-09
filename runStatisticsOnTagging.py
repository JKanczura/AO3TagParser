import matplotlib.pyplot as plt
import xlwt as xl
# import TemporaryFile

class runStatisticsOnTagging:

    def sortedKeyList(self, tags):
        return sorted(tags, key=tags.get, reverse=True)

    def sortedValueList(self, tags):
        return sorted(tags.values(), reverse=True)

    def topTenPie(self, keyList, valueList):
        plt.pie(valueList[0:9], labels=keyList[0:9],
           autopct=None)
        plt.show()

    def exportTagsXlsx(self, keyList, valueList):
        book = xl.Workbook()
        mainSheet = book.add_sheet("sheet1", cell_overwrite_ok=True)

        #TODO: debug why the first value is one that appears once
        #Rest are in order???
        for i, e in enumerate(keyList):
            mainSheet.write(i, 0, keyList[i-1])
            mainSheet.write(i, 1, valueList[i-1])

        book.save("villaneveStats.xls")
        # book.save(TemporaryFile())

        

    