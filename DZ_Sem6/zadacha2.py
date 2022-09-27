# Планеты и элипсы через списочное выражение
# S = PI*a*b - площадь элипса
import math


orbits = [(1, 3), (2, 6), (9, 6), (7, 2), (4, 3), (20, 20)]

def find_farthest_orbit(list):
    S = round(max([math.pi*i[0]*i[1] for i in orbits if i[0] != i[1]]), 2)
    return [i for i in orbits if round((i[0]*i[1]*math.pi),2) == S]
  
print(*find_farthest_orbit(orbits))
    
