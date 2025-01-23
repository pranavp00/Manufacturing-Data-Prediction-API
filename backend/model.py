from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, cohen_kappa_score
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.preprocessing import RobustScaler
import pandas as pd

def train_model(data: pd.DataFrame):
    # Separate features and target
    X = data.drop(columns=['Target'])
    y = data['Target']
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

    # Initialize variables for metrics
    acc_RF = []
    f1_scores = []
    kappa_scores = []

    # Stratified K-Fold cross-validation
    kf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    
    # Initialize the Random Forest classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    for fold, (trn_idx, val_idx) in enumerate(kf.split(X=X_train, y=y_train)):
        # Split into training and validation subsets
        X_trai = X_train.iloc[trn_idx, :]
        y_trai = y_train.iloc[trn_idx]
        X_valid = X_train.iloc[val_idx, :]
        y_valid = y_train.iloc[val_idx]

        # Scale the features using RobustScaler
        ro_scaler = RobustScaler()
        X_trai = ro_scaler.fit_transform(X_trai)
        X_valid = ro_scaler.transform(X_valid)
        X_test_scaled = ro_scaler.transform(X_test)

        # Train the model
        model.fit(X_trai, y_trai)

        # Predict on the validation and test sets
        y_valid_pred = model.predict(X_valid)
        y_test_pred = model.predict(X_test_scaled)

        # Calculate metrics
        acc_RF.append(model.score(X_valid, y_valid))  # Accuracy on validation set
        f1_scores.append(f1_score(y_valid, y_valid_pred, average='weighted'))  # F1-score
        kappa_scores.append(cohen_kappa_score(y_test, y_test_pred))  # Cohen's Kappa on test set

    # Average metrics across folds
    metrics = {
        "accuracy_mean": sum(acc_RF) / len(acc_RF),
        "f1_score_mean": sum(f1_scores) / len(f1_scores),
        "kappa_mean": sum(kappa_scores) / len(kappa_scores)
    }

    return model, metrics
def make_prediction(model, input_data):
    X_new = [[input_data['Air temperature'], input_data['Rotational speed'], input_data['Tool wear']]]
    prediction = model.predict(X_new)[0]
    confidence = max(model.predict_proba(X_new)[0])
    return prediction, confidence