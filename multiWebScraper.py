from bs4 import BeautifulSoup
import urllib

languages = ["cmn","es","hi","ar","arz","ru"]
words = []

print("\n")
print("THIS PROGRAM WILL SEARCH FOR TRANSLATIONS IN WIKTIONARY")
print("\n")
searchWord = raw_input("Enter a word to translate:\t")
url = "https://en.wiktionary.org/wiki/" + searchWord
mode = input("Enter 1 for \"1st word entry\" mode, 0 for \"all words\" mode:\t")
print("\n")
print("Searching in " + url)
print("\n")

r = urllib.urlopen(url).read()
soup = BeautifulSoup(r, "html.parser")


if mode == 0: # find all unique entries
    
    # for each language
    for language in languages:
        
        finders = soup.find_all("span", lang=language)
        
        # if found something
        if finders != None:
            
            # keep unique entries and put into a list
            finders = list(set(finders))
            # add all entries to running list for all languages
            words += finders

elif mode == 1: # find first entries
    
    # for each language
    for language in languages:
        
        found = soup.find("span", lang=language)
        
        # if found something
        if found != None:
            
            # add new entry to running list for all languages
            words.append(found.get_text())


if mode == 0:
    # print out word entries
    for word in words:
        print(word.get_text())
elif mode == 1:
    # print out word entries
    for word in words:
        print(word)


if words == []:
    print ":( NONE FOUND :("


print("\n")
