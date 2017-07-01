function p = predict_logistic(theta, X)

p = round(sigmoid(X * theta));

end