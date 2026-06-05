
# Load necessary libraries
library(caret)
library(ranger)  # For Random Forest
library(gbm)
library(e1071)
library(class)
library(xgboost)

#sw
setwd("/Users/fakhr/Documents/Python Scripts/Crop")
# Load your dataset (replace 'your_dataset.csv' with your file path)
data <- read.csv("Crop_r.csv")

# Assuming the target column is named 'crop_name' and the rest are features
X <- data[, -which(names(data) == "label")]  # Features
y <- data$label  # Target (crop names)

# Encode the target labels (crop names) into numerical values
y <- as.factor(y)

# Split the dataset into training and testing sets
set.seed(42)
train_index <- createDataPartition(y, p = 0.8, list = FALSE)
X_train <- X[train_index, ]
X_test <- X[-train_index, ]
y_train <- y[train_index]
y_test <- y[-train_index]

# Define a function to evaluate models
evaluate_model <- function(model, X_test, y_test) {
  y_pred <- predict(model, X_test)
  confusion_matrix <- confusionMatrix(y_pred, y_test)
  print(confusion_matrix)
}

# Set up randomized search control
ctrl <- trainControl(method = "cv", number = 5, search = "random")

# 1. Random Forest using ranger
set.seed(42)
rf_model <- train(
  x = X_train,
  y = y_train,
  method = "ranger",
  tuneLength = 10,  # Number of random combinations to try
  trControl = ctrl
)
print("Random Forest Results:")
evaluate_model(rf_model, X_test, y_test)

# # 2. Gradient Boosting (GBM)
# # 2. Gradient Boosting (GBM) - Simplified
# set.seed(42)
# gbm_model <- train(
#   x = X_train,
#   y = y_train,
#   method = "gbm",
#   tuneLength = 3,  # Reduce the number of combinations
#   trControl = ctrl,
#   verbose = FALSE
# )
# print("Gradient Boosting Results:")
# evaluate_model(gbm_model, X_test, y_test)

# 3. Support Vector Machine (SVM)
set.seed(42)
svm_model <- train(
  x = X_train,
  y = y_train,
  method = "svmRadial",
  tuneLength = 10,
  trControl = ctrl
)
print("SVM Results:")
evaluate_model(svm_model, X_test, y_test)

# 4. K-Nearest Neighbors (KNN)
set.seed(42)
knn_model <- train(
  x = X_train,
  y = y_train,
  method = "knn",
  tuneLength = 10,
  trControl = ctrl
)
print("KNN Results:")
evaluate_model(knn_model, X_test, y_test)

# 5. XGBoost
set.seed(42)
xgb_model <- train(
  x = X_train,
  y = y_train,
  method = "xgbTree",
  tuneLength = 10,
  trControl = ctrl
)
print("XGBoost Results:")
evaluate_model(xgb_model, X_test, y_test)