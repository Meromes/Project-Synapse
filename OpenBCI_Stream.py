"""Example program to show how to read a multi-channel time series from LSL."""

from pylsl import StreamInlet, resolve_stream

# first resolve an EEG stream on the lab network
print("looking for EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])
rows, cols = (8, 125)
samples = [[0 for i in range(cols)] for j in range(rows)]

while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    for i in range(0, 8):
        samples[i], timestamp = inlet.pull_sample()
    sums = [0] * 8
    for y in range(0, 8):
        for x in range(100, 125):
            sums[y] += samples[y][x]
    for j in range(0, 8):
        sums[j] /= 25
        print(sums[j])
