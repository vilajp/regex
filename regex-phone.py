import re

myregex = re.compile(r"(\(\d\d\d\)|\d\d\d-)?\d\d\d-\d\d\d\d")

mytext = "you can call me at 155-555-6666 or (155)-555-8888"

lista = myregex.findall(mytext)

print(lista)



