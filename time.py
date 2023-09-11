import schedule as sc
import time
import os

directory = "templates/"

for filename in os.listdir(directory) :
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        print(os.path.getctime(os.path.join(directory, filename)))
'''
def cleanTemp() :
        print("wtf")

sc.every(6).hour.do(cleanTemp)

while True:
    sc.run_pending()
    time.sleep(5)
    '''