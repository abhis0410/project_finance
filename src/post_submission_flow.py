from streamlit.runtime.uploaded_file_manager import UploadedFile

from src.final_response.response import FinalFormResponse
from utils.dict_to_html import dict_to_email_html
from utils.email_handler import EmailHandler


class PostSubmissionFlow:
    def __init__(self, final_form_response: FinalFormResponse):
        self.final_form_response = final_form_response

    def _get_subject(self):
        personal_info = self.final_form_response.personal_information_response
        first_name = personal_info.first_name.value
        last_name = personal_info.last_name.value

        return f"Tax Submission for {first_name} {last_name}"

    def _get_html_body(self):
        d = self.final_form_response.get_dict()
        return dict_to_email_html(d)

    def _get_attached_files(self, d, files=None):
        if files is None:
            files = []
        for key, value in d.items():
            if isinstance(value, dict):
                self._get_attached_files(value, files)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        self._get_attached_files(item, files)
                    elif isinstance(item, UploadedFile):
                        files.append(item)
            elif isinstance(value, UploadedFile):
                files.append(value)

    def _email_submission(self):
        subject = self._get_subject()
        body = self._get_html_body()
        to_email = self.final_form_response.personal_information_response.email.value
        files = []
        self._get_attached_files(self.final_form_response.get_dict(), files)

        email_handler = EmailHandler()
        email_handler.generate_mail(
            to_email=to_email,
            subject=subject,
            html_body=body,
            files=files,
        )
        email_handler.send()

    def execute(self):
        self._email_submission()

        return True