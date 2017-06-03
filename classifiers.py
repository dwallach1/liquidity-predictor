import os
import subprocess
import csv

import numpy as np
import pydotplus 
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold

# for decision trees
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz

#for KNN
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

#for MLP
from sklearn.neural_network import MLPClassifier

# ClASSIFIERS : {DecisionTree, KNN, MLP, NaiveBayes, Linear Regression}

def read_training_data(fname, drop=None):
	"""
	Input:
		fname -- (string) the path to the csv file of data
		drop -- (None or int) defaulted to none, otherwise indicated index to drop

	Returns:
		the orginal dataset in an array format with attribute dropped in drop is not None
	"""
	col_start = 0	
	col_end = 11 # number of attributes
	data = []
	f = open(fname)
	csv_reader = csv.reader(f)
	for j, line in enumerate(csv_reader):
		if j == 0:
			# if it is the header file, parse as is (string)
			if drop != None:
				append_line = [line[header] for header in range(col_start, col_end)]
				del append_line[drop]
			else:
				append_line = [line[header] for header in range(col_start, col_end)]
		if j != 0:
			# otherwise, cast as float
			if drop != None:
				append_line = [float(line[cell]) for cell in range(col_start,col_end)]
				del append_line[drop]
			else:
				append_line = [float(line[cell]) for cell in range(col_start,col_end)]
		data.append(append_line)
	f.close()
	return data

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
	# data is 2D array -- get each val
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
	# means = [total.mean() for total in totals]
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
				# print ("setting value to mean of %s" % means[j])
	return data				

def mlp(x,y):
	clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                     hidden_layer_sizes=(100,100,100,100,100,100,100,100,100,100,100,100,100), random_state=1)
	scores = cross_val_score(estimator=clf, X=x, y=y, cv=10, n_jobs=4)
	print("MLP (alpha=1e-5) 10 Cross Validation Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

def mlp_graphs(X, y):
	h = .02  # step size in the mesh

	alphas = np.logspace(-5, 3, 5)
	names = []
	for i in alphas:
	    names.append('alpha ' + str(i))

	classifiers = []
	for i in alphas:
	    classifiers.append(MLPClassifier(alpha=i, random_state=1))

	datasets = [(X, y)]
	figure = plt.figure(figsize=(17, 9))
	
	i = 1
	# iterate over datasets
	for X, y in datasets:
	    # preprocess dataset, split into training and test part
	    X = StandardScaler().fit_transform(X)
	    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.4)

	    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
	    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
	    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
	                         np.arange(y_min, y_max, h))

	    # just plot the dataset first
	    cm = plt.cm.RdBu
	    cm_bright = ListedColormap(['#FF0000', '#0000FF'])
	    ax = plt.subplot(len(datasets), len(classifiers) + 1, i)
	    # Plot the training points
	    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright)
	    # and testing points
	    ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, alpha=0.6)
	    ax.set_xlim(xx.min(), xx.max())
	    ax.set_ylim(yy.min(), yy.max())
	    ax.set_xticks(())
	    ax.set_yticks(())
	    i += 1

	    # iterate over classifiers
	    for name, clf in zip(names, classifiers):
	        ax = plt.subplot(len(datasets), len(classifiers) + 1, i)
	        clf.fit(X_train, y_train)
	        score = clf.score(X_test, y_test)

	        # Plot the decision boundary. For that, we will assign a color to each
	        # point in the mesh [x_min, x_max]x[y_min, y_max].
	        if hasattr(clf, "decision_function"):
	            Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
	        else:
	            Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]

	        # Put the result into a color plot
	        Z = Z.reshape(xx.shape)
	        ax.contourf(xx, yy, Z, cmap=cm, alpha=.8)

	        # Plot also the training points
	        ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright)
	        # and testing points
	        ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright,
	                   alpha=0.6)

	        ax.set_xlim(xx.min(), xx.max())
	        ax.set_ylim(yy.min(), yy.max())
	        ax.set_xticks(())
	        ax.set_yticks(())
	        ax.set_title(name)
	        ax.text(xx.max() - .3, yy.min() + .3, ('%.2f' % score).lstrip('0'),
	                size=15, horizontalalignment='right')
	        i += 1

	figure.subplots_adjust(left=.02, right=.98)
	plt.show()

def knn(x, y, k=15, graph=None):
	"""
	inputs:
		train_file: the file to train and test the classifier


	Returns:
		Nothing
	"""
	n_neighbors = k
	h = .02  # step size in the mesh
		# Create color maps
	cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
	cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

	if graph:
		for weights in ['uniform', 'distance']:
		    # we create an instance of Neighbours Classifier and fit the data.
		    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
		    clf.fit(x, y)

		    # Plot the decision boundary. For that, we will assign a color to each
		    # point in the mesh [x_min, x_max]x[y_min, y_max].
		    x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
		    y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1
		    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
		                         np.arange(y_min, y_max, h))
		    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

		    # Put the result into a color plot
		    Z = Z.reshape(xx.shape)
		    plt.figure()
		    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

		    # Plot also the training points
		    plt.scatter(x[:, 0], x[:, 1], c=y, cmap=cmap_bold)
		    plt.xlim(xx.min(), xx.max())
		    plt.ylim(yy.min(), yy.max())
		    plt.title("3-Class classification (k = %i, weights = '%s')"
		              % (n_neighbors, weights))

		plt.show()

	if not graph:
		weights = ['uniform', 'distance']
		for w in weights:
			clf = neighbors.KNeighborsClassifier(n_neighbors, weights=w)
			scores = cross_val_score(estimator=clf, X=x, y=y, cv=10, n_jobs=4)
			print("KNN 10 Cross Validation Accuracy: %0.4f (+/- %0.2f) for weights %s" % (scores.mean(), scores.std() * 2, w))

