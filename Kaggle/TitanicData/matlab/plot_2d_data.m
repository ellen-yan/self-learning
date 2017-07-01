function plot_2d_data(X, y)
%PLOTDATA Plots the data points X and y into a new figure 
%   PLOTDATA(x,y) plots the data points with + for the positive examples
%   and o for the negative examples. X is assumed to be a Mx2 matrix.

% Create New Figure
figure; hold on;

% ====================== YOUR CODE HERE ======================
% Instructions: Plot the positive and negative examples on a
%               2D plot, using the option 'k+' for the positive
%               examples and 'ko' for the negative examples.
%

% find is unnecessary when matrix itself specifies the logic
%ind_zeros = find(y == 0); % find indices where value of y is zero
%ind_ones = find(y == 1); % find indices where value of y is one

plot(X(y == 0, 1),X(y == 0, 2),'k+', 'LineWidth', 2, 'MarkerSize', 7, 'MarkerFaceColor', 'r');
%figure(2); hold on;
plot(X(y == 1, 1),X(y == 1, 2),'ko', 'LineWidth', 2, 'MarkerSize', 7, 'MarkerFaceColor', 'b');
% i.e. plotting first column of X vs second column of X, first for
% rows where y == 0, then for rows where y == 1







% =========================================================================



hold off;

end
