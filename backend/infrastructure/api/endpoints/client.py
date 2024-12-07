from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from infrastructure.mongo.client_handler import register_client, get_client


router = APIRouter()

@router.post("/register")
async def upload_client_endpoint(
    email: str = Form(...),
    payment_address: str = Form(...),
    delivery_address: str = Form(...),
    nip: str = Form(...),
    orders: str = Form(...),
    password: str = Form(...),
    company_name: str = Form(...),
):
    try:
        
        client_id = register_client(email, payment_address, delivery_address, nip, orders, password, company_name)
        
        return {"info": f"Client '{email}' registered successfully", "client_id": client_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/clients/{client_id}")
async def get_client_endpoint(client_id: str):
    try:
        client = get_client(client_id)
        
        if not client:
            raise HTTPException(status_code=404, detail="Product not found")
        
        client_info = {
            "email": client["email"],
            "payment_address": client["payment_address"],
            "delivery_address": client["delivery_address"],
            "nip": client["nip"],
            "orders": client["orders"],
            "password": client["password"],
            "company_name": client["company_name"],
        }
        
        return {"client": client_info}
    
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
