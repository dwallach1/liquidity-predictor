# Liquidity Predictor



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


# Ablation Results

To find the most important attribute, we took our three best learners (KNN from sci-kit, J48 from Weka, Logistic Regression in Weka) and dropped each attribute individually from both the Dropped dataset and the Filled-In dataset, and examined the results to see which attribute was most important. For decision trees and logistic regression (our best two learners), the most important attribute was attr_7, which is NumberOfTimes90DaysLate. The KNN results didn't show this same drop, but because accuracy drops the most with removing this attribute in our best two learners, we are confident in saying this is the most important attribute for borrowers to be aware of when trying to obtain a loan. All results are below.


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
Dropped  |93.12 %| 93.12% | 93.10% | 93.12% | 93.12% | 93.11% | 93.06% | 93.11% |  93.07%| 93.13%  |
Filled-In| 93.39%| 93.40% | 93.37% | 93.39% | 93.38% | 93.39% | 93.32% | 93.38% | 93.33% | 93.39%  | 


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
Dropped | Uniform| 93.07% |93.10% | 93.07% | 93.07%	|93.27%  | 93.08% |	93.07% |  93.07%|  93.07%| 93.07%  |
Dropped | Distance|93.00% |93.00% | 93.02% | 93.02% |93.02%  | 93.07% |	93.01% |  93.02%|  93.02%| 93.02%  |
Filled-In| Uniform|93.35% |93.36% | 93.35% | 93.37% |93.50%  | 93.35% |	93.35% |  93.35%|  93.35%| 93.35%  |
Filled-In| Distance|93.28%|93.25% | 93.30% | 93.28% |93.29%  | 93.26% |	93.29% |  93.30%|  93.30% | 93.30% |




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
