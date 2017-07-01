function [X_norm, mu, sigma] = feature_norm(X)
% Normalizes the features in X 
%   feature_norm(X) returns a normalized version of X where
%   the mean value of each feature is 0 and the standard deviation
%   is 1. This is often a good preprocessing step to do when
%   working with learning algorithms.

% ====================== YOUR CODE HERE ======================
% Instructions: First, for each feature dimension, compute the mean
%               of the feature and subtract it from the dataset,
%               storing the mean value in mu. Next, compute the 
%               standard deviation of each feature and divide
%               each feature by it's standard deviation, storing
%               the standard deviation in sigma. 
%
%               Note that X is a matrix where each column is a 
%               feature and each row is an example. You need 
%               to perform the normalization separately for 
%               each feature.   

mu = mean(X); % default computes mean of each column, same as mean(X, 1)
sigma = std(X); 
X_norm = (X - mu) ./ sigma; % need ./ otherwise something weird happens and it doesn't divide by each column



% ============================================================

end
