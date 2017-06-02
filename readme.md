# Liquidity Predictor

We used machine learning algorithms to develop a model that best predicts a potential borrower's future 
liquidity. For each classifier, we used 10-fold cross validation to determine the accuracy 
of the classifier given our dataset. For missing attributes, we developed statistics by both dropping 
training examples with missing attributes as well as replacing missing attributes with their means 
relative to the entire dataset. 

The classifiers we used were:
- Decision Trees
- Logistic Regression
- Naive Bayes
- Multilayer Perceptron
- Nearest Neighbor


# Results

_Overview_

The table below (Table 1) displays the best accuracy given the classifiers for both the dataset comprised of
examples dropped if missing attributes are present and the dataset comprised of missing attributes replaced
with the mean of that attribute. 

__Table 1__

Classifier | Dropping Missing Attributes | Replacing Missing Attributes |
-----------|-----------------------------|------------------------------|
Decision Tree 			| 				 |	90%	|
Nearest Neighbor 		| 				 |	93%	|
Multilayer Perceptron 	|				 |	93%	|
Logistic Regression 	|				 |	93%	|
Naive Bayes 			|			 	 |	93%	|



_K-Nearest Neighbor_
![KNN Graph](/graphs/KNN.png)


_Decsion Trees_


_Multilayer Perceptrons_

_Naive Bayes_


_Logistic Regression_



# The Code

Our data came in the form a csv file with 11 attributes, a binary classifier, and
150,000 training examples. We generated two datasets: (1) the original dataset with missing attributes
calibrated to their associated means and (2) the original dataset with examples contianing 
missing attributes dropped. This was done by our function _read_training_data_ which takes in two possible
arguments: calibrate=True, drop=None. Calibrate is a boolean value that determines which 
of the two prior datasets to develop (true corresponding to option (1)) and drop is defaulted to None and
determines if there is an attribute we want to drop. 


```python
def read_training_data(fname, calibrate=True, drop=None):
	col_start = 0
	col_end = 11
	data = []
	f = open(fname)
	csv_reader = csv.reader(f)
	for j, line in enumerate(csv_reader):
		# if it is the header file, parse as is (string)
		if j == 0:	
			append_line = [line[header] for header in range(col_start, col_end)]
		# otherwise, cast as float
		if j != 0:
			append_line = [float(line[cell]) for cell in range(col_start,col_end)]
		data.append(append_line)
	f.close()
	return data
```



