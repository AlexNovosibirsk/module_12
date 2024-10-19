import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        cls.list_tests = []

    def setUp(self):
        self.Husain = Runner("Усэйн", 10)
        self.Andy = Runner("Андрей", 9)
        self.Nike = Runner("Ник", 3)

    def test_1(self):
        tournament = Tournament(90, self.Husain, self.Nike)
        self.all_results = tournament.start()
        self.list_tests.append(self.all_results)
        # сравниваются последний объект из all_results (брать по наибольшему ключу) и
        # предполагаемое имя последнего бегуна.
        max_num_keys = max(self.all_results.keys())
        self.assertTrue(self.all_results.get(max_num_keys) == self.Nike.name)  # Ник всегда последний.

    def test_2(self):
        tournament = Tournament(90, self.Andy, self.Nike)
        self.all_results = tournament.start()
        self.list_tests.append(self.all_results)
        max_num_keys = max(self.all_results.keys())
        self.assertTrue(self.all_results.get(max_num_keys) == self.Nike.name)

    def test_3(self):
        tournament = Tournament(90, self.Husain, self.Andy, self.Nike)
        self.all_results = tournament.start()
        self.list_tests.append(self.all_results)
        max_num_keys = max(self.all_results.keys())
        self.assertTrue(self.all_results.get(max_num_keys) == self.Nike.name)

    @classmethod
    def tearDownClass(cls):  # tearDownClass - метод, где выводятся all_results по очереди в столбец.
        d = {}
        for dict_ in cls.list_tests:
            for key, val in dict_.items():
                d[key] = val.name
            print(d)


if __name__ == "__main__":
    unittest.main()

# Вывод на консоль:
# {1: Усэйн, 2: Ник}
# {1: Андрей, 2: Ник}
# {1: Андрей, 2: Усэйн, 3: Ник}
# Ran 3 tests in 0.003s
# OK
