#Import unittest
import unittest
import opcoes_modelo_binomial as opcoes

#Define a class for the test
class TestPrecoCall(unittest.TestCase):
    #Define a test case
    def test_preco_call(self):
        #Define the expected result
        expected = 0.9628
        #Define the actual result
        actual = opcoes.preco_call(S=8.5, K=10, r=0.1, sigma=0.35, T=1, n=300)
        #Assert that the expected and actual results are equal
        self.assertEqual(expected, round(actual,4))

#Run the test
unittest.main(argv=[''], verbosity=2, exit=False)


