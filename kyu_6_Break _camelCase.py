
s = "helloWorld"

def solution(s):
    """
        Queremos hacer un espacio entre una mayuscula encontrada
        
        1. Primero debemos recorrer el array del str para encontrar la mayusucula.
        2. SI hay mayuscula -> join[posición] un espacio " ". Si no hay pass
        3. return el string
        Solución: 
            Con el join hacemos la lógica del espacio o juntas los caracteres. Luego generamos
            un operador ternario para saber si es una mayúscula con el isupper() y como los ternarios
            admiten multiples operaciones recorremos el str con un for
        
    """
    print(''.join([" " + a if a.isupper() else a for a in s]))      
    

solution(s)