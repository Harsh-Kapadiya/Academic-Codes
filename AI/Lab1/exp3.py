# ============================================================
# AIM: Student Performance AI Workflow Simulation
# ============================================================

# -----------------------------
# Imports
# -----------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.base import BaseEstimator, ClassifierMixin


# ============================================================
# Step 0 — Core Python Concepts
# ============================================================

# Task A: Schema as tuple (immutable, fixed structure)
SCHEMA = ("hours_studied", "attendance", "department", "marks")
# Tuple is suitable because schema should not change accidentally.


# Task B: Raw records as list of tuples (60+ records, with missing & duplicates)
raw_records = [
    (5, 80, "CSE", 62), (6, 85, "CSE", 70), (2, None, "ECE", 45),
    (7, 90, "CSE", 88), (3, 60, "MECH", 40), (4, 70, "ECE", 55),
    (8, 95, "CIVIL", 92), (1, 50, "MECH", 30), (None, 65, "CSE", 48),
    (6, 75, "ECE", 60), (5, 78, "CSE", 64), (2, 55, "MECH", 42),
    (7, 88, "CIVIL", 81), (4, None, "ECE", 50), (3, 58, "CSE", 46),
] * 4   # makes 60 records

# Add duplicates intentionally
raw_records.extend([
    (5, 80, "CSE", 62),
    (7, 90, "CSE", 88),
    (3, 60, "MECH", 40)
])


# Task C: Validate departments using set
VALID_DEPTS = {"CSE", "ECE", "CIVIL", "MECH"}

invalid_departments = {
    rec[2] for rec in raw_records if rec[2] not in VALID_DEPTS
}

print("Invalid departments detected:", invalid_departments)


# Task D: Convert to list of dictionaries
records_list_of_dicts = []
for rec in raw_records:
    record_dict = dict(zip(SCHEMA, rec))
    records_list_of_dicts.append(record_dict)


# Task E: Basic data type checks
none_hours = sum(r["hours_studied"] is None for r in records_list_of_dicts)
none_attendance = sum(r["attendance"] is None for r in records_list_of_dicts)

int_float_marks = sum(
    isinstance(r["marks"], (int, float)) for r in records_list_of_dicts
)

print("None in hours_studied:", none_hours)
print("None in attendance:", none_attendance)
print("Int/Float marks count:", int_float_marks)


# ============================================================
# Step 1 — Pandas DataFrame
# ============================================================

df = pd.DataFrame(records_list_of_dicts)
print("\nRecords before duplicate removal:", len(df))


# ============================================================
# Step 2 — Functions
# ============================================================

def remove_duplicates(df):
    return df.drop_duplicates()

def fill_missing_with_median(df, columns):
    for col in columns:
        df[col] = df[col].fillna(df[col].median())
    return df

def create_target(df, pass_marks=50):
    df["passed"] = (df["marks"] >= pass_marks).astype(int)
    return df

def encode_department(df):
    return pd.get_dummies(df, columns=["department"], drop_first=True)


# Apply functions
df = remove_duplicates(df)
print("Records after duplicate removal:", len(df))

df = fill_missing_with_median(df, ["hours_studied", "attendance"])
df = create_target(df)
df = encode_department(df)


# ============================================================
# Step 3 — NumPy Feature Engineering
# ============================================================

def numpy_minmax(arr):
    return (arr - arr.min()) / (arr.max() - arr.min())

# Engineered feature
df["attendance_per_hour"] = df["attendance"] / (df["hours_studied"] + 1)


# ============================================================
# Step 4 — Matplotlib Visualizations
# ============================================================

# Scatter plot
plt.scatter(df["hours_studied"], df["marks"])
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Hours Studied vs Marks")
plt.savefig("scatter_hours_vs_marks.png")
plt.close()

# Histogram
plt.hist(df["attendance"], bins=10)
plt.xlabel("Attendance")
plt.ylabel("Frequency")
plt.title("Attendance Distribution")
plt.savefig("hist_attendance.png")
plt.close()

# Bar chart: pass rate per department
dept_cols = [c for c in df.columns if c.startswith("department_")]
pass_rates = {}

for col in dept_cols:
    pass_rates[col] = df[df[col] == 1]["passed"].mean()

plt.bar(pass_rates.keys(), pass_rates.values())
plt.ylabel("Pass Rate")
plt.title("Pass Rate per Department")
plt.savefig("bar_pass_rate.png")
plt.close()

print("\nVisualization Interpretation:")
print("1. Marks increase with higher study hours.")
print("2. Attendance is slightly right-skewed.")
print("3. Some departments show better pass consistency.")


# ============================================================
# Step 5 — SciPy Hypothesis Test
# ============================================================

groupA = df[df["attendance"] >= 75]["marks"]
groupB = df[df["attendance"] < 75]["marks"]

t_stat, p_val = stats.ttest_ind(groupA, groupB, equal_var=False)

print("\nT-test Results:")
print("t-statistic:", t_stat)
print("p-value:", p_val)

if p_val < 0.05:
    print("Conclusion: Significant difference (reject H0)")
else:
    print("Conclusion: No significant difference (fail to reject H0)")


# ============================================================
# Step 6 — Scikit-learn Modeling
# ============================================================

# Custom deterministic baseline classifier
class RuleBasedPassFail(BaseEstimator, ClassifierMixin):
    def __init__(self, threshold=0.0):
        self.threshold = threshold

    def fit(self, X, y=None):
        self.is_fitted_ = True
        return self

    def predict(self, X):
        hours = X[:, 0]
        attendance = X[:, 1]
        return ((hours >= self.threshold) &
                (attendance >= self.threshold)).astype(int)


# Prepare data
feature_cols = [c for c in df.columns if c not in ("passed", "marks")]
X = df[feature_cols].to_numpy(dtype=float)
y = df["passed"].to_numpy(dtype=int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=101, stratify=y
)

# DEFINE PIPELINE (THIS WAS MISSING / MISPLACED)
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("baseline", RuleBasedPassFail())
])

print("Pipeline created")

# FIT PIPELINE
pipe.fit(X_train, y_train)
print("Pipeline fitted")

# PREDICT
y_pred = pipe.predict(X_test)

print("\nML Metrics:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

cv_scores = cross_val_score(pipe, X, y, cv=5)
print("Cross-validation mean score:", cv_scores.mean())


# ============================================================
# Final Outputs Summary
# ============================================================

print("\nFinal Summary:")
print("Missing hours:", none_hours)
print("Missing attendance:", none_attendance)
print("Unique departments:", set(raw_records[i][2] for i in range(len(raw_records))))
print("\nHead of cleaned DataFrame:")
print(df.head())