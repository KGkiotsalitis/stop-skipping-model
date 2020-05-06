# Rolling Horizon Stop-skipping Model

This repository is meant for publishing some of the code related to the **stop-skipping problem in rolling horizons** applied in public transit (in particular, **bus services**).

Currently, this repository contains a couple of modules:

1. The `stop_skipping_model.py` script contains the rolling horizon stop-skipping model introduced in the paper **Stop Stop-skipping in Rolling Horizons**, which is currently under scientific review. This Python script contains all necessary functions to calculate the performance of a stop-skipping solution. 

2. The `main.hs` script contains the implementation of the rolling horizon stop-skipping model in Haskell - a functional programming language. It also computes the solution performance of the toy network instance with 5 stop-skipping candidate stops presented in the numerical experiments section of the manuscript.

3. The `main.lg4` script containts the implementation of the rolling horizon stop-skipping model in LINDO - an off-the-self-optimization solver. It computes the solution of the model for the toy network instance with 5 stop-skipping candidate stops presented in the numerical experiments section of the manuscript. 

# Referencing

In case you use this code for scientific purposes, it is appreciated if you provide a citation to the paper **Stop Stop-skipping in Rolling Horizons** once it is publicly available.

# License

MIT License

# Dependencies

Note that the scripts are programmed in Python, Haskell and LINDO. Running or modifying the scripts requires an installed version of **Python 3.6**, **Haskell 8.6.3* or **LINGO 18.0*. 
