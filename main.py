import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

# 1. CREATE A TEST DATABASE (This simulates your CSV file)
data = {
    'herb_name': ['Ashwagandha', 'Turmeric', 'Ginkgo Biloba', 'Brahmi', 'Ginger'],
    'drug_name': ['Diazepam', 'Warfarin', 'Aspirin', 'Paracetamol', 'Heparin'],
    'interaction_type': ['Moderate Risk (Drowsiness)', 'High Risk (Bleeding)', 'High Risk (Bleeding)', 'Safe', 'Moderate Risk (Bleeding)']
}
df = pd.DataFrame(data)

# 2. PREPARE THE BRAIN
# We combine the names so the AI learns pairs
df['combined'] = df['herb_name'] + " " + df['drug_name']

# 3. BUILD THE AI PIPELINE
# TF-IDF turns names to math, RandomForest finds the patterns
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', RandomForestClassifier(n_estimators=100))
])

# 4. TRAIN THE MODEL
model.fit(df['combined'], df['interaction_type'])

# 5. TEST FUNCTION
def check_medicine(herb, drug):
    query = f"{herb} {drug}"
    prediction = model.predict([query])[0]
    
    print(f"\n--- AI Analysis ---")
    print(f"Herb: {herb}")
    print(f"Modern Drug: {drug}")
    print(f"Result: {prediction}")
    print("-------------------\n")

# --- TRY IT OUT ---
# Test 1: An interaction we taught it
check_medicine("Turmeric", "Warfarin")

# Test 2: Another interaction we taught it
check_medicine("Ashwagandha", "Diazepam")

# Test 3: Something safe we taught it
check_medicine("Brahmi", "Paracetamol")
