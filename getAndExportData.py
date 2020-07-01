from bs4 import BeautifulSoup
import requests
import datetime

class getAndExportData:

    def __init__(self, ship):
        print(datetime.datetime.now())
        self.ship = ship

    #create soup from url
    #since there are now multiple parsing functions
    #makes sense to reuse this
    def createSoup(self, url):
        print("Creating soup: " + datetime.datetime.now())

        #get raw HTML from provided URL
        r = requests.get(url)

        #convert raw html to String
        pageHTML = r.text

        #create soup from whole page
        soup = BeautifulSoup(pageHTML, "html.parser")
        print("Created soup: " + datetime.datetime.now())

        return soup 

    #pull data for each story in this category
    def pullAllStoryDataFromPage(self, url, existing_data):
        print("Getting data from page: " + datetime.datetime.now())

        soup = self.createSoup(url)


    def pullTagsFromPage(self, url, tags):
        print("Getting tags from page: " + datetime.datetime.now())

        soup = self.createSoup(url)

        #creates list of all tags, separated by each work
        allTags = soup.find_all("ul", "tags commas")

        print("Found all tags")

        #iterate through all tags to find the ones we want
        #this goes fic by fic on the page
        print("Iterate through tags for each story")
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
        print("Tags all found")
        return tags

    

    def incrementPage(self, url):
        print(datetime.datetime.now())
        #check if page is already in the url
        if "page=" in url:
            prevPage = url[(len(url)-1)]
            prevPage = int(prevPage)
            prevPage = prevPage + 1

            url = url[:-1]
            url = url + str(prevPage)
        #if page is not in the url, automatically assume it's on page 1
        else:
            url = url + "?page=2"
        #return the modified url
        return url

    def doesPageContainFics(self, url):
        print(datetime.datetime.now())
         #get raw HTML from provided URL
        r = requests.get(url)
        #convert raw html to String
        pageHTML = r.text
        print("Creating soup for contain fics")
        #create soup from whole page
        soup = BeautifulSoup(pageHTML, "html.parser")

        print("Find if page exists")
        #only exists on pages that have fics
        blurbs = soup.find_all("li", "work blurb group")
        
        if len(blurbs) == 0:
            return False
        else:
            return True


