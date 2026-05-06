🪙 Cryptocurrency Scam Detection System

ML Project | Electronics & Communication Engineering
Narasaraopeta Engineering College, 2025


📌 Overview
With the rise of cryptocurrency, fraudulent tokens and scam projects have become a major threat to investors. This project builds a Machine Learning model using Random Forest to detect fraudulent cryptocurrency tokens based on on-chain behavioral patterns.
The model analyzes token characteristics to classify them as Scam or Legitimate with high accuracy.

✨ Key Features

✅ Detects scam crypto tokens using token metadata
✅ Handles imbalanced datasets using SMOTE oversampling
✅ High precision and recall on fraud detection
✅ Lightweight and fast — no deep learning needed
✅ Easy to extend with real blockchain data


🧠 Model

Algorithm: Random Forest Classifier (100 estimators)
Imbalance Handling: SMOTE (Synthetic Minority Oversampling Technique)
Train/Test Split: 80% / 20%
Class Weight: Balanced


📊 Features Used
FeatureDescriptioncontract_age_daysHow old the token contract isis_verifiedWhether the contract is verifiednum_holdersNumber of token holderstotal_supply_millionsTotal token supply in millions
Label: scam_reported → 1 (Scam) / 0 (Legitimate)

🔍 How Scam Tokens Behave
FeatureScam TokenLegitimate TokenContract AgeVery new (5–200 days)Older (200–1000 days)Verified❌ No✅ YesHoldersLow (10–1000)High (1000–10000)Total SupplyVery high (500M–1000M)Normal (1M–499M)

🛠️ Tech Stack
ToolPurposePythonCore languageScikit-learnRandom Forest modelImbalanced-learnSMOTE oversamplingPandas & NumPyData processing
