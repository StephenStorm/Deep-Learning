function [f,g] = linear_regression(theta, X,y)
  %
  % Arguments:
  %   theta - A vector containing the parameter values to optimize. n*1
  %   X - The examples stored in a matrix.
  %       X(i,j) is the i'th coordinate of the j'th example.
  %   y - The target value for each example.  y(j) is the target for
  %   example j.        1*m
  %
     
  m=size(X,2);
  n=size(X,1);

  f=0;
  g=zeros(size(theta));

  %
  % TODO:  Compute the linear regression objective by looping over the examples in X.
  %        Store the objective function value in 'f'.
  %
  % TODO:  Compute the gradient of the objective with respect to theta by looping over
  %        the examples in X and adding up the gradient for each example.  Store the
  %        computed gradient in 'g'.
  
%%% YOURCODE HERE %%%
fact1 = theta' * X - y ;  %1 * m
f =0.5 * sum(fact1 .^ 2);
tt = repmat(fact1,n,1);
g = sum(tt .* X,2);
%for i = 1:n
 %    g(i) = sum(fact1 .* X(i,:));
%end
end
