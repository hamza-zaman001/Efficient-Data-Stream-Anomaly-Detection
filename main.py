from data_stream import DataStream
from anomaly_detection import AnomalyDetector
from visualization import DataVisualizer

def main():
    stream = DataStream()
    detector = AnomalyDetector(window_size=100)
    visualizer = DataVisualizer()

    try:
        for data_point in stream.generate():
            if not visualizer.is_running:  # Check if the visualizer is running
                break
            anomaly = detector.process(data_point)
            visualizer.update(data_point, anomaly)

    except KeyboardInterrupt:
        print("Data stream interrupted, exiting...")
    finally:
        visualizer.close()  # Ensure proper exit on close

if __name__ == "__main__":
    main()
