# Inspiration source:  https://automatetheboringstuff.com/chapter11/

import webbrowser
from bs4 import BeautifulSoup

# examples of urls for searching "Web search engine":
# https://www.google.ca/?gws_rd=ssl#q=Web+search+engine
# https://en.wikipedia.org/wiki/Web_search_engine

# webbrowser.open('https://automatetheboringstuff.com/chapter11/') # this would open the website in your browser

print("Welcome to the \"multi-search\" program.")

# list of possible "yes" answers
yes = ["y","yes","yup","yeah","yep","yap","ok","k"]

# ask user for search string
searchString = raw_input("Enter a search string:\t")
# ask user whether they want to do fuller search
fullerSearch = raw_input("Enter 'y' to do fuller search:\t")
# check if user said "yes"
if fullerSearch in yes:
    # double-check (for usability)
    fullerSearch = raw_input("Are you sure?:\t")

# search in Google
searchGoogle = searchString.replace(" ","+")
webbrowser.open('https://www.google.ca/?gws_rd=ssl#q=' + searchGoogle)
# search in Wikipedia
searchWikipedia = searchString.replace(" ","_")
webbrowser.open('https://en.wikipedia.org/wiki/' + searchWikipedia)

# make user input into lower case (this is after both checks for "yes")
fullerSearch = fullerSearch.lower()

# check if doing fuller search
if fullerSearch in yes:
    # search in Wiktionary
    searchWiktionary = searchString.replace(" ","_")
    webbrowser.open('https://en.wiktionary.org/wiki/' + searchWiktionary)
    # search in Dictionary
    searchDictionary = searchString.replace(" ","--")
    webbrowser.open('http://www.dictionary.com/browse/' + searchDictionary)
    # search in WolframAlpha
    searchWolframAlpha = searchString.replace(" ","+")
    webbrowser.open('http://www.wolframalpha.com/input/?i=' + searchWolframAlpha)