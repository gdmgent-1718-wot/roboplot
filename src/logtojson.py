import json
# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str
# data
data = []
#create data
x = 1
while x < 50:
    item = {"l": 4,"r": 5}
    data.append(item)
    print("nummer %d " % (x))
    x += 1

# Write
with io.open('data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,indent=4, sort_keys=True,separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
