# this creates a linear regression model
def mean(vals):
    return float(sum(vals)) / float(len(vals))

def varience(vals, mean):
    return sum([(val - mean)**2 for val in vals])

def covar(x, x_mean, y, y_mean):
    covar = 0
    for a in range(len(x)):
        covar += (x[a] - x_mean) * (y[a] - y_mean)
    return covar

def slope(covarience, x_var):
    return covarience / x_var

def y_int(y_mean, x_mean, m):
    return y_mean - (x_mean * m)

def get_line_eq(x, y):
    x_mean = mean(x)
    y_mean = mean(y)
    m = slope(covar(x, x_mean, y, y_mean), varience(x, x_mean))
    y_intercept = y_int(y_mean, x_mean, m)
    return [m, y_intercept]

def make_prediction(m, y_int, x):
    return (m * x) + y_int



