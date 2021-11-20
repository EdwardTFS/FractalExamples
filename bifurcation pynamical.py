#uses pynamical - works with py 3.9 cannot install in 3.10
from pynamical import logistic_map, simulate, bifurcation_plot
pops = simulate(model=logistic_map, num_gens=100, rate_min=0, rate_max=4, num_rates=1000, num_discard=100)
bifurcation_plot(pops)