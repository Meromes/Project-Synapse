"""Example program to show how to read a multi-channel time series from LSL."""

from pylsl import StreamInlet, resolve_stream

# first resolve an EEG stream on the lab network
print("looking for EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])
samples = [0, 0, 0, 0, 0, 0, 0, 0]
while True:
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
    for i in range(0, 8):
        samples[i] = inlet.pull_sample()
    #print(sample1)
    #print(sample2)
    #print(sample3)
    #print(sample4)
    #print(sample5)
    #print(sample6)
    #print(sample7)
    #print(sample8)
    sums = [0, 0, 0, 0, 0, 0, 0, 0]
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    sum6 = 0
    sum7 = 0
    sum8 = 0
    for x in range(100, 125):
        sum1 += sample1[x]
        sum2 += sample2[x]
        sum3 += sample3[x]
        sum4 += sample4[x]
        sum5 += sample5[x]
        sum6 += sample6[x]
        sum7 += sample7[x]
        sum8 += sample8[x]
        for y in range(0, 8):
            sums[y] = samples[x]
    sum1 /= 25
    sum2 /= 25
    sum3 /= 25
    sum4 /= 25
    sum5 /= 25
    sum6 /= 25
    sum7 /= 25
    sum8 /= 25
    for j in range(0, 8):
        sums[j] /= 25
    print(sum1)
    print(sum2)
    print(sum3)
    print(sum4)
    print(sum5)
    print(sum6)
    print(sum7)
    print(sum8)

