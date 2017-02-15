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

# Inspiration source:  https://automatetheboringstuff.com/chapter11/
# Note:  This code is for practice purposes.  Please do not abuse the terms of service of the websites.

import webbrowser

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