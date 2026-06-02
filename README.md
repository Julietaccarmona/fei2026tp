Trabajo Practico Nro. 1

El presente documento tiene como finalidad servir como guía para la confección del tercer Trabajo Practico. El motivo final del trabajo es la creación desde cero de un proyecto completamente
funcional, con un backend utilizando el framework Django de Python, conectado a una Base de Datos Postgres.

El desarrollo, conclusión y entrega del mismo sera en un repositorio git creado por el alumno.

IMPORTANTE:
En cada punto de esta guía se indicara si corresponde realizar un commit y push al repositorio git con el comentario apropiado que refleje el motivo de los cambios.

Requerimientos
Para la confección del trabajo se requiere una PC con Docker y docker-compose instalado, un editor de texto, y contar con una cuenta de GitHub, ademas, el comando “http” (httpie), o similar, para testear las APIs.

Desarrollo
1) Tareas previas
En la PC de trabajo crear una carpeta vacía con el nombre “fei2026tp”, la misma servirá de almacenamiento a todos los datos del proyecto. Se puede utilizar el repositorio del último TP anterior de PWA.
Dentro de esta carpeta se deben crear los siguientes archivos vacíos: dockercompose.yml, .gitignore y .env-dist

2) Creación del proyecto en GitHub
En el sitio web de GitHub se debe crear un proyecto publico con el mismo nombre que la carpeta creada en el punto 1. Una vez creado el proyecto, si no se reutiliza el repositorio anterior, se deberá inicializar como repositorio git la carpeta del punto 1 y se deberá realizar el primer commit (Commit inicial)
donde se suben al repositorio los 3 archivos existentes en nuestro proyecto.

3) Base de Datos
En el archivo docker-compose.yml se deberá agregar la sección que permita levantar una instancia de Base de Datos Postgresql versión 16. Para esto se debe tener en cuenta lo siguiente:
 a.- Indicar en la sección un volumen, mapeado a una carpeta dentro del proyecto, donde Postgres pueda persistir los archivos y carpetas de la Base de Datos.
 b.- Indicar en el archivo .gitignore la carpeta del punto “a” a fin de evitar que la misma suba al repositorio git.
 c.- Utilizar variables de entorno para indicar a Postgres el nombre de la Base de Datos, el Usuario y la Password.
 d.- Las variables de entorno deben estar reflejadas a modo de ejemplo en el archivo .env-dist y a su vez en el archivo funcional a crear .env, este ultimo también ignorado en .gitignore.
 e.- El contenedor de la Base de Datos debe exportar el puerto 5432 para permitir conexiones desde la PC de usuario desarrollador.

Una vez que se compruebe el correcto funcionamiento se deberá hacer un commit y push con los cambios realizados.

4) Creación del Backend
Dentro de la carpeta del proyecto crear una nueva carpeta, de nombre backend, que sirva para el almacenamiento del proyecto DJango. Agregar al archivo docker-compose.yml un nuevo contenedor, con nombre django, con una imagen con nombre alusivo (tipo fei2026tp) y una versión preliminar.
Esta imagen debemos construirla especialmente para nuestro proyecto, con las dependencias necesarias. Para esto tienen que: En la carpeta “config/django-image” crear el archivo Dockerfile que se base en la imagen python:3.12.2-bookworm que sea capaz de incluir las dependencias enumeradas en el archivo
requirements.txt e incluir un script de bash para arrancar el servicio http de desarrollo de Django dentro del contenedor. El script debe poder crear una proyecto vacío en caso que no exista ninguno, intentar crear y
aplicar migraciones, crear un “superusuario” con variables de entorno definidas en el archivo .env y , finalmente, arrancar el servicio de desarrollo.

En este punto, el proyecto debe poder quedar funcionando con la configuración por default en el puerto 8000.

5) Conectar Backend con BBDD
Se debe conectar el backend a la base de datos. Los datos de conexión deben salir de variables de entorno definidas en el .env. Al levantar el proyecto debemos ver que se aplican las migraciones en la nueva base de datos, y comprobar que se crea el usuario “superusuario”.
Una vez comprobado que funciona todo correctamente, hacer un commit y push.

