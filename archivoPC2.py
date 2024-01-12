import os
import subprocess

def setup_environment():
    # Configura la variable de entorno GRUPO_NUMERO
    os.environ['GRUPO_NUMERO'] = '29'

def clone_repository():
    # Clona el repositorio en la máquina virtual
    subprocess.run(["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2.git"])

def install_dependencies():
    # Instala las dependencias
    subprocess.run(["pip3", "install", "-r", "practica_creativa2/bookinfo/src/productpage/requirements.txt"])

def modify_application():
    # Modifica el archivo productpage.html para incluir el nombre del grupo en el título
    grupo_numero = os.environ.get('GRUPO_NUMERO', 'DefaultGroup')

    # Realiza las modificaciones necesarias en el archivo de la plantilla HTML
    with open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "r") as file:
        data = file.read()

    # Reemplaza el título original con el nuevo título que incluye el número de grupo
    nuevo_titulo = f"Simple Bookstore App - Grupo {grupo_numero}"
    data = data.replace("{% block title %}Simple Bookstore App{% endblock %}", f"{{% block title %}}{nuevo_titulo}{{% endblock %}}")

    # Escribe los cambios de vuelta al archivo
    with open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "w") as file:
        file.write(data)

def start_application(port):
    # Inicia la aplicación en un puerto específico
    subprocess.run(["python3", "practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", str(port)])

def main():
    setup_environment()
    clone_repository()
    install_dependencies()
    modify_application()
    start_application(9080)  # Cambia 9080 al puerto deseado

if __name__ == "__main__":
    main()
