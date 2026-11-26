import pandas as pd
from collections import defaultdict
import math

# Load dataset
data = pd.read_csv("AI/Lab13/PlayTennis.csv")

# Split features and target
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Step 1: Calculate Prior Probabilities
def calculate_priors(y):
    priors = {}
    total = len(y)
    
    for cls in y.unique():
        priors[cls] = len(y[y == cls]) / total
    
    return priors

# Step 2: Calculate Likelihood Probabilities
def calculate_likelihoods(X, y):
    likelihoods = {}
    
    for col in X.columns:
        likelihoods[col] = {}
        
        for value in X[col].unique():
            likelihoods[col][value] = {}
            
            for cls in y.unique():
                count = len(X[(X[col] == value) & (y == cls)])
                total_cls = len(y[y == cls])
                
                # Laplace smoothing
                likelihoods[col][value][cls] = (count + 1) / (total_cls + len(X[col].unique()))
    
    return likelihoods

# Step 3: Prediction Function
def predict(sample, priors, likelihoods):
    posteriors = {}
    
    for cls in priors:
        posterior = math.log(priors[cls])
        
        for col in sample.index:
            value = sample[col]
            posterior += math.log(likelihoods[col][value][cls])
        
        posteriors[cls] = posterior
    
    return max(posteriors, key=posteriors.get)

# Train model
priors = calculate_priors(y)
likelihoods = calculate_likelihoods(X, y)

# Test on a sample
sample = X.iloc[0]
prediction = predict(sample, priors, likelihoods)

print("Sample:", sample.to_dict())
print("Predicted Class:", prediction)