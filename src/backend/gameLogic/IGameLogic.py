class IGameLogic:
    def __init__(self) -> None:
        pass

    def calculate_result(self, rounds: dict) -> None:
        """This function should calculate the result of the game
        """
        raise NotImplementedError("calculate_result not implemented")

    def get_file_names(self) -> list:
        """This function should return the names of files present at destination directory
        """
        raise NotImplementedError("get_file_names not implemented")

    def get_rounds_num(self) -> int:
        """This function should return number of rounds in a game
        """
        raise NotImplementedError("get_file_names not implemented")
