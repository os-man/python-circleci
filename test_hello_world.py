 
import hello_world
import unittest


class TestHelloWorld(unittest.TestCase):
    def test_greeting_message(self):
       self.assertEqual(hello_world.hello(),'Hello, World!')
      

unittest.main()
        
        