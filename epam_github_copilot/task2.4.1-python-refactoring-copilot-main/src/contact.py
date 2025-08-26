class Contact:

    EMAIL_CONTACT_TYPE = 'EMAIL'
    SKYPE_CONTACT_TYPE = 'SKYPE'
    FACEBOOK_CONTACT_TYPE = 'FACEBOOK'
    LINKEDIN_CONTACT_TYPE = 'LINKEDIN'

    def __init__(self, type_, contact):
        self.type_ = type_
        self.contact = contact

    def __str__(self):
        return f'{self.type_} {self.contact}'
