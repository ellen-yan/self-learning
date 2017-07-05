"""
Train a neural network with one hidden layer.

cost_function(numpy.array X, numpy.array theta1,
              numpy.array theta2, numpy.array y, l=0) -> float J
    Use theta1 and theta2 parameters on the input and hidden layers
    to calculate the predictions for each example and evaluate the
    cost function of the neural network. Each row of theta1 or theta2
    contain weights used to calculate a single node in the next layer.
    Regularization is applied with parameter l.

prop_one_layer(numpy.array nodes, numpy.array theta) -> numpy.array new_nodes
    Propagate the neural network forward one layer (sigmoid(theta.dot(nodes))).
    Assumes each row of theta corresponds to the weights used to
    generate a single node in the next layer.

forward_prop(numpy.array X, numpy.array theta1, numpy.array theta2) ->
                    numpy.array hypotheses
    Evaluates the hypotheses of the neural network by applying theta1
    on the input layer and theta2 on the hidden layer. Adds the bias
    intercept of the hidden layer within the function. Assumes there is
    one hidden layer and one node in the output layer. Assumes the bias term
    is provided in X.

predict(numpy.array X, numpy.array theta1, numpy.array theta2) ->
                    numpy.array predictions
    Predicts the results of the neural network using forward_prop and
    rounding to the nearest integer, and returns a numpy array of type int.

accuracy_rate(numpy.array X, numpy.array theta1, numpy.array theta2,
              numpy.array y) -> float accuracy
    Provides the accuracy of the neural network given the known results
    y as a fraction between 0 and 1 inclusive.

back_prop_grad(numpy.array X, numpy.array thet1, numpy.array theta2,
               numpy.array y) -> numpy.array grad1, numpy.array grad2
    Implements forward and back-propagation of neural network
    and returns two numpy arrays with the gradients corresponding to
    theta1 and theta2. Assumes bias term in X is included and the given
    arrays theta1 and theta2 have the appropriate dimensions to account
    for bias terms in each layer.

train_neural_network(numpy.array X, numpy.array theta1, numpy.array theta2,
                     numpy.array y, float alpha=0.1, float l=0,
                     tolerance=0.000001, max_iter=400) ->
                            numpy.array theta1, numpy.array theta2,
                            numpy.array costs
    Train a neural network with one hidden layer and one node
    in the output layer. Note that given initial theta1 and theta2
    must be randomized values and should not contain symmetry for
    the neural network to work well. Assumes the bias term in X
    is included and the given theta1 and theta2 have the appropriate
    dimensions to account for bias terms in each layer.

train(numpy.array X, numpy.array init_theta1, numpy.array init_theta2,
      numpy.array y, float alpha=0.1)
    Train a neural network using the function train_neural_network with
    various values of lambds and determines the best value of lambda and
    the parameters associated with it. 60%% of examples are used in the
    training set, 20%% in the cross-validation set, and 20%% in the test set.
"""
import math
import matplotlib.pyplot as plt
import numpy as np

import logistic_regression as lr

def cost_function(X, theta1, theta2, y, l=0):
    """
    Returns the cost of the neural network with weights
    theta1 and theta2 for input and hidden layers. Assumes X
    contains the bias term and there is only one node in the
    output layer.

    Parameters
    ----------
    X : 2D numpy array
        Training examples where examples are separated by row
        The bias term is assumed to be present.
    theta1 : 2D numpy array
        Weights to apply to a single training example in the input
        layer to obtain nodes in the hidden layer. Each row contain
        weights used to calculate one node in the next layer.
    theta2: 1D numpy array
        Weights to apply to a single training example in the
        hidden layer to obtain the value of the node in the output
        layer.
    y : 1D numpy array
        The results of each training example.
    l : float, default 0
        The regularization parameter

    Returns
    -------
    J : float
        The cost function result.
    """
    # The number of training examples
    m = X.shape[0]

    # Get the prediction for each example
    predictions = forward_prop(X, theta1, theta2)

    # Calculate the cost without regularization
    J = (-1/m) * (y.dot(np.log(predictions)) +
                  (1 - y).dot(np.log(1 - predictions)))

    # Add regularization term
    J = J + (l/2/m) * ((np.sum(theta1[1:,:] ** 2)) +
                       (theta2[1:].dot(theta2[1:])))

    return J


