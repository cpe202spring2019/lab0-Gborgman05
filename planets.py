def weight_on_planets():
   # write your code here
    weight = int(input("What do you weigh on earth? "))    
    weightM = weight * 0.38
    weightJ = weight * 2.34
    print("\nOn Mars you would weigh {0} pounds.\nOn Jupiter you would weigh {1} pounds.".format(weightM, weightJ))
   
   
   
if __name__ == '__main__':
   weight_on_planets()
