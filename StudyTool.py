import csv
import random

#create empty dictionary
dictionary = {}

#defining function to import csv date from a file(filename)
def load(filename):
    #for each row of the file opened(dictionary.csv) in reader(r) mode
    for rows in csv.reader(open(filename, 'r')):
        #assign the first row to the key, and second row to the value
        dictionary[rows[0]] = rows[1]

#defining function to export csv to a file(filename)
def save(filename):
    #assigns opening/creating a file in write(w) mode
    file = csv.writer(open(filename, "w"))
    #for field 1 and field 2 of each dictionary item;
    for key, value in dictionary.items():
        #write field 1 and field 2 into the opened file
        file.writerow([key, value])

def showall():
    for row in dictionary:
        print ()
        print (row + ":", dictionary[row])

def delete():
    deleteterm = input("What do you want to delete? ").capitalize()
    del dictionary[deleteterm]

def study():
    temp = 'studying'
    points = 0
    print ("* guess the term for points")
    choice = input("Study [term] or [definition*]? ").lower().strip()
    if choice == 'term':
        print ()
        print ("To exit, enter 'quit'.")
        print ()
        while temp != 'quit':
            randomized = list(dictionary.items())
            random.shuffle(randomized)
            dictionized = dict(randomized)
            for term in dictionized:
                print ()
                print ("    ", term)
                print ()
                temp = input().lower().strip()
                if temp == 'quit':
                    print ()
                    break
                print ()
                print (dictionized[term])
                print ()
                temp = input().lower().strip()
                if temp == 'quit':
                    print ()
                    break

    elif choice == 'definition':
        print ()
        print ("To exit, enter 'quit'.")
        print ()
        while temp != 'quit':
            randomized = list(dictionary.items())
            random.shuffle(randomized)
            dictionized = dict(randomized)
            for term in dictionized:
                print ()
                print (dictionized[term])
                print ()
                temp = input().lower().strip()
                if temp == 'quit':
                    print ("points:", points)
                    print ()
                    break
                elif temp == term.lower():
                    points += 1
                    print ("points :", points)
                    print ()
                else:
                    print ()
                    print ("    ", term)
                    print ()
                    temp = input().lower().strip()
                    if temp == 'quit':
                        print("points:", points)
                        print ()
                        break
    else:
        print('invalid option')

def add():
    term = (input("Enter term: ")).capitalize()
    if term in dictionary:
        print ("Invalid entry")
        
    else:
        definition = (input("Enter definition for term: "))
        dictionary[term] = definition

while True:
    print()
    print("MAIN MENU")
    print("OPTIONS: [Study] [Edit] [Quit]")
    choice = input("What do you want to do? ").lower().strip()
    if choice == 'study':
        study()

    elif choice == 'edit':
        while True:
            print ()
            print ("EDIT MENU")
            print("OPTIONS: [add] [delete] [load] [save] [show] [back]")
            choice = input("what do you want to do? ").lower().strip()

            if choice == 'add':
                add()

            elif choice == 'load':
                loadname = input ("filename: ")
                try:
                    load(loadname)
                    print("load complete")
                except:
                    print("load unsuccessful")
                break
            
            elif choice == 'delete':
                try:
                    delete()
                    print ("delete complete")
                except:
                    print ("delete unsuccessful")

            elif choice == 'save':
                print ("*IF A FILE HAS THE SAME NAME, IT WILL OVERWRITE THAT FILE*")
                savename = input ("What do you what the file to be named? ")
                try:
                    save(savename)
                    print ("save complete")
                except:
                    print ("save unsuccessful")

            elif choice == 'show':
                showall()

            elif choice == 'back':
                break
            
            else:
                print ()
                print ("invalid option")

    elif choice == 'quit':
        break
        
    else:
        print ()
        print ("invalid option")
