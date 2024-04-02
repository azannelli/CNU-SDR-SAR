% Parameters
center_frequency = 900e6;  % Center frequency in Hz
chirp_frequency = 0.75e6;  % Chirp frequency in Hz
chirp_period = 1e-3;       % Chirp period in seconds
sampling_rate = 195312;    % Sampling rate in Hz


% Load data from file
fid = fopen('New.dat', 'r');
data = fread(fid, 'float32');
fclose(fid);

% Number of samples
num_samples = length(data);

% Time vector
time = (0:num_samples-1) / sampling_rate;

% Generate chirp signal
t_chirp = 0:1/sampling_rate:chirp_period;
chirp_signal = exp(1j * 2 * pi * (chirp_frequency * t_chirp + ...
                  (chirp_frequency / chirp_period / 2) * t_chirp.^2));

% Matched filter
matched_filter = conj(fliplr(chirp_signal));

% Apply matched filter
filtered_data = conv(data, matched_filter, 'same');

% Low-pass filtering
cutoff_frequency = 0.1 * chirp_frequency; % Adjust cutoff frequency as needed
[b, a] = butter(5, cutoff_frequency/(sampling_rate/2), 'low');
filtered_data = filter(b, a, filtered_data);

% Calculate magnitude of filtered signal
magnitude = abs(filtered_data);

% Perform FFT
fft_data = fftshift(fft(filtered_data));

% Frequency vector
f = linspace(-sampling_rate/2, sampling_rate/2, length(filtered_data));

% Find peaks in the FFT data
[~, locs] = findpeaks(abs(fft_data), 'MinPeakHeight', max(abs(fft_data))/2);

% Plot recevied signal
subplot(4,1,1);
plot(time, real(data));
xlabel('Time (s)');
ylabel('Amplitude');
title('Recevied Signal');

% Plot FFT magnitude
subplot(4,1,2);
plot(f, abs(fft_data));
hold on;
plot(f(locs), abs(fft_data(locs)), 'ro');
hold off;
xlabel('Frequency (Hz)');
ylabel('Magnitude');
title('FFT of Filtered Signal');
grid on;

% Plot mag vs time
subplot(4,1,3);
plot(time, magnitude);
xlabel('Time (s)');
ylabel('Magnitude');
title('Magnitude vs Time');
grid on;

% Object detection based on magnitude threshold
magnitude_threshold = 0.5 * max(magnitude); % CAN BE CHANGED BASED ON BACKGROUND SIGNAL RETURN
detected_indices = find(magnitude > magnitude_threshold);

% Plot magnitude vs time
subplot(4,1,4);
plot(time, magnitude);
hold on;
plot(time(detected_indices), magnitude(detected_indices), 'ro');
hold off;
xlabel('Time (s)');
ylabel('Magnitude');
title('Magnitude vs Time W/ Object Detection');
grid on;

% Calculating the dections
speed_of_light = 3e8; % Speed of light in m/s
detected_time = time(detected_indices);
ranges = detected_time * speed_of_light / 2;

disp('Ranges of detected objects (in meters):');
disp(ranges);