def prop_one_layer(nodes, theta):
    """
    Propagates the neural network forward one layer by applying
    theta on the given nodes, where each row of the "matrix" theta
    corresponds to the weights used to generate one node in the
    new layer. Applies the sigmoid function. Assumes the bias
    term in the nodes is already present.

    Parameters
    ----------
    nodes : 1D numpy array
        Array representing nodes in the layer
    theta : 2D numpy array
        Weights of the nodes, where each row contains the weights
        applied to each node in nodes (the current layer) to generate
        a single node in the new layer

    Returns
    -------
    new_nodes : 1D numpy array
        Array representing the nodes in the new layer
    """
    return lr.sigmoid(theta.dot(nodes))


def forward_prop(X, theta1, theta2):
    """
    Propagates the neural network and returns the results without
    rounding. Assumes the bias term is provided.

    Parameters
    ----------
    X : 2D numpy array
        The training examples, separated by rows.
    theta1 : 2D numpy array
        The weights of the first (input) layer.
    theta2 : 1D numpy array
        The weights of the second (hidden) layer, generates only
        one node in the output layer.

    Returns
    -------
    results : 1D numpy array
        The hypothesis values of the results (using logistic
        regression).
    """
    # Total number of examples given
    m = X.shape[0]

    # Store the predictions
    hypotheses = []

    for i in range(0, m):
        a2 = prop_one_layer(X[i,:], theta1)

        # Add bias term to hidden layer
        a2 = np.concatenate([np.ones(1), a2])
        a3 = prop_one_layer(a2, theta2)
        hypotheses.append(a3)

    return np.array(hypotheses)


def predict(X, theta1, theta2):
    """
    Predicts the results of the trained neural network using the function
    forward_prop(). Assumes the bias term is provided.

    Parameters
    ----------
    X : 2D numpy array
        The training examples, separated by rows.
    theta1 : 2D numpy array
        The weights of the first (input) layer.
    theta2 : 1D numpy array
        The weights of the second (hidden) layer, generates only
        one node in the output layer.

    Returns
    -------
    predictions : 1D numpy array
        The predicted values of the results (using logistic
        regression) rounded to 0 or 1 as integers.
    """

    return np.round(forward_prop(X, theta1, theta2)).astype(int)

def accuracy_rate(X, theta1, theta2, y):
    """
    Returns the accuracy rate of the trained weights
    based on the known results.

    Parameters
    ----------
    X : 2D numpy array
        The training examples
    theta1 : 2D numpy array
        Weights for the input layer
    theta2 : 1D numpy array
        Weights for the hidden layer. Assumes one
        node is outputted.
    y : 1D numpy array
        Results of the training examples

    Returns
    -------
    accuracy : float
        The fraction of predictions which match the given
        results, given as a decimal between 0 and 1 inclusive.
    """
    p = predict(X, theta1, theta2)
    return np.sum(p == y) / len(y)


