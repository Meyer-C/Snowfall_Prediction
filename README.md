# Snowfall_Prediction

Attempting to make a decent model for predicting snowfall in the Colorado mountains as a fun side project. I don't have a background in meteorology so I am learning as I go. 
I'm hoping to learn about machine learning and metiorolgy to predict weather just for fun. I'll be posting my learning curve and everything here as well.

## basic_knn

This does a basic k nearest neighbor comparison in order to find what a point on a 2D plane will most likely identify as based on the highest count of types of the K number of nearest neighbors.

### class testing_point

This class creates a new testing point which will be used to identify what it is closest to. This has 2 attributes that are the X and Y coordinates of the testing point.

### class training_point

This class creates a training point which the testing points will be compared to. It has the attributes of X and Y coordinates as well as an identifier to tell what the point is.

### get_training_data

This gets testing data from an excel file with the input argument of the excel file's filepath. This gets training data from an excel file. The excel file must be formatted as X coordinate, Y coordinate, identifier, and can have as many points as you would like.

### get_testing_data

This gets testing data from an excel file with the input argument of the excel file's filepath. The excel file must be formatted as X coordinate, Y coordinate, and can have as many points as you would like.

### point_dist

This function takes the arguments of point_a and point_b. Each point must be formatted as formatted as [X coord, Y coord]. The function then returns the distance between the 2 points.

### run_predictions

This function takes the arguments of the 2 excel filepaths for the training data and the testing data as well as k (the number of nearest neighbors to compare it to). It will use the above functions to get the datasets, find the points that are closest to the testing point, and then find the most frequently occuring identifiers for each point. It will return a list of the most frequent identifiers for each point.
