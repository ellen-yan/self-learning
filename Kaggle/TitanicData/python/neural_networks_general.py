"""
Train a neural network with an arbitrary number of hidden layers,
assuming only one node in the output layer.


"""
import math
import matplotlib.pyplot as plt
import numpy as np

import logistic_regression as lr

def cost_function(X, thetas, y, l=0):
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
    thetas : list of numpy arrays
        Weights to apply to a single training example in the input
        layer to obtain nodes in the hidden layers and output layer.
        Each row in any 2D numpy array contains weights used to calculate
        one node in the next layer. The last theta is array is a 1D array.
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
    predictions, _ = forward_prop(X, thetas)

    # Calculate the cost without regularization
    J = (-1/m) * (y.dot(np.log(predictions)) +
                  (1 - y).dot(np.log(1 - predictions)))

    # Add regularization term, last theta separately since it is 1D
    for i in range(0, len(thetas) - 1):
        J = J + (l/2/m) * (np.sum(thetas[i][1:,:] ** 2))
    J = J + (l/2/m) * (thetas[-1][1:].dot(thetas[-1][1:]))

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
    theta : numpy array
        Weights of the nodes, where each row contains the weights
        applied to each node in nodes (the current layer) to generate
        a single node in the new layer

    Returns
    -------
    new_nodes : 1D numpy array
        Array representing the nodes in the new layer
    """
    return lr.sigmoid(theta.dot(nodes))


def forward_prop(X, thetas):
    """
    Propagates the neural network and returns the results without
    rounding. Assumes the bias term is provided.

    Parameters
    ----------
    X : 2D numpy array
        The training examples, separated by rows.
    thetas : list of numpy arrays
        The weights of the input and hidden layers, generates only
        one node in the output layer.

    Returns
    -------
    results : 1D numpy array
        The hypothesis values of the results (using logistic
        regression).
    a : 1D numpy array
        A list of numpy arrays, each of which is an array of the
        nodes at each layer, including the input and output layers.
    """
    # Total number of examples given
    m = X.shape[0]

    # Store the predictions
    hypotheses = []

    # Store the nodes at each layer
    a = []

    for i in range(0, m):
        a.append(X[i,:])
        for t in range(0, len(thetas)):
            a_next = prop_one_layer(a[t], thetas[t])
            if t == len(thetas) - 1:
                a.append(a_next)
                break
            # Add bias term to new layer and store
            a.append(np.concatenate([np.ones(1), a_next]))

        # Store the hypothesis for this training
        hypotheses.append(a[-1])

    return np.array(hypotheses), a


def predict(X, thetas):
    """
    Predicts the results of the trained neural network using the function
    forward_prop(). Assumes the bias term is provided.

    Parameters
    ----------
    X : 2D numpy array
        The training examples, separated by rows.
    thetas : list of numpy arrays
        The weights of the input and hidden layers, generates only
        one node in the output layer.

    Returns
    -------
    predictions : 1D numpy array
        The predicted values of the results (using logistic
        regression) rounded to 0 or 1 as integers.
    """
    hypotheses, _ = forward_prop(X, thetas)
    return np.round(hypotheses).astype(int)

def accuracy_rate(X, thetas, y):
    """
    Returns the accuracy rate of the trained weights
    based on the known results.

    Parameters
    ----------
    X : 2D numpy array
        The training examples
    thetas : list of numpy arrays
        Weights for the input and hidden layers. Assumes one
        node is outputted.
    y : 1D numpy array
        Results of the training examples

    Returns
    -------
    accuracy : float
        The fraction of predictions which match the given
        results, given as a decimal between 0 and 1 inclusive.
    """
    p = predict(X, thetas)
    return np.sum(p == y) / len(y)


def back_prop_grad(X, thetas, y, l=0):
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
    thetas : list of numpy arrays
        Weights for the input and hidden layers, each row representing
        weights to generate one node in the hidden layer.
    y : 1D numpy array
        Results of training examples.
    l : float, default 0
        Regularization parameter.

    Returns
    -------
    grads : list of numpy arrays
        The gradients for the theta parameters.
    """
    # Number of training examples
    m = X.shape[0]

    # Initialize list of gradient arrays, corresponding to
    # list of theta arrays
    grads = []
    for theta in thetas:
        grads.append(np.zeros(theta.shape))

    for i in range(0, m):
        # Forward propagate neural network
        hypotheses, a = forward_prop(X, thetas)

        # Errors at each layer (deltas)
        d = []

        # Compute the error in the last layer
        d_last = a[-1] - y[i]
        d.append(d_last)

        # Compute the errors at each layer up to the first
        # hidden layer
        d_new = thetas[-1].transpose().dot(d_last) * (a[-1] * (1 - a[i]))
        d.insert(0, d_new)
        for i in range(len(thetas) - 2, 0, -1):
            d_new = thetas[i].transpose().dot(d[0][1:]) * (a[i] * (1 - a[i]))
            d.insert(0, d_new)

        # Compute gradients
        for i in range(len(grads) - 1):
            grads[i] = grads[i] + d[i][1:, None].dot(a[i][None, :])
        grads[-1] = grads[-1] + d[-1] * a[-1]

    # Compute regularized gradients, leaving out the bias term
    # (first column of theta)
    for i in range(len(grads) - 1):
        grads[i][:, 1:] = (1/m) * grads[i][:, 1:] + l * thetas[i][:, 1:]
    grads[-1] = (1/m) * grads[-1] + l * theta[-1]

    return grads


