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
