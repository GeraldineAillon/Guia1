from db_conection import client
from bson.objectid import ObjectId
from bson import errors
import pprint 
import datetime

#se obtiene la base de datos sobre la cual se trabajará 
main_db=client.guia1

#Se asigna la coleccion con la que se van a ejecutar las consultas
collection = main_db.books

#Obtenemos el año del sistema para evitar conflictos con las fechas
system_year=datetime.datetime.now().year
#------Functions--------#

#op 1: La primera funcion es la query para añadir nuevos documentos, donde se preguntan
#      los datos de acuerdo a el esquema establecido para la coleccion en la base de datos.

def addOne():
    print("Adding new book...\n")
    print("Type the book's details:\n")
    title=input("Title: ")
    author=input("Author: ")
    #bucle para que no ingrese letras o años mayores al actual
    while True:
        try:
            year= int(input("Year: "))
            if( year > system_year):
                print("¡¡Enter a vallid year!!") 
            else: break   
        except ValueError:
            print("Enter the whole year in numbers please(e.g:1990)")

    movieadp=input("Does it have a movie adaptation?(yes/no): ")
    pub=input("Original publisher: ")
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
        print("\nYour book was saved sucesfully :) Here are the details: \n")
        pprint.pprint(book,sort_dicts=False )

    return(False)

#op 2: Muestra un solo libro por
#titulo
def showOnebyTitle(book_name):
    query={"Title": {"$regex": book_name,"$options": "i"}}
    book=collection.find(query)
    if(book):
        for aux in book:
            pprint.pprint(aux, sort_dicts=False)
    else:
        print("The book you're lookign for doesn't exist in the database")
        ad=input(" Would you like to add it?(y/n): ")
        if(ad=="y"): addOne()
    return(False)

#id
def showOneById(book_id):
    try:
        _id=ObjectId(book_id)
        book= collection.find_one({"_id":_id})
    except errors.InvalidId:
        print("\n\t! ! ! ! ! ! ! ! !\tInvalid id format\t! ! ! ! ! ! ! ! !\n")
    else:
        if book:
            print("\n")
            pprint.pprint(book,sort_dicts=False)
            print("\n")
        else:
                print("\nThe book you're looking for doesn't exist in the database :(\n")
    return(False)

#autor
def showOnebyAuthor(author):
    query={"Author": {"$regex": author,"$options": "i"}}
    books=collection.find(query)
    if(books):
        for aux in books:
            pprint.pprint(aux, sort_dicts=False)
    else:
        print("The author you're lookign for doesn't exist in the database")
    return(False)

#op 3 
def update_by_id(book_id):
    try:
        _id=ObjectId(book_id)
    except errors.InvalidId:
        print("You entered an invalid ID")
    else:
        print("This is the actual book:\n")
        pprint.pprint(collection.find_one({"_id":_id}),sort_dicts=False)
        print("\n1. Title\n2. Author\n3. Year\n4. Movie adaptation?\n5. Publisher\n6. Genres")
        f=True

        while f==True:
            key=int(input("Enter the number of the field you want to modify: "))
            if(not isinstance(key,int)):
                print("Only enter the NUMBER of the option!")
            else:
                if(key==1):
                    value=input("Enter the new value: ")
                    collection.update_one({"_id":_id},{'$set':{"Title":value}})
                    res=input("Do you want to update another field of this book? (y/n): ")
                    if(res=="y"): continue
                    else:break
                elif(key==2):
                    value=input("Enter the new value: ")
                    collection.update_one({"_id":_id},{'$set':{"Author":value}})
                    res=input("Do you want to update another field of this book? (y/n): ")
                    if(res=="y"): continue
                    else:break
                elif(key==3):
                    while True:
                        try:
                            value= int(input("Enter the new value: "))
                            if( value > system_year):
                                print("¡¡Enter a vallid year!!") 
                            else: break   
                        except ValueError:
                            print("Enter the whole year in numbers please(e.g:1990)\n")
                    collection.update_one({"_id":_id},{'$set':{"Year":value}})
                    res=input("Do you want to update another field of this book? (y/n): ")
                    if(res=="y"): continue
                    else:break
                elif(key==4):
                    value=input("Enter the new value: ")
                    collection.update_one({"_id":_id},{'$set':{"MovieAdaptation":value}})
                    res=input("Do you want to update another field of this book? (y/n): ")
                    if(res=="y"): continue
                    else:break
                elif(key==5):
                    value=input("Enter the new value: ")
                    collection.update_one({"_id":_id},{'$set':{"Publisher":value}})
                    res=input("Do you want to update another field of this book? (y/n): ")
                    if(res=="y"): continue
                    else:break
                elif(key==6):
                    value=input("Enter the new value: ")
                    collection.update_one({"_id":_id},{'$set':{"Genres":value}})
                    res=input("Do you want to update another field of this book? (y/n): ")
                    if(res=="y"): continue
                    else:break
                else:
                    print("Invalid option!")
                    key = int(input("Please enter a valid option: "))
        print("Your updated book looks like this: \n")
        pprint.pprint(collection.find_one({"_id":_id}),sort_dicts=False)
        return(False)

#op 4: Borra un documento de la colección segun el id entregado, si el id no existe o esta incorrecto
#      se vuelve al menu principal
def delete_by_id(book_id):
    try:
        _id=ObjectId(book_id)
        aux=collection.delete_one({"_id":_id})
    except errors.InvalidId:
        print("! ! ! ! ! ! ! ! !Invalid id format! ! ! ! ! ! ! ! !\nnothing was deleted\n")
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
        print("\n")
    
    return(False)







