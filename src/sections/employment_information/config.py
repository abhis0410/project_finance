from src.field_value import BoolField, IntField

class EmploymentConfig:
    title: str = "Employment Information"

    enabled: BoolField = None
    manual_count: IntField = None
    upload_count: IntField = None

    def __init__(self):
        self.enabled = BoolField(
            title="I have employment income",
            required=True
        )
        self.manual_count = IntField(
            title="Number of Employers for Manual Filling- T4 form",
            required=True,
            min_value=0,
            max_value=10,
        )
        self.upload_count = IntField(
            title="Number of T4 slips to upload",
            required=True,
            min_value = 0,
            max_value = 10,
        )

    def setter(self, enabled: bool, manual_count: int, upload_count: int):
        self.enabled.set_value(enabled)
        self.manual_count.set_value(manual_count)
        self.upload_count.set_value(upload_count)
