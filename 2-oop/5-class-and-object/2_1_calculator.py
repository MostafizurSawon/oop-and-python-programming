# task
class Calculator:
    brand = 'Casio Mx190'

    def add(self, num1, num2):
        return num1 + num2

    # deduct method
    def deduct(self, num1, num2):
        return num1 - num2

    # multiply method
    def mul(self, num1, num2):
        return num1 * num2

    # divide method
    def div(self, num1, num2):
        return num1 / num2


my_call = Calculator()

res = my_call.deduct(9, 4)
print("Your result is:", res)
