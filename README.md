# Rolling Horizon Stop Skipping Model

This repository is meant for publishing some of our code related to the stop-skipping problem in rolling horizons applied in public transit (in particular, bus services).

Currently, this repository contains a couple of modules:

The stop_skipping_model module contains functions that calculate the feasibility and the performance of a stop-skipping solution. This module is the rolling horizon stop-skipping model. 

The tsp-drones-heur module module contains the data of the toy network (bus line) discussed in the paper Stop Stop-skipping in Rolling Horizons, which is currently under scientific review. Classes related to the brute-force solution method and the metaheuristics (sequential hill-climbing and genetic algorithm) discussed in the paper are also presented there.
