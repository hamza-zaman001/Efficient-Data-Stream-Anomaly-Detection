import numpy as np
from collections import deque
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self, window_size=100):
        self.window_size = window_size
        self.data_window = deque(maxlen=window_size)
        self.model = IsolationForest(contamination=0.1)  # Contamination set to 10%

    def process(self, value):
        self.data_window.append(value)

        if len(self.data_window) < self.window_size:
            return False  # Not enough data to make a decision yet

        # Train the Isolation Forest on the current data window
        data = np.array(self.data_window).reshape(-1, 1)
        self.model.fit(data)

        # Predict if the current point is an anomaly
        prediction = self.model.predict([[value]])

        # Return True if it's an anomaly, otherwise False
        return prediction[0] == -1
