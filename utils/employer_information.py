



class EmployerInformation:
    def __init__(self, manual_entry_count, file_upload_count):
        self.manual_entry_count = manual_entry_count
        self.file_upload_count = file_upload_count

        self.is_completed = False
        self.employers = []


    def add_manual_entry(self, entry):
