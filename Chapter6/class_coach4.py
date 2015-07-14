class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.Name = a_name
        self.Dob  = a_dob
        self.Times= a_times


    def top3(self):
        return (sorted(set([sanitize(t) for t in self.Times]))[0:3])


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp1 = data.strip().split(',')
        return(Athlete(temp1.pop(0), temp1.pop(0), temp1))
    except IOError as ioerr:
        print("File Error: " + str(ioerr))
        return(None)

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'

    elif ':' in time_string:
        splitter = ':'

    else:
        return (time_string)
        
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')

print(james.Name + "'s fastes times are: " + str(james.top3()))
print(julie.Name + "'s fastes times are: " + str(julie.top3()))
