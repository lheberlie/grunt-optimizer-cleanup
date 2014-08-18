__author__ = 'lloy3317'

import re

import pprint

pp = pprint.PrettyPrinter(indent=4)

fileToRead = "./library-before/3.9custom/esri/css/esri.css"
saveToFile = "extract-urls-from-css.txt"

itemsArr = []

try:
    with open(fileToRead, 'rb') as data:
        fileContent = ""

        for line in data:
            fileContent += line

        if fileContent:


            regEx = "\\.\\.(\\/[a-zA-Z0-9-_]+)*\\.(png|jpg|gif)"

            p = re.compile(regEx)
            p.findall(fileContent)
            items = p.finditer(fileContent)

            for item in items:
                #print item.group(0)
                itemsArr.append(item.group(0))

        pp.pprint(itemsArr)
except IOError:
    print "An error occurred while trying to read " + fileToRead

try:
    with open(saveToFile, 'wba') as fileWriter:
        fileWriter.write("CSS image backgrounds declared in esri.css\n")
        fileWriter.write(pprint.pformat(sorted(list(set(itemsArr)))))
        fileWriter.close()
except IOError:
    print "An error occurred while writing to %s", saveToFile