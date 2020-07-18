#!python3
import re
from pathlib import Path
'''
Example of voting showout in text file(for regex):
<tr>
<td>(string county_name)</td>
<td>(int republican_count)</td>
<td>(int democrat_count)</td>
<td>(int minor[minority?])</td>
<td>(int none)</td>
<td>(int total)</td>
</tr>

'''

#Make regex object
myFile = open(Path.cwd() / 'floridaVoters.html')
floridaVoters = myFile.read()

DataRegex = re.compile(r'''(
    #Name with tags
    (<td>)([a-zA-Z]+)(</td>) [\n\r]
    #repub with tags
    (<td>)([0-9,]+)(</td>) [\n\r]
    #democratic count with tags
    (<td>)([0-9,]+)(</td>) 
    )''',re.VERBOSE)
myMatches = DataRegex.findall(floridaVoters)
myFile.close()

#group[2] is county
#group[5] is republican_count
#group[8] is democrat_count
#List to store found values in
voterList = []
#Take matches and put into list of tuples
for groups in myMatches:
    #tempTuple = tuple(groups[2],int(group[5],int(group[8])
    republican_count = int(groups[5].replace(',',''))
    democrat_count = int(groups[8].replace(',',''))
    voterList.append((groups[2],republican_count,democrat_count))

#Sort by number of democratic voters
sortedVoters = sorted(voterList, key = lambda tup:tup[2])

for county in sortedVoters:
    for statistic in county:
        print(statistic, end = ' ')
    print()

