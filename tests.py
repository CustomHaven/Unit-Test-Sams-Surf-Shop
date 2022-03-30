# Write your code below: Q1
import unittest
import surfshop
# Q13
import datetime

# Q2
class SurfShopTests(unittest.TestCase):
  # Q3
  def setUp(self):
    self.cart = surfshop.ShoppingCart()
  # Q4
  def test_add_surfboard(self):
    # print(self.cart.add_surfboards(1))
    self.assertEqual(self.cart.add_surfboards(1), 'Successfully added 1 surfboard to cart!')
  # Q5 Q6
  def test_add_surfboards(self):
    # Q10 loop with subTest although we done it before
    for i in range(2, 10):
      with self.subTest(i):
        if i < 5:
          message = self.cart.add_surfboards(i)
          self.assertEqual(message, 'Successfully added {i} surfboards to cart!'.format(i=i))
        else:
          # Q9 is SKIP but before we ran it
          self.skipTest("No more limit to a max of 4 people")
          print(i) #NOTHING RUNS HERE CUZ ALL OF SKIP!!
          self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, i) # i is 5 or more up to 9atm
      self.cart = surfshop.ShoppingCart() # RESTARTING
  
  
  # Q7 Q8 MARK AS EXPECTED FAILURE
  # Q11 we commentout expected failure because we fix the error in surfshop.py
  # @unittest.expectedFailure
  def test_apply_locals_discount(self):
      self.cart.apply_locals_discount()
      self.assertTrue(self.cart.locals_discount)


  # Q13
  def test_checkout_date_today(self):
    today = datetime.datetime.now()
    self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, today)

  def test_checkout_date_before_today(self):
    last_year = datetime.datetime(2020, 12, 3, 10, 20, 59)
    self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, last_year)
  
  def test_checkout_date_in_the_future(self):
    time_to_come = datetime.datetime(2023, 1, 27, 14, 30,20)
    self.cart.set_checkout_date(time_to_come)
    self.assertEqual(time_to_come, self.cart.checkout_date)


# Q8 
unittest.main()