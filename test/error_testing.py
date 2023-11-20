# def any_division3(number):
#     try:
#         if number == 13:
#             raise ValueError("13 is an unlucky number")
#         if number == 14:
#             raise ZeroDivisionError("Avanti Fer!!!")
#         print(100 / number)
#     except ZeroDivisionError:
#         print("Enter a number other than zero")
#         raise
#     except TypeError:
#         print("Enter a numerical value")
#     except ValueError as ex:
#         print("No way!", ex.args)
#         raise
#     else:
#         print("There were no errors")
#     finally:
#         print("This will always be printed")
#
#
# any_division3(14)

import random
some_exceptions = [ValueError, TypeError, IndexError, None]
try:
    choice = random.choice(some_exceptions)
    print("raising{}".format(choice))
    if choice:
        raise choice("An error")
except ValueError:
    print("Caught a ValueError")
except TypeError: print("Caught a TypeError")
except Exception as ex:
    print("Caught some other error: %s" % ex.__class__.__name__)
else:
    print("This code called if there is no exception")
finally:
    print("This cleanup code is always called")


# class InvalidWithdrawal(Exception):
#     def __init__(self, balance, amount):
#         super().__init__(f"account doesn't have${amount}")
#         self.amount = amount
#         self.balance = balance
#
#     def overage(self):
#         return self.amount - self.balance
#
#
# try:
#     raise InvalidWithdrawal(25, 100)
# except InvalidWithdrawal as ex:
#     print("Your withdrawal is more than your balance by {} leva".format(ex.overage()))
#     print("Your withdrawal is more than your balance by %s" % ex.overage(), "leva")
#     print(f"Your withdrawal is more than your balance by {ex.overage()} leva")