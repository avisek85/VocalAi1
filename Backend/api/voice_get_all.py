from fastapi import APIRouter
from db import Ndatabase

router = APIRouter()

@router.get("/voices")
def get_all_voices():
    """
    Get all voices from the database.
    """
    
    voices = Ndatabase.get_all_voice_names()
    return {"voices": voices}