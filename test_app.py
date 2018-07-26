import os
import unittest
import app
 
 
 
class BasicTests(unittest.TestCase):
 
###############
#### tests ####
###############
 
    def test_main_page(self):
        self.app = app
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
 
if __name__ == "__main__":
    unittest.main()
