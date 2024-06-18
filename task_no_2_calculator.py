def main(num1 ,num2 ):
    req=Calculator()
    req.a=num1
    req.b=num2
    req.addition()
    req.subtraction()
    req.multiplication()
    req.modulo()
    req.division()
    req.exponent()
class Calculator:
    def addition(self):
        print(self.a + self.b)
    def subtraction(self):
        print(self.a - self.b)
    def multiplication(self):
        print(self.a * self.b)
    def modulo(self):
        print(self.a % self.b)
    def division(self):
        print(self.a / self.b)
    def exponent(self):
        print(self.a ** self.b)
num1=int(input( "Enter the number"))
num2=int(input( "Enter the number"))
main(num1 ,num2)       
        
