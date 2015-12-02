#Michael Thomas
#BIOT-E 100
#Assignment 4
#zip-map

#declare x,y,z
x = ["a", "b", "c"]
y = [1, 2, 3]
z = ["m", "l"]

#Zips x,y,z
for i, j, k in zip(x, y, z):
    print i, j, k, "\n"

#Use map to add "none" when the lists are un-even
print map(None, x, y, z)
