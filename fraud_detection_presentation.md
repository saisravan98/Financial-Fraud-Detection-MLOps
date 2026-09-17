<!-- .slide: data-background="#003366" -->
# 💳 Fraud Detection Using Machine Learning
### Interactive Presentation<br>Built with Streamlit & Scikit-Learn
---

## 🎯 Problem Statement
- Financial fraud causes billions in annual losses.
- Detecting fraud in real-time is a major challenge.
- Our goal: **Build a machine learning model** to identify fraudulent transactions.

---

## 📊 Dataset Overview
- Simulated dataset inspired by real banking transactions.
- **Key features**:
  - `type`, `amount`
  - `oldbalanceOrg`, `newbalanceOrig`
  - `oldbalanceDest`, `newbalanceDest`
- **Target**: `isFraud` (1 = fraud, 0 = normal)

---

## 📈 Class Imbalance Challenge
- Fraudulent transactions are **rare (< 0.1%)**
- Used techniques like:
  - SMOTE (oversampling minority class)
  - Class weights (Random Forest)

---

## 🧠 Model Pipeline
**Preprocessing:**
- Label encoding for `type`
- Feature normalization

**Algorithm:**
- ✅ Random Forest Classifier
- Ensemble method, handles imbalance & overfitting well

---

## 🧪 Evaluation Metrics
- **Accuracy**: ~99%
- **Precision**: ~90%
- **Recall**: ~95%
- **F1 Score**: Balanced metric for fraud detection
- **ROC AUC**: Measures classifier performance across thresholds

---

## 📺 Live App: Streamlit Interface
- Built with Python + Streamlit
- Inputs:
  - Transaction type, Amount
  - Sender & Receiver balances
- Output:
  - 🟢 Safe or 🔴 Fraudulent transaction

---

## 🧠 Feature Importance
Top contributing features:
- `amount`
- `oldbalanceOrg`
- `type`
- `newbalanceOrig`

Can be visualized using SHAP or LIME

---

## 🚧 Limitations & Future Work
**Limitations:**
- Simulated data ≠ real-world behavior
- Model may need tuning for deployment

**Future Enhancements:**
- Real-time API deployment
- Sequential model: LSTM for transaction history
- Anomaly detection + fraud prediction hybrid

---

## 📦 Project Assets
- Model Training: `Analysis_model.ipynb`
- UI: `fraud_detection.py`
- Trained model: `fraud_detection_pipeline.pkl`

---

## 🙋‍♂️ Questions?
**Let’s discuss:**
- Model choices
- Fraud-specific challenges
- Scalability options

---

<!-- .slide: data-background="#003366" -->
# Thank You! 🙌<br>
**Presented by: [Your Name]**