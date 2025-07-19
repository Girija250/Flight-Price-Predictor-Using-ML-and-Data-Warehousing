import pandas as pd  
import pickle  
from sklearn.model_selection import train_test_split  
from sklearn.ensemble import RandomForestRegressor  

# Load Dataset  
df = pd.read_csv("../data/flight_prices_cleaned.csv")

# Encode Categorical Data  
df['Airline'] = df['Airline'].astype('category').cat.codes  
df['Source'] = df['Source'].astype('category').cat.codes  
df['Destination'] = df['Destination'].astype('category').cat.codes  

# Select Features & Target  
X = df[['Airline', 'Source', 'Destination', 'Stops', 'Duration']]  
y = df['Price']  

# Split Data  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  

# Train Model  
model = RandomForestRegressor(n_estimators=100)  
model.fit(X_train, y_train)  

# Save Model  
with open('../models/flight_model.pkl', 'wb') as f:  
    pickle.dump(model, f)  

print("✅ Model Trained & Saved Successfully!")  
 
