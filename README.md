# Rolling Horizon Stop Skipping Model

This repository is meant for publishing some of our code related to the stop-skipping problem in rolling horizons applied in public transit (in particular, bus services).

Currently, this repository contains a couple of modules:

The stop_skipping_model.py script contains the rolling horizon stop-skipping model introduced in the paper Stop Stop-skipping in Rolling Horizons, which is currently under scientific review. This script contains all necessary functions to calculate the performance of a stop-skipping solution. 

The implementation_toy network.py script contains the data of the toy network (bus line) discussed in the paper Stop Stop-skipping in Rolling Horizons. Classes related to the brute-force solution method and the metaheuristics (sequential hill-climbing and genetic algorithm) discussed in the same paper are also presented there. Changing the number of stops, limit_S, the results from different scenarios can be obtained.
