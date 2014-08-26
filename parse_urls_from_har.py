__author__ = 'lloy3317'

import re, string

apiDirectoryName = "3.9custom"
#removeURL = "http://js.arcgis.com/3.9compact/"
removeURL = "http://heb.esri.com/js/playground-js/esrijs-playground/reduce-optimizer-sample/"

fileToRead = "app-traffic.har"

fileToSave = "api-files-to-keep.txt"

urlItems = []

try:
    with open(fileToRead, 'rb') as data:
        fileContent = ""

        for line in data:
            fileContent += line

        if fileContent:
            p = re.compile("\"url\": \"(http|https)://[a-zA-z0-9]+[.][a-zA-Z]+[.][a-zA-Z]+(/[a-zA-Z%20]*)*.*")
            p.findall(fileContent)
            items = p.finditer(fileContent)

            urlToKeepPattern = re.compile(apiDirectoryName)

            urlToRemovePattern = re.compile(removeURL)
            #re.search("3.9custom", searchText, re.M)

            for item in items:
                matchString = item.group(0)
                lastIndex = len(matchString) - 2
                subString = matchString[8:lastIndex]
                print subString
                subMatch = urlToKeepPattern.search(subString)

                if subMatch != None:
                    print "%s matches %s" % (subString, str(subMatch.group(0)))
                    #print subString

                    #filePatternResult = urlToRemovePattern.sub("!<%= pkg.api_dir_after %>/", subString)
                    filePatternResult = urlToRemovePattern.sub("", subString)


                    #stringToWrite ='%s%s%s' % ('"', subString, '",')
                    #urlItems.append(stringToWrite)
                    urlItems.append(filePatternResult)

except IOError:
    print "An error occurred while trying to read " + fileToRead

try:
    with open(fileToSave, 'wba') as fileWriter:
        #fileWriter.write("\n".join(map(str,urlItems)))
        #fileWriter.write(pprint.pformat(sorted(list(set(itemsArr))))
        sortedItems = sorted(list(set(urlItems)))
        fileWriter.write(str(sortedItems).replace("'","\"").replace(",", ",\n"))
        fileWriter.close()
except IOError:
    print "An error occurred while writing to %s", fileToSave