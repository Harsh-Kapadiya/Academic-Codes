import csv

# 1. Define your pre-trained model coefficients (Example values)
# Equation: Predicted_Value = (Weight * Hours_Studied) + Bias
weight = 0.1
bias = -0.3
threshold = 1.5  # Boundary to classify as passed (1) or failed (0)

# Initialize confusion matrix counters
tp, tn, fp, fn = 0, 0, 0, 0

# 2. Open and process the CSV file safely without external modules
file_path = "Lab3/student-por.csv"  # Update this path to your actual CSV file location

try:
    with open(file_path, mode="r", encoding="utf-8") as file:
        # Use Python's built-in csv reader to handle commas correctly
        reader = csv.reader(file)
        
        # Read the header and find column indices dynamically
        header = [col.strip().lower() for col in next(reader)]
        
        # Adjust names here if your dataset fields use different headers
        x_col_index = header.index("age")  # Assuming 'age' is the feature column
        y_col_index = header.index("studytime")  # Assuming 'studytime' is the target column
        
        # Loop through each row in the dataset
        for row in reader:
            if not row: 
                continue # Skip blank rows
                
            # Extract features and convert string values to numeric types
            hours_studied = float(row[x_col_index])
            actual_class = int(row[y_col_index])
            
            # 3. Compute continuous linear regression output
            raw_prediction = (weight * hours_studied) + bias
            
            # 4. Apply threshold logic to convert to a binary class
            if raw_prediction >= threshold:
                predicted_class = 1
            else:
                predicted_class = 0
                
            # 5. Build and populate the confusion matrix counters
            if actual_class == 1 and predicted_class == 1:
                tp += 1
            elif actual_class == 0 and predicted_class == 0:
                tn += 1
            elif actual_class == 0 and predicted_class == 1:
                fp += 1
            elif actual_class == 1 and predicted_class == 0:
                fn += 1

    # 6. Display the formatted confusion matrix layout
    print("\n" + "="*35)
    print("        CONFUSION MATRIX")
    print("="*35)
    print(f"True Negative (TN):  {tn:4d} | False Positive (FP): {fp:4d}")
    print(f"False Negative (FN): {fn:4d} | True Positive (TP):  {tp:4d}")
    print("="*35)
    
    # Calculate Overall Accuracy
    total = tp + tn + fp + fn
    accuracy = (tp + tn) / total if total > 0 else 0
    print(f"Calculated Accuracy: {accuracy:.2%}\n")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please check your path.")
except ValueError as e:
    print(f"Column Mapping Error: {e}. Check your CSV header column names.")
