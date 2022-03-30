# https://www.codecademy.com/courses/learn-intermediate-python-3/projects/int-python-sams-surf-shop
import datetime

class TooManyBoardsError(Exception):
  # Q12
    def __str__(self):
      return 'Cart cannot have more than 4 surfboards in it!'

class CheckoutDateError(Exception):
    # Q13
    def __str__(self):
      return 'No dates in the past allowed, select a date in the future!'

class ShoppingCart:
    def __init__(self):
        self.num_surfboards = 0
        self.checkout_date = None
        self.locals_discount = False

    def add_surfboards(self, quantity=1):
      # should delete this condition of more than 4
        if self.num_surfboards + quantity > 4:
            raise TooManyBoardsError
        else:
            self.num_surfboards += quantity
            suffix = '' if quantity == 1 else 's'
            return f'Successfully added {quantity} surfboard{suffix} to cart!'

    def set_checkout_date(self, date):
        if date <= datetime.datetime.now():
            raise CheckoutDateError
        else:
            self.checkout_date = date

    def apply_locals_discount(self):
      # Q11 TO SET locals_discount = True
      self.locals_discount = True


# Q12 testing  
# t = ShoppingCart()
# t5 = t.add_surfboards(5)
# print(t5)

# Q13 testing
past = datetime.datetime(2020, 12, 3, 10, 20, 59)
# print(datetime.datetime.now())
# t = ShoppingCart()
# t_past = t.set_checkout_date(past)
# print(t_past)

# DOCS! for datetime
# A combination of a date and a time. Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.