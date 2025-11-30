# -*- coding: utf-8 -*-

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.inference import InstacartPredictor
from src import config

app = FastAPI(title="Instacart Prediction API")
predictor = InstacartPredictor()

demo_df = pd.DataFrame()
if config.DEMO_DATA_PATH.exists():
    try:
        demo_df = pd.read_csv(config.DEMO_DATA_PATH)
    except:
        pass

class PredictionRequest(BaseModel):
    features: dict

@app.get("/")
def home():
    return {"status": "active"}

@app.post("/predict")
def predict_manual(request: PredictionRequest):
    try:
        return predictor.predict(request.features)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/demo_users")
def get_demo_users():
    if demo_df.empty:
        return []
    return sorted(demo_df['user_id'].unique().tolist())

@app.get("/get_user_data/{user_id}")
def get_user_data(user_id: int):
    if demo_df.empty:
        raise HTTPException(status_code=404, detail="No demo data")
    
    user_rows = demo_df[demo_df['user_id'] == user_id]
    if user_rows.empty:
        raise HTTPException(status_code=404, detail="User not found")
    
    sample_row = user_rows.iloc[0].to_dict()
    features = {k: v for k, v in sample_row.items() if k not in config.DROP_COLS}
    
    return {
        "user_id": user_id,
        "product_id": sample_row.get('product_id', 0),
        "features": features
    }