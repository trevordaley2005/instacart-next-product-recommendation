# -*- coding: utf-8 -*-
"""
Config.py
---
projenin tüm dosya yollarını tek bir yerdeen konrol etmek için hazırlanmıştır.
proje'nin sürdürülebilirliği açısından SRC yapı sistemi tercih edilmiştir.

"""

import os
from pathlib import Path
import json

SRC_DIR = Path(__file__).parent
ROOT_DIR = SRC_DIR.parent

DATA_DIR = ROOT_DIR / "data" / "interim"
TRAIN_FEATURES_PATH = DATA_DIR / "train_features.csv"

DEMO_DATA_PATH = ROOT_DIR / "app" / "demo_data" / "sample_users.csv"

MODELS_DIR = ROOT_DIR / "models"
MODEL_PATH = MODELS_DIR / "lgb_model_final.pkl"
THRESHOLD_PATH = MODELS_DIR / "best_threshold.txt"
FEATURE_NAMES_PATH = MODELS_DIR / "feature_names.json"

DROP_COLS = [
    'user_id', 'product_id', 'order_id', 'reordered', 'eval_set', 
    'add_to_cart_order', 'up_orders', 'up_order_rate', 
    'up_last_order_number', 'up_orders_since_last', 
    'up_reorder_rate', 'up_cart_mean'
]

def load_feature_names():
    if not FEATURE_NAMES_PATH.exists():
        return []
    with open(FEATURE_NAMES_PATH, "r") as f:
        return json.load(f)

def load_threshold(default=0.40):
    if not THRESHOLD_PATH.exists():
        return default
    with open(THRESHOLD_PATH, "r") as f:
        try:
            return float(f.read().strip())
        except ValueError:
            return default