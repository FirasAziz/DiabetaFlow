import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import pickle
from sqlalchemy import create_engine

username = "root"
password = "12345678"
host = "localhost"
port = "3306"
db_name = "diabetes_DB"
train_table = "diabetes"
test_table = "Diabetes_unseen"
model_file = "diabetes_model.pkl"

def run_ml():
    engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}")

    try:
        connection = engine.raw_connection() 
        df_train = pd.read_sql(f"SELECT * FROM {train_table}", con=connection)
        connection.close()  
        print(f"Training data loaded successfully from table '{train_table}'.")
    except Exception as e:
        print(f"Error loading training data: {e}")
        exit(1)

    feature_columns = df_train.columns[:-3].tolist()  
    target_column = "class"
    X = df_train[feature_columns]
    y = df_train[target_column]

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    print("training ")
    model = RandomForestClassifier(n_estimators=20, random_state=42)
    model.fit(X_train, y_train)

    print(f"Saving the model to {model_file}...")
    model_data = {
        "model": model,
        "feature_columns": feature_columns,
        "target_column": target_column,
    }
    with open(model_file, "wb") as file:
        pickle.dump(model_data, file)
    print("Model saved ")

    print("report on validation data")
    y_val_pred = model.predict(X_val)
    val_accuracy = accuracy_score(y_val, y_val_pred)
    print(f"Validation Accuracy: {val_accuracy:.2f}")
    print("Validation Classification Report:")
    print(classification_report(y_val, y_val_pred))

    try:
        connection = engine.raw_connection()  
        df_test = pd.read_sql(f"SELECT * FROM {test_table}", con=connection)
        connection.close()  
    except Exception as e:
        print(f"Error loading test data: {e}")
        exit(1)

    missing_cols = set(feature_columns) - set(df_test.columns)
    if missing_cols:
        raise ValueError(f"Missing columns in test data: {missing_cols}")

    X_test = df_test[feature_columns]
    y_test = df_test[target_column]

    print("report on test data...")
    y_test_pred = model.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    print(f"Test Accuracy: {test_accuracy:.2f}")
    print("Test Classification Report:")
    print(classification_report(y_test, y_test_pred))

    print(f"Predicted Classes : {y_test_pred}")
