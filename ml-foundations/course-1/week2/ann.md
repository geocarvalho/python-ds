## Linear regression: a model-based approach
- Cost of using a given line: Residual sum of squares (RSS) is the distance between the real actual value and the predicted value (positive or negative)
$ RSS(w_0,w_1) = ($_house1-[w_0 + w_1*sq.ft._{house1}])^2 + ($_house2-[w_0 + w_1*sq.ft._{house2}])^2 + ... $

## Adding higher order effects
- What about a quadratic function?
$f_w(x) = w_0 + w_1*x + w_2*x^2$

> Where the intercept ($w_0$) is where the curve is up and donw in the y-axis. The slope ($w_1$) is linear term of x and the extra term ($x^2$) that is the quadratic component
> Still linear regression because $x^2$ is just another feature. We still have to minimize the RSS.
 
## Evaluating regression models via training/test split
- The model is exact about the actual observation with RSS next to zero but don't generalize well thinking about new predictions.
1. Remove some houses; 
2. Fit the model on remaining data (training set);
3. Predict heldout houses (test set).
- Training error = RSS on the training set
- Test error = RSS on the test set

## Training/test curves
- The training error decreases with the increase of the model complexity.
- The test error decrease with the increase of the model complexity, but after a point starts to increase.

## Regression ML block diagram
- What you can do now
    * Describe the input (features) and output (real-valued predictions) of a regression model;
    * Calculate a goodness-of-fit metric (e.g., RSS)
    * Estimate model parameters by minimizing RSS (algorithms to come..)
    * Exploit the estimated model to form predictions;
    * Perform a training/test split of the data;
    * Analyze performance of various regression models in terms of test error;
    * Use test error to avoid overfitting when selecting amongst candidate models;
    * Describe a regression model using multiple features;
    * Describe other applications where regression is useful.

## Predicting house prices assignment
- In the module we discussed residual sum of squares (RSS) as an error metric for regression, but Turi Create uses root mean squared error (RMSE).  These are two common measures of error regression, and RMSE is simply the square root of the mean RSS: 

![rmse](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/9ca1bnk7EeWK7BIWTMqIaQ_86a40b81780f8876fad7b2a5ccbd3825_RMSE.png?expiry=1654560000000&hmac=VOPh7rYKUrLyVOnoJFLhfGNrFa3dE4qN3KIE6ay0SLw)

> where N is the number of data points.  RMSE can be more intuitive than RSS, since its units are the same as that of the target column in the data, in our case the unit is dollars ($), and doesn't grow with the number of data points, like the RSS does.