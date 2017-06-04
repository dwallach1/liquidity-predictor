
# Results Using Smaller Subsets of Data

We began with a file containing 150,000 examples. While this may seem good in theory, the
data was undersampled and therefore did not fully representative of the model we were aiming to 
generate. Of the 150,000 examples 139,974 were classified as 0 and only 10,0026 were classified as 1. 
This led to our ZeroR classification to be around 93%. The implications of this caused
more complex classifiers to yield only minimal increases (less than one percent). To combat 
the undersampling, we used a subset of our training data that had more even distrobution of 
classifications so that our ZeroR was a value closer to 50%. We did this by dropping an N number of examples
that were classified as 1 as shown in the table below. The dataset refers to which dataset we were using to generate 
the subset, the N is the number of examples dropped, and the difference is the percentage difference between ZeroR and 
the best classifier's accuracy.


Dataset | N | ZeroR | Decision Tree | 25-NN | Logistic Regression | Naive Bayes | Multi-layer Perceptron | Best Classifier| Difference |
--------|---|-------|---------------|-------|---------------------|-------------|------------------------|----------------|------------|
Dropped | 90,000 | 72.39% | 81.1253% | 75.3965% |78.6342% | 74.3987% |                               |Decision Tree |8.7353% |
Dropped | 100,000 | 58.7675% | 77.6199% | 67.7669%  | 73.6728% | 63.4547% |         			| Decision Tree | 18.8524% |
Dropped | 110,000 | 81.3888% | 84.6026% | 81.642%  |82.1679% | 44.887% |            			| Decision Tree | 3.2138% |
Filled-in | 90,000 | 83.2897% | 86.9631% | 84.5931% | 84.4764% | 83.5081% |        				 | Decision Tree | 3.6734% |
Filled-in | 100,000 | 79.9476% | 85.2297% |  81.7896% |81.7576% | 80.2836% |      				  | Decision Tree | 5.2821% |
Filled-in | 110,000 | 74.9344% | 82.9321% |  77.9894%  | 78.227% | 75.5444% |      				 | Decision Tree | 7.9977% |
Filled-in | 120,000 | 66.5789% | 80.306% |  72.3824%  | 75.6959% | 67.5923% |      				 | Decision Tree | 13.7271% |
Filled-in | 130,000 | 50.1235% | 77.9089% |    66.8333%   | 72.6736% | 51.9126% |  			  | Decision Tree | 27.7854% |
__Means__ | __N/A__ | __70.92755%__ | __82.08595%__ |  __76.04915__  | __78.413175%__ | __67.697675%__ | | __N/A__ | __11.1584%__ |

 
 ** The Dropped dataset only went up to an N of 110,000 because a value for N any greater than that caused the dataset
 to be only comprised of the same classifications. This is because in the Dropped dataset, we are also dropping examples 
 that have missing attributes. 


Parsing the results above, we can see that the decision tree classifier consistently outperformed the others. For this reason, we took 
a deeper look into decision trees. The table below details the decision tree's 10-fold cross validation when dropping each attribute. We 
found that the Filled-In dataset with dropping 130,000 examples yielded the best difference thus the best learner. We call this dataset 
the best-learner. We also further investigate the dataset that yielded the best accuracy which was the Filled-In dataset that skipped
90,000 examples. We call this one the highest-accuracy dataset. Below, we drop each attribute and build a decision tree using the 
best learner dataset. The attribute dropping should see the same results across the datasets, so there was no need to 
run this for each dataset. 

- __Attr_1:__ RevolvingUtilizationOfUnsecuredLines
- __Attr_2:__ Age
- __Attr_3:__ NumberOfTime30-59DaysPastDueNotWorse
- __Attr_4:__ DebtRatio
- __Attr_5:__ MonthlyIncome
- __Attr_6:__ NumberOfOpenCreditLinesAndLoans
- __Attr_7:__ NumberOfTimes90DaysLate
- __Attr_8:__ NumberRealEstateLoansOrLines
- __Attr_9:__ NumberOfTime60-89DaysPastDueNotWorse
- __Attr_10:__ NumberOfDependents

Attr_1 | Attr_2 | Attr_3 | Attr_4 | Attr_5 | Attr_6 | Attr_7 | Attr_8 | Attr_9 | Attr_10 |
-------|--------|--------|--------|--------|--------|--------|--------|--------|---------|
76.2388%|77.6989%|76.7188%|78.0539%|77.8239%|77.6889%|76.1788%|77.5239%|76.9988% | 77.9539%|  

We found the "NumberOfTimes90DaysLate" attribute had the largest effect on our decision tree's accuracy. This makes sense because it was 
the root of the tree when no attributes were dropped. The reason that the drop in accuracy is not large, is because other attributes like
"RevolvingUtilizationOfUnsecuredLines" had a lot of information gain as well. When we dropped both "NumberOfTimes90DaysLate" and 
"RevolvingUtilizationOfUnsecuredLines", the accurcay fell to 73.4337%. 

![DecisionTreeAccuracyGraph](/graphs/DT_accuracy.png)
