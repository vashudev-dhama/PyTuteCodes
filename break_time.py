import time
import webbrowser

print("Started on: "+ time.ctime())
#repeate for 3 times
i=2
while(i>-1):

    #wait/suspend for 2 sec
    time.sleep(2)

    # open a web browser in Python
    webbrowser.open("https://www.google.com")

    #decrease the counter
    i = i - 1
