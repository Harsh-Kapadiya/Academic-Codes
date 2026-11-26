# Function to remove duplicate records
import exp1.py
def Remove_duplicates(records):
    seen = set()
    unique_records = []
    for record in records:
        record_tuple = tuple(record.items())
        if record_tuple not in seen:
            seen.add(record_tuple)
            unique_records.append(record)
    return unique_records
unique_records = Remove_duplicates(all_records_as_dicts)
print("\nUnique Records:")
for record in unique_records:
    print(record)