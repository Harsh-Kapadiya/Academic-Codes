import networkx as nx
import matplotlib.pyplot as plt


class Ontology:

    def __init__(self):
        self.classes = {}
        self.instances = {}
        self.properties = []

    # Add class with optional parent classes
    def add_class(self, class_name, parents=None):
        if parents is None:
            parents = []
        self.classes[class_name] = parents

    # Add instance of a class
    def add_instance(self, instance, class_name):
        self.instances[instance] = class_name

    # Add property relationship
    def add_property(self, subject, relation, obj):
        self.properties.append((subject, relation, obj))

    # Get all superclasses recursively
    def get_superclasses(self, class_name):
        supers = set()
        parents = self.classes.get(class_name, [])

        for parent in parents:
            supers.add(parent)
            supers.update(self.get_superclasses(parent))

        return supers

    # Automatic inference of higher-level classes
    def infer_instance_classes(self, instance):
        if instance not in self.instances:
            return []

        base_class = self.instances[instance]
        super_classes = self.get_superclasses(base_class)

        return [base_class] + list(super_classes)

    # Check if two instances share superclass
    def same_superclass(self, inst1, inst2):
        c1 = self.infer_instance_classes(inst1)
        c2 = self.infer_instance_classes(inst2)

        return bool(set(c1) & set(c2))

    # Check if class derives from another
    def is_subclass(self, child, parent):
        return parent in self.get_superclasses(child)

    # Visualize ontology graph
    def visualize(self):
        G = nx.DiGraph()

        for cls, parents in self.classes.items():
            G.add_node(cls)
            for p in parents:
                G.add_edge(p, cls)

        for inst, cls in self.instances.items():
            G.add_node(inst)
            G.add_edge(cls, inst)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue")
        plt.show()


ontology = Ontology()

# Ontology hierarchy
ontology.add_class("Animal")
ontology.add_class("Mammal", ["Animal"])
ontology.add_class("Human", ["Mammal"])
ontology.add_class("Teacher", ["Human"])
ontology.add_class("Student", ["Human"])
ontology.add_class("Bird", ["Animal"])
ontology.add_class("Eagle", ["Bird"])

# Multiple inheritance example
ontology.add_class("Researcher", ["Teacher", "Scientist"])
ontology.add_class("Scientist", ["Human"])

# Instances
ontology.add_instance("Ravi", "Student")
ontology.add_instance("Mary", "Teacher")
ontology.add_instance("Lion", "Mammal")

# Properties
ontology.add_property("Mary", "teaches", "Math")
ontology.add_property("Ravi", "studies", "Math")

# Automatic inference
print("Classes of Ravi:", ontology.infer_instance_classes("Ravi"))
print("Classes of Mary:", ontology.infer_instance_classes("Mary"))

# Semantic reasoning
print("Ravi and Mary share superclass:", ontology.same_superclass("Ravi", "Mary"))

print("Is Human subclass of Animal:", ontology.is_subclass("Human", "Animal"))

# Dynamic input example
while True:
    ans = input("Add new class? (yes/no): ")

    if ans.lower() == "no":
        break

    name = input("Class name: ")
    parent = input("Parent class (comma separated): ").split(",")

    ontology.add_class(name, parent)

# Visualization
ontology.visualize()
