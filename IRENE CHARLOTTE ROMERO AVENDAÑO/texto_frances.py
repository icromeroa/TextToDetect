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

texto = texto = u"""Bonjour! En 2025, 11 artistes exposent ensemble. Liste: pinceau, toile, couleurs. Le prix est de 38,90€. Les étoiles (★) inspirent la nuit. 7 chats peignent, 6 chiens dessinent. Le code #7788 est connu. 10 jours d'expo, 4 jours de repos. @tous créent. Le numéro magique est 313. Que feriez-vous avec 28,70€? La réponse est dans la liste: peindre, dessiner, imaginer. Créez sans limites! 100 mots, 10 entiers, 3 décimaux, 2 listas."""

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