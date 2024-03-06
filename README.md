# Automatización de Análisis de Documentos PDF con GROBID

Este proyecto automatiza la extracción y análisis de información de documentos PDF académicos o científicos utilizando el servicio GROBID. GROBID es una herramienta poderosa diseñada para convertir documentos PDF en datos estructurados XML, permitiendo un análisis detallado y preciso del contenido. El objetivo principal del proyecto es facilitar el procesamiento masivo de documentos PDF para extraer insights valiosos, como la generación de nubes de palabras de los abstracts, el conteo de enlaces y la identificación del número de figuras en cada documento.

## Requisitos Previos

Para ejecutar este proyecto, necesitas tener Docker instalado en tu sistema. Si aún no lo tienes, puedes descargarlo e instalarlo desde [Docker Hub](https://hub.docker.com/).

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

## Licencia

Información sobre la licencia bajo la cual se distribuye el proyecto.
