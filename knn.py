import math, os, sys, io, time

class ProbablisticKNN(object):
    """
    ProbablisticKNN
    """

    def __init__(self, training_data):
        """
        The training data must be list
        of tuples. The first element in
        each tuple must be an integer
        that corresponds to a particular
        class. The second element in
        each tuple is a list, which is
        the input vector. Each input
        vector must have the same number
        as the others or an exception
        will be raised.
        """

        self._class_column = []
        self._feature_column = []
        for x in training_data:
            self._validateDataPoint(x)
            self._class_column.append(x[0])
            self._feature_column.append(x[1])

    def getProbabilityForPoint(self, k_value, point, class_id):
        """
        The point must be of type list.
        It is to be a vector with the
        same number of dimensions as
        each of the input vectors from
        the training data set (or an
        exception will be raised).
        The classification is the
        particular class that the data
        point supposedly belongs to.
        This method will return a
        floating point between 1 and
        0 representing the probability
        that the given point is a
        member of the given class.
        The classification is an
        integer corresponding to
        the class. If the integer
        provided does not correspond
        to a class from the training
        data, an exception will be
        raised.
        """

        index_list = self._findKNearestNeighbors(k_value, point)

        if type(class_id) is not type(int(0)):
            raise TypeError("class ID must be" +
                             "of type integer")

        if class_id not in self._class_column:
            raise RuntimeError("class ID must be" +
                               "one of the values" +
                               "found in the" +
                               "classes of the" +
                               "training data" +
                               "points")

        numerator_sum = int(0)
        for x in index_list:
            if self._class_column[x] == class_id:
                numerator_sum = numerator_sum + 1

        return float(numerator_sum) / float(k_value)

    def _findKNearestNeighbors(self, k_value, point):
        """
        Returns a list of indexes
        to a subset of elements in
        the training dataset that
        make up the K-nearest
        neighbors to the input
        point.
        """

        if type(k_value) is not type(int(0)):
            raise TypeError("k value must be " +
                            "an integer")

        length_of_feature_vector = len(self._feature_column[0])

        if type(point) is not type([]):
            raise TypeError("test point must be " +
                            "feature vector of " +
                            "type list")

        if len(point) != length_of_feature_vector:
            raise TypeError("test point feature " +
                            "vector must have " +
                            "the same cardinality " +
                            "as the feature " +
                            "vectors in the " +
                            "training data ")

        # just for testing...
        #print(length_of_feature_vector)
        #print(len(self._feature_column))
        #print(len(self._class_column))

        proximity_column = []
        ctr = int(0)
        for x in self._feature_column:
            proximity_float = self._proximity(x, point)
            temp_proximity_tuple = (ctr, proximity_float)
            proximity_column.append(temp_proximity_tuple)
            ctr = ctr + 1

        # just for testingg
        #for x in proximity_column:
        #    print(x[0])
        #    print(x[1])

        #just for testingg
        #for p in proximity_column:
        #    print(p)
        #    print("---")
        #print("--end--")

        countdown_k = k_value
        temp_prox_col = proximity_column
        k_nearest_proximities_tuples = []
        while(True):
            if countdown_k == int(0): break
            if len(temp_prox_col) == 0:
                raise RuntimeError("not enough data " +
                                   "points for " +
                                   "specified k " +
                                   "value")
            temp_prox_tuple = temp_prox_col[0]
            first_iteration = True
            for i in temp_prox_col:
                if first_iteration == True:
                    first_iteration = False
                    continue
                if i[1] < temp_prox_tuple[1]:
                    temp_prox_tuple = i
            k_nearest_proximities_tuples.append(temp_prox_tuple)
            countdown_k = countdown_k - 1
            temp_prox_col.remove(temp_prox_tuple)
        indexes_of_k_nearest_neighbors = []
        for j in k_nearest_proximities_tuples:
            indexes_of_k_nearest_neighbors.append(j[0])
        return indexes_of_k_nearest_neighbors

    def _validateDataPoint(self, x):
        """
        make sure the the data point
        is given in the proper format
        (and raise exception if not)
        """

        if type(x) is not type(tuple()):
            raise TypeError("all data points " +
                            "in training data " +
                            "must be of type " +
                            "tuple")

        if type(x[0]) is not type(int(0)):
            raise TypeError("all class IDs " +
                            "must be of type " +
                            "integer")

        if type(x[1]) is not type([]):
            raise TypeError("feature vector " +
                            "for each data " +
                            "must be of " +
                            "type list")

        if len(self._feature_column) != 0:
            if len(x[1]) != len(self._feature_column[0]):
                raise TypeError("the feature " +
                                "vector of " +
                                "each point " +
                                "in the " +
                                "training " +
                                "data set " +
                                "must have " +
                                "the same " +
                                "cardinality")

        float_list = x[1]

        for value in float_list:
            if type(value) is not type(float(0.0)):
                raise TypeError("each value in the " +
                                "feature vector " +
                                "must be of type " +
                                "float")

    def _proximity(self, list1, list2):
        """
        determine the distance from
        one feature vector to another
        """

        current_val = float(0.0)
        for i in range(0, len(list1)):
            temp = float(list1[i]) - float(list2[i])
            temp = math.pow(temp, 2)
            current_val = math.pow(math.pow(current_val, 2) + temp, 0.5)

        return current_val

    def listProbabilitiesAtPoint(self, k_value, point):
        """
        returns a list of tuples
        each containing a class
        ID and a corresponding
        probability
        """

        existing_class_ids = []
        for x in self._class_column:
            if x not in existing_class_ids:
                existing_class_ids.append(x)

        sorted_class_ids = []
        while(True):
            if len(existing_class_ids) < 1:
                break
            temp_lowest_id_val = existing_class_ids[0]
            for i in existing_class_ids:
                temp_lowest_id_val
            sorted_class_ids.append(temp_lowest_id_val)
            existing_class_ids.remove(temp_lowest_id_val)

        list_of_tuples = []
        for x in sorted_class_ids:
            temp_prob = self.getProbabilityForPoint(k_value, point, x)
            temp_tuple = (x, temp_prob)
            list_of_tuples.append(temp_tuple)
        return list_of_tuples

    def classifyPoint(self, k_value, point):
        """
        call the listProbabilitiesAtPoint
        method and determine which class
        has the highest probability for
        the given point
        """

        probabilities = self.listProbabilitiesAtPoint(k_value, point)
        if len(probabilities) == 0:
            raise RuntimeError("listProbabilitiesAtPoint method " +
                               "returned empty list")
        counter = int(0)
        for x in probabilities:
            if counter == 0:
                max_prob_obj = x
            else:
                if x[1] > max_prob_obj[1]:
                    max_prob_obj = x
            counter = counter + 1
        return max_prob_obj

    def classifyPointAndReturnOnlyClassID(self, k_value, point):
        """
        just like classifyPoint except
        only the class ID (of type
        integer) is returned
        """

        return self.classifyPoint(k_value, point)[0]

    def classifyPointAndReturnOnlyProbabilityValue(self, k_value, point):
        """
        just like classifyPoint except
        only the probability value
        corresponding to the class
        with the highest probability
        is returned (only a float
        value is returned)
        """

        return self.classifyPoint(k_value, point)[1]
