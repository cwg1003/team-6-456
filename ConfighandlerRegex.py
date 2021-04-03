#Author: Naresh Adh
#Date: 03/26/2021
#Through this program, students will learn to:
    #1. validate an input file and contents in it using regular expression.
    #2. Handle file opening in a mode
    #2.1. Handle file exceptions, etc.
    #3. Search file contents
    #4. Use tools to check is a regular expression is 'evil'

#function-1
import re


def classify_settings(filename):

    # implement function-1 as instructed

    seton = []
    setoff = []
    setdefault = []

    #Open the file
    file = open(filename, "r")
    #Read line by line from the file
    lines = file.readlines()

    for line in lines:
        # use regular expression to find a line which is set to be 'true'
        # then parse the line to get the keyword, and insert it into seton list
        if re.search("true", line):
            onword = re.split(":", line)
            seton.append(onword[0])
        # use regular expression to find a line which is set to be 'false'
        # then parse the line to get the keyword, and insert it into setoff list
        elif re.search("false", line):
            offword = re.split(":", line)
            setoff.append(offword[0])
        # use regular expression to find a line which is set to be 'default'
        # then parse the line to get the keyword, and insert it into setoff list
        elif re.search("default", line):
            defaultword = re.split(":", line)
            setdefault.append(defaultword[0])

    file.close()
    # return lists
    return seton, setoff, setdefault
    pass


#function-2
def  print_settings(setonlist, setofflist, setdefaultlist) :

    # implement function-2 as instructed
    non = len(setonlist)
    non2 = len(setofflist)
    non3 = len(setdefaultlist)
    print("1) Set On keywords:")
    for i in range(0, non):
        print("\t"+str((i+1))+")", setonlist[i])
    print("2) Set Off keywords:")
    for i in range(0, non2):
        print("\t"+str((i+1))+")", setofflist[i])
    print("3) Set Default keywords:")
    for i in range(0, non3):
        print("\t"+str((i+1))+")", setdefaultlist[i])

    pass

# Main program, do not modify it.
if __name__ == "__main__":
    filename="my_config.txt"
    setonlist, setofflist, setdefaultlist=classify_settings(filename)

    #call function to print items in the lists.
    if setonlist or setofflist or setdefaultlist:
        print_settings(setonlist, setofflist, setdefaultlist)
    else:
        print("No settings found on the file.")
