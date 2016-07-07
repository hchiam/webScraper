from bs4 import BeautifulSoup
import urllib

chi, spa, hin, ara, rus = [], [], [], [], []

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

if mode == 0:
    # find Mandarin Chinese translations
    chi = soup.find_all("span", lang="cmn")
    if chi != None:
        chi = list(set(chi))
    # find Spanish translations
    spa = soup.find_all("span", lang="es")
    if spa != None:
        spa = list(set(spa))
    # find Hindi translations
    hin = soup.find_all("span", lang="hi")
    if hin != None:
        hin = list(set(hin))
    # find Standard Arabic translations
    ara = soup.find_all("span", lang="ar")
    if ara != None:
        ara = list(set(ara))
    # find Egyptian Arabic translations
    ara2 = soup.find_all("span", lang="arz")
    if ara2 != None:
        ara2 = list(set(ara2))
        ara = ara + ara2
    # find Russian translations
    rus = soup.find_all("span", lang="ru")
    if rus != None:
        rus = list(set(rus))
elif mode == 1:
    # find Mandarin Chinese translation
    found = soup.find("span", lang="cmn")
    if found != None:
        chi.append(found.get_text())
    # find Spanish translation
    found = soup.find("span", lang="es")
    if found != None:
        spa.append(found.get_text())
    # find Hindi translation
    found = soup.find("span", lang="hi")
    if found != None:
        hin.append(found.get_text())
    # find Standard Arabic translation
    found = soup.find("span", lang="ar")
    if found != None:
        ara.append(found.get_text())
    # find Egyptian Arabic translation
    found = soup.find("span", lang="arz")
    if found != None:
        ara2.append(found.get_text())
        ara = ara + ara2
    # find Russian translation
    found = soup.find("span", lang="ru")
    if found != None:
        rus.append(found.get_text())

words = chi + spa + hin + ara + rus

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