def knn_graph(x, y):
	x_axis =[]
	y1_axis = []
	y2_axis = []
	for k in range(1,30):
		n_neighbors = k
		h = .02  # step size in the mesh
		weights = ['uniform', 'distance']
		clf_1 = neighbors.KNeighborsClassifier(n_neighbors, weights=weights[1])
		clf_2 = neighbors.KNeighborsClassifier(n_neighbors, weights=weights[0])
		scores_1 = cross_val_score(estimator=clf_1, X=x, y=y, cv=10, n_jobs=4)
		scores_2 = cross_val_score(estimator=clf_2, X=x, y=y, cv=10, n_jobs=4)
		y1_axis.append(scores_1.mean())
		y2_axis.append(scores_2.mean())
		x_axis.append(k)
		print("%dNN 10-fold Cross Validation Accuracy: %0.4f (+/- %0.2f) weights %s" % (k, scores_1.mean(), scores_1.std() * 2, weights[1]))
		print("%dNN 10-fold Cross Validation Accuracy: %0.4f (+/- %0.2f) weights %s" % (k, scores_2.mean(), scores_2.std() * 2, weights[0]))

	plt.plot(x_axis, y1_axis, 'r-', x_axis, y2_axis, 'b-.')
	plt.show()
	# plt.plot(x_axis, y_axis)
	# plt.show()

def decision_tree(x, y, headers=None, output_file=None, colored=True, graph=False):
	"""
	Decision Trees are non-parametric supervised learning method used to for classification and regression. 
	scikit-learn uses an optimised version of the CART (Classification and Regression Trees) algorithm to form decision trees.
	CART constructs binary trees using the feature and threshold that yield the largest information gain at each node. 
	This uses an optimized version of CART. 

	** uses means of the column for missing values **
	** perfroms 10-fold cross validation **

	Inputs:
		train_file: the file to train and test the classifier
		output_file: str describing name of the output file you want
		colored: bool descibing the type of output
	reads the training data and accounts for missing values by using the mean of that attribute for all
	training examples (in compute_missing_data). 
	It then builds the decision tree and writes a pdf of the outcome to the output_file

	Returns:
		Nothing
	"""


	if graph:
		if output_file is None:
			print("Need to specify an output file to store graph")
			return
		dt = tree.DecisionTreeClassifier()
		dt = dt.fit(x, y)
		print ("Making Graph")
		with open("dt.dot", 'w') as f:
			f = tree.export_graphviz(dt, out_file=f)
		os.unlink('dt.dot')
		if not colored:
			dot_data = tree.export_graphviz(dt, out_file=None) 
		else:

			dot_data = tree.export_graphviz(dt, out_file=None, 
		                     feature_names=headers,  
		                     class_names=[str(x) for x in classifications],  
		                     filled=True, rounded=True,  
		                     special_characters=True)  
		graph = pydotplus.graph_from_dot_data(dot_data) 
		graph.write_pdf(output_file)
		print ("wrote graph to file: %s" % output_file) 


	clf = tree.DecisionTreeClassifier()
	scores = cross_val_score(estimator=clf, X=x, y=y, cv=10, n_jobs=4)
	print("Decison Tree 10-fold Cross Validation Accuracy: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))
	

def main():
	# train_file = 'data/cs-training.csv'
	# train_file = 'data/training_no_missing_attrs.csv'
	# train_file = 'data/training_missing_dropped.csv'
	train_file = 'data/training_no_missing_attrs_SMALL.csv'

	_data = read_training_data(train_file)
	headers = _data[0]

	data = _data[1:]
	assert(len(headers) == len(data[1]))
	
	X = [attrs[1:] for attrs in data] # data with the class attribute missing
	Y = [int(_class[0]) for _class in data] # classifications for the data	
	np_x = np.array(X)
	np_y = np.array(Y)
	assert len(np_x) == len(np_y)
	# decision_tree(np_x, np_y)
	# knn(np_x, np_y, k=15, graph=False)
	knn_graph(np_x, np_y)
	# mlp_graphs(np_x, np_y)
	# decision_tree(np_x, np_y, headers=headers[1:], output_file="graphs/dt-newest.pdf", graph=True, colored=True)

	# for j in range(1,11):
	# 	_data = read_training_data(train_file, drop=j)		
	# 	headers = _data[0]
		
	# 	data = _data[1:]
	# 	assert(len(headers) == len (data[1]))
	# 	X = [attrs[1:] for attrs in data] # data with the class attribute missing
	# 	Y = [int(_class[0]) for _class in data] # classifications for the data	
	# 	np_x = np.array(X)
	# 	np_y = np.array(Y)

	# 	assert(len(np_x[0]) == 9)
	# 	assert len(np_x) == len(np_y)
	# 	# print("Finding Decision Tree for dropping attribute %s", j)
	# 	print("Finding 15-NN for dropping attribute %s", j)
	# 	# decision_tree(np_x, np_y)
	# 	knn(np_x, np_y, k=15, graph=False)
	# 	# mlp(np_x,np_y)

if __name__ == '__main__':
	main()