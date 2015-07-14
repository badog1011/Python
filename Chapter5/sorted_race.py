

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


print("James: ", end='')
james2 = sorted(james)
print(james2)
print("Julice: ", end='')
julie2 = sorted(julie)
print(julie2)
print("Mikey: ", end='')
mikey2 = sorted(mikey)
print(mikey2)
print("Sarah: ", end='')
sarah2 = sorted(sarah)
print(sarah2)
