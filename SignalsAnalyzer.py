import numpy as np
import pandas as pd
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt


class SignalsAnalyzer:

    @staticmethod
    def load_file_into_dataframe(file_name, number_of_channels, voltage_resolution, num_ADC_bits):
        data = np.fromfile(file_name, dtype=np.uint16)
        data = np.reshape(data, (number_of_channels, -1), order='F')
        data = np.multiply(voltage_resolution, (data - np.float_power(2, num_ADC_bits - 1)))
        return data

    @staticmethod
    def convert_to_pandas_dataframe(data):
        return pd.DataFrame(data.T)

    @staticmethod
    def help_zero_phase_bandpass(lowcut, highcut, fs, order=4):
        nyquist = 0.5 * fs
        low = lowcut / nyquist
        high = highcut / nyquist
        b, a = butter(order, [low, high], btype='band')
        return b, a

    @staticmethod
    def zero_phase_bandpass(data, lowcut, highcut, fs, order=4):
        filter_data = pd.DataFrame()
        for column in data.columns:
            b, a = SignalsAnalyzer.help_zero_phase_bandpass(lowcut, highcut, fs, order=order)
            y = filtfilt(b, a, data[column])
            filter_data[column] = y

        return filter_data

    @staticmethod
    def plot_signals(df):
        df.plot(subplots=True, layout=(len(df.columns), 1), figsize=(10, 10))
        plt.show()

