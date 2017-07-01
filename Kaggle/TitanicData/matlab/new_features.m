function out = new_features(X)

% Col 1: Pclass
% Col 2: Sex
% Col 3: Age
% Col 4: SibSp
% Col 5: Parch
% Col 6: Fare
out = [X(:, :),X(:,3).^0.5, X(:,1).*X(:,3), X(:,4)+X(:,5), X(:,1).*X(:,2)];

% ===== Adding extra features =====

% Sex-age polynomial feature
new_f = map_feature(X(:,2),X(:,3));
out = [out, new_f(:, 3:end)];

new_f = map_feature(X(:,3),X(:,6));
out = [out, new_f(:, 3:end)];

new_f = map_feature(X(:,2),X(:,6));
out = [out, new_f(:, 3:end)];

end