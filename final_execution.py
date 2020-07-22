import codecs
import subprocess
import os
#The OS module provides functions for interacting with the operating system
while (True):
    corona = input("Do you want to know more about Coronavirus-COVID-19?                                                             answer in yes/no format \n")
    if corona== "yes":
        url = "CORONAVIRUS.htm"
#Python executes code following the try statement as a “normal” part of the program
        try:
            os.startfile(url)
#The code that follows the except statement is the response to any exceptions in the preceding try clause
        except AttributeError:
            try:
                    subprocess.call(['open', url])
            except:
                    print('Could not open URL')
            break
    elif corona=="no":
       print("Have a nice day!")
       break
    else:
        print("Enter either yes/no")