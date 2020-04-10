from bs4 import BeautifulSoup
import requests

class getAndExportData:

    def __init__(self, ship):
        self.ship = ship

    def pullTagsFromPage(self, url, tags):

        #get raw HTML from provided URL
        r = requests.get(url)
        #convert raw html to String
        pageHTML = r.text

        #create soup from whole page
        soup = BeautifulSoup(pageHTML, "html.parser")

        #creates list of all tags, separated by each work
        allTags = soup.find_all("ul", "tags commas")

        #iterate through all tags to find the ones we want
        #this goes fic by fic on the page
        for i in allTags:
            #separate out "freeforms" aka custom tags
            temp = i.find_all("li", "freeforms")

            #iterates through each freeform tag for the current fic
            for x in temp:
                #pulls out the text value of the tag
                #i.e. not the link or any of the other junk
                tagVal = x.find('a').text

                #has this tag been used before?
                if tagVal in tags:
                    #increment the counter for this tag
                    tags[tagVal] = tags[tagVal] + 1
                else: 
                    #create new key value pair for this tag
                    tags[tagVal] = 1
                
        return tags

    def incrementPage(self, prevUrl):
        return True



        
        
        

#Call methods...for the purpose of testing
test = getAndExportData("Villaneve")
test.pullTagsFromPage("https://archiveofourown.org/tags/Eve%20Polastri*s*Villanelle%20%7C%20Oksana%20Astankova/works", {})
