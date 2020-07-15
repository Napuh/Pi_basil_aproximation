import math
import sys
import os
import time
from tqdm import tqdm

if(len(sys.argv)!=2 or type(sys.argv[0])!=int):
    print("Error interpreting arguments")
else:
    def pi_basilea(iterations):
        pi_aprox_value = 0
        for value in tqdm(range(1, iterations+1)):
            pi_aprox_value += 1/(value**2)
        return math.sqrt(6*pi_aprox_value)
    if os.path.exists("Pi_basil.txt"):
        os.remove("Pi_basil.txt")
    txt = open("Pi_basil.txt", "wt")
    number_of_iterations = int(sys.argv[1])
    txt.write(str(pi_basilea(number_of_iterations)))
    txt.close()