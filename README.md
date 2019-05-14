# Rolling Horizon Stop-skipping Model

This repository is meant for publishing some of the code related to the **stop-skipping problem in rolling horizons** applied in public transit (in particular, **bus services**).

Currently, this repository contains a couple of modules:

1. The `stop_skipping_model.py` script contains the rolling horizon stop-skipping model introduced in the paper **Stop Stop-skipping in Rolling Horizons**, which is currently under scientific review. This script contains all necessary functions to calculate the performance of a stop-skipping solution. 

2. The `implementation_toy network.py` script contains the data of the toy network (bus line) discussed in the paper Stop Stop-skipping in Rolling Horizons. Classes related to the brute-force solution method and the metaheuristics (sequential hill-climbing and genetic algorithm) discussed in the same paper are also presented there. Changing the number of stops, limit_S, the results from different scenarios can be obtained. This is done in the code:

~~~~
limit_S=... #choose any number of bus stops from 3 to 6, or add more input include additional stops
~~~~

# Referencing

In case you use this code for scientific purposes, it is appreciated if you provide a citation to the paper **Stop Stop-skipping in Rolling Horizons** once it is publicly available.

# License

MIT License

# Dependencies

Note that the scripts are programmed in Python. Running or modifying the scripts requires an installed version of **Python 3.6**. In addition, the following libraries should also be installed:
* numpy 
* math
* itertools
* time
