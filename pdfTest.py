import random
import string
import subprocess
import time
import uuid
import os
import sys

from fpdf import FPDF

start_time = time.time()

# Iterate over the data and write it out row by row.
need_size = int(sys.argv[1])

filename = str(uuid.uuid4()) + ".pdf"


def generate_pdf(m_count):
    pdf = FPDF()
    pdf.add_page()
    for i in range(0, m_count):
        pdf.set_font("Arial", size=12)
        pdf.cell(i % 3, i % 4, txt=id_generator(), ln=i % 5 + 1)
    pdf.output(filename)

    size = os.stat(filename).st_size
    return size


# need some optimizations here
def id_generator(size=need_size // 42, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def cls():
    subprocess.call("cls", shell=True)


count = 50
size50 = generate_pdf(count)
k50 = -(-size50 // 50)
count = int(need_size / k50) + 1


size = generate_pdf(count)
if size < need_size:
    count = int(count - (-(need_size - size) // k50))

    size = generate_pdf(count)

# print(str(size / 1024 / 1024) + " MBytes")
# print("--- %s seconds ---" % (time.time() - start_time))
print(filename)
