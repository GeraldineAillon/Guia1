from functions import showAll,delete_by_id,showOneById,update_by_id,addOne,showOnebyTitle,showOnebyAuthor, showByGenre


#Se imprime este mensaje la primera vez que se ejecute el programa
print("\nThis is a book directory, you can search for a specific book, author or genre, add new books,\ndelete existing ones,update them and see all the books available.\n")

#Menu principal
def menu():
    print("\n/*/ MAIN MENU /*/\n")
    print("1: Add new book\n2: Search\n3: Edit book\n4: Delete book\n5: Show all books\n6: Quit\n")
    while True:
                try:
                        option= int(input("Type the number of the option you want: "))
                        break
#se valida que el usuario no ingrese letras ni numeros que no esten en la lista.
#tambien se considera cualquier interrucion por teclado, por ejemplo ctrl+c
                except ValueError:
                        print("Invalid character, please enter a number")
                except KeyboardInterrupt:
                       print("\nClosing program")
                       exit()  
    state=True
    while state==True:
        if(option==1):
                print("\n")
                state=addOne()
        elif option==2:
                print("\n1. Search by ID\n2. Search by title\n3. Search by author\n4. Search by genre\n5. Return to main menu")
                while True:
                        try:
                                opt=int(input("?: "))
#se valida que el usuario no ingrese letras ni numeros que no esten en la lista.
#tambien se considera cualquier interrucion por teclado, por ejemplo ctrl+c
                        except ValueError:
                                print("!!!\t Just type the number of the option please")
                        except KeyboardInterrupt:
                               print("\nClosing program")
                               exit()
                        else:
                                if(opt==1):
                                        try:
                                                id=input("Enter the book id: ")
                                        except KeyboardInterrupt:
                                                print("\nClosing program")
                                                exit()
                                        state=showOneById(id)
                                        break
                                elif(opt==2):
                                        try:
                                                title=input("Ente the title of the book: ")
                                        except KeyboardInterrupt:
                                                print("\nClosing program")
                                                exit()
                                        state=showOnebyTitle(title)
                                        break
                                elif(opt==3):
                                        try:
                                                author=input("Enter the Author's name: ")
                                        except KeyboardInterrupt:
                                                print("\nClosing program")
                                                exit()
                                        state=showOnebyAuthor(author)
                                        break
                                elif(opt==4):
                                        try:
                                                genre=input("Enter a genre: ")
                                        except KeyboardInterrupt:
                                                print("\nClosing program")
                                                exit()
                                        state=showByGenre(genre)
                                        break
                                elif(opt==5):
                                       state=False
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
                    option = int(input("Please enter a valid option: "))
                    break
                except ValueError:
                    print("Invalid option!")
                    
    if(state==False):
        menu()
menu()
