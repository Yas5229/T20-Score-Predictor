# T20 Totalitarian: Mastering Score Predictions

## Project Description

The **T20 World Cup Score Prediction** project aims to predict the total runs scored by a team in a T20 cricket match. The project leverages advanced machine learning techniques, with a focus on the XGBoost algorithm, to build an accurate and robust predictive model.

## Workflow Overview

### 1. Data Collection
Data is collected from various sources, including cricket databases, APIs, and websites. The dataset includes historical records of past T20 cricket matches, capturing information such as:
- Teams playing
- Runs scored
- Wickets taken
- Overs bowled
- Other relevant match details
**Data Set Link:** [Data Set Link](https://www.kaggle.com/datasets/veeralakrishna/cricsheet-a-retrosheet-for-cricket)

### 2. Data Preprocessing
The collected data is cleaned and preprocessed to ensure consistency and accuracy. Key preprocessing steps include:
- Handling missing values
- Encoding categorical variables
- Feature engineering to create new, relevant variables

### 3. Feature Selection
Relevant features are identified using:
- Correlation analysis
- Feature importance ranking
- Domain knowledge

These features are crucial for building a predictive model that captures the essential aspects of a T20 match.

### 4. Model Training
Multiple regression models are trained on the preprocessed data:
- **Linear Regression**
- **Random Forest Regression**
- **XGBRegressor** (XGBoost)

Among these, **XGBRegressor** is chosen as the primary model due to its superior performance in terms of the R² score. XGBoost, a gradient boosting algorithm that uses decision trees as base learners, is optimized for this task.

### 5. Model Evaluation
The performance of the models is evaluated

### Website Links
- **T20 Score Predictor Mobile:** [https://t-20-score-predictor-i3ge.onrender.com](https://t-20-score-predictor-i3ge.onrender.com)
- **T20 Score Predictor Desktop:** [https://t20-score-app-19.streamlit.app](https://t20-score-app-19.streamlit.app)
