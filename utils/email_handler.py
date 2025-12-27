import smtplib
import ssl
from typing import List, Optional, Union, Dict
from email.message import EmailMessage
from email.utils import make_msgid
from pathlib import Path
import mimetypes


class EmailAttachment:
    def __init__(
        self,
        filename: str,
        content: Union[bytes, Path],
        mime_type: Optional[str] = None,
    ):
        self.filename = filename
        self.content = content
        self.mime_type = mime_type


class EmailHandler:
    def __init__(
        self,
        smtp_host: str,
        smtp_port: int,
        username: str,
        password: str,
        use_tls: bool = True,
        use_ssl: bool = False,
        timeout: int = 30,
    ):
        if use_tls and use_ssl:
            raise ValueError("Only one of use_tls or use_ssl can be True")

        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        self.use_tls = use_tls
        self.use_ssl = use_ssl
        self.timeout = timeout

    def send(
        self,
        from_email: str,
        to_emails: List[str],
        subject: str,
        body_text: Optional[str] = None,
        body_html: Optional[str] = None,
        attachments: Optional[List[EmailAttachment]] = None,
        cc: Optional[List[str]] = None,
        bcc: Optional[List[str]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> None:
        if not to_emails:
            raise ValueError("At least one recipient is required")

        msg = EmailMessage()
        msg["From"] = from_email
        msg["To"] = ", ".join(to_emails)
        msg["Subject"] = subject

        if cc:
            msg["Cc"] = ", ".join(cc)

        if headers:
            for k, v in headers.items():
                msg[k] = v

        recipients = to_emails + (cc or []) + (bcc or [])

        # Message body
        if body_html and body_text:
            msg.set_content(body_text)
            msg.add_alternative(body_html, subtype="html")
        elif body_html:
            msg.add_alternative(body_html, subtype="html")
        elif body_text:
            msg.set_content(body_text)
        else:
            raise ValueError("Either body_text or body_html must be provided")

        # Attachments
        if attachments:
            for attachment in attachments:
                self._add_attachment(msg, attachment)

        # Send email
        self._send_message(msg, recipients)

    def _add_attachment(self, msg: EmailMessage, attachment: EmailAttachment):
        if isinstance(attachment.content, Path):
            data = attachment.content.read_bytes()
            filename = attachment.content.name
        else:
            data = attachment.content
            filename = attachment.filename

        mime_type, encoding = (
            attachment.mime_type,
            None,
        )

        if not mime_type:
            mime_type, encoding = mimetypes.guess_type(filename)

        if mime_type:
            maintype, subtype = mime_type.split("/", 1)
        else:
            maintype, subtype = "application", "octet-stream"

        msg.add_attachment(
            data,
            maintype=maintype,
            subtype=subtype,
            filename=filename,
        )

    def _send_message(self, msg: EmailMessage, recipients: List[str]) -> None:
        context = ssl.create_default_context()

        if self.use_ssl:
            with smtplib.SMTP_SSL(
                self.smtp_host,
                self.smtp_port,
                context=context,
                timeout=self.timeout,
            ) as server:
                server.login(self.username, self.password)
                server.send_message(msg, to_addrs=recipients)

        else:
            with smtplib.SMTP(
                self.smtp_host,
                self.smtp_port,
                timeout=self.timeout,
            ) as server:
                if self.use_tls:
                    server.starttls(context=context)

                server.login(self.username, self.password)
                server.send_message(msg, to_addrs=recipients)
