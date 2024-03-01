#Without to DateTime

from pathlib import Path
import re

path = Path(__file__).parent / 'practicedata'

# american = re.compile(r'^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{4})$')
# for file_path in path.iterdir():
#     if not file_path.is_file() or file_path.suffix != ".txt":
#         continue 
#     if american.match(file_path.name.removesuffix(".txt")) is None:
#         continue
#     american_date = american.match(file_path.name.removesuffix(".txt"))
#     european_date = '-'.join((american_date.group(2), american_date.group(1), american_date.group(3)))
#     file_path.rename(european_date + '.txt')   

#With datetime
    
from datetime import datetime

for file_path in path.iterdir():
    if not file_path.is_file() or file_path.suffix != ".txt":
        continue 
    try:
        date = datetime.strptime(file_path.name.removesuffix('.txt'), '%m-%d-%Y')
    except ValueError:
        continue
    file_path.rename(date.strftime('%d-%m-%Y')+'.txt') 