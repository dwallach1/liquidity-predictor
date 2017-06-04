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
- [Weka](http://www.cs.waikato.ac.nz/ml/weka/) (a desktop application)

# The Data

__Attributes__

Feature |Variable Name | Description | Type |
--------|--------------|-------------|------|
__Classifier__ | __SeriousDlqin2yrs__ | __Person experienced 90 days past due delinquency or worse__ | __Y/N__ |
Attr_1 | RevolvingUtilizationOfUnsecuredLines | Total balance on credit cards and personal lines of credit except real estate and no installment debt like car loans divided by the sum of credit limits | percentage
Attr_2 |age | Age of borrower in years | integer
Attr_3 | NumberOfTime30-59DaysPastDueNotWorse | Number of times borrower has been 30-59 days past due but no worse in the last 2 years. | integer
Attr_4 | DebtRatio | Monthly debt payments, alimony,living costs divided by monthy gross income | percentage
Attr_5 | MonthlyIncome | Monthly income | real
Attr_6 | NumberOfOpenCreditLinesAndLoans | Number of Open loans (installment like car loan or mortgage) and Lines of credit (e.g. credit cards) | integer
Attr_7 | NumberOfTimes90DaysLate | Number of times borrower has been 90 days or more past due. | integer
Attr_8 | NumberRealEstateLoansOrLines | Number of mortgage and real estate loans including home equity lines of credit | integer
Attr_9 | NumberOfTime60-89DaysPastDueNotWorse | Number of times borrower has been 60-89 days past due but no worse in the last 2 years. | integer
Attr_10 | NumberOfDependents | Number of dependents in family excluding themselves (spouse, children etc.) | integer


# Results

__Overview__

For the purposes of conciseness, we will use the following definitions:
- __Examples:__ refers to a training set (a row in the csv file)
- __Original dataset:__ refering to the dataset with missing attributes denoted as "NA"
- __Filled in dataset:__ refering to the dataset with the missing attributes filled in by using their means
- __Dropped dataset:__ refering to the dataset with examples containing missing attributes being dropped
- __Classifier:___ SeriousDlqin2yrs (binary)
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

Classifier | Dropped Dataset | Filled in Dataset |
-----------|-----------------|-------------------|
ZeroR					|   93.05%  |   93.32%   |
Decision Tree 			| 	93.27%	|	93.55%	 |
Nearest Neighbor 		| 	93.07%	|	93.35%	 |
Multilayer Perceptron 	|	92.83%	|	92.92%	 |
Logistic Regression 	|	93.12%	|	93.39%	 |
Naive Bayes 			|	93.00%	|	93.28%	 |



__K-Nearest Neighbors__

The graph below depicts the accuracy of the KNN algorithm for a K values in the range 0 to 30 using the sci-kit KNN algorithm. The red 
dotted line uses a distance function to determine the proximity of the neighbors while the red line 
uses a uniform function to calculate neighbors. As you can see, the uniform distance 
did better overall, but as K increased both methods converged on a similar value 
slightly above 93% accuracy. These values were calculated using the filled in dataset.
![KNN Graph](/graphs/KNN_smalldata.png)


Because at a K of 15 for the KNN algorithm converges on the maximum accuracy, we used this K to 
determine the values when dropping attributes. The accuracy results using the filled in dataset 
we found are depicted below: 


Dataset | Weight |attr_1 | attr_2 | attr_3 | attr_4 | attr_5 | attr_6 | attr_7 | attr_8 | attr_9 | attr_10 |
--------|--------|-------|--------|--------|--------|--------|--------|--------|--------|--------|---------|
Dropped | Uniform| 98%   |93%     | 93%    | 93% 	|93%     | 94%    |	93%	   |  93%	|  93%   | 93%	   |
Dropped | Distance|98%   |93%     | 93%    | 93%    |93%     | 93%    |	93%	   |  93%	|  93%   | 93%	   |
Filled-In| Uniform|93.35% |93.36% | 93.35% | 93.37% |93.50%  | 93.35% |	93.35% |  93.35%|  93.35%| 93.35%  |
Filled-In| Distance|93.28%|93.25% | 93.30% | 93.28% |93.29%  | 93.26% |	93.29% |  93.30%|  93.30% | 93.30% |

__Decsion Trees__

Dropping attribues for the decision tree classifier in Weka on the filled in dataset, we get the following 
accuracy results:

Dataset | attr_1 | attr_2 | attr_3 | attr_4 | attr_5 | attr_6 | attr_7 | attr_8 | attr_9 | attr_10 |
--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|---------|
Dropped  | 93.27%| 93.33% | 93.31% | 93.30% |93.25%  | 93.29% |93.10% | 93.34% |  93.27%| 93.34%  |
Filled-In| 93.56%| 93.52% | 93.62% | 93.55% | 93.57% | 93.57% | 93.43% | 93.61% | 93.50% | 93.57%  | 


__Logistic Regression__

Finally, we dropped all attributes individually from both datasets in Weka and ran logistic regressions on them. The results of those tests in 10-fold cross validation are the following:

Dataset | attr_1 | attr_2 | attr_3 | attr_4 | attr_5 | attr_6 | attr_7 | attr_8 | attr_9 | attr_10 |
--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|---------|
Dropped  | %| % | % | % |%  | % | % | % |  %| %  |
Filled-In| 93.39%| 93.40% | 93.37% | 93.39% | 93.38% | 93.39% | 93.32% | % | 93.33% | 93.39%  | 


# The Code


We first need to create our 3 datasets. We start with the original dataset with missing attributes denoted
as "NA" (this is one of the three datasets). We then use the following code to generate our second dataset
with all the examples containing "NA" dropped by calling this .

```python
def read_training_data(fname, dropped=False):
	col_start = 1
	col_end = 12
	data = []
	f = open(fname)
	csv_reader = csv.reader(f)
	for line in csv_reader:
	    append_line = [line[i] for i in range(col_start,col_end)]
	    if dropped:
		    if "NA" in append_line:
		    	continue
	    data.append(append_line)
	f.close()
	return data

def dropped():
	d_new = read_training_data('data/cs-training.csv', dropped=True)	

	with open("data/training_missing_dropped.csv", "wb") as f:
	    writer = csv.writer(f)
	    writer.writerows(d_new)
```

To generate the third dataset, we use the same read_training_data function but instead of dropped,
we use a fill in function. The filled in function uses a compute missing data function that uses
a helper function to generate the means and replace the missing attributes.

```python
def get_means(data):
	"""
	get the mean values of each columns to fill missing attribute values
	input:
		a list of lists representing the excel data
 
	returns:
		single list of means associated with each column
	"""
	totals = [[] for x in range(0, 11)]
	entries = [0] * 11
	header = 0
	for d in data:
		if header == 0:
			header += 1
			continue
		for i, x in enumerate(d):
			if x != "NA":
				totals[i].append(float(x))
				entries[i] += 1
	
	sums = [sum(total) for total in totals]
	means = [sums[i]/float(entries[i]) for i in range(0,11)]
	return means


def compute_missing_data(data):
	"""
	fills in the missing attribute with the means of the associated columns 

	inputs:
		a list of lists representing the excel data

	returns:
		the same lists of lists with the missing attributes filled in
	"""
	means = get_means(data)
	for d in data:
		for j,x in enumerate(d):
			if x == 'NA':
				d[j] = means[j]
	return data		

def generate_filled_in():
	d = read_training_data('data/cs-training.csv')	
	d_new = compute_missing_data(d)
	
	with open("data/training_no_missing_attrs.csv", "wb") as f:
	    writer = csv.writer(f)
	    writer.writerows(d_new)
```



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
	col_end = 11  # number of attributes
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

By doing this, we are able to iterate through which attribute we want to drop and use them to get
the accuracy of the classifier. This is shown below:

```python
	for j in range(1,11):
		_data = read_training_data(train_file, drop=j)
		headers = _data[0]
		data = _data[1:]
		assert(len(headers) == len deata[1])
		
		X = [attrs[1:] for attrs in data] # data with the class attribute missing
		Y = [int(_class[0]) for _class in data] # classifications for the data	
		np_x = np.array(X)
		np_y = np.array(Y)
		assert len(np_x) == len(np_y)
		
		print("Finding Decision Tree for dropping attribute %s", headers[j])
		decision_tree(np_x, np_y)
```
