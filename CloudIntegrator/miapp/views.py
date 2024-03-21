from django.shortcuts import render, redirect
from django.http import HttpResponse
import psycopg2
import mysql.connector

# Diccionario de configuración de las bases de datos
DATABASES = {
    'controlboxcloud': {
        'HOST': 'maquiaridos.controlbox.es',
        'USER': 'postgres',
        'PASSWORD': 'Infonet',
        'NAME': 'controlboxcloud_db',
        'PORT': '9343',
        'USER_TABLE': 'login',  # Tabla de usuarios en PostgreSQL
        'URL': 'https://controlbox.cloud.gal:9343',  # URL correspondiente
    },
    'controlboxcloud2': {
        'HOST': 'ucoga.controlbox.es',
        'USER': 'postgres',
        'PASSWORD': 'Infddonet',
        'NAME': 'controlboxcloud2_db',
        'PORT': '9343',
        'USER_TABLE': 'login',  # Tabla de usuarios en PostgreSQL
        'URL': 'https://ucoga.cloud.gal:9343',  # URL correspondiente
    },
    'controlboxcloud3': {
        'HOST': 'uco.controlbox.es',
        'USER': 'softaes',
        'PASSWORD': 'Infddonet',
        'NAME': 'controlboxcloud3_db',
        'PORT': '9343',
        'USER_TABLE': 'login',  # Tabla de usuarios en PostgreSQL
        'URL': 'https://uco.cloud.gal:9343',  # URL correspondiente
    },
    'cloudhub': {
        'HOST': 'cloud.infonet.es',
        'USER': 'root',
        'PASSWORD': 'Infonet',
        'NAME': 'cloudhub_db',
        'PORT': '5443',
        'USER_TABLE': 'oc_users',  # Tabla de usuarios en MySQL
        'URL': 'https://cloudhub.cloud.gal:5443',  # URL correspondiente
    },
    'cloudhub2': {
        'HOST': 'cloud.infonet.es',
        'USER': 'root',
        'PASSWORD': 'Infonddet',
        'NAME': 'cloudhub2_db',
        'PORT': '6443',
        'USER_TABLE': 'oc_users',  # Tabla de usuarios en MySQL
        'URL': 'https://cloudhub2.cloud.gal:6443',  # URL correspondiente
    },
    'cloudhub3': {
        'HOST': 'cloud.infonet.es',
        'USER': 'root',
        'PASSWORD': 'Infonddet',
        'NAME': 'cloudhub3_db',
        'PORT': '8443',
        'USER_TABLE': 'oc_users',  # Tabla de usuarios en MySQL
        'URL': 'https://cloudhub3.cloud.gal:8443',  # URL correspondiente
    },
}

# Patrón Factory para crear instancias de bases de datos
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
        self.user_table = DATABASES['cloudhub']['USER_TABLE']
        self.url = DATABASES['cloudhub']['URL']

    def check_user(self, username, password):
        """
        Verifica si el usuario existe en la tabla correspondiente de la base de datos.

        Args:
            username (str): El nombre de usuario a verificar.
            password (str): La contraseña del usuario.

        Returns:
            bool: True si el usuario existe, False de lo contrario.
        """
        # Conexión a la base de datos
        conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )
        cursor = conn.cursor()

        # Verificar el usuario en la tabla
        query = "SELECT * FROM {} WHERE username=%s AND password=%s".format(self.user_table)
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        # Cerrar conexiones
        cursor.close()
        conn.close()

        return result is not None


class CloudHubDatabase2:
    """
    Clase para la base de datos CloudHub2.
    """

    def __init__(self):
        self.db_type = 'cloudhub2'
        self.host = DATABASES['cloudhub2']['HOST']
        self.user = DATABASES['cloudhub2']['USER']
        self.password = DATABASES['cloudhub2']['PASSWORD']
        self.database = DATABASES['cloudhub2']['NAME']
        self.port = DATABASES['cloudhub2']['PORT']
        self.user_table = DATABASES['cloudhub2']['USER_TABLE']
        self.url = DATABASES['cloudhub2']['URL']

    def check_user(self, username, password):
        """
        Verifica si el usuario existe en la tabla correspondiente de la base de datos.

        Args:
            username (str): El nombre de usuario a verificar.
            password (str): La contraseña del usuario.

        Returns:
            bool: True si el usuario existe, False de lo contrario.
        """
        # Conexión a la base de datos
        conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )
        cursor = conn.cursor()

        # Verificar el usuario en la tabla
        query = "SELECT * FROM {} WHERE username=%s AND password=%s".format(self.user_table)
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        # Cerrar conexiones
        cursor.close()
        conn.close()

        return result is not None


