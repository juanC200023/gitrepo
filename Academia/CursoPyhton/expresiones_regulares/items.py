import re

text = "Hoy estamos a 11/07/2024 y despues de un dia estaremos a 12/07/2024"

patron = r"\b(\d{2}\/\d{2}\/\d{4})\b"

for match in re.finditer(patron, text):
    print(f"La fecha es: {match.group(0)}, la cual comienza en la posicion {match.start()} y termina en la posicion {match.end()}")
