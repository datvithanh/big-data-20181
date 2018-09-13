import numpy as np
import sys
a = np.random.random_sample([30,30]) > 0.9
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        if(a[i,j]):
            a[j,i] = True
for i in range(a.shape[0]):
    sys.stdout.write(str(i))
    sys.stdout.write(" ")
    ok = False
    for j in range(a.shape[1]):
        if(a[i,j] and i != j):
            if(ok):
                sys.stdout.write(",")            
            sys.stdout.write(str(j))
            ok = True
    sys.stdout.write("\n")
# print(np.random.random_sample([30,30]))