from typing import Callable, List
from functools import reduce


PatientData = dict


def calculate_risk_factor(data: PatientData) -> float:
    
    weights = {'glucose': 0.5, 'bmi': 0.3, 'age': 0.2}
    return sum(data.get(k, 0) * v for k, v in weights.items()) / 100


def process_batch_data(patients: List[PatientData]) -> List[float]:
    return list(map(calculate_risk_factor, patients))


def analyze_trends(results: List[float]) -> str:
    avg_risk = reduce(lambda x, y: x + y, results) / len(results)
    return "STABLE" if avg_risk < 0.6 else "VOLATILE"


sample_patients = [
    {'glucose': 120, 'bmi': 28, 'age': 45},
    {'glucose': 180, 'bmi': 34, 'age': 50}
]

print(f"Quant Analysis Results: {process_batch_data(sample_patients)}")

