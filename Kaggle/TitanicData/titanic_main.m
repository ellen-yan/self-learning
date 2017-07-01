% Kaggle Competition - Titanic Data
% ---------------------------------

% Initialization
clear; close all; clc

% Load data. 
% First column contains survival data, second to 7th columns contain other
% features. First row contains headers.

data = load('titanic_data_clean1_matlab.csv');
X = data(:, 2:end); y = data(:, 1);

% ===== Determining the subset of data to work with =====

X_1 = new_features(X);

fprintf('Size of design matrix:\n');
fprintf('%f\n', size(X_1));

% ===== Feature Normalization =====

fprintf('Normalizing features ...\n');
[X_1, mu, sigma] = feature_norm(X_1);

fprintf('Press any key to continue plotting\n');
pause;

% ===== Plotting 2D data =====

%plot_2d_data(X(:,[1,6]), y);

fprintf('Press any key to continue optimization\n');
pause;

% ===== Optimizing using fminunc =====

[m, n] = size(X_1); % number of training examples and features
% Add intercept term
X_1 = [ones(m,1) X_1];

initial_theta = zeros(n + 1, 1); % initialize fitting parameters

lambda = 20;

options = optimset('GradObj', 'on', 'MaxIter', 400);
[theta, cost] = ...
    fminunc(@(t)(cost_function_logistic_reg(t, X_1, y, lambda)), initial_theta, options);

fprintf('Minimized theta: %f\n', theta);
fprintf('Program paused. Press anything to continue.\n');
pause;

% ===== Accuracy on training set =====

p = predict_logistic(theta, X_1);

fprintf('Train Accuracy: %f\n', mean(double(p == y)) * 100);
fprintf('Press any key to continue and run predictions on test file\n');
pause;

% ===== Testing on test set =====

data = load('titanic_test_clean1_matlab.csv');
X_test = new_features(data(:,:));

X_test = (X_test - mu) ./ sigma; % feature normalization
X_test = [ones(size(X_test,1),1), X_test];
fprintf('Dimension of test matrix: %f\n', size(X_test));
fprintf('Dimension of theta matrix: %f\n', size(theta));

p = predict_logistic(theta, X_test);
id = (892:1309)';

csvwrite('predictions.csv', [id,p]);


