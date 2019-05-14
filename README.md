# Rolling Horizon Stop Skipping Model

This repository is meant for publishing some of our code related to the stop-skipping problem in rolling horizons applied in public transit (bus services).

Currently, this repository contains a couple of modules:
The tsp-drones-core module contains classes that can be used to work with, read and/or write instances, solutions and images of the problem.
The tsp-drones-heur module contains classes related to the heuristics discussed in the paper Optimization Approaches for the Traveling Salesman Problem with Drone.
The tsp-drones-mip module contains classes related to the exact Integer Programming solution discussed in the same paper. In order to compile this you need to have IBM ILOG CPLEX Optimization Studio V12.6.3 installed and the appropriate CPLEX_STUDIO_DIR1263 environment variable must be set.
The tsp-drones-generate module contains a Spring Shell based command line utility that can be used to generate instances.
In the future we aim to publish more modules as new solution approaches are developed. If time allows a second command line utility to run the solvers will be provided. As of now, it is still necessary to write your own code to call our solvers, so all modules except the tsp-drones-generate module must be considered as a library.
