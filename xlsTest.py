import sys
import time
import uuid

import xlwt
import os

start_time = time.time()

# Iterate over the data and write it out row by row.
sheet_size = 5
need_size = int(sys.argv[1])
# need_size = 1024 * 1024 * 100

filename = str(uuid.uuid4()) + ".xls"


def generate_xls(m_count):
    wb = xlwt.Workbook(filename)
    new_sheet = wb.add_sheet('Sheet1')
    for row in range(0, m_count):  # write NEW data
        for col in range(sheet_size):
            new_sheet.insert_bitmap('r100.bmp', row, col)
    wb.save(filename)
    size = os.stat(filename).st_size
    return size


count = 1
size50 = generate_xls(count)
k50 = -(-size50 // 1)
count = int(need_size / k50) + 1

size = generate_xls(count)
if size < need_size:
    count = int(count - (-(need_size - size) // k50))
    size = generate_xls(count)

# print(str(size / 1024 / 1024) + " MBytes")
# print("--- %s seconds ---" % (time.time() - start_time))
print(filename)
