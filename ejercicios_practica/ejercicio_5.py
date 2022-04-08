# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# --------------------------------
# Aquí copiar la función "generar_invitados"
# ya elaborada

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

# --------------------------------
# Aquí copiar la función "ordenar"
# ya elaborada

def ordenar(lista):

    lista_aux = sorted(lista)

    return lista_aux


# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Alumno: Copiar las funciones "generar_invitados" y "ordenar"
    # creadas en los ejercicios anteriores
    # Deberá copiarlas fuera del bucle "__main__" como se detalla
    # al comienzo del archivo
    # --> El objetivo es generar una lista de invitados y ordenala

    # Luego de copiar las funciones, invocarla en este lugar:

    # 1) Primero generar una lista de invitados con "generar_invitados"
    #    Almacenar el resultado en "lista_invitados"

    cantidad_invitados = int(input("Ingrese la cantidad de invitados a cargar: ")) #se utiliza un input y agregar por consola la cantidad de invitados a cargar, se guarda en esta variable y le pasamos este dato a la funcion

    lista_invitados = generar_invitados(cantidad_invitados)

    # 2) Luego ordenar la lista de invitados con "ordenar"
    #    --> Pasar como parámetro la "lista_invitados"
    #    --> Retornar la lista de invitados ordenada

    lista_invidatos_ordenada = ordenar(lista_invitados)

    # Imprimir en pantalla "lista_invidatos_ordenada":

    print("La lista de invitados original es ", lista_invitados, " y la lista ordenada es ", lista_invidatos_ordenada)

    print("terminamos")
