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

fprintf('Press any key to continue gradient descent\n');
pause;

[m, n] = size(X_1); % number of training examples and features
% Add intercept term
X_1 = [ones(m,1) X_1];

initial_theta = zeros(n + 1, 1); % initialize fitting parameters
lambda = 10;
alpha = 0.5; % Crazy things at alpha = 1!

[theta, J_history] = gradient_descent(X_1, y, initial_theta, alpha, 100, lambda);
fprintf('Theta values after minimization: \n');
fprintf('%f\n',theta);

% ===== Plotting cost function values =====

figure; hold on;
plot(J_history, 'r', 'MarkerSize', 10, 'LineWidth', 2);
hold off;

% ===== Accuracy on training set =====

p = predict_logistic(theta, X_1);
fprintf('Train Accuracy: %f\n', mean(double(p == y)) * 100);

% ===== Testing on test set =====

fprintf('Press any key to continue and run predictions on test file\n');
pause;
data = load('titanic_test_clean1_matlab.csv');
X_test = new_features(data(:,:));

X_test = (X_test - mu) ./ sigma; % feature normalization
X_test = [ones(size(X_test,1),1), X_test];
fprintf('Dimension of test matrix: %f\n', size(X_test));
fprintf('Dimension of theta matrix: %f\n', size(theta));

p = predict_logistic(theta, X_test);
id = (892:1309)';

csvwrite('predictions.csv', [id,p]);

