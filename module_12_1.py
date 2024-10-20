"""
Задача "Проверка на выносливость"

Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest.
В классе пропишите следующие методы:
test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual
сравните distance этого объекта со значением 50.

test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
Далее вызовите метод run у этого объекта 10 раз.
После чего методом assertEqual сравните distance этого объекта со значением 100.

test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
Далее 10 раз у объектов вызываются методы run и walk соответственно.
Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.
"""

import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("Runner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner_1 = Runner("Runner_1")
        runner_2 = Runner("Runner_2")
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == "__main__":
    unittest.main()