6) Script de soporte para Shell
En la raíz de nuestro proyecto debemos crear una carpeta “bin” para almacenar nuestros scripts de soporte. Primeramente tenemos que crear un script con el nombre shell.sh que nos permita acceder de forma mucho mas fácil al Shell de DJango dentro del contenedor del backend. De tal modo que
ejecutado este script quedemos en la consola del Django Shell. Una vez comprobado que funciona todo correctamente, hacer un commit y push.

7) Script de soporte para Python
Dentro de la carpeta “bin” creada en el punto 1 debemos crear un script con el nombre python.sh de tal forma que todos los parametros que reciba este script seran pasados al comando Python dentro del contenedor. De esta manera podremos ejecutar el comando python del contenedor
desde la consola de nuestro sistema operativo. Una vez comprobado que funciona todo correctamente, hacer un commit y push.

8) Creación de la Aplicación
Usando el script python.sh del punto anterior crear una nueva Application en Django. La aplicación debe tener el nombre “aulas”.
Una vez creada, activarla dentro del archivo settings.py del proyecto.

9) Creación de Tablas
Para crear las siguientes tablas debemos crear los models correspondientes dentro de la aplicación Aulas.
Tabla             Campos           Tipo
carrera             id           Autonumerico, Clave Primaria,
                 nombre          String, no nulo, de 128 caracteres.

Tabla             Campos           Tipo
profesor             id            Autonumerico, Clave Primaria,
                  nombre           String, no nulo, de 128 caracteres.
                  apellido         String, no nulo, de 128 caracteres.
                  mostrar          String, no nulo, de 256 caracteres.

Tabla             Campos           Tipo
materia             id             Autonumerico, Clave Primaria,
                  nombre           String, no nulo, de 128 caracteres.
                cant_alumnos       Numérico, no nulo, valor por default 5.
                id_carrera         Clave foranea de la tabla carrera
                id_profesor        Clave foranea de la tabla profesor

Tabla             Campos           Tipo
aula                 id            Autonumerico, Clave Primaria,
                descripcion        String, no nulo, de 128 caracteres.
                ubicación          String, no nulo, de 128 caracteres.
                cant_proyector     Numero, valor por default 0
                aforo              Numero, valor por default 0
                es_climatizada     Booleano, valor por default falso

                
Una vez creados los models reiniciar los contenedores y comprobar que las migraciones se generaron y ejecutaron correctamente, hacer un commit y push.

10) Creación de tablas relacionadas
Seguidamente se deben crear los models de las siguientes tablas:

Tabla              Campos           Tipo
reserva_aula         id             Autonumerico, Clave Primaria,
                    id_aula         Clave foránea de la tabla aula
                    fh_desde        Fecha-Hora desde
                    fh_hasta        Fecha-Hora hasta
                  observacion       Texto de 256 caracteres.

Tabla              Campos           Tipo
horario_materia      id             Autonumerico, Clave Primaria,
                  id_materia        Clave foránea de la tabla materia
                  id_reserva        Clave foránea de la tabla reserva
                  fh_desde          Fecha-Hora desde
                  fh_hasta          Fecha-Hora hasta

Una vez creados los models reiniciar los contenedores y comprobar que las migraciones se generaron y ejecutaron correctamente, hacer un commit y push.

12) DRF & Serializadores
Debemos asegurarnos que en nuestro contenedor esta instalado el aquete DRF (Django Rest Framework) y el mismo se encuentra activo en nuestro settings.py. Por cada una de las tablas (models) creadas en el punto 9 debemos crear su correspondiente model serializer, de forma que queden disponibles para la creación de las APIs Rest.

13) API Rest Carrera
En nuestras views debemos crear una clase con el nombre CarreraMixin basada en 3 clase de DRF: GenericAPIView, ListModelMixin y CreateModelMixin. Y que utilice el serializador de Carrera como helper para resolver el acceso a la base de datos. Luego debemos asegurarnos de crear las URLs necesarios para que puedan ser invocadas nuestras funciones desde la App.

14) API Rest Profesor
En las views debemos crear la clase ProfesorMixinDetail basada en GenericAPIView, RetrieveModelMixin, UpdateModelMixin y DestroyModelMixin. Que utilice el serializador de Profesor ya creado.
Debemos asegurarnos de crear las URLs necesarias para la correcta ejecución de las APIs.
