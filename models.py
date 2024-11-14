from pydantic import BaseModel, EmailStr, Field
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class Employee(BaseModel):
    name: str = Field(..., example="John Doe")
    mail_id: EmailStr = Field(..., example="john.doe@example.com")
    salary: float = Field(..., example=50000.0)
    designation: str = Field(..., example="Software Engineer")
    contact_number: str = Field(..., example="123-456-7890")

class EmployeeInDB(Employee):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
