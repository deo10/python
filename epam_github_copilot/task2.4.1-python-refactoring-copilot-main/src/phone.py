class Phone:

    PRIMARY_PHONE_TYPE = 'PRIMARY'
    HOME_PHONE_TYPE = 'HOME'
    WORK_PHONE_TYPE = 'WORK'
    MOBILE_PHONE_TYPE = 'MOBILE'

    def __init__(self, type_, number):
        self.type_ = type_
        self.number = number

    def __str__(self):
        return f'{self.type_} {self.number}'
