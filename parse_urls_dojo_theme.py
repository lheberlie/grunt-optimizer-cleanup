__author__ = 'lloy3317'

import os.path
import re

themeName = "claro"

fileToRead = "3.9custom/dijit/themes/%s/%s.css" % (themeName, themeName)
fileToRead2 = "3.9custom/dijit/themes/%s/%s_rtl.css" % (themeName, themeName)

fileList = [fileToRead, fileToRead2]
fileToSave = "assets_in_%s_theme.txt" % themeName

#print fileToRead
#print fileToRead2

urlItems = []

fileContents = ""


def fileSeparationComment(filePath):
    comment = "// -------------------------------------------------------------------\n// %s\n// -------------------------------------------------------------------\n"
    return comment % filePath


for filename in fileList:
    print filename
    try:
        with open(filename, 'rb') as data:
            fileContent = ""

            for line in data:
                fileContent += line

            if fileContent:
                regEx = "\\.\\.(\\/[a-zA-Z0-9-_]+)*\\.(png|jpg|gif)"

                p = re.compile(regEx)
                p.findall(fileContent)
                items = p.finditer(fileContent)

                for item in items:
                    matchString = item.group(0)

                    print matchString
                    urlItems.append(matchString)

                fileContents = fileContents + str(fileSeparationComment(filename))

                sortedItems = sorted(list(set(urlItems)))
                fileContents = fileContents + str(sortedItems).replace("'", "\"").replace(",", ",\n") + "\n"
        urlItems = []


    except IOError:
        print "An error occurred while trying to read " + fileToRead


try:
    with open(fileToSave, 'wba') as fileWriter:
        fileWriter.write(fileContents)
        fileWriter.close()
except IOError:
    print "An error occurred while writing to %s" % fileToSave