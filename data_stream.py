import numpy as np
import random

class DataStream:
    def __init__(self, size=1000):
        self.size = size

    def generate(self):
        """Generate a data stream with seasonal patterns, trends, and random noise."""
        trend = 0  # Start with a baseline trend
        for i in range(self.size):
            # Introduce a linear trend over time
            trend += 0.05  # Gradual increase in trend
            
            # Create a seasonal component with noise
            seasonality = 5 * np.sin(i * 0.1) + 5 * np.cos(i * 0.2)  # Combining sine and cosine
            noise = random.gauss(0, 1)  # Gaussian noise
            spike = 0
            
            # Introduce random spikes as anomalies
            if random.random() < 0.05:  # 5% chance of anomaly
                spike = random.uniform(15, 30)  # Anomaly value
            
            # Yield the combined value of trend, seasonality, noise, and spikes
            yield trend + seasonality + noise + spike
