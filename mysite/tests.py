from django.test import TestCase

# Create your tests here.


import unittest

class TestProblem(unittest.TestCase):
    """
    ============== tesstcase brainstorm==========
    - url configuration for search in eccommerce portion appears BEFORE
    any slug related category/category item url config in the url_patterns
    list
    -item quantity in cart is natural number >=1 before calculating price
    of that item
    - cart must have at least one item to calculate price
    """
    def test_sample(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
