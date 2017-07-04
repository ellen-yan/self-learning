"""
Train a neural network with one hidden layer.

cost_function()

prop_one_layer(numpy.array nodes, numpy.array theta) -> numpy.array new_nodes
    Propagate the neural network forward one layer (sigmoid(theta.dot(nodes))).
    Assumes each row of theta corresponds to the weights used to
    generate a single node in the next layer.


"""
import numpy as np
import logistic_regression as lr

def cost_function():
    pass


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

def forward_prop():
    pass

def back_prop():
    pass


def train_neural_network(X, y, ALPHA=1.0):
    """
    Train a neural network with one hidden layer and the same number
    of nodes in the hidden layer as the input layer.

    Parameters
    ----------
    X : 2D numpy array
        Training examples with each example separated by row.
    y : 1D numpy array
        Results of training examples
    ALPHA : float
        The learning rate

    Returns
    -------

    """
    # Learning rate
