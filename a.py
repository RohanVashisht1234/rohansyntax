
import yaml
 
from yaml.loader import SafeLoader
# open yaml file in read
with open('./generated.lua', 'w') as f:
    f.write("")
name = ""
def write(x):
    with open('./generated.lua', 'a') as f:
        f.write(x + "\n")



with open('./my.yaml', 'r') as f:
    write('-- mod-version:3')
    write('local syntax = require "core.syntax"')
    write('syntax.add {')
    yaml_data = list(yaml.load_all(f, Loader=SafeLoader))
    write('name = "'+yaml_data[0]["name"]+'",')

    write("files = {")
    for i in yaml_data[0]["file"]:
        write('   "'+i+'"'+",")
    write("},")


    write("patterns = {")
    for i in yaml_data[0]["patterns"]:
        write(f"    {{ pattern = '{str(i)}', type = {{{str(yaml_data[0]["patterns"][i])[1:-1]}}} }},")
    write("},")

    write("symbols = {")
    keywords = yaml_data[0]["keywords"].split()
    for i in keywords:
        write(f"    ['{i}'] = 'keyword',")

    keywords2 = yaml_data[0]["keywords2"].split()
    for i in keywords2:
        write(f"    ['{i}'] = 'keyword2',")
    
    literals = yaml_data[0]["literal"].split()
    for i in literals:
        write(f"    ['{i}'] = 'literal',")
    write("},")
    write("}")