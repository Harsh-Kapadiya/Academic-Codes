# knowledge representation using predicate logic

facts = {
    "human": [
        "socrates",
        "ram",
        "sita",
        "teacher",
        "student",
        "employee",
        "ajay",
        "ravi",
    ],
    "male": ["ram", "ajay"],
    "female": ["sita"],
    "teacher": ["ajay"],
    "student": ["ravi"],
    "parent": ["ram", "sita"],
    "employee": ["ram"],
    "parent_of": [("ram", "ravi"), ("ram", "sita")],  # Relations: (parent, child)
    "man": [],  # Will be inferred
    "woman": [],  # Will be inferred
}


# Rules
def is_human(x):
    return (
        x in facts["human"]
        or x in facts["teacher"]
        or x in facts["student"]
        or x in facts["parent"]
        or x in facts["employee"]
    )


def is_parent(x, y):
    return (x, y) in facts["parent_of"]


def is_father(x, y):
    return is_parent(x, y) and x in facts["male"]


def is_mortal(x):
    return is_human(x)  # ∀x Human(x) → Mortal(x)


def is_man(x):
    return is_human(x) and x in facts["male"]


def is_woman(x):
    return is_human(x) and x in facts["female"]


# Infer man and woman
for person in facts["human"]:
    if is_man(person):
        facts["man"].append(person)
    if is_woman(person):
        facts["woman"].append(person)


def check_property(x, property_name):
    if property_name == "mortal":
        return is_mortal(x)
    elif property_name == "human":
        return is_human(x)
    elif property_name == "man":
        return is_man(x)
    elif property_name == "woman":
        return is_woman(x)
    return False


def check_relationship(x, y, relation):
    if relation == "parent":
        return is_parent(x, y)
    elif relation == "father":
        return is_father(x, y)
    return False


def add_fact(category, value):
    if category in facts:
        if isinstance(facts[category], list):
            if value not in facts[category]:
                facts[category].append(value)
        elif isinstance(facts[category], list) and isinstance(value, tuple):
            if value not in facts[category]:
                facts[category].append(value)
    print(f"Added {value} to {category}.")


# Dynamic query system
def query_system():
    while True:
        query = (
            input(
                "Enter query (e.g., 'is ram mortal' or 'is ram parent of ravi' or 'add human john' or 'quit'): "
            )
            .strip()
            .lower()
        )
        if query == "quit":
            break
        parts = query.split()
        if len(parts) >= 3 and parts[0] == "is" and parts[2] == "mortal":
            x = parts[1]
            if check_property(x, "mortal"):
                print(f"{x} is mortal.")
            else:
                print(f"{x} is not mortal.")
        elif len(parts) >= 4 and parts[0] == "is" and parts[3] == "of":
            x, relation, y = parts[1], parts[2], parts[4]
            if check_relationship(x, y, relation):
                print(f"{x} is {relation} of {y}.")
            else:
                print(f"{x} is not {relation} of {y}.")
        elif len(parts) >= 3 and parts[0] == "add":
            category, value = parts[1], parts[2]
            add_fact(category, value)
        else:
            print(
                "Invalid query. Try 'is X mortal', 'is X parent of Y', or 'add category value'."
            )


# Run queries
if __name__ == "__main__":
    query_system()
