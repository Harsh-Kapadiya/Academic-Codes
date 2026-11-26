from collections import Counter, defaultdict

# Weather dataset
data = [
    ("Sunny", "Hot", "High", "Weak", "No"),
    ("Sunny", "Hot", "High", "Strong", "No"),
    ("Overcast", "Hot", "High", "Weak", "Yes"),
    ("Rain", "Mild", "High", "Weak", "Yes"),
    ("Rain", "Cool", "Normal", "Weak", "Yes"),
    ("Rain", "Cool", "Normal", "Strong", "No"),
    ("Overcast", "Cool", "Normal", "Strong", "Yes"),
    ("Sunny", "Mild", "High", "Weak", "No"),
    ("Sunny", "Cool", "Normal", "Weak", "Yes"),
    ("Rain", "Mild", "Normal", "Weak", "Yes"),
    ("Sunny", "Mild", "Normal", "Strong", "Yes"),
    ("Overcast", "Mild", "High", "Strong", "Yes"),
    ("Overcast", "Hot", "Normal", "Weak", "Yes"),
    ("Rain", "Mild", "High", "Strong", "No"),
]


# Split features and labels
X = [row[0:4] for row in data]
y = [row[4] for row in data]


# Training function
def train_naive_bayes(X_train, y_train):
    class_counts = Counter(y_train)
    total = len(y_train)
    priors = {}
    likelihoods = defaultdict(lambda: defaultdict(Counter))
    feature_values = defaultdict(set)
    # Priors
    for cls in class_counts:
        priors[cls] = class_counts[cls] / total
    # Count feature values for each class
    for features, cls in zip(X_train, y_train):
        for i, value in enumerate(features):
            likelihoods[cls][i][value] += 1
    feature_values[i].add(value)
    return priors, likelihoods, class_counts, feature_values


# Prediction function
def predict(sample, priors, likelihoods, class_counts, feature_values):
    posteriors = {}
    for cls in priors:
        prob = priors[cls]
    for i, value in enumerate(sample):
        count = likelihoods[cls][i][value]
    total_count = class_counts[cls]
    # Laplace smoothing
    prob *= (count + 1) / (total_count + len(feature_values[i]))
    posteriors[cls] = prob
    predicted_class = max(posteriors, key=posteriors.get)
    return predicted_class, posteriors


# Train model
priors, likelihoods, class_counts, feature_values = train_naive_bayes(X, y)
# Test samples
test_samples = [
    ("Sunny", "Cool", "High", "Strong"),
    ("Overcast", "Mild", "High", "Weak"),
    ("Rain", "Cool", "Normal", "Weak"),
]
print("Predictions:\n")
for sample in test_samples:
    pred, probs = predict(sample, priors, likelihoods, class_counts, feature_values)
    print("Sample:", sample)
    print("Posterior Probabilities:", probs)
    print("Predicted Class:", pred)
    print()
# Accuracy on dataset
correct = 0
for sample, actual in zip(X, y):
    pred, _ = predict(sample, priors, likelihoods, class_counts, feature_values)
    if pred == actual:
        correct += 1
accuracy = correct / len(y) * 100
print("Accuracy on dataset:", accuracy, "%")
