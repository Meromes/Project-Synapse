"""Example program to show how to read a multi-channel time series from LSL."""

from pylsl import StreamInlet, resolve_stream

# first resolve an EEG stream on the lab network
print("looking for EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

#while True :
   # get a new sample (you can also omit the timestamp part if you're not
   # interested in it)
sample1, timestamp1 = inlet.pull_sample()
sample2, timestamp2 = inlet.pull_sample()
sample3, timestamp3 = inlet.pull_sample()
sample4, timestamp4 = inlet.pull_sample()
sample5, timestamp5 = inlet.pull_sample()
sample6, timestamp6 = inlet.pull_sample()
sample7, timestamp7 = inlet.pull_sample()
sample8, timestamp8 = inlet.pull_sample()
print(sample1)
print(sample2)
print(sample3)
print(sample4)
print(sample5)
print(sample6)
print(sample7)
print(sample8)
