from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create and train model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Predict for a sample flower
prediction = model.predict([[5.1, 3.5, 1.4, 0.2]])

print("Predicted Class:", prediction)
print("Predicted Flower:", iris.target_names[prediction[0]])