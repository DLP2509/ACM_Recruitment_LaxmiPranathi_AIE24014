import numpy as np
from sklearn.linear_model import LinearRegression

data = [[0.0, 0.0, 0.0], [0.5, 1.5, 23.4], [1.2, 2.3, 45.6], [1.8, 3.7, 12.1],
        [2.4, 4.2, 78.9], [2.9, 5.1, 34.5], [3.5, 6.4, 56.7], [4.1, 7.8, 67.8],
        [4.7, 8.5, 89.0], [5.2, 9.1, 12.3], [5.8, 1.0, 45.6], [6.3, 2.4, 78.9],
        [6.9, 3.1, 34.5], [7.4, 4.6, 56.7], [8.0, 5.2, 67.8], [8.6, 6.8, 89.0],
        [9.1, 7.3, 12.3], [9.7, 8.9, 45.6], [10.0, 9.0, 78.9], [10.5, 0.5, 34.5]]

data = np.array(data)

X = data[:, :2]
y = data[:, 2]

model = LinearRegression()
model.fit(X, y)

a, b = 8, 15
print(f"Predicted value for a={a}, b={b}: {model.predict([[a, b]])[0]}")
