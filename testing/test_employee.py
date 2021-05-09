
import unittest
from unittest.mock import patch
from employee import Employee

class testEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')


    def setUp(self):
        self.emp_1 = Employee('John', 'Lennon', 50000)
        self.emp_2 = Employee('Paul', 'McCartney', 60000)

    def tearDown(self):
        pass

    def test_email(self):

        self.assertEqual(self.emp_1.email, 'john.lennon@email.com')
        self.assertEqual(self.emp_2.email, 'paul.mccartney@email.com')

        self.emp_1.first = 'Ringo'
        self.emp_2.first = 'George'

        self.assertEqual(self.emp_1.email, 'ringo.lennon@email.com')
        self.assertEqual(self.emp_2.email, 'george.mccartney@email.com')

    def test_apply_raise(self):

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Lennon/May')


            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False
            
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/McCartney/June')

            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()