from src.sections.additional_income.response import AdditionalIncomeResponse
from src.sections.employment_information.response import EmploymentResponse
from src.sections.personal_information.response import PersonalInformationResponse
from src.sections.tuition_credits_information.response import TuitionCreditsInformationResponse


class FinalFormResponse:
    personal_information_response: PersonalInformationResponse
    employment_information_response: EmploymentResponse
    tuition_credits_information_response: TuitionCreditsInformationResponse
    additional_income_information_response: AdditionalIncomeResponse
    rental_information_response: None


    is_rendered: bool
    def __init__(self):
        self.personal_information_response = PersonalInformationResponse()
        self.employment_information_response = EmploymentResponse()
        self.tuition_credits_information_response = TuitionCreditsInformationResponse()
        self.additional_income_information_response = AdditionalIncomeResponse()
        self.is_rendered = False
