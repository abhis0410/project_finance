from src.custom_form.response import CustomFormResponse
from src.sections.employment_information.response import EmploymentResponse
from src.sections.personal_information.response import PersonalInformationResponse


class FinalFormResponse:
    personal_information_response: PersonalInformationResponse
    employment_information_response: EmploymentResponse
    tuition_credits_information_response: None
    rental_information_response: None


    is_rendered: bool
    def __init__(self):
        self.personal_information_response = PersonalInformationResponse()
        self.employment_information_response = EmploymentResponse()
        self.is_rendered = False
