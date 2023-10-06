from Exercise_2 import self_service
import unittest

class TestSelfService(unittest.TestCase):
    
    def test_01_n_is_1_then_the_time_required_is_the_sum_of_the_times(self):
       self.assertEqual(self_service([5,3,4],1), 12)
       
    def test_02_n_is_3_and_the_list_is_3_then_the_time_required_is_the_longest_time(self):
       self.assertEqual(self_service([5,3,4],3), 5)
       
    def test_03_n_is_2_and_the_list_is_4_then_the_time_required_is_acumulative_and_return_the_max_value(self):
       self.assertEqual(self_service([10,2,3,3],2), 10)
      
    def test_04_n_is_2_and_the_list_is_3_then_the_time_required_is_acumulative_and_return_the_max_value(self):
       self.assertEqual(self_service([2,3,10],2), 12) 
       
if __name__ == '__main__':
    unittest.main()