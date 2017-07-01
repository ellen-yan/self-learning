function [J, grad] = cost_function(theta, X, y)

% Computes cost of using theta as the parameter for logistic regression
% and the gradient of the cost w.r.t. the parameters.

m = length(y);

predictions = sigmoid(X * theta);
J = (1/m) * (-y' * log(predictions) - (1 - y') * log(1 - predictions));
grad = (1/m) * (X' * (predictions - y));

end