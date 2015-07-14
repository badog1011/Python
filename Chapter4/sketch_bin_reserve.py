import nester
import pickle

new_man = []

try:
    with open('../man_data_bin.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
        nester.print_lol(new_man)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error:' + str(perr))
