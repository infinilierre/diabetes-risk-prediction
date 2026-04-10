import pandas as pd
import numpy as np

def check_model_drift(current_accuracy, threshold=0.85):
    """
    Monitor model performance. 
    Triggers an alert if accuracy falls below the defined threshold.
    """
    if current_accuracy < threshold:
        print(f"🚨 ALERT: Model performance is critical! Current Accuracy: {current_accuracy}")
        print("💡 RECOMMENDATION: Triggering automated retraining pipeline due to Data Drift.")
        return True
    else:
        print(f"✅ System Stable: Model performance is within limits. Current Accuracy: {current_accuracy}")
        return False


test_accuracy = 0.82  
check_model_drift(test_accuracy)

