import re
def buscar_datos(texto):
    resultados = []

    expresiones = {
        "decimal": r"\d+\,\d+",
        "entero": r"(?<![\d,])-?\b\d+\b(?!\,\d)",
        "booleano": r"(true|false)",
        "string": r"\'(.*?)\'",
        "lista": r"[^\d\W]+(?:,\s*[^\d\W]+){2,}"
    }

#Iterar y buscar cada tipo de dato en el texto

    for tipo, expresion in expresiones.items():
        for coincidencia in re.finditer(expresion, texto):
            resultados.append((coincidencia.group(), tipo))
    
    return resultados

texto = "Ciao! Nel 2025, 12 artisti espongono insieme. Lista: pennello, tela, colori. Il prezzo è €35,80. Le stelle (★) ispirano la notte. 6 gatti dipingono, 5 cani disegnano. Il codice #9911 è noto. 9 giorni di mostra, 5 di riposo. @tutti creano. Il numero magico è 323. Cosa faresti con 22,50€? La risposta è nella lista: dipingere, disegnare, immaginare. Crea senza limiti! 100 parole, 9 interi, 3 decimali, 2 listas."
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