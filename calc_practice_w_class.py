
# Provide data input
x = 5


# Define Class MulCalc with Functions
class MulCalc:
    a = x * 6
    b = x * 10

    def __init__(self,a,b):
        self.a = a
        self.b = b

        def calc1(x):
            return a

        def calc2(x):
            return b


# Define Function Calc to provide output based on MulCalc Class
def Calc():
    print("The value of a = " + str(MulCalc.a))
    print("The value of b = " + str(MulCalc.b))


Calc()

