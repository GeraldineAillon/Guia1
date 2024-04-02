from functions import showAll,delete_by_id,showOne,update_by_id,addOne

#Menu

def menu():
    print("/*/ MAIN MENU /*/\n")
    print("This is a book directory, you can add new books, delete existing ones,\nupdate them and see all the books available.\n")
    print("1: Add new book\n2: Look for a book\n3: Edit book\n4: Delete book\n5: Show all books\n6: Quit")
    option= int(input("Type the number of the option you want: "))
    state=True
    while state==True:
        if(option==1):
            state=addOne()
        elif option==2:
            id=input("Enter the book id: ")
            state=showOne(id)
        elif option==3:
            state=update_by_id()
        elif option==4:
            id=input("Enter the book id: ")
            state=delete_by_id(id)
        elif option==5:
            state=showAll()
        elif option==6:
            print("Exiting...")
            exit()
        else:
            print("Invalid option!")
            option = int(input("Please enter a valid option: "))    
    if(state==False):
        print("\n")
        menu()
menu()
