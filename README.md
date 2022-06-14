# insitustressprediction

The purpose of this project is to predict maximum horizontal stress magnitude (sigma SHmax) using machine learning model. In this project we use Random Forest Regressor.
The dataset used is a dataset from well lost hill. We use several independent variables to predict the value of Sigma SHmax, below are the variables used:

 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   DEPTH          167 non-null    int64  
 1   Pore_Pressure  167 non-null    int64  
 2   Density        167 non-null    float64
 3   dt_comp        167 non-null    int64  
 4   dt_shear       167 non-null    int64  
 5   Porosity       167 non-null    float64
 6   Vp             167 non-null    int64  
 7   Vs             167 non-null    int64  
 8   Edyn           167 non-null    int64  
 9   PR             167 non-null    float64
 10  Esta           167 non-null    int64  
 11  E'sta          167 non-null    int64 
