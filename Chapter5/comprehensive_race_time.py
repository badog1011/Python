"""Transformat the original time list to uniform time format"""

def sanitize(time_string):
    """input argument, time_string, is an orginal time format that isn't united.
    Therefore, we sprobed the pronunciation, which include, period, dash and colon.
    And, we assinged them to identifer, splitter. Then, split the strings on the basic
    of 'splitter'. After all, return the amended string. """
    if '-' in time_string:
        splitter = '-'

    elif ':' in time_string:
        splitter = ':'

    else:
        return (time_string)
        
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

try:
    with open('james.txt', 'r') as athelet_james:
        data = athelet_james.readline()
        james = data.strip().split(',')

    with open('julie.txt', 'r') as athelet_julie:
        data = athelet_julie.readline()
        julie = data.strip().split(',')

    with open('mikey.txt', 'r') as athelet_mikey:
        data = athelet_mikey.readline()
        mikey = data.strip().split(',')

    with open('sarah.txt', 'r') as athelet_sarah:
        data = athelet_sarah.readline()
        sarah = data.strip().split(',')

except IOError as err:
    print('File error: ' + str(err))

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []



clean_james = sorted([sanitize(each_t) for each_t in james])
clean_julie = sorted([sanitize(each_t) for each_t in julie])
clean_mikey = sorted([sanitize(each_t) for each_t in mikey])
clean_sarah = sorted([sanitize(each_t) for each_t in sarah])



print( clean_james)
print( clean_julie)
print( clean_mikey)
print( clean_sarah)


unique_james = []

for each_t in clean_james:
    if each_t not in unique_james:
        unique_james.append(each_t)
#print(unique_james)
print(unique_james[0:3])

unique_julie = []

for each_t in clean_james:
    if each_t not in unique_julie:
        unique_julie.append(each_t)
#print(unique_julie)
print(unique_julie[0:3])

unique_mikey = []

for each_t in clean_mikey:
    if each_t not in unique_mikey:
        unique_mikey.append(each_t)
#print(unique_mikey)
print(unique_mikey[0:3])

unique_sarah = []

for each_t in clean_sarah:
    if each_t not in unique_sarah:
        unique_sarah.append(each_t)
#print(unique_sarah)
print(unique_sarah[0:3])

