library(caret)
library(ggplot2)
library(nnet) # for multinom (logistic regression)

# Loading data
data(iris)
X <- iris[,1:4]
y <- iris$Species

# Split data
set.seed(0)
trainIndex <- createDataPartition(y, p = .7, list = FALSE)
trainX <- X[trainIndex,]
testX <- X[-trainIndex,]
trainY <- y[trainIndex]
testY <- y[-trainIndex]

# Creating model
model <- multinom(Species ~ ., data = data.frame(Species = trainY, trainX), maxit = 200)

# Predicting
pred <- predict(model, testX)

# Check accuracy
acc <- mean(pred == testY)

# Plot results
plot_data <- data.frame(testX, Predicted = pred, Actual = testY)
ggplot(plot_data, aes(x = Sepal.Length, y = Sepal.Width, color = Actual, shape = Predicted)) +
  geom_point() +
  labs(title = "Iris Classification Results", x = "Feature 1", y = "Feature 2") +
  theme_minimal() +
  scale_shape_manual(values=c(16,17,18)) +
  scale_color_manual(values=c("red", "green", "blue")) +
  theme(legend.title = element_blank()) +
  geom_point()

# Print accuracy
print(paste("Accuracy is", acc))

# Train and evaluate
train_and_evaluate <- function(X, y) {
  set.seed(42)
  trainIndex <- createDataPartition(y, p = .75, list = FALSE)
  X_train <- X[trainIndex,]
  X_test <- X[-trainIndex,]
  y_train <- y[trainIndex]
  y_test <- y[-trainIndex]
  
  mdl <- multinom(Species ~ ., data = data.frame(Species = y_train, X_train), maxit = 200)
  preds <- predict(mdl, X_test)
  acc <- mean(preds == y_test)
  return(list(mdl = mdl, acc = acc))
}

model2 <- train_and_evaluate(X, y)

a <- b <- 0
for (i in 1:length(pred)) {
  if (pred[i] == testY[i]) {
    a <- a + 1
  } else {
    b <- b + 1
  }
}
print(paste("Correct predictions:", a, "Incorrect predictions:", b))
