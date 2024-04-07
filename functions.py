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
    print("Type the book's details\n")

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
            "Genres":gen
        }
        collection.insert_one(record)
        book=collection.find_one(record)
    except errors.BSONError:
        print("An error ocurred, please try again")
    else:
        print("\nYour book was saved sucesfully :) Here are the details: \n")
        pprint.pprint(book,sort_dicts=False )

    return(False)

#op 2: Mostrar libros segun algun parametro

#por titulo: busca e imprime el o los libros que concuerden con el titulo, ya sea por una palabra o el titulo completo
# Si el titulo del libro no está, pregunta si se desea agregar, dando opcion a insertar inmediatamente

def showOnebyTitle(book_name):
    query={"Title": {"$regex": book_name,"$options": "i"}}
    count = collection.count_documents(query)
    
    if (count > 0):
        book=collection.find(query)
        for aux in book:
            print("\n")
            pprint.pprint(aux, sort_dicts=False)
    else:
        print("The book you're looking for doesn't exist in the database\n")
        ad=input("Would you like to add it?(y/n): ")
        if(ad=="y"):
            print("\n") 
            addOne()
    return(False)

#Por id: busca un solo libro en especifico por la id unica del documento
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

#por autor: busca y muestra todos los libros de un autor
def showOnebyAuthor(author):
    query={"Author": {"$regex": author,"$options": "i"}}
    books=collection.find(query)
    if(books):
        for aux in books:
            pprint.pprint(aux, sort_dicts=False)
    else:
        print("The author you're lookign for doesn't exist in the database")
    return(False)

#por genero: busca y muestra todos los libros que tengan algun genero en comun
def showByGenre(genre):
    query={"Genres": {"$regex":genre, "$options":"i"}}
    books=collection.find(query)
    if(books):
        for aux in books:
            print("\n")
            pprint.pprint(aux, sort_dicts=False)
    else:
        print("No book matches with that genre")
    return(False)

#op 3 actualiza los datos del documento solicitando la _id correspondiente. Se hace manejo de errores en caso
# de problemas con el _id

def update_by_id(book_id):
    try:
        _id=ObjectId(book_id)
    except errors.InvalidId:
        print("\nYou entered an invalid ID")
        return(False)
    else:
        print("This is the actual book:\n")
        pprint.pprint(collection.find_one({"_id":_id}),sort_dicts=False)
        print("\n1. Title\n2. Author\n3. Year\n4. Movie adaptation?\n5. Publisher\n6. Genres")

        while True:
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
                            value= int(input("New year: "))
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
        print("\nThe document doesn't exist or couldn't be deleted\nNothing was deleted\n")
    return(False)

#op 5: Muestra toda la coleccion en la base de datos
def showAll():
    data_set = collection.find()
    for document in data_set:
        pprint.pprint(document,sort_dicts=False)
        print("\n")
    
    return(False)







