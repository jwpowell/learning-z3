# learning-z3
Scripts written to learn z3

To run the example scripts:

~~~sh
$ python3 -mvenv venv
$ source ./venv/bin/activate
$ pip install -e .
$ time learn_z3
942 716 385
385 924 761
671 583 294

564 279 138
128 365 479
793 841 526

819 432 657
437 658 912
256 197 843

real    0m0.887s
user    0m0.864s
sys     0m0.020s
~~~

## Sudoku Solver

The `learn_z3/cli.py` file contains a simple sudoku solver. Currently, this is
all the `learn_z3` command does. If you want to enter a sudoku, add it to the
`learn_z3/cli.py` file.
