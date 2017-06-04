
# Finding the Best Classifier

We began with a file containing 150,000 examples. While this may seem good in theory, t
he data was undersampled and therefore not fully representative of the model we were aiming to 
generate. Of the 150,000 examples 139,974 were classified as 0 and only 10,0026 were classified as 1. 
This led to our ZeroR classification to be around 93%. The implications of this were 
that using more complex classifiers yielded only minimal increases (less than one percent). To combat 
the undersampling, we used a subset of our training data that had more even distrobution of 
classifications so that our ZeroR was a value closer to 50%. 


Dataset | N | ZeroR | Decision Tree | Logistic Regression | Naive Bayes | Multi-layer Perceptron | Best Classifier| Difference |
--------|---|-------|---------------|---------------------|-------------|------------------------|----------------|------------|
Dropped | 90,000 | 72.39% | 81.1253% |  78.6342% | 74.3987% | |Decision Tree |8.7353% |
Dropped | 100,000 | 58.7675% | 77.6199% |  73.6728% | 63.4547% | | Decision Tree | 18.8524% |
Dropped | 110,000 | 81.3888% | 84.6026% |  82.1679% | 44.887% | | Decision Tree | 3.2138% |
Filled-in | 90,000 | 83.2897% | 86.9631% |  84.4764% | 83.5081% | | Decision Tree | 3.6734% |
Filled-in | 100,000 | 79.9476% | 85.2297% |  81.7576% | 80.2836% | | Decision Tree | 5.2821% |
Filled-in | 110,000 | 74.9344% | 82.9321% |  78.227% | 75.5444% | | Decision Tree | 7.9977% |
Filled-in | 120,000 | 66.5789% | 80.306% |  75.6959% | 67.5923% | | Decision Tree | 13.7271% |
Filled-in | 130,000 | 50.1235% | 77.9089% |  72.6736% | 51.9126% | | Decision Tree | 27.7854% |
__Means__ | N/A | 70.92755% | 82.08595% | 78.413175% | 67.697675% | | N/A | 11.1584% |


Parsing the results above, we can see that the decision tree classifier consistently 