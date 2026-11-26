# knowledge representation using predicate logic

facts = {
    "human": ["socrats", "ram"],
    "male": ["ram"],
    "female": ["sita"]
}

def is_human(x):
    return x in facts["human"]

def is_mortal(x):
    if is_human(x):
        return True
    return False

def check_mortality(x):
    if is_mortal(x):
        print(f"{x} is mortal.")
    else:
        print(f"{x} is not mortal.")

# queries
check_mortality("socrats")
check_mortality("ram")
check_mortality("sita")