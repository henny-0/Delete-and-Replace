from os import rename, listdir, system

from time import sleep
print("What do you want to remove from the front of your files?")
remove_front = input()
print("What do you want to remove from the within of your files?")
remove_rear = input()
countf = 0
countm = 0
for filename in listdir("."):
    if filename.startswith(remove_front) and remove_front:
        rename(filename, filename.replace(remove_front,'',1))
        countf = countf + 1
    if remove_rear in filename and remove_rear:
        rename(filename, filename.replace(remove_rear,''))
        countm = countm + 1
    # rename(filename, filename.rstrip())
print("Files completed - beginning of file: " + str(countf))    
print("Files completed - within file: " + str(countm))
print("All Done.")
system("pause")