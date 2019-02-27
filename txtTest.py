import time
import uuid
import sys
import os

start_time = time.time()

# Iterate over the data and write it out row by row.
sheet_size = 5
need_size = int(sys.argv[1])
# need_size = 1024 * 1024 * 1024

filename = str(uuid.uuid4()) + ".txt"


def generate_txt(m_count):
    with open(filename, "w") as my_empty_txt:
        for i in range(0, m_count):
            my_empty_txt.write("somerandometext")
        pass
    size = os.stat(filename).st_size
    return size


count = 50
size50 = generate_txt(count)
k50 = -(-size50 // 50)
count = int(need_size / k50) + 1

size = generate_txt(count)
if size < need_size:
    count = int(count - (-(need_size - size) // k50))
    size = generate_txt(count)

# print(str(size / 1024 / 1024) + " MBytes")
# print("--- %s seconds ---" % (time.time() - start_time))
print(filename)
