

try:
    with open('james.txt', 'r') as athelet_james:
        data = athelet_james.readline()
        james = data.strip().split(',')
        print("James: ", end='')
        print(james)
    with open('julie.txt', 'r') as athelet_julie:
        data = athelet_julie.readline()
        julie = data.strip().split(',')
        print("Julice: ", end='')
        print(julie)
    with open('mikey.txt', 'r') as athelet_mikey:
        data = athelet_mikey.readline()
        mikey = data.strip().split(',')
        print("Mikey: ", end='')
        print(mikey)
    with open('sarah.txt', 'r') as athelet_sarah:
        data = athelet_sarah.readline()
        sarah = data.strip().split(',')
        print("Sarah: ", end='')
        print(sarah)
except IOError as err:
    print('File error: ' + str(err))
