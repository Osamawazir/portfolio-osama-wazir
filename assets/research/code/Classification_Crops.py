#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from scipy.stats import randint, uniform
from pathlib import Path
import os

# Load your dataset from a CSV file
# Replace 'your_dataset.csv' with the path to your dataset
# Set the working directory
new_directory = Path('/Users/fakhr/Documents/Python Scripts/Crop')
os.chdir(new_directory)
setwd('/Users/fakhr/Documents/Python Scripts/Crop')
data = pd.read_csv('Crop_r.csv')

# Assume the target column is named 'crop_name' and the rest are features
X = data.drop(columns=['label'])  # Features
y = data['label']  # Target (crop names)

# Encode the target labels (crop names) into numerical values
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a function to evaluate models
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model: {model.__class__.__name__}")
    print(f"Accuracy: {accuracy:.4f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))
    print("-" * 50)

# 1. Logistic Regression
param_dist_lr = {
    'C': uniform(0.1, 10),  # Regularization strength
    'penalty': ['l1', 'l2', 'elasticnet'],
    'solver': ['liblinear', 'saga']
}
lr_clf = LogisticRegression(random_state=42, max_iter=1000)
random_search_lr = RandomizedSearchCV(lr_clf, param_distributions=param_dist_lr, n_iter=10, cv=5, random_state=42)
random_search_lr.fit(X_train, y_train)
evaluate_model(random_search_lr.best_estimator_, X_test, y_test)

# 2. Random Forest Classifier
param_dist_rf = {
    'n_estimators': randint(50, 200),
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 10)
}
rf_clf = RandomForestClassifier(random_state=42)
random_search_rf = RandomizedSearchCV(rf_clf, param_distributions=param_dist_rf, n_iter=10, cv=5, random_state=42)
random_search_rf.fit(X_train, y_train)
evaluate_model(random_search_rf.best_estimator_, X_test, y_test)

# 3. Gradient Boosting Classifier
param_dist_gb = {
    'n_estimators': randint(50, 200),
    'learning_rate': uniform(0.01, 0.2),
    'max_depth': randint(3, 10),
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 10)
}
gb_clf = GradientBoostingClassifier(random_state=42)
random_search_gb = RandomizedSearchCV(gb_clf, param_distributions=param_dist_gb, n_iter=10, cv=5, random_state=42)
random_search_gb.fit(X_train, y_train)
evaluate_model(random_search_gb.best_estimator_, X_test, y_test)

# 4. Support Vector Classifier (SVC)
param_dist_svc = {
    'C': uniform(0.1, 10),
    'kernel': ['linear', 'rbf', 'poly'],
    'gamma': ['scale', 'auto']
}
svc_clf = SVC(random_state=42)
random_search_svc = RandomizedSearchCV(svc_clf, param_distributions=param_dist_svc, n_iter=10, cv=5, random_state=42)
random_search_svc.fit(X_train, y_train)
evaluate_model(random_search_svc.best_estimator_, X_test, y_test)

# 5. K-Nearest Neighbors Classifier (KNN)
param_dist_knn = {
    'n_neighbors': randint(1, 20),
    'weights': ['uniform', 'distance'],
    'p': [1, 2]  # 1: Manhattan distance, 2: Euclidean distance
}
knn_clf = KNeighborsClassifier()
random_search_knn = RandomizedSearchCV(knn_clf, param_distributions=param_dist_knn, n_iter=10, cv=5, random_state=42)
random_search_knn.fit(X_train, y_train)
evaluate_model(random_search_knn.best_estimator_, X_test, y_test)

# 6. XGBoost Classifier
param_dist_xgb = {
    'n_estimators': randint(50, 200),
    'learning_rate': uniform(0.01, 0.2),
    'max_depth': randint(3, 10),
    'subsample': uniform(0.6, 0.4),
    'colsample_bytree': uniform(0.6, 0.4)
}
xgb_clf = XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss')
random_search_xgb = RandomizedSearchCV(xgb_clf, param_distributions=param_dist_xgb, n_iter=10, cv=5, random_state=42)
random_search_xgb.fit(X_train, y_train)
evaluate_model(random_search_xgb.best_estimator_, X_test, y_test)