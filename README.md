# 0–1 Knapsack Problem Instances

This repository contains benchmark instances for the 0–1 Knapsack Problem that are frequently referenced in research (e.g., \[1, 2]).
These instances were extracted from [JordiHOFC/knapsackproblemboolean](https://github.com/JordiHOFC/knapsackproblemboolean), retaining only the instance files for convenience and clarity.

The original source of these instances was [this link](https://www.artemisa.unicauca.edu.co/~johnyortega/instances_01_KP/),
which is no longer active and is also unavailable on the [Internet Archive](https://web.archive.org/web/20231117103352/http://artemisa.unicauca.edu.co/~johnyortega/instances).

As noted in \[1], the instances were originally obtained from optimization codes developed by David Pisinger.
A related website is available [here](https://hjemmesider.diku.dk/~pisinger/codes.html), 
which includes a [link to the generator](http://www.diku.dk/~pisinger/generator.c); however, this link for the generator also appear to be inaccessible at present.


## File Structure
- `low-dimensional/`: Instances with a small number of items (low-dimensional).
- `high-dimensional/`: Instances with a larger number of items (high-dimensional).
- `optimum_values.csv`: Contains the optimal value for each problem instance.
- `knapsack_parser.py`: A simple Python script demonstrating how to parse an instance file.


## Knapsack Problem Instance Format
Each instance file is structured as follows:
- The first line has two integers: the number of items $N$ and the knapsack capacity $C$.
- The next $N$ lines each has two numbers: the value $v_i$ and weight $w_i$ of each item.
  - All instances use integer values and weights, except for instance `f5_l-d_kp_15_375`, which are float.
- Optionally, the last line may contain $N$ binary values (0 or 1), representing the optimal solution.


## Dataset Property
| Data Set              | Low-dimensional | Uncorrelated high-dimensional | Weakly correlated high-dimensional | Strongly correlated high-dimensional |
|-----------------------|:---------------:|:-----------------------------:|:----------------------------------:|:------------------------------------:|
| Filename Pattern      | `f\d+_l-d_kp_.*` |         `knapPI_1_.*`          |            `knapPI_2_.*`            |             `knapPI_3_.*`             |
| Number of Items $N$   |      4-20       |          100-10,000           |             100-10,000             |              100-10,000              |
| Item Weights $w_i$    |        -        |         Rand(1, 1000)         |           Rand(1, 1000)            |            Rand(1, 1000)             |
| Item Values $v_i$     |        -        |         Rand(1, 1000)         |   Rand($w_i$ - 100, $w_i$ + 100)   |             $w_i + 100$              |
| Knapsack Capacity $C$ |        -        | 0.75 $\times$ sum of weights  |    0.75 $\times$ sum of weights    |     0.75 $\times$ sum of weights     |


---
## References
\[1] A. E. Ezugwu, V. Pillay, D. Hirasen, K. Sivanarain, and M. Govender, “A Comparative Study of Meta-Heuristic Optimization Algorithms for 0–1 Knapsack Problem: Some Initial Results,” *IEEE Access*, vol. 7, pp. 43979–44001, 2019. doi: [10.1109/ACCESS.2019.2908489](https://doi.org/10.1109/ACCESS.2019.2908489).

\[2] N. Moradi, V. Kayvanfar, and M. Rafiee, “An efficient population-based simulated annealing algorithm for 0–1 knapsack problem,” *Engineering with Computers*, vol. 38, pp. 2771–2790, 2022. doi: [10.1007/s00366-020-01240-3](https://doi.org/10.1007/s00366-020-01240-3).
