import unittest

from src.backend.gameCore.utils.sharedData import SharedData, State


class SharedDataTests(unittest.TestCase):
    def test_init_sets_default_attributes(self):
        shared_data = SharedData()
        self.assertIsNone(shared_data.socket)
        self.assertFalse(shared_data.stopFlag)
        self.assertEqual(shared_data.state, State.Idle)
        self.assertIsNone(shared_data.msg)
        self.assertEqual(shared_data.clients, {})
        self.assertTrue(shared_data.isConnectionMonitor)
        self.assertEqual(shared_data.maxNumberOfRounds, 0)
        self.assertEqual(shared_data.roundNumber, -1)
        self.assertEqual(shared_data.rounds, {})
        self.assertEqual(shared_data.roundStatus, {})

    def test_init_data_resets_attributes(self):
        shared_data = SharedData()
        shared_data.socket = True  # Modify some attributes
        shared_data.stopFlag = True
        shared_data.state = State.StartGame

        shared_data.init_data()
        self.assertIsNone(shared_data.socket)
        self.assertFalse(shared_data.stopFlag)
        self.assertEqual(shared_data.state, State.Idle)

    def test_next_round_creates_new_round_if_not_exceeded(self):
        shared_data = SharedData()
        shared_data.maxNumberOfRounds = 3
        shared_data.roundNumber = 0
        result = shared_data.next_round("first", "second")
        self.assertTrue(result)
        self.assertEqual(shared_data.roundNumber, 1)
        self.assertIsNotNone(shared_data.rounds[1].gameObject.get('first'))
        self.assertIsNotNone(shared_data.rounds[1].gameObject.get('second'))

    def test_next_round_returns_false_if_max_rounds_reached(self):
        shared_data = SharedData()
        shared_data.maxNumberOfRounds = 2
        shared_data.roundNumber = 1
        result = shared_data.next_round("first", "second")
        self.assertFalse(result)
        self.assertEqual(shared_data.roundNumber, 2)  # Round number unchanged


if __name__ == '__main__':
    unittest.main(verbosity=2)
