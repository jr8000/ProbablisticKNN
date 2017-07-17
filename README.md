# ProbablisticKNN
Machine Learning model that uses the KNN (K Nearest Neighbors) algorithm

The input vector(s) for the training data/test input can be any number of dimensions (any cardinality) provided that the cardinality of all of them are the same (if one is off, an exception will be raised).

The training data is given as a python type list in the during initialization (see example Batch file). It must be a list of tuples. The first element in each tuple is an integer that denotes the particular class the data point is classified as. The second element in each tuple is the input (feature) vector of that data point. Each of these feature vectors must also be of type list and must all have matching lengths. Each feature inside the feature vectors are either floats or integers (integers here will automatically be converted to floats during initialization).

There will be 5 public methods for each model instance:
- getProbabilityForPoint(self, k_value, point, class_id)
- listProbabilitiesAtPoint(self, k_value, point)
- classifyPoint(self, k_value, point)
- classifyPointAndReturnOnlyClassID(self, k_value, point)
- classifyPointAndReturnOnlyProbabilityValue(self, k_value, point)

For more information on a specific one, view its doc string.

Finally, see the example file "start_knn.bat" for more details (keep in mind that the part of this file that reads "[PATH TO KNN PROJECT FOLDER]" must be changed to the directory where your copy of "knn.py" is located).
