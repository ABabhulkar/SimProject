import unittest
import json
from server.backend.gameLogic.gameLogic import GameLogic

valid_json = '''[{"key":[0,0],"value":[3,3]},
                 {"key":[0,1],"value":[0,5]},
                 {"key":[1,0],"value":[5,0]},
                 
                 {"key":[1,1],"value":[1,1]}]'''


class GetFileNamesTest(unittest.TestCase):
    def __init__(self, method_name: str = "runTest") -> None:
        super().__init__(method_name)
        # Create an instance of the class containing the function
        self.gameLogic = GameLogic(result_metric=json.loads(valid_json),
                                   root_path='server\\test\\resources\\game_files\\')  # Replace 'MyClass' with the actual class name

    def test_get_file_names(self):
        """Tests that the function returns the expected list of file paths."""

        # This needs to be conditionally checked and then paths needs to be used
        # as windows and linux have different way to show paths.
        expected_result = [
            'server\\test\\resources\\game_files\\TestApp1',
            'server\\test\\resources\\game_files\\TestApp2'
        ]

        # Call the function and get the result
        actual_result = self.gameLogic.get_file_names()
        print(f'This is file paths: {actual_result}')

        # Assert that the actual result matches the expected result
        self.assertEqual(actual_result, expected_result)

    def test_empty_data(self):
        """
        Tests if the function returns empty dictionaries for empty input data.
        """
        empty_data = {}
        processed_data, total_scores = self.gameLogic._GameLogic__process_rounds(
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
        processed_data, total_scores = self.gameLogic._GameLogic__process_rounds(
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
            self.gameLogic._GameLogic__process_rounds(invalid_data)

    def test_invalid_move_combination1(self):
        """
        Tests if the function raises an error for invalid move combinations.
        """
        invalid_data = '''{"0": {"gameRound": {"P0": {"move": "0", "score": 0}, "P1": {"move": "1", "score": 0}}}, "1": {"gameRound": {"P0": {"move": "1", "score": 0}, "P1": {"move": "1", "score": 0}}}}'''

        with self.assertRaises(KeyError):
            self.gameLogic._GameLogic__process_rounds(json.loads(invalid_data))

    def test_calculate_result(self):
        """
        Tests if the function raises an error for invalid move combinations.
        """
        invalid_data = '''{"0": {"gameRound": {"P0": {"move": "0", "score": 0}, "P1": {"move": "1", "score": 0}}}, "1": {"gameRound": {"P0": {"move": "1", "score": 0}, "P1": {"move": "1", "score": 0}}}}'''
        with self.assertRaises(KeyError):
            self.gameLogic.calculate_result(invalid_data)

    def test_calculate_result(self):
        """
        Tests if the function raises an error for invalid move combinations.
        """
        valid_data   = '''{"1": {"gameRound": {"P0": {"move": 0, "score": 0}, "P1": {"move": 0, "score": 0}}}, "2": {"gameRound": {"P0": {"move": 1, "score": 0}, "P1": {"move": 0, "score": 0}}}}'''
        self.gameLogic.calculate_result(valid_data)

    def test_valid_json(self):
        expected_result = {(0, 0): [3, 3],
                           (0, 1): [0, 5],
                           (1, 0): [5, 0],
                           (1, 1): [1, 1]}

        j = json.loads(valid_json)
        result = self.gameLogic._GameLogic__parse_result_metric(j)
        self.assertEqual(result, expected_result)

    def test_empty_json(self):
        empty_json = '[]'
        expected_result = {}

        j = json.loads(empty_json)
        result = self.gameLogic._GameLogic__parse_result_metric(j)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
