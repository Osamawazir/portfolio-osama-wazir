#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:35:09 2025

@author: fakhr
"""
# Import necessary libraries
import os
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from scipy.stats import randint


# Set the working directory and load the dataset
new_directory = Path('/Users/fakhr/Documents/Python Scripts/Crop')
os.chdir(new_directory)

data = pd.read_csv('Crop_r.csv')

# Assuming the target column is named 'label' and the rest are features
X = data.drop(columns=["label"])  # Features
y = data["label"]  # Target (crop names)

# Check for missing values
print("Missing values in the dataset:")
print(data.isnull().sum())

# Remove rows with missing values (if any)
data = data.dropna()

# Re-define X and y after removing missing values
X = data.drop(columns=["label"])
y = data["label"]

# Encode the target labels (crop names) into numerical values
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the parameter distribution for Randomized Search
param_dist = {
    "max_depth": [None, 10, 20, 30, 50],  # Maximum depth of the tree
    "min_samples_split": randint(2, 20),  # Minimum samples required to split a node
    "min_samples_leaf": randint(1, 20),   # Minimum samples required at a leaf node
    "criterion": ["gini", "entropy"]      # Splitting criterion
}

# Initialize the Decision Tree classifier
dt_model = DecisionTreeClassifier(random_state=42)

# Perform Randomized Search
random_search = RandomizedSearchCV(
    estimator=dt_model,
    param_distributions=param_dist,
    n_iter=50,  # Number of parameter combinations to try
    cv=5,       # 5-fold cross-validation
    scoring="accuracy",
    random_state=42,
    verbose=1
)

# Fit the Randomized Search to the training data
random_search.fit(X_train, y_train)

# Get the best model and its hyperparameters
best_dt_model = random_search.best_estimator_
best_params = random_search.best_params_
print("Best Hyperparameters:")
print(best_params)

# Evaluate the best model on the test set
y_pred = best_dt_model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

# Print classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# Print confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))