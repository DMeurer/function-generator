from algorithms.linear import linear1
from algorithms.exponential import exponential1
from algorithms.limited_growth import limited_growth1
from algorithms.second_degree import second_degree

print("starting")
linear1.alg(2, 1, -5, 4)
print("----------------------")
exponential1.alg(5, 1, 6)
print("----------------------")
limited_growth1.alg(20, 3, 1, 2)
print("----------------------")
second_degree.alg(20, 19, 1, 1, 2, 2)
print("end")