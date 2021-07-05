people = [
  { "name": "Harry", "house": "Grifinória" },
  { "name": "Cho", "house": "Corvinal" },
  { "name": "Draco", "house": "Sonserina" },
]

# I cant do that because sort() dont know how compare the values correctly

# Podemos fazer o seguinte
def sortDefinition(person):
  return person["name"]

people.sort(key=sortDefinition)
print(people)

# Ou poderíamos fazer o seguinte (ordenando people através da propriedade 'house' dos dicionários)
people.sort(key=lambda person: person["house"])
print(people)
