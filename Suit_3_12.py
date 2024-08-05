import unittest
import Runner_3_run_test
import Runner_3_tour_test

runner = unittest.TestSuite()
runner.addTest(unittest.TestLoader().loadTestsFromTestCase(Runner_3_run_test.RunnerTest))
runner.addTest(unittest.TestLoader().loadTestsFromTestCase(Runner_3_tour_test.TournamentTest))

test = unittest.TextTestRunner(verbosity=2)
test.run(runner)

