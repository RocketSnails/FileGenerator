from PIL import Image
import math
import uuid
import os
import sys

# filename = str(uuid.uuid4()) + ".jpeg"
#
need_size = int(sys.argv[1])
filename = str(uuid.uuid4()) + ".bmp"

xx = int(math.sqrt(need_size/141.9))
if 6*xx < 65535 & 8*xx<65535:
    img = Image.new('RGB', (6 * xx, 8 * xx))
    img_import = Image.open('test.jpeg')
    for x in range(0, xx * 6, 600):
        for y in range(0, xx * 8, 800):
            img.paste(img_import, (x, y))
    img.save(filename)
else:
    print("pic is out of limits > 65535 pix on one side")
print(filename)
