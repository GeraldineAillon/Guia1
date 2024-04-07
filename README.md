# DESCRIPCION DEL PROGRAMA

Aplicacion de consola desarrollada en Python usando MongoDB, permite administrar una base de datos de libros mediante la creacion,
actualización y borrado de los metadatos, asi como también permite mostrar todos o algun libro en específico junto con toda la información.

**_Por comodidad el programa fue escrito en inglés, aun así, es posible registrar "libros" (documentos) en español_**

# REQUERIMIENTOS

-> Python 3.12 o mayor

-> MongoDB Atlas

-> pymongo

-> python-dotenv

# USO DEL PROGRAMA

1. Instalar las dependencias del proyecto (pymongo y python-dotenv)
    -> En Windows con el comando <py -m pip install [nombre libreria]>
    -> En linux con el comando <pip install [nombre libreria]>

2. Para ejecutar el programa por consola escribir el comando "python3 main.py" (**py main.py** en windows)
aparecerá un menu con 6 opciones:

    1. Add new book
    2. Search
    3. Edit book
    4. Delete book
    5. Show all books
    6. Quit

se debe insertar solo el numero de la opcion que se desee ejecutar.

# Opciones del menu y que hace cada una
### Consideraciones

Siempre que se solicite ingresar una opcion de cualquier menu ésta debe ser **solo** el número, de lo contrario lanza un mensaje de error solicitando ingresar la opcion correctamente.

Cuando se habla de _id_ se refiere **siempre** al id asignado automaticamente por MongoDB, el cual es único por cada documento insertado. Si el id es tipeado erroneamente o este no existe, se lanza un mensaje de error o advertencia segun la query que se esté realizando.

### 1. Insertar un nuevo libro(documento)

Se van solicitando uno por uno los campos del libro y al finalizar se guarda en la coleccion y se muestra por pantalla el documento completo.

### Ejemplo de inserción:

    Title: Carmilla
    Author: Joseph Sheridan Le Fanu
    Year: 1872
    Does it have a movie adaptation?(yes/no): yes
    Original Publiser: The Dark Blue
    Genres (if more than one, separate by commas in the same line): Gothic, horror
Al finalizar, si todos los campos han sido ingresados correctamente, el programa devuelva el documento tal cual se guardó en la colección. Para el ejemplo se vería asi:

     {'_id': ObjectId('661318a5b3969d15eee28f27'),
        'Title': 'Carmilla',
        'Author': 'Joseph Sheridan Le Fanu',
        'Year': 1872,
        'MovieAdaptation': 'yes',
        'Publisher': 'The Dark Blue',
        'genres': 'Gothic, horror'}
### 2. Buscar libros
**Considerar:** da igual si los nombres de libros, autor o genero se escriben con mayusculas o minusculas ya que la busqueda no toma en cuenta esos detalles y entrega igualmente los resultados que coincidan.

Esta opcion despliega 5 opciones de busqueda:

1. **Buscar por ID:** Se ingresa el id del libro a buscar y muestra toda la informacion del libro.

2. **Buscar por título:** Se escribe el titulo ya sea completo o solo una parte, y se muestran todos los libros que coinciden con la busqueda. Si el titulo del libro no existe en la colección, se da la opcion de agregarlo inmeediatamente sin tener que salir al menu principal. En este caso el proceso es el mismo de la opcion 1.
3. **Buscar por autor:** Se ingresa el nombre del autor y se muestran todos los libros escritos por el. No es necesario escribir todo el nombre de autor, con el apellido o nombre bastará para que se muestren todos los libros que coincidan con la busqueda.(P.ej: Lovecraft)
4. **Buscar por género:** Se ingresa un genero y se muestran todos los libros que coincidan con la busqueda. (P.ej: Horror)
5. **Volver a menu principal:** Eso. Devuelve al menú principal.

### 3. Editar un libro


