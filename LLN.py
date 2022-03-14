import random
import numpy as np
import matplotlib.pyplot as plt

def dice_simulation (count_num):
    num_random = random.randrange(1,7)
    if(num_random == 1):
        count_num [0] += 1
    elif(num_random == 2):
        count_num [1] += 1   
    elif(num_random == 3):
        count_num [2] += 1 
    elif(num_random == 4):
        count_num [3] += 1
    elif(num_random == 5):
        count_num [4] += 1 
    else:
        count_num [5] += 1

def dice_statistics ():     
    count_num = [0, 0, 0, 0, 0, 0]
    prob_dif_list = [0]
    for i in range(0, 1000000):
        dice_simulation (count_num)
        prob = count_num[0] / (i + 1)
        prob_dif = prob - 1/6
        prob_dif_list.insert(i + 1, prob_dif)
    plt.plot(prob_dif_list)
    plt.show()
    print(count_num)
dice_statistics()    
    

