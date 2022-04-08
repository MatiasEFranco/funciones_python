# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# --------------------------------
# Aquí dentro definir la función que solicitará
# el nombre de tres invitados
#from ejemplos_clase.ejemplo_1 import cantidad_productos


def generar_invitados(cantidad):

    invitados = cantidad    #aqui se guarda la cantidad de invitados a cargar

    lista = []              #aqui inicializamos la lista donde se guardaran los ivnitados que carguen
   
    print("La canitdad de Invitado a cargar es ", invitados, "\n")
   
    for i in  range(invitados):

        if i == 0:  #utilizamos este if solo para cambiar el texto del primer print
        
            lista.append (input("Por favor ingrese el nombre de un invitado :\n"))

        else:       #despues del primer invitado el resto se cargarian con este print

            lista.append (input("Por favor ingrese el nombre de otro invitado :\n"))

    return lista

# --------------------------------


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno: Crear la función "generar_invitados"

    # Dentro de esa función el sistema deberá solicitar
    # al usuario por consola que ingrese tres nombres de 
    # tres invitados.
    # IMPORTANTE: Utilizar un "input" por cada invitado
    # que se solicite ingresar

    # Los tres nombres ingresados se deberán guardar en
    # una lista

    # La función generar_invitados deberá retornar
    # la lista de invitados generados

    # NOTA: Recomendamos utilizar bucles para no repetir código
    # y solicitar los 3 invitiados, uno en cada iteración del bucle

    # Luego de crear la función invocarla en este lugar:
    
    cantidad_invitados = 3  #se prodria utilizar un input y agregar por consola la cantidad de invitados a cargar, se guarda en esta variable y le pasamos este dato a la funcion

    lista_invitados = generar_invitados(cantidad_invitados)

    # Imprimir en pantalla "lista_invitados":

    print("Los invitados cargados son ", lista_invitados)

    print("terminamos")
