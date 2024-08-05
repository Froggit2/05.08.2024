from Runner_3_1 import *
import unittest

is_frozen = True


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        walker = Runner("Billy")
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(is_frozen, reason="Тесты в этом кейсе заморожены")
    def test_run(self):
        rurunnern = Runner("Bob")
        for i in range(10):
            rurunnern.run()
        self.assertEqual(rurunnern.distance, 100)

    def test_challenge(self):
        walker = Runner("Billy")
        runner = Runner("Bob")
        for i in range(10):
            walker.walk()
            runner.run()
        self.assertNotEqual(walker.distance, runner.distance)
