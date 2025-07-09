"""
Access the SuiteSparse library with Python.
===========================================

Classes
-------
- :class:`MatrixProblem`: The class for a SuiteSparse matrix.
- :class:`MatrixSVDs`: The class for SuiteSparse matrix singular values.

Functions
---------
- :func:`get_index`: Download and load the SuiteSparse index into a DataFrame.
- :func:`get_problem`: Download and load a problem from the collection.
- :func:`get_row`: Get a row from the index.
- :func:`get_stats`: Download and load the SuiteSparse statistics into a DataFrame.
- :func:`get_svds`: Download and load the singular values of a problem.
- :func:`load_problem`: Load a SuiteSparse matrix problem from a file path.
- :func:`ssweb`: Open the webpage for the given problem.
"""

from .suitesparseget import *

__all__ = [x for x in dir() if not x.startswith('_')]
