from dataclasses import dataclass

from src.sections.personal_information.config import PersonalInformationConfig
from src.sections.employment_information.config import EmploymentConfig
from src.sections.tuition_credits_information.config import TuitionConfig
from src.sections.rental_information.config import RentalInformationConfig
from src.sections.additional_income.config import AdditionalIncomeConfig


class CustomFormResponse:
    personal_information_config: PersonalInformationConfig
    employment_config: EmploymentConfig
    tuition_config: TuitionConfig
    rental_config: RentalInformationConfig
    additional_income_config: AdditionalIncomeConfig


    def __init__(self):
        self.personal_information_config = PersonalInformationConfig()
        self.employment_config = EmploymentConfig()
        self.tuition_config = TuitionConfig()
        self.rental_config = RentalInformationConfig()
        self.additional_income_config = AdditionalIncomeConfig()