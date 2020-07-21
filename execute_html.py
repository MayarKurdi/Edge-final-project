import codecs
import subprocess
import os



file = codecs.open("coronavirus.htm", "r", "utf-8")
url = "CORONAVIRUS.htm"
try:
    os.startfile(url)
except AttributeError:
    try:
        subprocess.call(['open', url])
    except:
        print('Could not open URL')

