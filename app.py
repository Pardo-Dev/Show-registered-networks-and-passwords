import subprocess

def obtenerRedes():
    try:
        # Ejecutar el comando para obtener los perfiles de redes WiFi
        command = ["netsh", "wlan", "show", "profiles"]
        redes_output = subprocess.check_output(command, shell=True).decode("latin-1")
        print("Redes WiFi guardadas:\n")
        print(redes_output)
        
        # Pedir al usuario que ingrese el nombre de la red WiFi
        red = input("Que red registrada deseas conocer su contraseña: ").strip()
        
        # Ejecutar el comando para obtener la información del perfil de red, incluyendo la clave de seguridad
        command = ["netsh", "wlan", "show", "profile", red, "key=clear"]
        resp_output = subprocess.check_output(command, shell=True).decode("latin-1")
        
        # Filtrar la línea que contiene "Contenido de la clave" (Key Content)
        for line in resp_output.split('\n'):
            if "Contenido de la clave" in line or "Key Content" in line:
                clave = line.split(":")[1].strip()
                print("=" * (((len(clave)+31))+len(red)))
                print(f"La contraseña de la red '{red}' es: {clave}")
                print("=" * (((len(clave)+31))+len(red)))
                return

        # Si no se encuentra la clave, informar al usuario
        print(f"No se encontró la contraseña para la red '{red}'.")

    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")
    except Exception as e:
        print(f"Se produjo un error: {e}")

obtenerRedes()