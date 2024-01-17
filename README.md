# Heart Disease Prediction

This repository provides a machine learning model for predicting heart disease using a Random Forest Classifier. Additionally, it includes a Streamlit web application for user-friendly interaction with the model.

## Dataset

The model is trained on the [Heart Disease dataset](https://www.kaggle.com/datasets/arezaei81/heartcsv) obtained from the UCI Machine Learning Repository. The dataset contains various clinical features that can be used to predict the presence of heart disease.


## Usage

1. **Train the Random Forest Classifier:**

   ```bash
   python train_model.py

This script loads the dataset, preprocesses the data, trains the Random Forest model, and saves the trained model to disk.

**Run the Streamlit web application**

    streamlit run app.py

## Input Patient Information:

Use the web interface to input patient information (features) and click the "Predict" button to get the model's prediction for the presence of heart disease.

## Contributing

Contributions to improve the model, add new features, or address issues are welcome. Fork the repository, make your changes, and submit a pull request.