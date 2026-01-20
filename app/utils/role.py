# app/utils/role.py

from fastapi import Depends, HTTPException
from app.utils.dependencies import get_current_user

def role_required(role: str):
    def checker(user = Depends(get_current_user)):
        if user.role != role:
            raise HTTPException(status_code=403, detail="Not allowed")
        return user
    return checker
