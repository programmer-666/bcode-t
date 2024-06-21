# suhaArslan 

from pandas import read_csv
from barcode import Code128
from barcode.writer import ImageWriter

props = {
    "module_width": 0.5,
    "module_height": 4.5,
    "font_size": 12,
    "text_distance": 5,
    "quiet_zone": 2,
}

for code in read_csv("wMachineCodes.csv")["kodlar"]:
    Code128(str(code), writer=ImageWriter()).save("barcodes/" + str(code), props)
