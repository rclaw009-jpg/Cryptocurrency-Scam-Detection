import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE

np.random.seed(42)
n = 300

# Make scam tokens behave more scammy
scam_flags = np.random.choice([0, 1], size=n, p=[0.7, 0.3])
data = {
    "token_name": [f"Token{i}" for i in range(n)],
    "contract_age_days": [np.random.randint(5, 200) if scam_flags[i] == 1 else np.random.randint(200, 1000) for i in range(n)],
    "is_verified": [0 if scam_flags[i] == 1 else 1 for i in range(n)],
    "num_holders": [np.random.randint(10, 1000) if scam_flags[i] == 1 else np.random.randint(1000, 10000) for i in range(n)],
    "total_supply_millions": [round(np.random.uniform(500, 1000), 2) if scam_flags[i] == 1 else round(np.random.uniform(1, 499), 2) for i in range(n)],
    "scam_reported": scam_flags
}

df = pd.DataFrame(data)
df.head()

X = df.drop(columns=["token_name", "scam_reported"])
y = df["scam_reported"]

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy*100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
