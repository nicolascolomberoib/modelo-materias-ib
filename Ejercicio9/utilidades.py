def numero_a_letras(numero):
    numeros = {
        0: "cero", 1: "uno", 2: "dos", 3: "tres", 4: "cuatro",
        5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve", 10: "diez"
    }
    return numeros.get(numero, "nota fuera de rango")
