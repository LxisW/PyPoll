class Helper:
    def __init__(self) -> None:
        pass

    @staticmethod
    def check_answers(answers):
        return all(answers[option] != "" for option in ["A", "B", "C", "D"])
