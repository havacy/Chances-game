import time 
import numpy as np 

Test = 0
Numb = np.arange(1,10)
Target = np.random.choice(Numb)
print("Get this number to win: "+ str( Target))

while True:
    Nam = np.random.choice(Numb)
    print(Nam)
    time.sleep(1)
    Test = Test + 1
    if Nam == Target: 
        print("You won!")
        print("Took you "+ str(Test) + " tries!")
        time.sleep(5)
        break
