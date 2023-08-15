from SignalsAnalyzer import SignalsAnalyzer


file_path = "NEUR0000.DT8"
number_of_channels = 8
num_ADC_bits = 15
voltage_resolution = 10 ** -74.12
sample_per_sec = 4000
LOWCUT = 1
HIGHCUT = 100

data = SignalsAnalyzer.load_file_into_dataframe(file_path, number_of_channels, voltage_resolution, num_ADC_bits)
data = SignalsAnalyzer.convert_to_pandas_dataframe(data)
data = SignalsAnalyzer.zero_phase_bandpass(data, LOWCUT, HIGHCUT, sample_per_sec)
SignalsAnalyzer.plot_signals(data)
print(data)
