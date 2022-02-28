
# Provide data input
x = 5


# Define Class MulCalc with Functions
class MulCalc:
    a = x * 6
    b = x * 10


    def __init__(self,a,b):
        self.a = a
        self.b = b

        def calc1(self):
            return a

        def calc2(self):
            return b


# Define Function Calc to provide output based on MulCalc Class
def Calc():
    print("The value of a = " + str(MulCalc.a))
    print("The value of b = " + str(MulCalc.b))


Calc()

###################  v.2.  ###############################

# Define Class MulCalc with Methods
class MulCalc:

    def __init__(self, x=0):
        self.x = x

    def calc1(self):
        return x * 6

    def calc2(self):
        return x * 10

# Define Function Calc to provide output from MulCalc Class Methods at once
def Calc():
    print("The value of calc1 = " + str(MulCalc().calc1()))
    print("The value of calc2 = " + str(MulCalc().calc2()))

# Run Calc 
Calc()
