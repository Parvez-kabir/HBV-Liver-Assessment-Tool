from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from catboost import CatBoostClassifier
import pandas as pd
import os
import uvicorn
import numpy as np

app = FastAPI()
templates = Jinja2Templates(directory="templates")

model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '1hbv_model.cbm')
model = CatBoostClassifier()
model.load_model(model_path)

feature_cols = ['Age', 'Gender', 'Blood Group', 'Total Anti-HBc', 'IgM Anti-HBc', 'HBeAg', 'Anti-HBe', 'HCV', 'HIV']

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"cols": feature_cols, "form_data": {}})

@app.post("/predict")
async def predict(request: Request):
    form_data = await request.form()
    # ইনপুট ডাটা তৈরি
    input_list = [float(form_data.get(c, 0)) for c in feature_cols]
    df = pd.DataFrame([input_list], columns=feature_cols)
    
    # প্রেডিকশন
    pred_result = model.predict(df)
    pred_class = int(np.array(pred_result).flatten()[0])
    
    # কনফিডেন্স স্কোর
    probs = model.predict_proba(df)[0]
    confidence = f"{float(np.max(probs) * 100):.2f}%"
    
    # ম্যাপিং
    severity_mapping = {0: "Mild Damage", 1: "Moderate Damage", 2: "Severe Damage"}
    
    return templates.TemplateResponse(request=request, name="index.html", context={
        "status": severity_mapping.get(pred_class, "Unknown"),
        "confidence": confidence,
        "form_data": form_data,
        "cols": feature_cols
    })

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8005)