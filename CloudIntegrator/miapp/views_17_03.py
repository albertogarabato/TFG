# Importaciones necesarias
from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
import mysql.connector

# Configuración de las conexiones a las bases de datos
DATABASES = {
    'controlboxcloud': {
        'HOST': 'maquiaridos.controlbox.es',
        'USER': 'postgres',
        'PASSWORD': 'Infonet',
        'NAME': 'controlboxcloud_db',
        'PORT': '9343',
    },
    'controlboxcloud2': {
        'HOST': 'ucoga.controlbox.es',
        'USER': 'postgres',
        'PASSWORD': 'Infddonet',
        'NAME': 'controlboxcloud2_db',
        'PORT': '9343',
    },
    'controlboxcloud3': {
        'HOST': 'uco.controlbox.es',
        'USER': 'softaes',
        'PASSWORD': 'Infddonet',
        'NAME': 'controlboxcloud3_db',
        'PORT': '9343',
    },
    'cloudhub': {
        'HOST': 'cloud.infonet.es',
        'USER': 'root',
        'PASSWORD': 'Infonet',
        'NAME': 'cloudhub_db',
        'PORT': '5443',
    },
    'cloudhub2': {
        'HOST': 'cloud.infonet.es',
        'USER': 'root',
        'PASSWORD': 'Infonddet',
        'NAME': 'cloudhub2_db',
        'PORT': '6443',
    },
    'cloudhub3': {
        'HOST': 'cloud.infonet.es',
        'USER': 'root',
        'PASSWORD': 'Infonddet',
        'NAME': 'cloudhub3_db',
        'PORT': '8443',
    },
}

# Factoría para seleccionar la base de datos
class DatabaseFactory:
    # Aquí comienza la implementación del patrón Factory
    def create_database(self, db_type):
        if db_type == 'controlboxcloud':
            return ControlBoxCloudDatabase()
        elif db_type == 'controlboxcloud2':
            return ControlBoxCloudDatabase2()
        elif db_type == 'controlboxcloud3':
            return ControlBoxCloudDatabase3()
        elif db_type == 'cloudhub':
            return CloudHubDatabase()
        elif db_type == 'cloudhub2':
            return CloudHubDatabase2()
        elif db_type == 'cloudhub3':
            return CloudHubDatabase3()
    # Aquí termina la implementación del patrón Factory

# Clases para las bases de datos específicas

class CloudHubDatabase:
    # Aquí comienza la clase CloudHubDatabase
    def __init__(self):
        self.db_type = 'cloudhub'
        self.host = DATABASES['cloudhub']['HOST']
        self.user = DATABASES['cloudhub']['USER']
        self.password = DATABASES['cloudhub']['PASSWORD']
        self.database = DATABASES['cloudhub']['NAME']
        self.port = DATABASES['cloudhub']['PORT']

    def connect(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )

class CloudHubDatabase2:
    # Aquí comienza la clase CloudHubDatabase2
    def __init__(self):
        self.db_type = 'cloudhub2'
        self.host = DATABASES['cloudhub2']['HOST']
        self.user = DATABASES['cloudhub2']['USER']
        self.password = DATABASES['cloudhub2']['PASSWORD']
        self.database = DATABASES['cloudhub2']['NAME']
        self.port = DATABASES['cloudhub2']['PORT']

    def connect(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )

class CloudHubDatabase3:
    # Aquí comienza la clase CloudHubDatabase3
    def __init__(self):
        self.db_type = 'cloudhub3'
        self.host = DATABASES['cloudhub3']['HOST']
        self.user = DATABASES['cloudhub3']['USER']
        self.password = DATABASES['cloudhub3']['PASSWORD']
        self.database = DATABASES['cloudhub3']['NAME']
        self.port = DATABASES['cloudhub3']['PORT']

    def connect(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )

class ControlBoxCloudDatabase:
    # Aquí comienza la clase ControlBoxCloudDatabase
    def __init__(self):
        self.db_type = 'controlboxcloud'
        self.host = DATABASES['controlboxcloud']['HOST']
        self.user = DATABASES['controlboxcloud']['USER']
        self.password = DATABASES['controlboxcloud']['PASSWORD']
        self.database = DATABASES['controlboxcloud']['NAME']
        self.port = DATABASES['controlboxcloud']['PORT']

    def connect(self):
        return psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )

class ControlBoxCloudDatabase2:
    # Aquí comienza la clase ControlBoxCloudDatabase2
    def __init__(self):
        self.db_type = 'controlboxcloud2'
        self.host = DATABASES['controlboxcloud2']['HOST']
        self.user = DATABASES['controlboxcloud2']['USER']
        self.password = DATABASES['controlboxcloud2']['PASSWORD']
        self.database = DATABASES['controlboxcloud2']['NAME']
        self.port = DATABASES['controlboxcloud2']['PORT']

    def connect(self):
        return psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )

class ControlBoxCloudDatabase3:
    # Aquí comienza la clase ControlBoxCloudDatabase3
    def __init__(self):
        self.db_type = 'controlboxcloud3'
        self.host = DATABASES['controlboxcloud3']['HOST']
        self.user = DATABASES['controlboxcloud3']['USER']
        self.password = DATABASES['controlboxcloud3']['PASSWORD']
        self.database = DATABASES['controlboxcloud3']['NAME']
        self.port = DATABASES['controlboxcloud3']['PORT']

    def connect(self):
        return psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )

# Vista para validar y conectar con la base de datos
def validate_and_connect(request):
    # Lógica para validar el usuario y contraseña
    # Patron factory para seleccionar la base de datos correspondiente
    db_type = request.POST.get('db_type')
    factory = DatabaseFactory()
    database = factory.create_database(db_type)
    
    try:
        connection = database.connect()
        # Realizar otras acciones con la conexión
        return HttpResponse('Conexión exitosa a la base de datos {}'.format(db_type))
    except Exception as e:
        return HttpResponse('Error de conexión a la base de datos {}: {}'.format(db_type, str(e)))

# Otras vistas y funciones
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contacto(request):
    return render(request, 'contacto.html')
