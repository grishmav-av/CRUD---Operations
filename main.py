from fastapi import FastAPI, HTTPException, Depends
from .models import Employee, EmployeeInDB
from .crud import create_employee, get_employee, update_employee, delete_employee

app = FastAPI()

@app.post("/employee/", response_model=EmployeeInDB)
async def create_employee_endpoint(employee: Employee):
    return await create_employee(employee)

@app.get("/employee/{employee_id}", response_model=EmployeeInDB)
async def read_employee_endpoint(employee_id: str):
    employee = await get_employee(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.put("/employee/{employee_id}", response_model=EmployeeInDB)
async def update_employee_endpoint(employee_id: str, employee: Employee):
    updated_employee = await update_employee(employee_id, employee)
    if updated_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee

@app.delete("/employee/{employee_id}", response_model=dict)
async def delete_employee_endpoint(employee_id: str):
    if not await delete_employee(employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"msg": "Employee deleted successfully"}
