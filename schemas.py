from pydantic import BaseModel, EmailStr, Field

class Employee(BaseModel):
    name: str = Field(..., example="John Doe")
    mail_id: EmailStr = Field(..., example="john.doe@example.com")
    salary: float = Field(..., example=50000.0)
    designation: str = Field(..., example="Software Engineer")
    contact_number: str = Field(..., example="123-456-7890")

class EmployeeInDB(Employee):
    id: str = Field(..., alias="_id")
