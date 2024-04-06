# Author: Rohan Vashisht
# License: Please check LICENSE file

import yaml
import sys
 
from yaml.loader import SafeLoader

x = sys.argv
if len(x) <= 2:
    print("Low number of inputs")

INPUT_FILE = x[1]
OUTPUT_FILE = x[2]
# open yaml file in read
with open(OUTPUT_FILE, 'w') as f:
    f.write("")
name = ""
def write(x = ""):
    with open(OUTPUT_FILE, 'a') as f:
        f.write(x + "\n")



with open(INPUT_FILE, 'r') as f:
    write('-- Generated using https://github.com/RohanVashisht1234/rohansyntax')
    write('-- mod-version:3')
    write('local syntax = require "core.syntax"')
    write('syntax.add {')
    yaml_data = list(yaml.load_all(f, Loader=SafeLoader))
    write('name = "'+yaml_data[0]["name"]+'",')

    write(f"block_comment = {{{str(yaml_data[0]['block-comment'])[1:-1]}}},")

    write("files = {")
    for i in yaml_data[0]["file"]:
        write('   "'+i+'"'+",")
    write("},")


    write("patterns = {")
    for i in yaml_data[0]["patterns"]:
        pattern = str(i["pattern"])[1:-1]
        type = str(i["type"])[1:-1]
        
        write(f"    {{ pattern = {{{pattern}}}, type = {{{type}}} }},")
    write("},")

    write("symbols = {")
    keywords = yaml_data[0]["keywords"]
    for i in keywords:
        write(f"    ['{i}'] = 'keyword',")

    keywords2 = yaml_data[0]["keywords2"]
    for i in keywords2:
        write(f"    ['{i}'] = 'keyword2',")
    
    literals = yaml_data[0]["literal"]
    for i in literals:
        write(f"    ['{i}'] = 'literal',")
    write("},")
    write("}")


print("You file has been generated!")
print(INPUT_FILE + " -> " + OUTPUT_FILE)
