import urllib.request
import sys
def read_file():
    quotes = open("D:\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_of_file):
    connection = urllib.request.urlopen("http://www.wdyl.com/profanity?q="+text_of_file)
    output = connection.read()
    print(output)
    connection.close()

read_file()
