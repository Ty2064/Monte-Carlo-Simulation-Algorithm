# Monte-Carlo-Simulation-Algorithm

## Overview

This project is a software application designed to perform **Monte Carlo simulations**. The system generates a large number of random scenarios based on defined parameters and probability distributions, allowing users to analyze uncertainty and evaluate possible outcomes.

The initial implementation is designed to support **10,000 simulation iterations**, although the architecture can be expanded to handle larger numbers of simulations.

## How It Works

The Monte Carlo method follows a simple process:

1. Define the problem to be simulated.
2. Identify the input variables.
3. Define the probability distribution for each uncertain variable.
4. Generate random values based on those distributions.
5. Execute the mathematical model.
6. Store the simulation result.
7. Repeat the process multiple times.
8. Analyze the final distribution of results.

### Simulation Flow

```text
Define Parameters
        ↓
Generate Random Values
        ↓
Execute Mathematical Model
        ↓
Store Result
        ↓
Repeat 10,000 Times
        ↓
Analyze Results
        ↓
Generate Statistics and Visualizations
```

## Features

* Monte Carlo simulation engine
* Support for 10,000 or more simulation iterations
* Random variable generation
* Support for probability distributions
* Statistical analysis of simulation results
* Calculation of mean and median
* Minimum and maximum result analysis
* Standard deviation calculation
* Percentile analysis
* Result visualization through charts
* Reproducible simulations using random seeds
* Optional permanent storage of simulation results

## Statistical Analysis

After completing the simulation, the application analyzes the generated results.

The main statistical metrics include:

* Mean
* Median
* Minimum value
* Maximum value
* Standard deviation
* Percentile 5 (P5)
* Percentile 50 (P50)
* Percentile 95 (P95)

These metrics help users understand the probability distribution and the range of possible outcomes.

## Technologies

The technologies used in this project may include:

* Python for simulation and statistical calculations
* NumPy for numerical operations
* Matplotlib for data visualization


## Project Status

This project is currently under development.

The main objective is to create a flexible and reliable Monte Carlo simulation application capable of generating, analyzing, and visualizing thousands of probabilistic scenarios.
