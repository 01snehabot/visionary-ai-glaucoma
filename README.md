# visionary-ai-glaucoma
Explainable AI for early glaucoma detection using fundus images with deep learning and Grad-CAM.

# Explainable AI for Early Glaucoma Detection Using Fundus Imaging

## Team: VISIONARY AI
Members: Sneha Murugan, Ajrul Amin

## 📌 Overview
Glaucoma is a leading cause of irreversible blindness worldwide. Early detection is crucial, yet traditional diagnosis requires expert ophthalmologists and specialized equipment.

This project presents an **Explainable AI system** that detects glaucoma from retinal fundus images using deep learning techniques, while providing visual explanations to improve trust and interpretability.

## 🎯 Objectives
- Develop a deep learning model to classify glaucoma vs normal eyes  
- Apply explainable AI (Grad-CAM) to interpret model decisions  
- Demonstrate the potential of AI for early glaucoma screening  

## 🧠 Methodology
### 🔹 Model
- EfficientNet-B0 (Transfer Learning)
- Fine-tuned for binary classification

### 🔹 Preprocessing
- Image resizing (224 × 224)
- Normalization
- Data augmentation (rotation, flipping, brightness)

### 🔹 Explainability
- Grad-CAM used to highlight important regions (optic disc)


## 📊 Results
- **Accuracy:** ~90%  
- **AUC Score:** ~0.90  
- Strong classification performance between glaucoma and normal images  

### 🔍 Visual Outputs
- Confusion Matrix  
- ROC Curve  
- Grad-CAM Heatmaps (model focuses on optic disc region)  

## 💡 Impact
- Enables early detection of glaucoma  
- Supports screening in low-resource settings  
- Reduces dependency on specialist diagnosis  
- Improves accessibility of eye healthcare  

## ⚙️ How to Run

1. Install dependencies:
