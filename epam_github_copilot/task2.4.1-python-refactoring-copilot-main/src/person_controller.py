from person import Person

from dotenv import load_dotenv
from fastapi import FastAPI, status
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from person_service import PersonService

load_dotenv(dotenv_path='../')
app = FastAPI()

templates = Jinja2Templates(directory='templates')
router = InferringRouter()


@cbv(router)
class PersonController:

    def __init__(self, person_service: PersonService):
        self.person_service = person_service

    @router.get("/contact")
    def find_by_email(self, request, response):
        email = request.query['email']

        if self.person_service.validation_service.is_valid_email(email):
            response.status_code = status.HTTP_200_OK
            return self.person_service.find_person_by_email(email)

        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            'message': 'Email is required',
            'details': 'email field is empty or invalid',
        }

    @router.post("/contact")
    def store_person(self, request, response):
        person = Person(
            request.body.firstName,
            request.body.lastName,
            request.body.birthday,
            request.body.addresses,
            request.body.phones,
            request.body.contacts,
        )

        if self.person_service.validation_service.validate_email(person):
            self.person_service.store(person)
            response.status_code = status.HTTP_200_OK

        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            'message': 'Email is required',
            'details': 'contact has no any valid emails',
        }

