import math
import sys
import os
import time
from tqdm import tqdm

if(len(sys.argv)!=2):
    print("Error interpreting arguments")
else:
    def pi_basilea(iterations):
        pi_aprox_value = 0
        for value in tqdm(range(1, iterations+1)):
            pi_aprox_value += 1/(value**2)
        return math.sqrt(6*pi_aprox_value)
    if os.path.exists("Pi_basilea.txt"):
        os.remove("Pi_basilea.txt")
    txt = open("Pi_basilea.txt","wt")
    number_of_iterations = int(sys.argv[1])
    txt.write(str(pi_basilea(number_of_iterations)))
    txt.close()