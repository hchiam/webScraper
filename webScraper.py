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

# Reference:  http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html
# A web scraper.  This code was created from me skimming the tutorial above from Stanford.

#_________________________________________________
# You'll need to install BeautifulSoup for this code to work on your computer

from bs4 import BeautifulSoup
import urllib

#_________________________________________________
# Code taken from the tutorial, plus some "print"s for feedback on the command-line interface:

r = urllib.urlopen('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts').read()
soup = BeautifulSoup(r, "html.parser")
print "\ntype(soup) = "
print type(soup)

letters = soup.find_all("div", class_="ec_statements")
print "\ntype(letters) = "
print type(letters)
if letters:
    print "\nletters[0] = "
    print letters[0]
    print "\nletters[0].a[\"href\"] = \n\t\t(using the \"a\" tag)"
    print letters[0].a["href"]
    print "\n\nletters[0].find(id=\"legalert_date\") = \n\t\t(finding div tags with id \"legalert_date\")"
    print letters[0].find(id="legalert_date")
    print "\n\nletters[0].find(id=\"legalert_title\") = \n\t\t(finding div tags with id \"legalert_title\")"
    print letters[0].find(id="legalert_title")
    print "\n\nletters[0].find(id=\"legalert_title\").get_text() = \n\t\t(finding text of div tags with id \"legalert_title\")"
    print letters[0].find(id="legalert_title").get_text()
    print "\n"

#_________________________________________________
# Code I made to get the Greek translation of the word "Lojban" from the website Wiktionary:

print "___________________________"
print "https://en.wiktionary.org/wiki/Lojban"
print "Getting the Greek translation of \"Lojban\" from Wiktionary:"
r = urllib.urlopen('https://en.wiktionary.org/wiki/Lojban').read()
soup = BeautifulSoup(r, "html.parser")
letters = soup.find_all("span", class_="Grek")
print "\nletters[0].get_text() = "
print letters[0].get_text()
print "\n"
