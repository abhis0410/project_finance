from src.field_value import BoolField, OptionField

class TuitionConfig:
    title: str = "Tuition Credits (T2202)"
    enabled: BoolField = None
    mode: OptionField = None

    def __init__(self):
        self.enabled = BoolField(
            title="I want to claim tuition credits",
            required=True,
        )

        self.mode = OptionField(
            title="How will you provide tuition details?",
            options=["manual", "upload"],
            required=False,
        )

    def setter(self, enabled: bool, mode: str | None):
        self.enabled.set_value(enabled)
        self.mode.set_value(mode)
