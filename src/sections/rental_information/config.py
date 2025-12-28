from src.field_value import BoolField, IntField
from utils.constants import Strings

class RentalInformationConfig:
    title: str = "Rental Information"
    disclaimer: str = Strings.RentalInformationConfigDisclaimer
    enabled: BoolField
    address_count: IntField

    def __init__(self):
        self.enabled = BoolField(
            title="I want to provide rental information",
            required=True
        )
        self.address_count = IntField(
            title="How many addresses",
            required=False,
            min_value=0,
            max_value=10,
        )

    def setter(self, enabled: bool, address_count: int | None = None):
        self.enabled.set_value(enabled)
        self.address_count.set_value(address_count)
