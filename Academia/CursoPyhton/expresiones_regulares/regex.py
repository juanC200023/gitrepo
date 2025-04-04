import re 

text = " Mi gato esta en el techo y mi otro gato esta en el jardin"

matches = re.findall("gato", text)
print(matches)

text2 = "Hoy estamos a 11/07/2024, manana estaremos a 12/07/2024"

match = re.findall("\d{2}\/\d{2}\/\d{4}", text2)

print(match)

text3 = "Los usuarios pueden contactarnos a soporte@hack4u.io o a info@hack4u.io"

match1 = re.findall("(\w+)@(\w+\.\w{2,})", text3)

print(match1)

texto = " mi gato esta en el techo y mi perro esta en el jardin"

nuevo_texto = re.sub("gato", "perro", texto)
print(nuevo_texto)

texto1 = "CAmpo1,Campo2,Campo3,Campo4,Campo5"

new_text = re.split(",", texto1)

