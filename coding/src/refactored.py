import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def load_iris_data():
    iris = load_iris()
    X, y = iris.data, iris.target
    return X, y

def split_data(X, y, test_size=0.3, random_state=0):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def train_logistic_regression(X_train, y_train, max_iter=200):
    model = LogisticRegression(max_iter=max_iter)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = np.mean(predictions == y_test)
    return accuracy

def plot_results(X, y, model=None):
    for i in range(3):
        plt.scatter(X[y == i, 0], X[y == i, 1], label=f"Class {i}")
    plt.title("Iris Classification Results")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    if model:
        plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1],
                    s=100, facecolors='none', edgecolors='k', label='Support Vectors')
    plt.legend()
    plt.show()

def train_and_evaluate(X, y, test_size=0.25, random_state=42):
    X_train, X_test, y_train, y_test = split_data(X, y, test_size=test_size, random_state=random_state)
    model = train_logistic_regression(X_train, y_train)
    accuracy = evaluate_model(model, X_test, y_test)
    return model, accuracy

def count_correct_incorrect_predictions(predictions, true_labels):
    correct_count, incorrect_count = np.sum(predictions == true_labels), np.sum(predictions != true_labels)
    return correct_count, incorrect_count

if __name__ == "__main__":
    # Load data
    X, y = load_iris_data()

    # Train and evaluate models
    model1, acc1 = train_and_evaluate(X, y)
    model2, acc2 = train_and_evaluate(X, y)

    # Plot results
    plot_results(X, y, model1)

    # Print accuracies
    print(f"Accuracy of Model 1: {acc1}")
    print(f"Accuracy of Model 2: {acc2}")

    # Count correct and incorrect predictions
    predictions = model1.predict(X)
    correct, incorrect = count_correct_incorrect_predictions(predictions, y)
    print(f"Model 1: Correct predictions: {correct}, Incorrect predictions: {incorrect}")

    predictions = model2.predict(X)
    correct, incorrect = count_correct_incorrect_predictions(predictions, y)
    print(f"Model 2: Correct predictions: {correct}, Incorrect predictions: {incorrect}")
