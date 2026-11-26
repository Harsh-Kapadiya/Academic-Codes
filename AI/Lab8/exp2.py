# Ontology representation using class hierarchy
ontology = {
 "Animal": [],
 "Mammal": ["Animal"],
 "Human": ["Mammal"],
 "Student": ["Human"]
}
instances = {
 "ram": "Student",
 "socrates": "Human"
}
def is_instance_of(obj, cls):
   current = instances.get(obj)
   while current:
     if current == cls:
       return True
     parent = ontology.get(current)
     if parent:
       current = parent[0]
     else:
       break
   return False
# Queries
print("Is Ram Human?", is_instance_of("ram", "Human"))
print("Is Ram Animal?", is_instance_of("ram", "Animal"))
print("Is Socrates Mammal?", is_instance_of("socrates", "Mammal"))