def back_prop_grad(X, theta1, theta2, y, l=0):
    """
    Implements forward and back-propagation of neural network
    and returns numpy arrays with the gradients for theta1 and theta2.
    Assumes bias term in X is included and the given arrays theta1
    and theta2 have the appropriate dimensions to account for bias
    terms in each layer.

    Parameters
    ----------
    X : 2D numpy array
        Training examples separated by row.
    theta1 : 2D numpy array
        Weights for the input layer, each row representing weights
        to generate one node in the hidden layer.
    theta2 : 1D numpy array
        Weights for the output layer.
    y : 1D numpy array
        Results of training examples.
    l : float, default 0
        Regularization parameter.

    Returns
    -------
    grad1 : 2D numpy array
        The gradients for the theta1 parameters.
    grad2 : 1D numpy array
        The gradients for the theta2 parameters.
    """
    # Number of training examples
    m = X.shape[0]

    # Initialize gradient arrays
    grad1 = np.zeros(theta1.shape)
    grad2 = np.zeros(theta2.shape)

    for i in range(0, m):
        # Set the nodes for the input layer to be the current
        # training example
        a1 = X[i, :]

        # Calculate values of nodes in hidden and output layers
        a2 = prop_one_layer(a1, theta1)
        # Add bias term
        a2 = np.concatenate([np.ones(1), a2])
        a3 = prop_one_layer(a2, theta2)

        # Compute the errors at each layer (deltas)
        d3 = a3 - y[i]
        d2 = theta2.transpose().dot(d3) * (a2 * (1 - a2))

        grad1 = grad1 + d2[1:, None].dot(a1[None, :])
        grad2 = grad2 + d3 * a2

    # Compute regularized gradients, leaving out the bias term
    # (first column of theta)
    grad1[:, 1:] = (1/m) * grad1[:, 1:] + l * theta1[:, 1:]
    grad2[1:] = (1/m) * grad2[1:] + l * theta2[1:]

    return grad1, grad2


def train_neural_network(X, theta1, theta2, y, alpha=0.1, l=0,
                         tolerance=0.000001, max_iter=400):
    """
    Train a neural network with one hidden layer and one node
    in the output layer. Note that given initial theta1 and theta2
    must be randomized values and should not contain symmetry for
    the neural network to work well. Assumes the bias term in X
    is included and the given theta1 and theta2 have the appropriate
    dimensions to account for bias terms in each layer.

    Parameters
    ----------
    X : 2D numpy array
        Training examples with each example separated by row.
    theta1 : 2D numpy array
        Weights for the input layer, each row representing weights
        to generate one node in the hidden layer.
    theta2 : 1D numpy array
        Weights for the output layer.
    y : 1D numpy array
        Results of training examples.
    alpha : float, default 0.1
        The learning rate.
    l : float, default 0
        The regularization parameter.
    tolerance : float, default 0.000001
        The learning algorithm stops gradient descent when the
        magnitude of successive changes in the cost function value is
        less than this value.
    max_iter : int, default 400
        The maximum number of iterations for gradient descent.

    Returns
    -------
    theta1 : 2D numpy array
        Trained weight parameters for the first (input) layer.
    theta2 : 1D numpy array
        Trained weight parameters for the second (hidden) layer.
    costs : 1D numpy array
        The successive values of the cost function after each iteration.
    """
    # Initialize the difference between successive iterations of
    # gradient descent
    diff = math.inf

    # Initialize an array of cost values to be used for verifying
    # that cost function is decreasing
    costs = []

    # Calculate the initial cost and gradients
    J = cost_function(X, theta1, theta2, y, l=l)
    grad1, grad2 = back_prop_grad(X, theta1, theta2, y, l=l)

    # Store cost function value and update theta parameters
    costs.append(J)
    theta1 = theta1 - alpha * grad1
    theta2 = theta2 - alpha * grad2
    J_previous = J

    # Evaluate the cost function twice before entering the loop
    count = 1
    while ((diff == math.inf) or (np.abs(diff) > tolerance)) and count <= max_iter:
        J = cost_function(X, theta1, theta2, y, l=l)
        grad1, grad2 = back_prop_grad(X, theta1, theta2, y, l=l)
        costs.append(J)

        # Store the difference between the current cost and
        # the cost calculated from the previous iteration then store
        # the cost from this iteration
        diff = J - J_previous
        J_previous = J

        # Change theta values according to learning rate alpha
        theta1 = theta1 - alpha * grad1
        theta2 = theta2 - alpha * grad2

        # Increment number of iterations completed
        count += 1

    return theta1, theta2, np.array(costs)

