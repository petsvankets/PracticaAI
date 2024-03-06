# Automatización de Análisis de Documentos PDF con GROBID

Este proyecto automatiza la extracción y análisis de información de documentos PDF académicos o científicos utilizando el servicio GROBID. GROBID es una herramienta poderosa diseñada para convertir documentos PDF en datos estructurados XML, permitiendo un análisis detallado y preciso del contenido. El objetivo principal del proyecto es facilitar el procesamiento masivo de documentos PDF para extraer insights valiosos, como la generación de nubes de palabras de los abstracts, el conteo de enlaces y la identificación del número de figuras en cada documento.

## Requisitos Previos

Para ejecutar este proyecto, necesitas tener Docker instalado en tu sistema. Si aún no lo tienes, puedes descargarlo e instalarlo desde [Docker Hub](https://hub.docker.com/).

Todas las dependencias y librerias de python necesarias se hayan ya sobre los Dockerfiles correspondientes.

## Estructura del Proyecto

El proyecto consta de dos servicios principales:

- **Servicio de GROBID**: Un servicio de extracción de información bibliográfica.
- **Servicio de Python**: Un servicio personalizado que interactúa con GROBID.

Cada servicio tiene su propio `Dockerfile` y se encuentra en su respectiva carpeta:

- `/grobid_client_python`
- `/Grobid`

## Configuración de la Red Docker

Para que los servicios puedan comunicarse entre sí, necesitan estar en la misma red Docker. Sigue estos pasos para configurar la red:

1. Crea una red Docker:

    ```bash
    docker network create grobid-network
    ```

## Ejecución del Servicio de GROBID

Para construir y ejecutar el contenedor de GROBID, sigue estos pasos:

1. Navega a la carpeta del servicio de GROBID:

    ```bash
    cd Grobid
    ```

2. Construye la imagen Docker:

    ```bash
    docker build -t mi-imagen-grobid .
    ```

3. Ejecuta el contenedor añadiéndolo a la red:

    ```bash
    docker run -t --rm --name contenedor-grobid --network grobid-network -p 8070:8070 -p 8071:8071 mi-imagen-grobid
    ```

## Ejecución del Servicio de Python

Para construir y ejecutar el contenedor del servicio de Python, sigue estos pasos:

1. Navega a la carpeta del servicio de Python:

    ```bash
    cd grobid_client_python
    ```

2. Construye la imagen Docker:

    ```bash
    docker build -t grobid-client-python .
    ```

3. Ejecuta el contenedor añadiéndolo a la misma red que GROBID:

    ```bash
    docker run --name mi-aplicacion-python-container --network grobid-network -e GROBID_URL=http://contenedor-grobid:8070 grobid-client-python
    ```

## Explicación Servicio de Python

El servicio Python recoge aquellos PDFs que se encuentran en la ruta:

- `/grobid_client_python/resources/test_pdf`

Y posteriormente llama al servicio GROBID del otro contenedor de Docker para procesar estos últimos.

La respuesta de este servicio es procesada y deja un archivo XML por cada uno de los PDFs que se encontraban en la ruta ya mencionada y deja la respuesta en:

- `/grobid_client_python/resources/test_out`

A partir de aquí, el script de arranque "example.py" alojado en el directorio raiz:

- `/grobid_client_python`

Se encargará de procesar la información contenida en los XMLs a través de los diferentes scripts que se encargan del análisis.


### Uso de los scripts "extract_abstracts.py" y "generate_wordcloud.py"

El primero extrae los 'abstracts' de todos los XMLs y los condensa en un solo archivo all_abstracts.txt en la ruta: 

- `/grobid_client_python/processed_xmls`

A continuación, el siguiente script es llamado y genera una nube de palabras en formato png sobre la raiz:

- `/grobid_client_python`

Ejemplo con 10 PDFs relacionados con el deporte: 

![Ejemplo de WordCloud](wordcloud.png)


### Uso del scripts "extract_links.py.py".

Este script obtiene los links de cada uno de los XMLs y genera un archivo .txt para cada PDF con sus respectivos links en: 

- `/grobid_client_python/processed_xmls`

Ejemplo de un txt:






