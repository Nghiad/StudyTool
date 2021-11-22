import csv
import random

dictionary = {}                                                         #create dictionary
          
def load(filename):                 #loop to insert data from a csv file into dictionary
    for rows in csv.reader(open(filename, 'r')):
        dictionary[rows[0]] = rows[1]

                                
def save(filename):             #loop to write each key, value from dictionary to csv file
    file = csv.writer(open(filename, "w"))
    for key, value in dictionary.items():
        file.writerow([key, value])

def showall():                                  #loops print for key, value of dictionary
    for row in dictionary:
        print ()
        print (row + ":", dictionary[row])
        
def add():                                  #get input, add key:value pair into dictionary
    term = (input("Enter term: ")).capitalize()
    if term in dictionary:
        print ("Invalid entry")
        
    else:
        definition = (input("Enter definition for term: "))
        dictionary[term] = definition

def delete():                                       #get input, then delete key:value pair
    deleteterm = input("What do you want to delete? ").capitalize()
    del dictionary[deleteterm]

def study():                                
    temp = 'studying'                                          
    points = 0
    print ("* guess the term for points")
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
                print ("points:", points)           #user can guess the term for points
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

if __name__ == '__main__':                                       #main program loop for UI
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
