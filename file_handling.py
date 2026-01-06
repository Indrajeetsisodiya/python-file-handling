# Python File Objects Explained in Simple Terms
# Exact code and outputs as shown in the Hashnode article


# --------------------------------------------
# file1.txt contains:
# apple
# banana
# grapes
# mango
# --------------------------------------------


# --------------------------------------------
# Reading from a file
# --------------------------------------------

f = open("file1.txt", "r")
print(f.read())
f.close()

# output
'''
apple
banana
grapes
mango
'''


# --------------------------------------------
# Writing to a file
# --------------------------------------------
# "w" mode overwrites existing content

f = open("file1.txt", "w")
f.write("orange")
f.close()

# After this, file1.txt contains:
# orange


# --------------------------------------------
# What happens if we use print() while writing?
# --------------------------------------------

f = open("file1.txt", "w")
print(f.write("orange"))
f.close()

# output
# 6
# write() returns number of characters written


# --------------------------------------------
# Appending to a file
# --------------------------------------------

# file2.txt initially contains:
# indrajeet,rishabh
# vimal,aman,rishi

f = open("file2.txt", "a")
f.write(",david")
f.close()

# Now file2.txt contains:
# indrajeet,rishabh
# vimal,aman,rishi ,david


# --------------------------------------------
# The golden rule: using 'with'
# --------------------------------------------

with open("file2.txt", "r") as f:
    data = f.read()
    print(data)

# output
'''
indrajeet,rishabh
vimal,aman,rishi ,david
'''


# --------------------------------------------
# Reading a range of characters
# --------------------------------------------

with open("file2.txt", "r") as f:
    data = f.read(6)
    print(data)

# output
# indraj


# now we try this and see what gets printed 

with open("file2.txt", "r") as f:
    data = f.read(6)
    data2 = f.read(6)
    print(data)
    print(data2)

# output
'''
indraj
eet,ri
'''

# --------------------------------------------
# Using seek() method in file object
# --------------------------------------------
with open("file2.txt", "r") as f:
    data = f.read(6)   # Reads first 6 characters (indraj)
    data2 = f.read(6)  # Reads next 6 characters (eet,ri)
    
    f.seek(0)          # Go back to the beginning
    
    data3 = f.read(6)  # Reads first 6 characters again (indraj)
    
    print(data)
    print(data2)
    print(data3)

'''
indraj
eet,ri
indraj
'''


# --------------------------------------------
# Jump to a specific position using seek()
# --------------------------------------------
with open("file2.txt", "r") as f:
    f.seek(6)  # Move the file pointer to byte (character) index 6
    print(f.read())

'''
eet,rishabh
vimal,aman,rishi ,david
'''

# --------------------------------------------
# Reading file line by line (very important)
# --------------------------------------------

with open("file2.txt", "r") as f:
    for i in f:
        print(i.strip())

# output
'''
indrajeet,rishabh
vimal,aman,rishi ,david
'''
