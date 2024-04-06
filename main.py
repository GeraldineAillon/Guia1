from functions import showAll,delete_by_id,showOneById,update_by_id,addOne,showOnebyTitle,showOnebyAuthor

#Menu

print("\nThis is a book directory, you can search for a specific book, add new books,\ndelete existing ones,update them and see all the books available.\n")

def menu():
    print("\n/*/ MAIN MENU /*/\n")
    print("1: Add new book\n2: Look for a book\n3: Edit book\n4: Delete book\n5: Show all books\n6: Quit\n")
    while True:
                try:
                        option= int(input("Type the number of the option you want: "))
                        break
                except ValueError:
                        print("Invalid character, please enter a number")
                
    state=True
    while state==True:
        if(option==1):
                print("\n")
                state=addOne()
        elif option==2:
                print("1. Search by ID\n2. Search by tittle\n3. Search by author")
                while True:
                        try:
                                opt=int(input("?: "))
                                
                        except ValueError:
                                print("!!!\t Just type the number of the option please")
                        else:
                                if(opt==1):
                                        id=input("Enter the book id: ")
                                        state=showOneById(id)
                                        break
                                elif(opt==2):
                                        title=input("Ente the title of the book: ")
                                        state=showOnebyTitle(title)
                                        break
                                elif(opt==3):
                                        author=input("Enter the Author's name: ")
                                        state=showOnebyAuthor(author)
                                        break
                                else:
                                      print("!!!\t Enter a VALID option") 
                                      continue 
                                
        elif option==3:
                print("\n")
                id=input("Enter the book id: ")
                state=update_by_id(id)
        elif option==4:
                print("\n")
                id=input("Enter the book id: ")
                state=delete_by_id(id)
        elif option==5:
                print("\n")
                state=showAll()
        elif option==6:
                print("\n")
                print("Exiting...")
                exit()             
        else:
            while True:
                try:
                    print("\n")
                    option = int(input("Please enter a valid option: "))
                    break
                except ValueError:
                    print("Invalid option!")
                    
    if(state==False):
        menu()
menu()
