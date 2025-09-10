import re
def buscar_datos(texto):
    resultados = []

    expresiones = {
        "decimal": r"\d+\.\d+",
        "entero": r"(?<![\d.])-?\b\d+\b(?!\.\d)",
        "booleano": r"(true|false)",
        "string": r"\'(.*?)\'",
        "lista": r"[^\d\W]+(?:,\s*[^\d\W]+){2,}"
    }

#Iterar y buscar cada tipo de dato en el texto

    for tipo, expresion in expresiones.items():
        for coincidencia in re.finditer(expresion, texto):
            resultados.append((coincidencia.group(), tipo))
    
    return resultados

texto = 'En el año 2025, 13 artistas crean juntos. ¡Hola! ¿Te gusta el arte? El cielo brillante, las estrellas (★) inspiran. 9 niños pintan, 8.25 horas de creatividad. Lista: pincel, lienzo, colores. El costo es $40.10. ¿Sabías que el código #5566 es famoso? La vida es expresión, @todos participan. El tiempo pasa, 10 días de exposición. ¡Inspiración! El número especial es 303. ¿Qué harías con 25.60 pesos? La respuesta está en la lista: pintar, dibujar, imaginar. ¡Crea sin límites! 100 palabras, 10 enteros, 3 decimales, 2 listas.'
print("Texto de entrada:", texto, "\n")

resultados = buscar_datos(texto)

print("Resultados:")
for valor, tipo in resultados:
    print(f"* {valor}: {tipo}")

print("\nCantidad por tipo:")
tipos_unicos = set(tipo for _, tipo in resultados)
for tipo in tipos_unicos:
    cantidad = len([1 for _, t in resultados if t == tipo])
    print(f"- {tipo}: {cantidad}")

palabras = re.findall(r"[^\s]+", texto, re.UNICODE)
print("\nCantidad de palabras:", len(palabras)) #86 palabras