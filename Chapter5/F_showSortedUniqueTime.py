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


def ShowSortedUniqueTime(time_string):
    print(sorted(set([sanitize(each_t) for each_t in time_string])))


#ShowSortedUniqueTime(james)

''' Define a function for making sure the file is opened successfully'''
def openFile(filename):
    try:
        with open(filename) as fn:
            data = fn.readline()
            print("Formating...")
        return(data.strip().split(','))
    except IOError as err:
        print("File Error" + str(err))



james = openFile('james.txt')

ShowSortedUniqueTime(james)
