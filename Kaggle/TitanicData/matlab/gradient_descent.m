function [theta, J_history] = gradient_descent(X, y, theta, alpha, num_iters, lambda)
%GRADIENTDESCENTMULTI Performs gradient descent to learn theta
%   theta = GRADIENTDESCENTMULTI(x, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCostMulti) and gradient here.
    %
    predictions = sigmoid(X * theta); % m x 1 vector of predictions
    grad = (1/m) * (X'*(predictions - y));
    theta = theta - alpha * (grad);


    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = cost_function_logistic_reg(theta, X, y, lambda);

end

end
