from src.field_value import BoolField, IntField
from utils.constants import Strings

class AdditionalIncomeConfig:
    title: str = "Additional Information"
    disclaimer: str = Strings.AdditionalIncomeConfigDisclaimer
    enabled: BoolField
    income_count: IntField

    def __init__(self):
        self.enabled = BoolField(
            title="I have additional income to report",
            required=True
        )
        self.income_count = IntField(
            title="How many additional incomes",
            required=False,
            min_value=0,
            max_value=10,
        )

    def setter(self, enabled: bool, income_count: int | None = None):
        self.enabled.set_value(enabled)
        self.income_count.set_value(income_count)
