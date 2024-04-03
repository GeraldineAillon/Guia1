#DESCRIPCION DEL PROGRAMA

Aplicacion de consola desarrollada en Python usando MongoDB, permite administrar una base de datos de libros mediante la creacion,
actualización y borrado de los metadatos, asi como también permite mostrar todos o algun libro en específico junto con toda la información.

#REQUERIMIENTOS

> Python 3.12 o mayor
> MongoDB Atlas
> pymongo
> dotenv

#USO DEL PROGRAMA

1. Instalar las librerias necesarias (pymongo y dotenv) con el comando "pip install <libreria>"
2. Configurar el archivo .env con el token de acceso y el nombre de la base de datos 
3. Para ejecutar el programa por consola escribir el comando "python3 main.py", aparecerá un menu con 6 opciones:
    1.añadir nuevo libro
    2. buscar un libro por su id
    3. editar un libro por su id
    4. borrar un libro por su id
    5. mostrar todos los libros
    6. salir del programa
se debe insertar el numero de la opcion que se desee ejecutar, luego segun la opcion escogida se solicitaran los datos necesarios segun:
    1. Solicita anotar cada uno de los valores del libro que se va a guardas
