# AlertAR API

Esta API fue diseñada para ser usada y modificada por el Equipo de DataRockers para el proyecto AlertAR, más endpoints serán agregados según necesidad del proyecto y pueden ser consultados en la sección de docs de la API, en [el sitio de la AlertAR API](https://alertar-api.onrender.com/docs)

# Tabla de contenidos

1. [Cómo Ejecutar el Proyecto](#ejecutar)
2. [Guía de uso rápido](#usorapido)
3. [Funciones de la API](#funciones)
4. [Links](#links)
5. [Licencia](#licencia)
6. [Contacto](#contacto)

---

`<a name="ejecutar"></a>`

## Cómo Ejecutar el Proyecto

Para ejecutar el proyecto localmente, sigue estos pasos:

1. Clona el repositorio desde [GitHub](https://github.com/Aspirina180mg/PI01_Misael_Garcia_Torres).
2. Instala las dependencias del proyecto utilizando el archivo `requirements.txt`, abriendo el terminal en la carpeta raíz del proyecto y corriendo el comando `> pip install -r requirements.txt` en la consola
   1. Nota: el proyecto fué creado con Python 3.11.6, se recomienda usar la misma versión.
3. Prueba la api, utilizando el comando `uvicorn main:app --reload` en la carpeta raíz del proyecto, una vez realizado esto podrás ingresar al localhost para ver la documentación sobre su funcionamiento y probar algunas búsquedas.
4. Para probar la api debes ingresar a tu [localhost, se recomienda ingresar a la sección de docs (127.0.0.1:8000/docs)](127.0.0.1:8000/docs), al hacer modificaciones en la API, uvicorn las leerá y recargará de manera automática.

`<a name="usorapido"></a>`

## Guía de uso rápido

para utilizar la API, puedes hacer consultas utilizando el siguiente formato:

`Enlace/Endpoint/consulta`

Donde `Enlace` puede ser la URL de la API, como la dirección Local, `Endpoint` es la función a llamar y `Consulta` es el argumento a entregar al endpoint

Un ejemplo de uso sería `[alertar-api.onrender.com/inversor/](https://alertar-api.onrender.com/Inversor/texto)datarockers`, cuyo resultado devolvería el texto `srekcoratad`

`<a name="funciones"></a>`

## Funciones de la API

A medida que la API se vaya complejizando, se listarán aquí todas las funciones (Endpoints) incluidas en la misma,

1. **inversor():** Devuelve el texto de la consulta, pero invertido, en formato de diccionario como {"TextoInvertido" : "texto"}

para más información se puede consultar la documentación de la api en :
[https://alertar-api.onrender.com/docs](https://alertar-api.onrender.com/docs)

`<a name="links"></a>`

## Links

Repositorio: https://github.com/Aspirina180mg/AlertAR_API
Seguimiento de problemas: https://github.com/Aspirina180mg/AlertAR_API/issues

- En caso de bugs sensibles como vulnerabilidades de seguridad, por favor
  contacte directamente al correo misagtor@gmail.com en lugar de abrir un
  problema (issue), esto para agilizar el proceso de resolución.
- `<a name="licencia"></a>`

## Licencia

Este proyecto se distribuye bajo la [licencia MIT](https://choosealicense.com/licenses/mit/). Consulta el archivo `LICENSE.txt` para obtener más detalles.

`<a name="contacto"></a>`

## Contacto

Para obtener más información o realizar preguntas sobre el proyecto, puedes ponerte en contacto con el autor:

- Nombre: Misael García Torres
- Teléfono: +56 931 854 247
- Correo Electrónico: [misagtor@gmail.com)
- LinkedIn: [linkedin.com/in/mgarciat](https://www.linkedin.com/in/mgarciat/)

`<a name="menciones"></a>`
