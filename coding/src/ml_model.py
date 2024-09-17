import matplotlib.pyplot as plt
import numpy as np
import sklearn.datasets as skd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Loading data
iris = skd.load_iris()
X, y = iris.data, iris.target

# Split data
trainX, testX, trainY, testY = train_test_split(X, y, test_size=0.3, random_state=0)

# Creating model
model = LogisticRegression(max_iter=200)
model.fit(trainX, trainY)

# Predicting
pred = model.predict(testX)

# Check accuracy
acc = np.mean(pred == testY)

# Plot results
for i in range(3):
    plt.scatter(testX[testY == i, 0], testX[testY == i, 1], label=f"Class {i}")
plt.title("Iris Classification Results")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()

# Print accuracy
print(f"Accuracy is {acc}")


# Train and evaluate
def train_and_evaluate(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )
    mdl = LogisticRegression()
    mdl.fit(X_train, y_train)
    preds = mdl.predict(X_test)
    acc = np.mean(preds == y_test)
    return mdl, acc


model2, model2_accuracy = train_and_evaluate(X, y)

a, b = 0, 0
for i in range(len(pred)):
    if pred[i] == testY[i]:
        a += 1
    else:
        b += 1
print(f"Correct predictions: {a}, Incorrect predictions: {b}")
