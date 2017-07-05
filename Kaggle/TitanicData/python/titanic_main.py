"""
Script for training the titanic data
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import logistic_regression as lr
import manipulate_features as mf
import make_predictions as mp
import neural_networks as nn

def simple_logistic_regression():
    """
    Run logistic regression on the data without extra
    features added.

    Note: With 6 features, alpha of 1-2 worked best.
    """
    # Read in Titanic data into a DataFrame
    df = pd.read_csv('titanic_data_clean1.csv')

    # Move result column ('Survived') to another variable
    y = df['Survived']
    del df['Survived']

    # Make values and results numpy arrays
    y = y.as_matrix()
    X = df.as_matrix()

    # Normalize values and store mean and std deviation
    X_norm, mu, sigma = mf.normalize(X)

    # Add bias intercept
    X_norm = np.append(np.ones((y.size, 1)), X_norm, axis=1)

    # Initialize theta values
    initial_theta = np.zeros(X_norm.shape[1])

    # Run training algorithm and store new theta values
    theta, _, _ = lr.train(X_norm, initial_theta, y,
                           plotcosts=False, outputs=True)

    #mp.predict_titanic(theta)
    # Plot the learning curve of the training algorithm to
    # evaluate the current feature set
    #lr.plot_learning_curve(X_norm, initial_theta, y)


def logistic_regression(power=4):
    """
    Run logistic regression on the data after adding additional
    features.

    Note: With many features, lower alpha (0.01-0.1) worked best.
    """
    # Read in Titanic data into a DataFrame
    df = pd.read_csv('titanic_data_clean1.csv')

    # Move result column ('Survived') to another variable
    y = df['Survived']
    del df['Survived']

    # Make values and results numpy arrays
    y = y.as_matrix()
    X = df.as_matrix()

    # Add additional polynomial features
    X_features = mf.add_polynomial_features(X, power)

    # Normalize values and store mean and std deviation
    X_norm, mu, sigma = mf.normalize(X_features)

    # Add bias intercept
    X_norm = np.append(np.ones((X_norm.shape[0], 1)), X_norm, axis=1)

    # Initialize theta values
    initial_theta = np.zeros(X_norm.shape[1])

    # Run training algorithm and store new theta values
    theta, _, _ = lr.train(X_norm, initial_theta, y,
                           plotcosts=False, outputs=True)

    # Make a prediction file from the Kaggle test file
    mp.predict_titanic_features(theta, power)

    # Plot the learning curve of the training algorithm to
    # evaluate the current feature set
    #lr.plot_learning_curve(X_norm, initial_theta, y)


def neural_network():
    """
    Train a neural network.
    """
    # Read in Titanic data into a DataFrame
    df = pd.read_csv('titanic_data_clean1.csv')

    # Move result column ('Survived') to another variable
    y = df['Survived']
    del df['Survived']

    # Make the values and results numpy arrays
    y = y.as_matrix()
    X = df.as_matrix()

    # Normalize values and store mean and std deviation
    X_norm, mu, sigma = mf.normalize(X)

    # Generate initial theta values randomly
    init_theta1 = np.random.rand(X_norm.shape[1], X_norm.shape[1] + 1)
    init_theta2 = np.random.rand(X_norm.shape[1] + 1)

    # Add bias intercept
    X_norm = np.append(np.ones((X_norm.shape[0], 1)), X_norm, axis=1)

    # Train theta parameters
    theta1, theta2, _ = nn.train(X_norm, init_theta1, init_theta2, y)

    # Make a prediction file from the Kaggle test file
    mp.predict_titanic_nn(theta1, theta2)


#simple_logistic_regression()
#logistic_regression()
neural_network()
