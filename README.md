# Descripción del programa

Aplicacion de consola desarrollada en Python usando MongoDB, permite administrar una base de datos de libros mediante la creacion,
actualización y borrado de los metadatos, asi como también permite mostrar todos o algun libro en específico junto con toda la información.

**_Por comodidad el programa fue escrito en inglés, aun así, es posible registrar "libros" (documentos) en español_**

# Requerimientos

-> Python 3.12 o mayor

-> MongoDB Atlas

-> virtualenv

-> pymongo

-> python-dotenv

# Uso del programa

Primeramente hay que crear un entorno virtual en la carpeta donde se guardará el proyecto, para eso hay que entrar por consola hasta la ruta de la carpeta, una vez dentro creamos el entorno virtual.

    >En linux
    python3 -m venv <nombre del entorno>

    > En windows:
    py -m venv <nombre del entorno>
**Para mayor información sobre como crear un entorno virtual revisar [este post](https://openwebinars.net/blog/entornos-de-desarrollo-virtuales-con-python3/)**
    

Luego se deben instalar las dependencias del proyecto: **_pymongo_** y **_python-dotenv_**

    > En Windows con el comando 
    py -m pip install [nombre libreria]

    > En linux con el comando 
    pip install [nombre libreria]

Una vez intaladas las dependencias se podrá ejecutar el programa por consola escribiendo el comando _python3 main.py_ (**py main.py** en windows). Aparecerá un menu con 6 opciones:

    1. Add new book
    2. Search
    3. Edit book
    4. Delete book
    5. Show all books
    6. Quit

se debe escribir solo el numero de la opcion que se desee ejecutar, de lo contrario saltará un mensaje de advertencia.

## Opciones del menu y que hace cada una
### Consideraciones

Siempre que se solicite ingresar una opcion de cualquier menu, esta debe ser **solo** el número, de lo contrario lanza un mensaje de error solicitando ingresar la opcion correctamente.

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
Al finalizar, si todos los campos han sido ingresados correctamente, el programa devuelve el documento tal cual se guardó en la colección. Para el ejemplo se vería asi:

     {'_id': ObjectId('661318a5b3969d15eee28f27'),
        'Title': 'Carmilla',
        'Author': 'Joseph Sheridan Le Fanu',
        'Year': 1872,
        'MovieAdaptation': 'yes',
        'Publisher': 'The Dark Blue',
        'Genres': 'Gothic, horror'}
### 2. Buscar libros
**Considerar:** da igual si los nombres de libros, autor o genero se escriben con mayusculas o minusculas _en esta sección_, ya que la busqueda no toma en cuenta esos detalles y entrega igualmente los resultados que coincidan.

Esta opcion despliega 5 opciones de busqueda:

1. **Buscar por ID:** Se ingresa el id del libro a buscar y muestra toda la informacion del libro.

2. **Buscar por título:** Se escribe el titulo ya sea completo o solo una parte, y se muestran todos los libros que coinciden con la busqueda. Si el titulo del libro no existe en la colección, se da la opcion de agregarlo inmediatamente sin tener que salir al menu principal. En este caso el proceso es el mismo de la opcion 1: insertar un libro.
3. **Buscar por autor:** Se ingresa el nombre del autor y se muestran todos los libros escritos por el. No es necesario escribir todo el nombre de autor, con el apellido o nombre bastará para que se muestren todos los libros que coincidan con la busqueda.(P.ej: Lovecraft)
4. **Buscar por género:** Se ingresa un genero y se muestran todos los libros que coincidan con la busqueda. Un libro puede tener mas de un genero pero si incluye el de la busqueda se mostrará igual. (P.ej: Horror)
5. **Volver a menu principal:** Eso. Devuelve al menú principal.

### 3. Editar un libro

En esta sección se da la opción de editar o _actualizar_ los datos de algun libro, siempre que se tenga el id correspondiente.
Una vez ingresado el id se despliega otro menu consultando cual es el campo que se desea cambiar. Siempre que se edite un campo el programa pregunta si desea continuar editando o no, si se ingresa la opcion **"y"** se vuelve a solicitar seleccionar alguno de los campos dispnibles para editar, si se ingresa cualquier otra letra y/o número se considera que no desea continuar y muestra el nuevo libro con los campos actualizados.

### 4. Borrar un libro por el id

Solo se solicita el id del libro que se quiera borrar y se elimina inmediatamente. Si el id igresado no es valido o no existe, se devuelva al menu principal.

### 5. Mostrar todos los libros

Esta opción muestra todos los libros existentes en la colección y devuelve al menu principal.

### 6. Salir/cerrar

Esta opción cierra y/o termina el programa en la consola.

# Esquema de la base de datos

El esquema de la coleccion en la base de datos es como se muestra a continuación:

    {"_id": ObjectId
     "Title": "String",
     "Author": "String",
     "Year": "int",
     "MovieAdaptation":"String",
     "Publisher":"String",
     "Genres":"String"    
    }

→El campo _"_id"_ es un identificador único de cada libro y es automáticamente generado por MongoDB.

→El campo _"Title"_ es una cadena de caractéres que indica el nombre del libro

→El campo _"Author"_ es una cadena de caractéres que indica el autor del libro

→El campo _"year"_ es un entero que indica el año de publicación del libro

→El campo _"MovieAdaptation"_ es una cadena de caractéres que indica si un libro tiene una adaptacion a película o no.

→El campo _"Publisher"_ es una cadena de caractéres que indica cual fue la editorial o editor en publicar la primera edicion del libro

→El campo _"Genres"_ es una cadena de caractéres que indica cuales son los generos literarios con los cuales se asocia un libro





