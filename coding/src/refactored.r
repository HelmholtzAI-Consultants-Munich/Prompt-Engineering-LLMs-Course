library(caret)
library(ggplot2)
library(nnet) # for multinom (logistic regression)

# Load and prepare data
data("iris")
set.seed(0)

# Simplify data splitting
splitIndex <- createDataPartition(iris$Species, p = .7, list = FALSE)
trainData <- iris[splitIndex, ]
testData <- iris[-splitIndex, ]

# Model training with multinomial logistic regression
model <- multinom(Species ~ ., data = trainData, maxit = 200)

# Prediction and evaluation
predictions <- predict(model, testData)
accuracy <- mean(predictions == testData$Species)

# Results plotting with ggplot2
ggplot(testData, aes(Sepal.Length, Sepal.Width, color = Species, shape = predictions)) +
  geom_point() + 
  labs(title = "Refined Iris Classification Results", x = "Sepal Length", y = "Sepal Width") +
  theme_minimal() +
  scale_shape_manual(values=c(16, 17, 18)) +
  scale_color_manual(values=c("red", "green", "blue")) +
  theme(legend.title = element_blank())

# Print refined accuracy
print(paste("Refined Accuracy is", accuracy))