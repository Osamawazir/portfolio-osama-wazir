library(rpart)

library(caret)
#library(adabag)

# Load dataset
data <- read.csv("Crop_r.csv")

# Remove rows with missing values
data <- na.omit(data)

# Ensure data is not empty after removing NA values
if (nrow(data) == 0) stop("Error: No valid rows after removing missing values")

# Define X (features) and y (target)
X <- data[, -which(names(data) == "label")]
y <- as.factor(data$label)  # Convert to factor

# Train-test split
set.seed(42)
train_index <- sample(1:nrow(data), 0.8 * nrow(data))
X_train <- X[train_index, ]
X_test <- X[-train_index, ]
y_train <- y[train_index]
y_test <- y[-train_index]

# Define train control
ctrl <- trainControl(method = "cv", number = 5, search = "random")


# Train Decision Tree model
dt_model <- train(
  x = X_train,
  y = y_train,
  method = "rpart",
  tuneLength = 10,
  trControl = ctrl
)
print("Decision Tree Results:")
evaluate_model(dt_model, X_test, y_test)