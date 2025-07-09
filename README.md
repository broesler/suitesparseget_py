# suitesparseget

suitesparseget makes it easy to get matrices from the [SuiteSparse Matrix
Collection](https://sparse.tamu.edu) into Python. It provides a simple interface
to download and access matrices from the collection, which is a widely used
resource for testing and benchmarking numerical algorithms.

It is a modern version of 
[ssgetpy](https://github.com/drdarshan/ssgetpy), which allows downloading of
matrix files, but does not provide a method to import them into Python.

suitesparseget uses the [pandas](https://github.com/pandas-dev/pandas) library
to manage the index of matrices, which allows easier manipulation and filtering
of the data than ssgetpy. 

An example in `examples/ssget_example.py` utilizes my
[C++Sparse](https://github.com/broesler/CppSparse) library to make spy plots of
the matrices.

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

## Configuration
You can configure the download directory for matrices by creating
a `suitesparseget.toml` file. On import, `suitesparseget` will look for this
file in:
1. the current working directory
2. the user's home directory
3. the default data directory (`~/.suitesparseget`).
The first file found will be used. If no configuration file is found, data will
be downloaded to the default data directory (`~/.suitesparseget`).

The configuration file can contain the following sections:

```toml
[paths]
data_directory = '.suitesparseget'
```

The path can either be absolute, or relative to the user's home directory.
