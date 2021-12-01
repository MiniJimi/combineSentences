import time
import os

#while True:
#    if os.path.exists("hiddenGem/data"):
 #       with open("hiddenGem/data") as file:
 #           print(file.read())
 #   else:
 #       print("File does not exist.")
 #   time.sleep(5)

while True:
    if os.path.exists("hiddenGem/data"):
        with open("hiddenGem/data") as file:
            print(file.read())
    else:
        print("File does not exist")
        
    time.sleep(3)


        