class ControlBoxCloudDatabase:
    """
    Clase para la base de datos ControlBoxCloud.
    """

    def __init__(self):
        self.db_type = 'controlboxcloud'
        self.host = DATABASES['controlboxcloud']['HOST']
        self.user = DATABASES['controlboxcloud']['USER']
        self.password = DATABASES['controlboxcloud']['PASSWORD']
        self.database = DATABASES['controlboxcloud']['NAME']
        self.port = DATABASES['controlboxcloud']['PORT']
        self.user_table = DATABASES['controlboxcloud']['USER_TABLE']
        self.url = DATABASES['controlboxcloud']['URL']

    def check_user(self, username, password):
        """
        Verifica si el usuario existe en la tabla correspondiente de la base de datos.

        Args:
            username (str): El nombre de usuario a verificar.
            password (str): La contraseña del usuario.

        Returns:
            bool: True si el usuario existe, False de lo contrario.
        """
        # Conexión a la base de datos
        conn = psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )
        cursor = conn.cursor()

        # Verificar el usuario en la tabla
        query = "SELECT * FROM {} WHERE username=%s AND password=%s".format(self.user_table)
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        # Cerrar conexiones
        cursor.close()
        conn.close()

        return result is not None


class ControlBoxCloudDatabase2:
    """
    Clase para la base de datos ControlBoxCloud2.
    """

    def __init__(self):
        self.db_type = 'controlboxcloud2'
        self.host = DATABASES['controlboxcloud2']['HOST']
        self.user = DATABASES['controlboxcloud2']['USER']
        self.password = DATABASES['controlboxcloud2']['PASSWORD']
        self.database = DATABASES['controlboxcloud2']['NAME']
        self.port = DATABASES['controlboxcloud2']['PORT']
        self.user_table = DATABASES['controlboxcloud2']['USER_TABLE']
        self.url = DATABASES['controlboxcloud2']['URL']

    def check_user(self, username, password):
        """
        Verifica si el usuario existe en la tabla correspondiente de la base de datos.

        Args:
            username (str): El nombre de usuario a verificar.
            password (str): La contraseña del usuario.

        Returns:
            bool: True si el usuario existe, False de lo contrario.
        """
        # Conexión a la base de datos
        conn = psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )
        cursor = conn.cursor()

        # Verificar el usuario en la tabla
        query = "SELECT * FROM {} WHERE username=%s AND password=%s".format(self.user_table)
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        # Cerrar conexiones
        cursor.close()
        conn.close()

        return result is not None


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
        elif db_type == 'cloudhub':
            return CloudHubDatabase()
        elif db_type == 'cloudhub2':
            return CloudHubDatabase2()


def index(request):
    """
    Vista para la página de inicio.

    Args:
        request: El objeto de solicitud de Django.

    Returns:
        Una respuesta HTTP para la página de inicio.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        factory = DatabaseFactory()

        # Comprueba en cada base de datos si el usuario existe
        for db_type, database in DATABASES.items():
            connection = factory.create_database(db_type)
            if connection.check_user(username, password):
                # Usuario válido, redirige a la página correspondiente
                return redirect('validate_and_connect', db_type=db_type)

        # Si no se encuentra el usuario en ninguna base de datos
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

    Args:
        request: El objeto de solicitud de Django.
        db_type (str): El tipo de base de datos.

    Returns:
        Un HttpResponse indicando el resultado de la conexión.
    """
    factory = DatabaseFactory()
    connection = factory.create_database(db_type)

    try:
        # Realizar conexión a la base de datos
        # Por ejemplo:
        # connection.connect()
        # Aquí puedes redirigir a la URL correspondiente
        url = DATABASES[db_type]['URL']
        return redirect(url)
    except Exception as e:
        return HttpResponse('Error de conexión a la base de datos {}: {}'.format(db_type, str(e)))
