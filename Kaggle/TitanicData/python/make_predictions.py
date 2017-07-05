import numpy as np
import pandas as pd
import logistic_regression as lr
import manipulate_features as mf
import neural_networks as nn

def predict_titanic_simple(theta):
    """
    Predict survival on titanic using only the given
    features in the original data.
    """
    # Read in Titanic data into a DataFrame
    df = pd.read_csv('titanic_test_clean1.csv')

    # Make values a numpy array
    X = df.as_matrix()

    # Normalize values and store mean and std deviation
    X_norm, mu, sigma = mf.normalize(X)

    # Add bias intercept
    X_norm = np.append(np.ones((X_norm.shape[0], 1)), X_norm, axis=1)

    # Make predictions
    y = lr.predict(X_norm, theta)

    # Generate all the passenger IDs
    ids = list(range(892, 1310))

    # Make DataFrame for exporting
    df = pd.DataFrame({'PassengerId': ids, 'Survived': y.tolist()})
    df.to_csv('submission01.csv', index=False)

def predict_titanic_features(theta, power):
    """
    Predict survival on titanic data using logistic
    regression with extra features.
    """
    # Read in Titanic data into a DataFrame
    df = pd.read_csv('titanic_test_clean1.csv')

    # Make values a numpy array
    X = df.as_matrix()

    # Add additional polynomial features
    X_features = mf.add_polynomial_features(X, power)

    # Normalize values and store mean and std deviation
    X_norm, mu, sigma = mf.normalize(X_features)

    # Add bias intercept
    X_norm = np.append(np.ones((X_norm.shape[0], 1)), X_norm, axis=1)

    # Make predictions
    y = lr.predict(X_norm, theta)

    # Generate all the passenger IDs
    ids = list(range(892, 1310))

    # Make DataFrame for exporting
    df = pd.DataFrame({'PassengerId': ids, 'Survived': y.tolist()})
    df.to_csv('submission03.csv', index=False)


def predict_titanic_nn(theta1, theta2):
    """
    Predict survival on titanic data using neural network.
    """
    # Read in Titanic data into a DataFrame
    df = pd.read_csv('titanic_test_clean1.csv')

    # Make values a numpy array
    X = df.as_matrix()

    # Normalize values and store mean and std deviation
    X_norm, mu, sigma = mf.normalize(X)

    # Add bias intercept
    X_norm = np.append(np.ones((X_norm.shape[0], 1)), X_norm, axis=1)

    # Make predictions from theta values
    y = nn.predict(X_norm, theta1, theta2)

    # Generate all passenger IDs
    ids = list(range(892, 1310))

    # Make DataFrame for exporting
    df = pd.DataFrame({'PassengerId': ids, 'Survived': y.tolist()})
    df.to_csv('submission04.csv', index=False)


theta = np.array([-0.54618434, -1.01096887, -1.20680903, -0.53412613,
                  -0.33130297, -0.15341355, 0.03545634])

predict_titanic_simple(theta)
