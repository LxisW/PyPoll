class Helper:
    def __init__(self) -> None:
        pass

    @staticmethod
    def check_answers(answer_A, answer_B, answer_C, answer_D):
        success = False
        if answer_A != "" and answer_B != "" and answer_C != "" and answer_D != "":
            success = True
        return success
