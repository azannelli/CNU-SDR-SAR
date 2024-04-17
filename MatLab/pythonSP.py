import numpy as np
import matplotlib.pyplot as plt

# Constants and radar parameters
c = 3e8  # Speed of light (m/s)
fc = 900e6  # Center frequency (Hz)
bandwidth = 195.312e3  # Bandwidth (Hz)
sample_rate = 195.312e3  # Sample rate (Hz)
v = 10  # Radar velocity (m/s)
R0 = 1000  # Range to scene center (m)

# Example variables - replace with your actual values
num_samples = 1024  # Number of samples per sweep
num_sweeps = 100  # Number of sweeps in the data
sweep_time = num_samples / sample_rate  # Time for one sweep

# Load data from file
def load_data(filename):
    data = np.fromfile(filename, dtype=np.complex64)
    # Reshape data into a matrix where each row is one sweep
    data = data.reshape((num_sweeps, num_samples))
    return data

# Process FMCW radar data
def process_fmcw_data(data, bandwidth, sweep_time, sample_rate):
    # Perform FFT on each sweep to get the beat frequencies
    fft_data = np.fft.fft(data, axis=1)
    # Calculate frequency bins
    freq_bins = np.fft.fftfreq(num_samples, 1/sample_rate)
    # Calculate the range from the beat frequencies
    ranges = c * freq_bins / (2 * bandwidth)
    return fft_data, ranges

# Backprojection algorithm for FMCW radar
def backprojection(fft_data, ranges, v, sweep_time, R0, fc):
    Nx, Ny = 512, 512  # Image dimensions
    image = np.zeros((Nx, Ny), dtype=np.complex64)
    
    # Define the image grid
    x = np.linspace(-R0, R0, Nx)
    y = np.linspace(-R0, R0, Ny)
    X, Y = np.meshgrid(x, y)
    
    # Process each sweep
    for sweep_idx in range(fft_data.shape[0]):
        # Calculate radar position for the current sweep
        radar_position = sweep_idx * sweep_time * v
        
        for range_idx, R in enumerate(ranges):
            # Calculate the range from the radar to each pixel
            range_to_pixel = np.sqrt((X - radar_position)**2 + Y**2 + R**2)
            # Find the pixel that corresponds to the current range bin
            pixel_idx = np.argmin(np.abs(range_to_pixel - R))
            # Update the SAR image with the backprojected signal
            image[pixel_idx] += fft_data[sweep_idx, range_idx]
    
    return image

# Load and process data
filename = 'path_to_your_fmcw_data.dat'
data = load_data(filename)
fft_data, ranges = process_fmcw_data(data, bandwidth, sweep_time, sample_rate)
sar_image = backprojection(fft_data, ranges, v, sweep_time, R0, fc)

# Convert to magnitude and display
magnitude_image = np.abs(sar_image)
plt.imshow(20 * np.log10(magnitude_image), extent=(-R0, R0, -R0, R0))
plt.colorbar()
plt.show()