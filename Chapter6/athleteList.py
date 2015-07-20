class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.Name = a_name
        self.Dob  = a_dob
        self.extend(a_times)


    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'

    elif ':' in time_string:
        splitter = ':'

    else:
        return (time_string)
        
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp1 = data.strip().split(',')
        return(AthleteList(temp1.pop(0), temp1.pop(0), temp1))
    except IOError as ioerr:
        print("File Error: " + str(ioerr))
        return(None)
    
vera = AthleteList("Vera Vi")
vera.append('1.31')
print(vera.top3())

vera.extend(['2.22', '1-21', '2:22'])
print(vera.top3())

james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')

print(james.Name + "'s fastest times are: " + str(james.top3()))
                    


print(str(vera.Name) + str([str(each) for each in vera.top3()])  )
for each in vera.top3():
    print(each)
