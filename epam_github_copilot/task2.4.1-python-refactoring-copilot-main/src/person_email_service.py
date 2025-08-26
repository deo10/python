import os
import smtplib

from fastapi.templating import Jinja2Templates
from .contact import Contact

templates = Jinja2Templates(directory='templates')


class EmailService:

    owner_name = os.getenv('OWNER_NAME')
    owner_email = os.getenv('OWNER_EMAIL')

    def greet_person(self, person):
        recipients = [contact for contact in person.contacts if contact.type == Contact.EMAIL_CONTACT_TYPE]

        body = self._prepare_email_body(person)
        self._send_email(
            recipients,
            body,
        )

    def _send_email(self, recipients, body):
        smtp = smtplib.SMTP(
            os.getenv('MAIL_HOST'),
            os.getenv('MAIL_PORT'),
        )
        smtp.starttls()

        smtp.login(
            os.getenv('MAIL_USERNAME'),
            os.getenv('MAIL_PASSWORD'),
        )
        smtp.sendmail(self.owner_email, recipients, body)
        smtp.quit()

    def _prepare_email_body(self, person):
        return templates.TemplateResponse('greeting.html', {'person': person})
