from django.shortcuts import render, redirect
from django.http import HttpResponse
import psycopg2
import mysql.connector
from .models import Usuario  # Importa el modelo de Usuario si lo tienes definido
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

# Diccionario para mapear base de datos a sus URLs correspondientes
DATABASE_URLS = {
    'controlboxcloud': 'https://controlbox.cloud.gal:9343',
    'controlboxcloud2': 'https://ucoga.cloud.gal:9343',
    'controlboxcloud3': 'https://uco.cloud.gal:9343',
    'cloudhub': 'https://cloudhub.cloud.gal:5443',
    'cloudhub2': 'https://cloudhub2.cloud.gal:6443',
    'cloudhub3': 'https://cloudhub3.cloud.gal:8443',
    # Agrega más bases de datos y sus URLs aquí
}

# Factoría para seleccionar la base de datos
class DatabaseFactory:
    """
    Factoría para crear instancias de bases de datos según el tipo.
    """
    def create_database(self, db_type):
        """
        Crea y devuelve una instancia de base de datos según el tipo especificado.

        Args:
            db_type (str): El tipo de base de datos.

        Returns:
            Una instancia de base de datos correspondiente al tipo.
        """
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

# Clases para las bases de datos específicas
class CloudHubDatabase:
    """
    Clase para la base de datos CloudHub.
    """
    def __init__(self):
        self.db_type = 'cloudhub'
        self.host = DATABASES['cloudhub']['HOST']
        self.user = DATABASES['cloudhub']['USER']
        self.password = DATABASES['cloudhub']['PASSWORD']
        self.database = DATABASES['cloudhub']['NAME']
        self.port = DATABASES['cloudhub']['PORT']

    def connect(self):
        """
        Conecta a la base de datos CloudHub.

        Returns:
            Una conexión a la base de datos CloudHub.
        """
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
 

def index(request):
 """
    Vista para la página de inicio.

    Si el método de solicitud es POST, verifica el usuario y contraseña en la base de datos
    y redirige a la página de la base de datos correspondiente si es válido.

    Si el método de solicitud es GET, simplemente renderiza la página inicial.

    Args:
        request: El objeto de solicitud de Django.

    Returns:
        Una respuesta HTTP para la página de inicio.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Lógica para validar el usuario y contraseña en la base de datos
        try:
            usuario = Usuario.objects.get(username=username, password=password)
            # Usuario válido, redirige a la página de plataforma con el tipo de base de datos
            return redirect('validate_and_connect', db_type=usuario.db_type)
        except Usuario.DoesNotExist:
            # Usuario no encontrado, muestra un mensaje de error
            error_message = "Usuario o contraseña incorrectos. Intente de nuevo."
            return render(request, 'index.html', {'error_message': error_message})
    else:
        # Si no es un POST, simplemente renderiza la página inicial
        return render(request, 'index.html')

def about(request):
    """
    Vista para la página "about".

    Args:
        request: El objeto de solicitud de Django.

    Returns:
        Una respuesta HTTP para la página "about".
    """
    return render(request, 'about.html')

def contacto(request):
    """
    Vista para la página de contacto.

    Args:
        request: El objeto de solicitud de Django.

    Returns:
        Una respuesta HTTP para la página de contacto.
    """
    return render(request, 'contacto.html')

def validate_and_connect(request, db_type):
    """
    Vista que valida y se conecta a la base de datos según el tipo de base de datos enviado.

    Esta vista recibe el tipo de base de datos como un parámetro y redirige al usuario a la URL correspondiente.

    Args:
        request: El objeto de solicitud de Django.
        db_type (str): El tipo de base de datos.

    Returns:
        Una redirección a la URL correspondiente a la base de datos.
    """
    factory = DatabaseFactory()
    database = factory.create_database(db_type)
    
    try:
        connection = database.connect()
        # Realizar otras acciones con la conexión
        
        # Obtener la URL correspondiente a la base de datos
        db_url = DATABASE_URLS.get(db_type)
        if db_url:
            # Redirigir al usuario a la URL de la base de datos
            return redirect(db_url)
        else:
            # Si no hay una URL definida para la base de datos, mostrar un error
            return HttpResponse('Error: Base de datos no encontrada.')
        
    except Exception as e:
        return HttpResponse('Error de conexión a la base de datos {}: {}'.format(db_type, str(e)))
