# import urllib.request 
# importing requests library which has more sensible api than urllib
import requests


def read_text():

    #make a object of file type using open() function
    quotes = open("/home/vashu/Desktop/file.txt")
    #read and store the content of file object
    contents_of_file = quotes.read()
    #print(contents_of_file)
    #close the file opened
    quotes.close()

    #call the funciton to check for profanity
    check_profanity(contents_of_file)

def check_profanity(text_to_check):

    # url = "http://www.wdylike.appspot.com/?q=shot"
    # headers = {}
    # headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    # req = urllib.request.Request(url,data, headers=headers)
    # resp = urllib.request.urlopen(req)

    #perform a 
    resp = requests.get('http://www.wdylike.appspot.com',{'q': text_to_check})

    #store the content of resp thus fetched 
    output = resp.text

    #check for the profanity
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("All clear")

read_text()
