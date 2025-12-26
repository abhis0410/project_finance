class FinalResponse:

    def __init__(self):
        self.personal_information = None
        self.employer_information = []


    def clear(self):
        self.personal_information = None
        self.employer_information = []


    def ready_for_verification(self) -> bool:
        # TODO: Add more checks as needed
        check = self.personal_information is not None

        return check
