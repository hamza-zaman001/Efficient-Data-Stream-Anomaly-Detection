import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self):
        self.data = []
        self.anomalies = []
        self.is_running = True  # Running state flag

        plt.ion()  # Enable interactive mode for real-time updates
        self.fig, self.ax = plt.subplots(figsize=(12, 6))  # Create larger plot

        # Ensure graph closes properly
        self.fig.canvas.mpl_connect('close_event', self.on_close)

    def update(self, value, anomaly):
        self.data.append(value)
        if anomaly:
            self.anomalies.append(value)
        else:
            self.anomalies.append(None)

        self.ax.clear()  # Clear the plot

        # Plot data stream and anomalies
        self.ax.plot(self.data, label='Data Stream', color='blue')
        self.ax.scatter(range(len(self.anomalies)), self.anomalies, color='red', label='Anomalies')

        # Automatically adjust the y-limits to fit data
        self.ax.set_ylim(min(self.data) - 10, max(self.data) + 10)

        self.ax.legend()
        plt.draw()  # Redraw plot
        plt.pause(0.01)  # Real-time update

    def on_close(self, event):
        print("Output window closed, stopping the stream.")
        self.is_running = False  # Set running state to False
        plt.close(self.fig)  # Close the figure

    def close(self):
        plt.close(self.fig)
