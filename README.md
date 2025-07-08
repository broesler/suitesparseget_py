# suitesparseget

suitesparseget makes it easy to get matrices from the SuiteSparse Matrix
Collection into Python. It provides a simple interface to download and access
matrices from the collection, which is a widely used resource for testing
and benchmarking numerical algorithms.

It is a modern version of 
[ssgetpy](https://github.com/drdarshan/ssgetpy), which allows downloading of
matrix files, but does not provide a method to import them into Python.

`suitesparseget` uses the `pandas` library to manage the index of matrices,
which allows easier manipulation and filtering of the data than `ssgetpy`. 

The repo is a work in progress, so check back soon for more features and
examples!


## Usage

```python
import suitesparseget as ssg

df = ssg.get_index()  # get the index of matrices
print(df.head())  # print the first few rows of the index

# Get a problem from the index
problem = ssg.get_problem(index=df, name='arc130')
print(problem)
```
