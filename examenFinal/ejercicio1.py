##Dado un string implemente una funcion que, haciendo uso de la tecnica de recursividad, regrese el inverso del string. Ejemplos:hola"-"aloh""Python"-"nohtyp"


# define the function 
def invString(string):
    # function will iterate n times so the string is inverted
    if len(string) == 0:
        return string
    else:
        # take out first index of the list the add it to the last part of the list
        return invString(string[1:]) + string[0]

str = "Hola, Mundo!"
invertida = invString(str)
print(f"El string ivertido es -> {invertida}")
