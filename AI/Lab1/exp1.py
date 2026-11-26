import pandas as pd
# Tuple of named schema
SCHEMA = ("hours_studied", "attendance", "department","marks")
# A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

# list of raw records with some missing values
raw_records = [(5, 80, "CSE", 62),
                    (None, None, "CIVIL", 50),
                    (2, None, "ECE", 45),
                    (None, 55, "MECH", 40),
                    (8, 90, "CSE", 85),
                    (None, 55, "MECH", 40),
                    (7, 95, "EE", None),
                    (None, None, "CIVIL", 50),
                    (None, 55, "MECH", 40)]

# validating departments using sets
Valid_departments  = {"CSE", "ECE", "MECH", "CIVIL", "EEE"}

# check all the right named departements are in the raw records or not
if (
    all(raw_records[2] in Valid_departments for raw_records in raw_records)
):       
    print("All records have valid departments.")

else:
    print("Some records have invalid departments.")

# The all() function returns True if all items in an iterable are true, otherwise it returns False.
# Using all() function to validate the departments in the raw records
# The in keyword is used to check if a value exists in a sequence (list, tuple, string) or not.


# Creating a list of dictionaries from raw records and schema
for i in range(len(raw_records)):
    _list_of_dicts = [dict(zip(SCHEMA, raw_records[i]))]
    print(_list_of_dicts)
# In Python, zip is a built-in function used to combine two or more iterables (like lists, tuples, strings, etc.) into an iterator of tuples, where each tuple contains elements from the iterables at the same position (index).
# The dict() function creates a dictionary in Python.


none_hours = sum(1 for record in raw_records if record[0] is None)
none_attendance = sum(1 for record in raw_records if record[1] is None)
print(f"Number of None in hours_studied: {none_hours}")
print(f"Number of None in attendance: {none_attendance}")

all_records_as_dicts = []
for record in raw_records:
    record_dict = dict(zip(SCHEMA, record))
    all_records_as_dicts.append(record_dict)

df_combined = pd.DataFrame(all_records_as_dicts)
print(df_combined)

# step 2 : creating a function to remove duplicate values 

def Remove_duplicates(raw_records):
    seen = set()
    unique_records = []
    for record in raw_records:
        if record not in seen:
            unique_records.append(record)
            seen.add(record)
    return unique_records