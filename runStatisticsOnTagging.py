import matplotlib.pyplot as plt

class runStatisticsOnTagging:

    def sortedKeyList(self, tags):
        return sorted(tags, key=tags.get, reverse=True)

    def sortedValueList(self, tags):
        return sorted(tags.values(), reverse=True)

    def topTenPie(self, keyList, valueList):
        plt.pie(valueList[0:9], labels=keyList[0:9],
           autopct=None)
        plt.show()

        

    