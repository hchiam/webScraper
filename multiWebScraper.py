# The MIT License (MIT)
# 
# Copyright (c) 2016 Howard Chiam
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# --------------

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
