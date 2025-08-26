class Address:

    HOME_ADDRESS_TYPE = 'HOME'
    WORK_ADDRESS_TYPE = 'WORK'

    def __init__(self, type_, address1, address2, zip_, country):
        self.type_ = type_
        self.address1 = address1
        self.address2 = address2
        self.zip = zip_
        self.country = country

    def __str__(self):
        return f'{self.type_} {self.address1} {self.address2} {self.zip} {self.country}'
