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
        record={"Title":title, "Author":author,"Year":year,"MovieAdaptation":movieadp,"Publisher":pub,"genres":gen}
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
        _id=ObjectId(book_id)
        new_doc={
         
        }
        collection.find_one_and_update({{"id":_id}, new_doc})

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







