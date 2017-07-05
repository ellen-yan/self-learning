"""
Module containing functions useful for manipulating features of a
training set.

Functions
---------

normalize(2D numpy.array data, method='stdev') ->
            2D numpy.array normdata, numpy.array mean, numpy.array scale
    Given a numpy array "matrix" that is tidy (features in columns,
    observations in rows) and contains only numbers, returns a matrix that is
    normalized by either the standard deviation (method='stdev', default)
    or the range of data (method='range') based on kwarg, where each value
    has been subtracted by the mean of that column and divided by the
    method (stdev or range), and returns the two numpy arrays, the first
    containing the mean of each column and the second containing the stdev
    or range of each column.

add_polynomial_features(numpy.array X, int power) -> numpy.array X_features
    Returns a feature set with added features such that
    all combinations of existing features are used to
    create a set of features with polynomial degrees less
    than or equal to power. Assumes no bias terms are included
    (i.e. all columns will be used to create new features) and
    that features are separated by columns.

"""
import numpy as np

def normalize(data, method='stdev'):
    """
    Returns a numpy array normalized by column by subtracting
    the mean and dividing by some scale.

    Parameters
    ----------
    data : 1D or 2D numpy array
        Data to be normalized where features are separated by columns.
    method : optional, default stdev
        Specifies the method of normalization in the scaling.
        'stdev' divides by the standard deviation, 'range' divides
        by the range of the data.

    Returns
    -------
    data : 2D numpy array
        Normalized data with same dimensions as the given data.
    mu : 1D numpy array
        The mean of each column.
    scale : 1D numpy array
        The scaling factor of each column.
    """
    mu = data.mean(axis=0) # mean by column
    if method  != 'range':
        if method != 'stdev':
            print ('Invalid entry for method kwarg. Used \
                    std deviation for scaling')
        scale = data.std(axis=0)
    else:
        scale = data.ptp(axis=0)

    return ((data - mu[None, :]) / scale[None, :]), mu, scale


def add_polynomial_features(X, power):
    """
    Returns a numpy array with new polynomial features added
    up to degree power. (Only combines two features at a time)

    Parameters
    ----------
    X : 2D numpy array
        A numpy array with features separated by columns,
        examples by rows.
    power : int
        The highest degree polynomial to generate. Must be
        an integer greater than 1.

    Returns
    -------
    X_features : 2D numpy array
        A numpy array with new features in addition to
        the given features from X.

    Examples
    --------
    >> A = numpy.array([[1, 2], [3, 4]])
    >> add_polynomial_features(A, 3)
    array([[ 1,  2,  4,  2,  1,  8,  4,  2,  1],
           [ 3,  4, 16, 12,  9, 64, 48, 36, 27]])
    """
    # New variable to store new features
    X_features = X

    # Generate all polynomial degrees up to specified power
    for max_degree in range(2,power + 1):

        # Identify the two features we are creating a new feature with
        for i in range(0, X.shape[1] - 1):
            for j in range(i + 1, X.shape[1]):
                feature1 = X[:, i]
                feature2 = X[:, j]

                for d in range(0, max_degree + 1):
                    new_feature = (feature1 ** d) * \
                                  (feature2 ** (max_degree - d))
                    X_features = np.concatenate([X_features,
                                                 new_feature[:, None]], axis=1)

    return X_features
