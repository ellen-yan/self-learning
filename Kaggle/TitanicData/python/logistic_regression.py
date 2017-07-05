"""
Module for training theta values for logistic regression with regularization.

Functions
---------

sigmoid(float) -> float
    Given a number, returns the result after applying the sigmoid function
    f(x) = 1 / (1 + exp(-x)).

predict(2D numpy.array matrix X, numpy.array theta) -> numpy.array
    Given a 2D numpy array matrix X and a 1D numpy array theta, returns
    a 2D numpy array containing the predicted value as 0 or 1 (rounded).

cost_function(2D numpy.array X, numpy.array theta, numpy.array y, l=0) ->
                            float J, numpy array grad
    Given a matrix of values X, the training parameters theta, the
    actual results y and a lambda (l) value for regularization, returns the
    cost of the logistic regression with current parameters and the
    gradients.

accuracy_rate(2D numpy.array X, numpy.array theta, numpy.array y) ->
                            float accuracy
    Given a matrix of values X, prediction parameters theta and the
    actual results y, returns the accuracy of the parameters given.

train_logistic(2D numpy.array X, numpy.array initial_theta, numpy.array y,
               float alpha, float lambda, float tolerance=1E-6,
               max_iter=math.inf) ->
                            numpy.array theta, numpy.array costs
    Given a matrix of values X, known results y, a value for alpha
    (learning rate), and a value for lambda (regularization
    parameter), returns a numpy array theta with the learned parameters.

train(2D numpy.array X, numpy.array initial_theta, numpy.array y,
      int num=None, bool plotcosts=False) ->
                            numpy.array theta, float Jtrain, float Jcv
    Given a matrix of training examples X, known results y (numpy array),
    and the number of desired training examples, randomly splits
    the given examples into a training set, cross-validation set, and
    test-set with the latter two sets of equal size. If no value for num
    is given (or the given value for num is invalid), then 60%% is used
    for training, 20%% for cross-validation, and 20%% for testing. Trains
    the parameters theta on various values of alpha (learning rate) and
    lambda (regularization) and tests these on the cross-validation set
    to determine the best values for alpha and lambda. Prints out the
    prediction accuracy on the training, cross-validation, and test sets.
    Returns the numpy array theta that contains the best parameters
    (lowest Jcv), and the values for Jtrain and Jcv.

plot_learning_curve(2D numpy.array X, , numpy.array initial_theta,
                    numpy.array y) -> None
    Given a matrix of training examples and known results y (a numpy
    array), trains for a set of parameters theta with increasing number
    of training examples and plots a learning curve of Jtest and Jcv with
    increasing number of training examples.

plot_cost_function(numpy.array J) -> None
    Plots the given array of costs in a matplotlib.pyplot.
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def sigmoid(z):
    """
    Returns a value or numpy array with the sigmoid function
    applied element-wise. Sigmoid function is f(x) = 1/(1 + exp(-x))

    Parameters
    ----------
    z : value, numpy array (1D or 2D)
        The object for the sigmoid function to be applied to.

    Returns
    -------
    An object with the same type and dimensions as the input z
    where the sigmoid function has been applied element-wise.
    """
    return 1 / (1 + np.exp(-1 * z))

def predict(X, theta):
    """
    Returns a numpy array of predicted values using logistic regression.
    (Does not add a 0th intercept of ones to X.)

    Parameters
    ----------
    X : 1D or 2D numpy array
        Each row is one training example.
    theta : 1D numpy array
        Theta parameters for each feature.
    """
    return np.round(sigmoid(X.dot(theta))).astype(int)


def cost_function(X, theta, y, l=0):
    """
    Returns the logistic regression cost (J) and gradients (grad)
    of the given data X, parameters theta, and known results y.
    Assumes the first term (bias intercept) is not regularized.

    Parameters
    ----------
    X : 2D numpy array
        A matrix where examples are separated by row.
    theta : 1D numpy array
        The theta parameters for predicting the results.
    y : 1D numpy array
        Known results of each example from X.
    l : optional, default 0
        The regularization parameter lambda.

    Returns
    -------
    J : float
        The cost function result.
    grad : 1D numpy array
        The gradient of the theta values.
    """

    m = y.size
    grad = np.empty(theta.shape)

    predictions = sigmoid(X.dot(theta))
    J = (1/m) * ((-1 * y).dot(np.log(predictions)) - \
                 (1 - y).dot(np.log(1 - predictions))) + \
                 (l/2/m) * theta[1:].dot(theta[1:])

    grad[0] = (1/m) * ((X[:,0].transpose().dot(predictions - y)))
    grad[1:] = (1/m) * ((X[:, 1:].transpose().dot(predictions - y)) + \
               (l/m) * theta[1:])

    return J, grad


def accuracy_rate(X, theta, y):
    """
    Returns the accuracy rate of the predictions using logistic
    regression.

    Parameters
    ----------
    X : 2D numpy array
        An array of examples which are separated by rows and
        contain the bias intercept of ones in the first column.
    theta : 1D numpy array
        The theta parameters for logstic regression, including
        the bias term.
    y : 1D numpy array
        The actual results to compare the predictions against.

    Results
    -------
    accuracy : float
        The fraction of correct predictions (0 <= accuracy <= 1).
    """

    p = predict(X, theta)
    return np.sum(p == y) / len(y)


def train_logistic(X, initial_theta, y, alpha, l,
                   tolerance=0.000001, max_iter=math.inf):
    """
    Returns a numpy array theta containing the trained theta parameters
    based on the given function arguments. Assumes bias argument is
    already included in the given training examples. The initial theta
    values are all set to zero.

    Parameters
    ----------
    X : 2D numpy array
        Training examples separated by rows.
    initial_theta : 1D numpy array
        Initial theta parameter values.
    y : 1D numpy array
        Known results of training examples.
    alpha : float
        The learning rate (coefficient before the gradient).
    l : float
        The regularization parameter.
    tolerance : float, default 0.000001
        The function tolerance for the gradient descent.
        When one step decreases the cost by less than this
        value, the gradient descent is considered converged.
    max_iter : int, default None
        Maximum number of iterations of gradient descent. If
        not specified, gradient descent runs until tolerance
        value reached.

    Returns
    -------
    theta : 1D numpy array
        The trained theta parameters.
    costs : 1D numpy array
        The values of the cost function at each iteration.
    """

    # Initialize the difference between successive iterations of
    # gradient descent
    diff = math.inf

    # Initialize an array of cost values to be used for verifying
    # that cost function is decreasing
    costs = []

    # Calculate the initial and second cost and gradients
    J, grad = cost_function(X, initial_theta, y, l=l)
    costs.append(J)
    theta = initial_theta - alpha * grad
    J_previous = J

    # Apply gradients until the cost difference between steps
    # is less than the tolerance limit
    count = 1
    while ((diff == math.inf) or (diff < -tolerance)) and count <= max_iter:
        J, grad = cost_function(X, theta, y, l=l)
        costs.append(J)

        # Store the difference between the current cost and
        # the cost calculated from the previous iteration then store
        # the cost from this iteration
        diff = J - J_previous
        J_previous = J

        # Change theta values according to learning rate alpha
        theta = theta - alpha * grad

        # Increment number of iterations completed
        count += 1

    return theta, np.array(costs)


def train(X, initial_theta, y, num=None, plotcosts=False, outputs=False):
    """
    Returns the theta parameters trained using train_logistic
    from the given training examples X and y with the number of
    examples in the training set given by num. Also returns the
    costs Jtrain and Jcv from each iteration of the training.
    During training, values of alpha (learning rate) and lambda
    (regularization parameter) from 0.01 to 30 are tested.

    Parameters
    ----------
    X : 2D numpy array
        Training examples where examples are separated by rows.
        The bias term is assumed to be included.
    initial_theta : 1D numpy array
        Initial theta parameter values.
    y : 1D numpy array
        The known results of examples from X.
    num : int, default None
        The number of examples to be used in the training set.
        Valid range: 1 to number of given examples minus 2
        (i.e. X.shape[0] - 2). If given num is invalid or the default,
        the number of training examples used is 60%% of the total size.
    plotcosts : bool, default False
        Plot the cost function for each lambda value tested
    outputs : bool, default False
        Output the training results (optimum value of lambda,
        accuracies of training, cross-validation, and test sets,
        and the theta values) to console.

    Returns
    -------
    theta : 1D numpy array
        Trained theta parameters
    Jtrain : float
        The value of the cost function for the training set
        using the trained parameters theta, Jtrain
    Jcv : float
        The value of the cost function for the cross-validation
        set using the trained parameters theta, Jcv
    """
    # The values of alpha and lambda
    ALPHAS = [0.01, 0.03, 0.1, 0.3, 1, 3, 10]
    LAMBDAS = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000, 3000]

    # The number of given examples
    m = X.shape[0]

    # If the number of training examples has been specified
    if (not num) or num <= 0 or num > (m - 2):
        num = int(np.round(0.6 * m)) # 60% of all examples given

    # The number of examples in the cross-validation set and test set
    num_cross = int(np.round((m - num) * 0.5))
    num_test = m - num - num_cross

    # Randomly shuffle the rows of the examples and reassign
    # the examples to X and y
    shuffle_array = np.concatenate([X, y[:, None]], axis=1)
    np.random.shuffle(shuffle_array)
    X = shuffle_array[:, :-1]
    y = shuffle_array[:, -1]

    # Extract the examples for training, cross-validation, and testing
    X_train = X[:num, :]
    y_train = y[:num]
    X_cv = X[num:(num + num_cross), :]
    y_cv = y[num:(num + num_cross)]
    X_test = X[(num + num_cross):, :]
    y_test = y[(num + num_cross):]

    performance = []
    for a in range(len(ALPHAS)):
        for l in range(len(LAMBDAS)):
            theta_train, J_array = train_logistic(X_train, initial_theta, y_train,
                                                  ALPHAS[a], LAMBDAS[l],
                                                  max_iter=400)
            performance.append(accuracy_rate(X_cv, theta_train, y_cv))
            if plotcosts:
                plot_cost_function(J_array)

    # Find index of the highest accuracy
    i = max(range(len(performance)), key=performance.__getitem__)
    a = math.floor(i/len(LAMBDAS))
    l = i % len(LAMBDAS)

    # Train theta values with the best alpha and lambdas
    theta, J_array = train_logistic(X_train, initial_theta, y_train,
                                    ALPHAS[a], LAMBDAS[l], max_iter=400)

    # Evaluate performances on the training, cross-validation, and test sets
    accuracy_train = accuracy_rate(X_train, theta, y_train)
    accuracy_cv = accuracy_rate(X_cv, theta, y_cv)
    accuracy_test = accuracy_rate(X_test, theta, y_test)

    if outputs:
        print("Training Complete")
        print("-----------------")
        print("The optimum value of alpha is :", ALPHAS[a])
        print("The optimum value of lambda is :", LAMBDAS[l])
        print("The accuracy on the training set is :", accuracy_train)
        print("The accuracy on the cross-valiation set is :", accuracy_cv)
        print("The accuracy on the test set is :", accuracy_test)
        print("Trained theta parameters:")
        print(theta)

    # Evaluate the cost function for training and cross-validation sets
    Jtrain, _ = cost_function(X_train, theta, y_train, l=LAMBDAS[l])
    Jcv, _ = cost_function(X_cv, theta, y_cv, l=LAMBDAS[l])

    print("The cost function of training set is:", Jtrain)
    print("The cost function of cross-validation set is:", Jcv)

    return theta, Jtrain, Jcv


def plot_learning_curve(X, initial_theta, y):
    """
    Plots the learning curve (Jtrain and Jcv vs. number of training
    examples) by calling train() with varying number of training
    examples using matplotlib.pyplot.

    Parameters
    ----------
    X : 2D numpy array
        Total training examples available, examples separated
        by row, bias term included.
    intial_theta : 1D numpy array
        Initial theta values
    y : 1D numpy array
        Results of training examples

    Returns
    -------
    None
    """
    # Store the values of Jtrain and Jcv
    Jtrain_array = []
    Jcv_array = []
    # Total number of training examples
    total_m = X.shape[0]

    for m in range(1, int(0.6 * total_m), int(total_m / 100)):
        _, Jtrain, Jcv = train(X, initial_theta, y, num=m, outputs=True)
        Jtrain_array.append(Jtrain)
        Jcv_array.append(Jcv)

    # Convert to numpy arrays
    Jtrain_array = np.array(Jtrain_array)
    Jcv_array = np.array(Jcv_array)

    # Plot the learning curves
    fig, ax = plt.subplots(1, 1)
    _ = ax.set_xlabel('Number of training examples')
    _ = ax.set_ylabel('Cost')
    _ = ax.plot(Jtrain_array, marker='.', label='Jtrain')
    _ = ax.plot(Jcv_array, marker='.', label='Jcv')
    _ = ax.legend(loc='upper right')
    plt.show()


def plot_cost_function(J):
    """
    Plots the cost function from one iteration of gradient descent
    using matplotlib.pyplot.

    Parameters
    ----------
    J : 1D numpy array
        The cost function values after each iteration of gradient
        descent.

    Returns
    -------
    None
    """
    fig, ax = plt.subplots(1, 1)
    _ = ax.set_xlabel('Number of gradient descent iterations')
    _ = ax.set_ylabel('Cost function J')
    _ = ax.plot(J, marker='.')
    plt.show()