def train_neural_network(X, thetas, y, alpha=0.1, l=0,
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
    thetas : list of numpy arrays
        Weights for the input and hidden layers, each row representing
        weights to generate one node in the next layer.
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
    thetas : list of numpy arrays
        Trained weight parameters for the input and hidden layers.
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
    J = cost_function(X, thetas, y, l=l)
    grads = back_prop_grad(X, thetas, y, l=l)

    # Store cost function value and update theta parameters
    costs.append(J)
    for i in range(len(thetas)):
        thetas[i] = thetas[i] - alpha * grads[i]
    J_previous = J

    # Evaluate the cost function twice before entering the loop
    count = 1
    while ((diff == math.inf) or (np.abs(diff) > tolerance)) and count <= max_iter:
        J = cost_function(X, thetas, y, l=l)
        grads = back_prop_grad(X, thetas, y, l=l)
        costs.append(J)

        # Store the difference between the current cost and
        # the cost calculated from the previous iteration then store
        # the cost from this iteration
        diff = J - J_previous
        J_previous = J

        # Change theta values according to learning rate alpha
        for i in range(len(thetas)):
            thetas[i] = thetas[i] - alpha * grads[i]

        # Increment number of iterations completed
        count += 1
        print("iteration #:",count)

    return thetas, np.array(costs)

def train(X, init_thetas, y, alpha=0.1):
    """
    Train a neural network with various values of lambda
    and determines the best value of lambda and the parameters
    associated with it. 60%% of examples are used in the training
    set, 20%% in the cross-validation set, and 20%% in the test set.

    Parameters
    ----------
    X : 2D numpy array
        The training examples, separated by row.
    init_thetas : list of numpy arrays
        Initial weights for the input and hidden layers.
    y : 1D numpy array
        Results of training examples.
    alpha : float, default 0.1
        The learning rate.

    Returns
    -------
    thetas : list of numpy arrays
        The weight parameters for the input and hidden layers evaluated
        using the value of lambda (the regularization parameter) that
        produced the highest accuracy in the cross-validation set.
    """
    # Experiment with these values
    MAX_ITER = 5000
    LAMBDAS = [0]

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
    # for i in range(0, len(LAMBDAS)):
    #     thetas, costs = train_neural_network(X_train, init_thetas, y_train,
    #                                          alpha=alpha, l=LAMBDAS[i],
    #                                          max_iter=MAX_ITER)
    #     performance.append(accuracy_rate(X_cv, thetas, y_cv))
    #     print("Finished testing lambda =", LAMBDAS[i])
    #     print("Performance is", performance[-1])
    #
    # i = max(range(len(performance)), key=performance.__getitem__)
    # l = LAMBDAS[i]

    thetas, costs = train_neural_network(X_train, init_thetas, y_train,
                                         alpha=alpha, l=0, max_iter=MAX_ITER)
    train_accuracy = accuracy_rate(X_train, thetas, y_train)
    cv_accuracy = accuracy_rate(X_cv, thetas, y_cv)
    test_accuracy = accuracy_rate(X_test, thetas, y_test)

    print("Finished training")
    print("-----------------")
    print("The optimum value of lambda:", 0)
    print("Accuracy on the training set:", train_accuracy)
    print("Accuracy on the cross-validation set:", cv_accuracy)
    print("Accuracy on the test set:", test_accuracy)
    print("Thetas:")
    for t in thetas:
        print(t)

    fig, ax = plt.subplots(1, 1)
    _ = ax.plot(costs, marker='.')
    plt.show()

    return thetas, costs
