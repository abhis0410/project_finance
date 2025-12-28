from src.field_value import BoolField


class PersonalInformationConfig:
    title: str = "Personal Information"
    enabled: BoolField

    def __init__(self):
        self.enabled = BoolField(
            title="I want to provide personal information",
            required=True
        )

    def setter(self, enabled: bool):
        self.enabled.set_value(enabled)