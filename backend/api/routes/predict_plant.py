from fastapi import APIRouter, Depends
from models.user import User
from typing import Annotated
from core.auth import get_current_active_user

import sys
import os

sys.path.append(os.path.abspath("..")) 

from mlmodel.xgb_model import predict_crop_probabilities

router = APIRouter()

@router.get("/api/predict_crops")
def predict_crops(nitrogen, phosphorus, potassium, temp_category, humidity, ph_category, rainfall, current_user: Annotated[User, Depends(get_current_active_user)]):
    return predict_crop_probabilities(nitrogen, phosphorus, potassium, temp_category, humidity, ph_category, rainfall)
    