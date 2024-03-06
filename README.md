# Nombre del Proyecto

Breve descripción de tu proyecto.

## Requisitos Previos

Para ejecutar este proyecto, necesitas tener Docker instalado en tu sistema. Si aún no lo tienes, puedes descargarlo e instalarlo desde [Docker Hub](https://hub.docker.com/).

## Estructura del Proyecto

El proyecto consta de dos servicios principales:

- **Servicio de GROBID**: Un servicio de extracción de información bibliográfica.
- **Servicio de Python**: Un servicio personalizado que interactúa con GROBID.

Cada servicio tiene su propio `Dockerfile` y se encuentra en su respectiva carpeta:

- `/servicio-grobid`
- `/servicio-python`

## Configuración de la Red Docker

Para que los servicios puedan comunicarse entre sí, necesitan estar en la misma red Docker. Sigue estos pasos para configurar la red:

1. Crea una red Docker:

    ```bash
    docker network create mi-red-docker
    ```

## Ejecución del Servicio de GROBID

Para construir y ejecutar el contenedor de GROBID, sigue estos pasos:

1. Navega a la carpeta del servicio de GROBID:

    ```bash
    cd servicio-grobid
    ```

2. Construye la imagen Docker:

    ```bash
    docker build -t mi-grobid .
    ```

3. Ejecuta el contenedor añadiéndolo a la red:

    ```bash
    docker run --rm --name grobid-container --network mi-red-docker -p 8070:8070 -p 8071:8071 mi-grobid
    ```

## Ejecución del Servicio de Python

Para construir y ejecutar el contenedor del servicio de Python, sigue estos pasos:

1. Navega a la carpeta del servicio de Python:

    ```bash
    cd servicio-python
    ```

2. Construye la imagen Docker:

    ```bash
    docker build -t mi-servicio-python .
    ```

3. Ejecuta el contenedor añadiéndolo a la misma red que GROBID:

    ```bash
    docker run --rm --name python-container --network mi-red-docker mi-servicio-python
    ```

## Contribuir

Instrucciones para contribuir al proyecto, si es aplicable.

## Licencia

Información sobre la licencia bajo la cual se distribuye el proyecto.
