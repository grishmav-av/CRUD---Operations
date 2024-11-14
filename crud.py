from .database import collection
from .models import Employee, EmployeeInDB
from bson import ObjectId

async def create_employee(employee: Employee) -> EmployeeInDB:
    employee_dict = employee.dict()
    result = await collection.insert_one(employee_dict)
    employee_dict["_id"] = str(result.inserted_id)
    return EmployeeInDB(**employee_dict)

async def get_employee(employee_id: str) -> EmployeeInDB:
    employee = await collection.find_one({"_id": ObjectId(employee_id)})
    if employee:
        employee["_id"] = str(employee["_id"])
        return EmployeeInDB(**employee)
    return None

async def update_employee(employee_id: str, employee: Employee) -> EmployeeInDB:
    await collection.update_one(
        {"_id": ObjectId(employee_id)}, {"$set": employee.dict()}
    )
    updated_employee = await get_employee(employee_id)
    return updated_employee

async def delete_employee(employee_id: str) -> bool:
    result = await collection.delete_one({"_id": ObjectId(employee_id)})
    return result.deleted_count > 0
