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


The Programs we used to develop our results are:
- [Scikit learn](http://scikit-learn.org/stable/index.html) (a Python package)
- [Weka](http://www.cs.waikato.ac.nz/ml/weka/)

# Results

_Overview_

For the purposes of conciseness, we will use the following definitions:
- __Examples:__ refers to a training set (a row in the csv file)
- __Original dataset:__ refering to the dataset with missing attributes denoted as "NA"
- __Filled in dataset:__ refering to the dataset with the missing attributes filled in by using their means
- __Dropped dataset:__ refering to the dataset with examples containing missing attributes being dropped
- __attr_1:__ RevolvingUtilizationOfUnsecuredLines
- __attr_2:__ Age
- __attr_3:__ NumberOfTime30-59DaysPastDueNotWorse
- __attr_4:__ DebtRatio
- __attr_5:__ MonthlyIncome
- __attr_6:__ NumberOfOpenCreditLinesAndLoans
- __attr_7:__ NumberOfTimes90DaysLate
- __attr_8:__ NumberRealEstateLoansOrLines
- __attr_9:__ NumberOfTime60-89DaysPastDueNotWorse
- __attr_10:__ NumberOfDependents

The table below displays the best accuracy given the classifiers for both the filled in dataset
and the dropped dataset.

Classifier | Dropping Missing Attributes (Best) | Replacing Missing Attributes |
-----------|------------------------------------|------------------------------|
Decision Tree 			| 	96%			 		|	90%	|
Nearest Neighbor 		| 	98%					|	93%	|
Multilayer Perceptron 	|						|	93%	|
Logistic Regression 	|						|	93%	|
Naive Bayes 			|			 	 		|	93%	|


_K-Nearest Neighbors_

The graph below depicts the accuracy of the KNN algorithm for a K values in the range 0 to 30. The red 
dotted line uses a distance function to determine the proximity of the neighbors while the red line 
uses a uniform function to calculate neighbors. As you can see, the uniform distance 
did better overall, but as K increased both methods converged on a similar value 
slightly above 93% accuracy. These values were calculated using the filled in dataset.
![KNN Graph](/graphs/KNN.png)


Because at a K of 15 for the KNN algorithm converges on the maximum accuracy, we used this K to 
determine the values when dropping attributes. The accuracy results using the filled in dataset 
we found are depicted below: 


Weight |attr_1 | attr_2 | attr_3 | attr_4 | attr_5 | attr_6 | attr_7 | attr_8 | attr_9 | attr_10 |
---------------|-------|--------|--------|--------|--------|--------|--------|--------|--------|---------|
Uniform|98%    |93%     | 93%    | 93% 	  |93%     | 94%    |	93%	 |  93%	  |  93%   | 93%	 |
Distance|98%   |93%     | 93%    | 93%    |93%     | 93%    |	93%	 |  93%	  |  93%   | 93%	 |


_Decsion Trees_

Dropping attribues for the decision tree classifier on the filled in dataset, we get the following 
accuracy results:

attr_1 | attr_2 | attr_3 | attr_4 | attr_5 | attr_6 | attr_7 | attr_8 | attr_9 | attr_10 |
-------|--------|--------|--------|--------|--------|--------|--------|--------|---------|
96%	   |89%     | 90%    | 90% 	  |90%     | 90%    |	90%	 |  89%	  |  90%   | 90%     |




_Multilayer Perceptrons_

_Naive Bayes_


_Logistic Regression_



# The Code

Our data came in the form a csv file with 11 attributes, a binary classifier, and
150,000 training examples. We generated two datasets: (1) the original dataset with missing attributes
calibrated to their associated means and (2) the original dataset with examples contianing 
missing attributes dropped. This was done by our function _read_training_data_ which takes in two possible
arguments: fname, drop=None. fname determines the path for the csv to read from and drop 
determines if there is an attribute we want to drop. 


```python
def read_training_data(fname, drop=None):
	"""
	Input:
		fname -- (string) the path to the csv file of data
		drop -- (None or int) defaulted to none, otherwise indicated index to drop

	Returns:
		the orginal dataset in an array format with attribute dropped in drop is not None
	"""
	col_start = 0
	col_end = 11
	data = []
	f = open(fname)
	csv_reader = csv.reader(f)
	for j, line in enumerate(csv_reader):
		if j == 0:
			# if it is the header file, parse as is (string)
			if drop != None:
				append_line = [line[header] for header in range(col_start, col_end)]
				_a = append_line.pop(drop)
			else:
				append_line = [line[header] for header in range(col_start, col_end)]
		if j != 0:
			# otherwise, cast as float
			if drop != None:
				append_line = [float(line[cell]) for cell in range(col_start,col_end)]
				_a = append_line.pop(drop)
			else:
				append_line = [float(line[cell]) for cell in range(col_start,col_end)]
		data.append(append_line)
	f.close()
	return data
```



