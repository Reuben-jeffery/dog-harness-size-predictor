🐶 Dog Harness Size Predictor

An end-to-end Machine Learning project that predicts the correct harness size for dogs based on their physical attributes and activity level.

This repo includes:

Jupyter notebooks for data preprocessing, training, and evaluation.

A trained Random Forest pipeline saved as a reusable model.

An interactive Streamlit app for real-time predictions (both manual input & CSV upload).

Deployment-ready structure (separating experimentation from production).

Project Structure

dog-harness-size-predictor/
│
├── app/                     # Deployment-ready app
│   ├── app.py
│   └── streamlit_app.py
│
├── models/                  # Trained ML models
│   └── rf_harness_model.pkl
│
├── notebooks/               # Training & experimentation
│   ├── data/                # Raw & processed datasets
│   │   └── new_dogs.csv
│   │
│   ├── EDA_and_Cleaning.ipynb
│   ├── Modeling.ipynb
│   └── Predictions_and_Deployment.ipynb
│
├── scripts/                 # Utility scripts
│   ├── generate_dataset.py
│   └── simulate_stream.py
│
├── config.py                # Project configuration
├── requirements.txt         # Dependencies for deployment
├── .gitignore               # Keeps repo clean
├── LICENSE                  # Project license (e.g., MIT)
└── README.md                # Project overview (this file)

Workflow

1️⃣ Data Preprocessing (EDA_and_Cleaning.ipynb)

Loaded raw dog data.

Handled missing values, duplicates, and inconsistent columns.

Normalized categorical values (lowercased breeds, activity levels).

Split into features (X) and target (y).

2️⃣ Model Training (Modeling.ipynb)

Defined numeric & categorical feature pipelines:

StandardScaler for numeric columns.

OneHotEncoder for categorical columns.

Trained a Random Forest Classifier using a pipeline.

Evaluated accuracy, confusion matrix, and classification report.

Tuned hyperparameters.

Saved the final pipeline into models/rf_harness_model.pkl.

3️⃣ Predictions (Predictions_and_Deployment.ipynb)

Loaded the trained model.

Predicted harness sizes for new dogs (new_dogs.csv).

Saved results to new_dogs_predictions.csv.

Visualized prediction outputs.

4️⃣ Deployment App (app/app.py)

Built with Streamlit.

Supports:

Manual Input Form → Enter breed, weight, chest, neck, boot size, age, and activity.

CSV Upload → Upload multiple dogs’ details and get bulk predictions.

Download results as a CSV.

Deployment

The app is deployed on Streamlit Cloud:
Live App Link
 (replace with your actual link once deployed)

Running Locally

1. Clone the repository

git clone https://github.com/your-username/dog-harness-size-predictor.git
cd dog-harness-size-predictor

2. Create & activate virtual environment

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the Streamlit app
streamlit run app/app.py

Example Prediction

Input:

Breed: Labrador

Weight: 30kg

Chest: 60cm

Neck: 35cm

Boot size: 5

Age: 3 years

Activity: High

Output:
Predicted Harness Size: M

Tech Stack

Python 3.10

pandas, numpy → Data processing

scikit-learn → ML pipeline, Random Forest

matplotlib, seaborn → Visualizations

joblib → Model persistence

Streamlit → App & deployment

Key Highlights

End-to-end ML pipeline (data → model → deployment).

Clean project structure (separating notebooks from app).

Recruiter-friendly app: easy to test predictions.

Streamlit deployment link (plug & play demo).

Author

Reuben Jeffery Ofuafo (CodeRonin)

Electrical Engineer turned Data/ML Engineer.

Passionate about ML deployment, pipelines, and data engineering.

🔗 LinkedIn: www.linkedin.com/in/jeffery-ofuafo-reuben-79bba5165
 
 | GitHub: https://github.com/Reuben-jeffery 

This project demonstrates how to build, train, and deploy a real ML model while keeping a clean, production-ready structure for recruiters and hiring managers.

License

This project is licensed under the MIT License – see the LICENSE
 file for details.

You are free to use, modify, and distribute this project, provided proper attribution is given.