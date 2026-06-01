
# HBV Liver Assessment Tool
APP Link : https://huggingface.co/spaces/parvez-kabir/HBV-Liver-Assessment-Tool

<img width="1027" height="728" alt="image" src="https://github.com/user-attachments/assets/6270032f-45bd-4d1b-9ee2-d8ab4a6656ca" />


HBV Liver Assessment Tool is an AI-powered diagnostic application designed to predict the severity of liver damage in patients with Hepatitis B Virus (HBV). By analyzing clinical biomarkers, this tool provides an automated assessment to assist healthcare professionals in making data-driven decisions.

## 🚀 Features
- **Accurate Predictions:** Utilizes a high-performance **CatBoost** machine learning model.
- **Clinical Integration:** Processes key medical indicators such as HBeAg, Anti-HBe, HCV, and HIV status.
- **Modern Interface:** Built with FastAPI and a clean, responsive UI for ease of use.
- **Fast Deployment:** Optimized for deployment on Hugging Face Spaces using Docker.

## 🛠 Tech Stack
- **Backend:** Python, FastAPI
- **Model:** CatBoost (Gradient Boosting)
- **Frontend:** HTML, Tailwind CSS, Jinja2
- **Deployment:** Docker, Hugging Face Spaces

## 📂 Project Structure
```text
├── app.py                # Main FastAPI application
├── 1hbv_model.cbm        # Trained CatBoost model
├── templates/            # HTML templates for the UI
├── Dockerfile            # Docker configuration for deployment
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
