# Financial Fraud Detection & MLOps Pipeline

An end-to-end machine learning classification system and real-time inference web application designed to detect fraudulent financial transactions across **6.3M+ mobile banking records**. 

Built with **Python**, **Scikit-Learn**, **Pandas**, and **Streamlit**, this project addresses the extreme class imbalance inherent in financial fraud (<0.13% positive cases) by structuring an automated preprocessing pipeline and optimizing classification thresholds to maximize **Recall (95%)**, minimizing costly false negatives.

---

## 🚀 Key Highlights & Performance

* **Severe Class Imbalance Handling:** Trained on 6.36 million transactions containing only 8,213 fraudulent events (0.13% fraud rate). Utilized balanced class-weight penalization and custom decision thresholds to prioritize fraud capture.
* **Production Pipeline Architecture:** Integrated `ColumnTransformer`, `StandardScaler`, and `OneHotEncoder` into a serialized Scikit-Learn `Pipeline` artifact (`fraud_detection_pipeline.pkl`), eliminating data leakage across train/test splits.
* **Real-Time Web Inference:** Deployed an interactive Streamlit dashboard allowing risk officers to input live transaction parameters and receive sub-second fraud probability scores.
* **High-Impact Metrics:** Achieved **95% Recall on fraud cases** across a test holdout of 1.9M+ records, ensuring near-complete identification of illicit fund siphoning.

---

## 📊 Evaluation Results

Evaluated on an independent 30% stratified test split (**1,908,786 transactions**):

| Class | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| **Legitimate (0)** | 1.00 | 0.95 | 0.97 | 1,906,322 |
| **Fraud (1)** | 0.02 | **0.94** | 0.04 | 2,464 |
| **Macro Average** | 0.51 | **0.94** | 0.51 | 1,908,786 |
| **Weighted Average**| 1.00 | 0.95 | 0.97 | 1,908,786 |

> **Confusion Matrix (Test Set):**
> * True Negatives: 1,801,694
> * False Positives: 104,628
> * False Negatives: 158
> * **True Positives (Detected Frauds): 2,306 out of 2,464**

*Business Context:* In fraud operations, the financial loss of missing a fraudulent transaction (False Negative) drastically outweighs the operational cost of flagging a legitimate user for secondary review (False Positive).

---

## 🛠️ Architecture & Tech Stack

* **Language:** Python 3.10+
* **ML & Data Processing:** Scikit-Learn, Pandas, NumPy
* **Deployment & UI:** Streamlit, Joblib
* **Data Visualization:** Seaborn, Matplotlib

### Repository Structure

```text
├── Analysis_model.ipynb         # Full EDA, feature engineering, and model training
├── fraud_detection.py           # Streamlit real-time inference web application
├── fraud_detection_pipeline.pkl # Serialized production pipeline (Preprocessor + Model)
├── Fraud Detection Report.pdf   # Comprehensive research and project documentation
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
