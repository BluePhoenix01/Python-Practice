import pyperclip
import requests

URL = pyperclip.paste()

res = requests.get(URL)
filename = URL.rstrip('/').rpartition('/')[2].partition('?')[0] 

if '.' not in filename:
    filename = filename + '.html'
with open(filename, 'wb') as file:
    file.write(res.content)


