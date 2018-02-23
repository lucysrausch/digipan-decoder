

from PIL import Image

import sys

with open(sys.argv[1] ) as f:
    content = f.readlines()

content = [(int(x.replace("digipan-1: ", "").replace("Frame error", "3596").replace("\n", "")) & 0xFFF)/16 for x in content]

#print content[1:][::2]

list1 = content[0:][::2]
list2 = content[1:][::2]


c = []

for i in range((len(list1)/1246)*2):
    for b in range(623):
        c.append(list1[b+(i*623)])
    for b in range(623):
        c.append(list2[b+(i*623)])

img = Image.new('1', (1246,len(content)/(1246))) #save as 32 bit
img.putdata(c)
img = img.rotate(90, expand=True)
img.show()
img.save('digipan_xray.png')
