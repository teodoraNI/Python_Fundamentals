# import re
#
# pattern_valid = r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+'
# pattern_group = r'(\d\w*?)'
# barcodes_number = int(input())
# for _ in range(barcodes_number):
#     string = input()
#     match = re.search(pattern_valid, string)
#     if not match:
#         print('Invalid barcode')
#     else:
#         group = ''.join(re.findall(pattern_group, string))
#         if not group:
#             group = '00'
#         print(f'Product group: {group}')

import re

def find_group(string):
    pattern_group = r'(\d\w*?)'
    group = ''.join(re.findall(pattern_group, string))
    if not group:
        group = '00'
    return group

def validation(string):
    pattern_valid = r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+'
    match = re.search(pattern_valid, string)
    if not match:
        print('Invalid barcode')
    else:
        group = find_group(string)
        print(f'Product group: {group}')


barcodes_number = int(input())
for _ in range(barcodes_number):
    string = input()
    validation(string)