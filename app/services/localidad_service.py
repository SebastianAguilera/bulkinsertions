from app.models import Localidad
from app.repositories import LocalidadRepository
import xml.etree.ElementTree as ET
import os


class LocalidadService:

    @staticmethod
    def crear_localidad(localidad: Localidad):
        LocalidadRepository.crear_localidad(localidad)
        return localidad

    @staticmethod
    def insertar_masivo(ruta: str):
        tree = ET.parse(ruta)
        root = tree.getroot()

        datos = []
        for item in root.findall('_expxml'):
            localidad_id = int(item.find('localidad').text)
            nombre = item.find('nombre').text.strip()
            cod_postal = item.find('codigo_postal').text.strip()
            id_provincia = int(item.find('id_provincia').text)
            datos.append({
                'id': localidad_id,
                'nombre': nombre,
                'codigo_postal': cod_postal,
                'id_provincia': id_provincia
            })

        LocalidadRepository.insertar_masivo(datos)
