#Michael Thomas
#BIOT-E 100
#Assignment 4
#pickling

import cPickle as pickle
saveFile = "neno.pkl"

with open(saveFile, "wb") as output:
    pickle.dump((d), output, protocol=pickle, HIGHEST_PROTOCOL)
