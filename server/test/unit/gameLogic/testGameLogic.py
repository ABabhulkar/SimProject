import unittest
import json
from server.backend.gameLogic.gameLogic import GameLogic


class GetFileNamesTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        # Create an instance of the class containing the function
        self.gameLogic = GameLogic()  # Replace 'MyClass' with the actual class name

    def test_get_file_names(self):
        """Tests that the function returns the expected list of file paths."""

        expected_result = [
            '/mnt/d/Projects/PythonWS/SimProject/prisonerD/src/clientApp.py',
            '/mnt/d/Projects/PythonWS/SimProject/prisonerD/src/clientApp.py'
        ]

        # Call the function and get the result
        actual_result = self.gameLogic.get_file_names()

        # Assert that the actual result matches the expected result
        self.assertEqual(actual_result, expected_result)

    def test_empty_data(self):
        """
        Tests if the function returns empty dictionaries for empty input data.
        """
        empty_data = {}
        processed_data, total_scores = self.gameLogic.process_rounds(
            empty_data)
        self.assertEqual(processed_data, {})
        self.assertEqual(total_scores, {"P0": 0, "P1": 0})

    def test_valid_data(self):
        """
        Tests if the function processes valid data correctly based on the score table.
        """
        valid_data = {
            "1": {
                "gameRound": {
                    "P0": {"move": 0, "score": 0},
                    "P1": {"move": 0, "score": 0},
                }
            },
            "2": {
                "gameRound": {
                    "P0": {"move": 1, "score": 0},
                    "P1": {"move": 0, "score": 0},
                }
            }
        }
        expected_processed_data = {
            "1": {
                "gameRound": {
                    "P0": {"move": 0, "score": 3},
                    "P1": {"move": 0, "score": 3},
                }
            },
            "2": {
                "gameRound": {
                    "P0": {"move": 1, "score": 5},
                    "P1": {"move": 0, "score": 0},
                }
            }
        }
        expected_total_scores = {"P0": 8, "P1": 3}
        processed_data, total_scores = self.gameLogic.process_rounds(
            valid_data)
        self.assertEqual(processed_data, expected_processed_data)
        self.assertEqual(total_scores, expected_total_scores)

    def test_invalid_move_combination(self):
        """
        Tests if the function raises an error for invalid move combinations.
        """
        invalid_data = {
            "1": {
                "gameRound": {
                    "P0": {"move": 2, "score": 0},  # Invalid move
                    "P1": {"move": 0, "score": 0},
                }
            }
        }
        with self.assertRaises(KeyError):
            self.gameLogic.process_rounds(invalid_data)

    def test_invalid_move_combination1(self):
        """
        Tests if the function raises an error for invalid move combinations.
        """
        invalid_data = '''{"0": {"gameRound": {"P0": {"move": "0", "score": 0}, "P1": {"move": "1", "score": 0}}}, "1": {"gameRound": {"P0": {"move": "1", "score": 0}, "P1": {"move": "1", "score": 0}}}}'''

        with self.assertRaises(KeyError):
            self.gameLogic.process_rounds(json.loads(invalid_data))

    def test_calculate_result(self):
        """
        Tests if the function raises an error for invalid move combinations.
        """
        invalid_data = '''{"0": {"gameRound": {"P0": {"move": "0", "score": 0}, "P1": {"move": "1", "score": 0}}}, "1": {"gameRound": {"P0": {"move": "1", "score": 0}, "P1": {"move": "1", "score": 0}}}}'''
        with self.assertRaises(KeyError):
            self.gameLogic.calculate_result(invalid_data)


if __name__ == '__main__':
    unittest.main(verbosity=2)
