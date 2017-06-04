
# Liquiditity Predictor
__Nicholas Kostiantos, Heath Reineke & David Wallach__
- [Full Dataset Results](/regular_dataset.md)
- [Undersampled Dataset Results](/small_dataset.md)


We began with a file containing 150,000 examples. While this may seem good in theory, the data was undersampled
and therefore not fully representative of the model we were aiming to generate. Of the 150,000 examples 139,974 
were classified as 0 and only 10,0026 were classified as 1. This led to our ZeroR classification to be 
around 93%. The implications of this were that using more complex classifiers yielded only minimal increases 
(less than one percent). To combat the undersampling, we used a subset of our training data that had more even 
distrobution of classifications so that our ZeroR was a value closer to 50%. 


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


