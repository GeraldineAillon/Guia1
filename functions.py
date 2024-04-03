from db_conection import client
from bson.objectid import ObjectId
from bson import errors
import pprint 


main_db=client.guia1

collection = main_db.books


#------Functions--------#

#op 1
def addOne():
    print("\nAdding new book...\n")
    print("Type the book's details:\n")
    title=input("Title: ")
    author=input("Author: ")
    year=int(input("Year: "))
    movieadp=input("Movie Adaptation?: ")
    pub=input("Publisher: ")
    gen=input("Genres (if more than one, separate by commas in the same line): ")
    try:
        record={
            "Title":title, 
            "Author":author,
            "Year":year,
            "MovieAdaptation":movieadp,
            "Publisher":pub,
            "genres":gen
        }
        collection.insert_one(record)
        book=collection.find_one(record)
    except errors.BSONError:
        print("An error ocurred, please try again")
    else:
        print("\nYour book was saved sucesfully :)\nHere are the details: \n")
        pprint.pprint(book,sort_dicts=False )

    return(False)

#op 2
def showOne(book_id):
    try:
        _id=ObjectId(book_id)
        book= collection.find_one({"_id":_id})
    except errors.InvalidId:
        print("! ! ! ! ! ! ! ! !\nInvalid id format\n! ! ! ! ! ! ! ! !")
    else:
        if book:
            pprint.pprint(book,sort_dicts=False)
        else:
                print("\nThe book you're looking for doesn't exist in the database :( )")
    return(False)

#op 3 
def update_by_id(book_id):
    try:
        _id=ObjectId(book_id)

    except errors.InvalidId:
        print("You entered an invalid ID")
    else:
        print("Enter the number of the field you want to modify:\n1. Title\n2. Author\n3. Year\n4. Movie adaptation?\n5. Publisher\n6. Genres")
        old_data=collection.find_one({"_id":_id})
        flag =True
        while flag:
            key=int(input(": "))
    
            if(key==1):
                value=input("Enter the new value: ")
                updated_value={'$set':{"Title":value}}
                flag=set_key(old_data,updated_value)
            elif(key==2):
                value=input("Enter the new value: ")
                updated_value={'$set':{"Author":value}}
                flag=set_key(old_data,updated_value)
            elif(key==3):
                value= int(input("Enter the new value: "))
                updated_value={'$set':{"Year":value}}   
                flag=set_key(old_data,updated_value)
            elif(key==4):
                value=input("Enter the new value: ")
                updated_value={'$set':{"MovieAdaptation":value}}
                flag=set_key(old_data,updated_value)
            elif(key==5):
                value=input("Enter the new value: ")
                updated_value={'$set':{"Publisher":value}}
                flag=set_key(old_data,updated_value)
            elif(key==6):
                value=input("Enter the new value: ")
                updated_value={'$set':{"Genres":value}}
                flag=set_key(old_data,updated_value)
            else:
                print("Invalid option!")
                key = int(input("Please enter a valid option: ")) 

            res=input("Do you want to update another field of this book? (y/n): ")
            if(res=='n'):
                print("Your updated book looks like this: \n")
                pprint.pprint(collection.find_one({"_id":_id}),sort_dicts=False)
                return(False)
            elif(res=='y'):
                update_by_id(book_id)
#setting the updated value
def set_key(old,new):
    try:
        collection.update_one(old,new)
    except errors.BSONError:
        print("Your data could not be updated")
    else:
        print("Data updated succesfully")

    return (False)


#op 4
def delete_by_id(book_id):
    try:
        _id=ObjectId(book_id)
        aux=collection.delete_one({"_id":_id})
    except errors.InvalidId:
        print("! ! ! ! ! ! ! ! !\nInvalid id format\nnothing was deleted\n! ! ! ! ! ! ! ! !")
    else:
        if(aux):
            print("\nDocument deleted succesfully")
        else:
             print("\nThe docuement could not be deleted")
    return(False)

#op 5
def showAll():
    data_set = collection.find()
    for document in data_set:
        pprint.pprint(document,sort_dicts=False)
    
    return(False)







