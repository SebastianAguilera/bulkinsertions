import os
from app import create_app, db
from app.services import (
    LocalidadService,
    OrientacionService,
    PlanService,
    EspecialidadService,
    UniversidadService,
    FacultadService,
    GradoService,
    MateriaService,
    PaisService
)

# Calcula el path absoluto a 'archivados_xml' sin importar desde dónde se ejecute el script
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
XML_DIR = os.path.join(BASE_DIR, 'archivados_xml')

def insersiones_masivas():
    LocalidadService.insertar_masivo(os.path.join(XML_DIR, "localidades.xml"))
    OrientacionService.insertar_masivo(os.path.join(XML_DIR, "orientaciones.xml"))
    PlanService.insertar_masivo(os.path.join(XML_DIR, "planes.xml"))
    EspecialidadService.insertar_masivo(os.path.join(XML_DIR, "especialidades.xml"))
    UniversidadService.insertar_masivo(os.path.join(XML_DIR, "universidades.xml"))
    FacultadService.insertar_masivo(os.path.join(XML_DIR, "facultades.xml"))
    GradoService.insertar_masivo(os.path.join(XML_DIR, "grados.xml"))
    MateriaService.insertar_masivo(os.path.join(XML_DIR, "materias.xml"))
    PaisService.insertar_masivo(os.path.join(XML_DIR, "paises.xml"))

if __name__ == "__main__":
    # Setea el entorno
    os.environ['FLASK_CONTEXT'] = 'development'

    # Crea la app y el contexto
    app = create_app()
    with app.app_context():
        db.create_all()  # Solo si querés crear las tablas
        insersiones_masivas()
        print("✔ Inserciones completadas correctamente.")
