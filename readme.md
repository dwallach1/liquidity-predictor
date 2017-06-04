
# Predicting Likelihood of Financial Distress
__Nicholas Kostiantos, Heath Reineke & David Wallach__

nicholaskotsiantos2019@u.northwestern.edu
heathreineke2018@u.northwestern.edu
davidwallach2018@u.northwestern.edu

Northwestern University 
EECS 349 - Machine Learning

__Abstract__

Bank’s play a critical role in market economies by operating as a source of credit and by deciding who can have access to credit and on what terms. Access to credit is a major ingredient for increased economic activity. However, a disturbance in this cycle of credit can have catastrophic consequences. Our task is to help borrowers and lenders make the best financial decisions by building a model that accurately predicts if a borrower will default on a loan within a two year time period. 
 
To approach this problem, we leveraged a dataset of 150,000 borrowers with attributes such as age, monthly income, debt ratio, number of open credit lines, and number of times of late over various time periods. All the attributes are numeric. From here, we trained our data with 5 different classification learners and applied 10-fold cross validation to measure the results. While the accuracy of the model may be very useful for the lenders, the borrowers would benefit most by understanding which attributes have the biggest bearing on determining if they will default on their loan as they can only realistically improve on a couple attributes in the near future. 
 
Of all the learners, the Decision Tree classifier performed the best, correctly classifying 82.09 percent of the instances in the validation set. Of all the features, NumberOfTimes90DaysLate and RevolvingUtilizationOfUnsecuredLines  were two most important features. We concluded this by dropping out features from the dataset and training the learners on the new dataset without the feature. From here, we were looking for which feature, when missing from the dataset, created the largest decline in accuracy of the model as compared to the model trained with the full dataset. 

![Classifier Accuracy | Dropping Features]('/graphs/Abstract_Chart.png')

The classifiers we used were:
- Decision Trees
- Logistic Regression
- Naive Bayes
- Multilayer Perceptron
- Nearest Neighbor


The Programs we used to develop our results are:
- [Scikit learn](http://scikit-learn.org/stable/index.html) (a Python package)
- [Weka](http://www.cs.waikato.ac.nz/ml/weka/) (a desktop application)


__Overview__ 

We began with a file containing 150,000 examples. While this may seem good in theory, the data was undersampled
and therefore not fully representative of the model we were aiming to generate. Of the 150,000 examples 139,974 
were classified as 0 and only 10,0026 were classified as 1. This led to our ZeroR classification to be 
around 93%. The implications of this were that using more complex classifiers yielded only minimal increases 
(less than one percent). To combat the undersampling, we used a subset of our training data that had more even 
distrobution of classifications so that our ZeroR was a value closer to 50%. 

_Attributes_

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



__Generating the Different Datasets__

Most of the code we used to generate the different datasets is in data_parser.py. From the [original dataset](/data/cs-training.csv),
we created subsets of data for two reasons. First, to handle missing attributes and second, to overcome the undersampled 
nature of the original dataset. 

_Handling Missing Attributes_

Our original dataset came with missing attributes denoted as "NA". To account for this, we generated one dataset 
with all examples containing missing attributes dropped which we call [Dropped Dataset](/data/training_missing_dropped.csv)
and another with missing data replaced by the attributes mean value which we call [Filled-In Dataset](/data/training_no_missing_attrs.csv).

In [data_parser.py](/data_parser.py), we use the read_training_data function as our main
parser to read and change datasets. The fname parameter indicates the file we want to read from, the col_start and
col_end parameters indicate the offset for attributes when reading, N is used to generate datasets with less 
examples classified as 1, and dropped is a boolean that when set to true, skips all examples with "NA".

```python
def read_training_data(fname, col_start, col_end, N=0, dropped=False):
	data = []
	x = 0
	f = open(fname)
	csv_reader = csv.reader(f)
	for line in csv_reader:
	    append_line = [line[i] for i in range(col_start,col_end)]
	    if dropped:
		    if "NA" in append_line:
		    	continue

	    if append_line[0] == '0' and x <= N:
	    	x += 1
	    	continue
	    data.append(append_line)
	f.close()
	print(len(data))
	return data
```

- To generate the Dropped dataset, we wrote `read_training_data('/data/cs-training.csv', 0, 11, dropped=True)`
- To generate the Filled-In dataset, we wrote `read_training_data('/data/cs-training.csv', 0, 11)`


_Handling Undersampled Dataset_

For this, we decided to make subsets of the original dataset with a more even spread of classifications. To create 
these subsets, we used the same read_training data and looped through an array of N values, skipping that many examples
with their classificiation being 1. The main function runs the loop while the generate_filled_in_small and the 
generate_dropped_small read and write the data. 

```python
def generate_filled_in_small(N):
	d = read_training_data('data/training_no_missing_attrs.csv',0, 11, N)
	f_out = "data/training_no_missing_attrs_SMALL_" + str(N) + ".csv"
	with open(f_out, "wb") as f:
	    writer = csv.writer(f)
	    writer.writerows(d)

def generate_dropped_small(N):
	d = read_training_data('data/training_missing_dropped.csv',0,11, N)
	f_out = "data/training_dropped_SMALL_" + str(N) + ".csv"
	with open(f_out, "wb") as f:
	    writer = csv.writer(f)
	    writer.writerows(d)

def main():
	Ns = [90000, 100000, 110000, 120000, 130000]
	for n in Ns:
		generate_filled_in_small(n)
		generate_dropped_small(n)
```


# Results

We generated results for both the Filled-In dataset as well as the Dropped dataset. From there we also partitioned our
results based on using the full (original dataset) versus using subsets of data with more equal classification 
distrobutions that we created. The results can be found be following the links below. 

- [Full Dataset Results](/regular_dataset.md)
- [Undersampled Dataset Results](/small_dataset.md)