def train(X, init_theta1, init_theta2, y, alpha=0.1):
    """
    Train a neural network with various values of lambda
    and determines the best value of lambda and the parameters
    associated with it. 60%% of examples are used in the training
    set, 20%% in the cross-validation set, and 20%% in the test set.

    Parameters
    ----------
    X : 2D numpy array
        The training examples, separated by row.
    init_theta1 : 1D numpy array
        Initial weights for the first (input) layer.
    init_theta2 : 1D numpy array
        Initial weights for the second (hidden) layer.
    y : 1D numpy array
        Results of training examples.
    alpha : float, default 0.1
        The learning rate.

    Returns
    -------
    theta1 : 2D numpy array
        The weight parameters for the first (input) layer evaluated
        using the value of lambda (the regularization parameter) that
        produced the highest accuracy in the cross-validation set.
    theta2 : 1D numpy array
        The weight parameters for the second (hidden) layer, evaluated
        using the value of lambda (the regularization parameter) that
        produced the highest accuracy in the cross-validation set.
    """
    # Experiment with these values
    MAX_ITER = 5000
    LAMBDAS = [0, 0.003, 0.01, 0.03, 0.1, 0.3]
    alpha = 0.005

    # Total number of training examples available
    m = X.shape[0]

    # Randomly divide the training examples into three sections
    # with 60% in the training set, 20% in the cross-validation
    # set and 20% in the test set
    # If the number of training examples has been specified
    m_train = int(np.round(0.6 * m)) # 60% of all examples given

    # The number of examples in the cross-validation set and test set
    num_cross = int(np.round((m - m_train) * 0.5))
    num_test = m - m_train - num_cross

    # Randomly shuffle the rows of the examples and reassign
    # the examples to X and y
    shuffle_array = np.concatenate([X, y[:, None]], axis=1)
    np.random.shuffle(shuffle_array)
    X = shuffle_array[:, :-1]
    y = shuffle_array[:, -1]

    # Extract the examples for training, cross-validation, and testing
    X_train = X[:m_train, :]
    y_train = y[:m_train]
    X_cv = X[m_train:(m_train + num_cross), :]
    y_cv = y[m_train:(m_train + num_cross)]
    X_test = X[(m_train + num_cross):, :]
    y_test = y[(m_train + num_cross):]

    # Keep track of how well each lambda value is
    performance = []

    # Iterate through all the values of lambda and train the neural
    # network using a range of lambdas
    for i in range(0, len(LAMBDAS)):
        theta1, theta2, costs = train_neural_network(X_train, init_theta1,
                                                     init_theta2, y_train,
                                                     alpha=alpha, l=LAMBDAS[i],
                                                     max_iter=MAX_ITER)
        performance.append(accuracy_rate(X_cv, theta1, theta2, y_cv))
        print("Finished testing lambda =", LAMBDAS[i])
        print("Performance is", performance[-1])

    i = max(range(len(performance)), key=performance.__getitem__)
    l = LAMBDAS[i]

    theta1, theta2, costs = train_neural_network(X_train, init_theta1,
                                                 init_theta2, y_train,
                                                 alpha=alpha,
                                                 max_iter=MAX_ITER)
    train_accuracy = accuracy_rate(X_train, theta1, theta2, y_train)
    cv_accuracy = accuracy_rate(X_cv, theta1, theta2, y_cv)
    test_accuracy = accuracy_rate(X_test, theta1, theta2, y_test)

    print("Finished training")
    print("-----------------")
    print("The optimum value of lambda:", l)
    print("Accuracy on the training set:", train_accuracy)
    print("Accuracy on the cross-validation set:", cv_accuracy)
    print("Accuracy on the test set:", test_accuracy)
    print("Theta1:")
    print(theta1)
    print("Theta2:")
    print(theta2)

    fig, ax = plt.subplots(1, 1)
    _ = ax.plot(costs, marker='.')
    plt.show()

    return theta1, theta2, costs
