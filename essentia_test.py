
import essentia.standard
import essentia.streaming
from matplotlib import pyplot as plt
import sys
import multiprocessing

# algorithm:
#       -> BeatTrackerDegara
# audio -> window -> spectrum -> bark
#                             -> frequencyBand -> NoveltyCurve
#

# create algorithms
loader1 = essentia.standard.MonoLoader(filename = 'video/pink_floyd_high_hopes.mp4')
# loader2 = essentia.standard.MonoLoader(filename = 'video/pink_floyd_high_hopes.mp3')
window_alg = essentia.standard.Windowing(type = 'hann')
spectrum_alg = essentia.standard.Spectrum()
bark_alg = essentia.standard.BarkBands(numberBands = 24)
frequencyBands_alg = essentia.standard.FrequencyBands()
noveltyCurve_alg = essentia.standard.NoveltyCurve()
beatTracker_alg = essentia.standard.BeatTrackerDegara()
rhythmExtractor2013_alg = essentia.standard.RhythmExtractor2013()
# load audio
audio1 = loader1()
# audio2 = loader2()
print 'audio1 len:', audio1.shape


# calculate spectrums
bitrate = 44100
window_size = 2048
beginning = 0
step = 1024
spectrums = []
for i in range(len(audio1)/step):
    # print 'beginning:', beginning
    frame = audio1[beginning : beginning + window_size]
    # print 'frame len:', len(frame), '\n'

    # if end of file - break
    if len(frame) < window_size:
        break
    spec = spectrum_alg(window_alg(frame))
    spectrums.append(spec)
    beginning += step
print 'len spectums:', len(spectrums)

# calcutate BarkBands
barks = []
for spec in spectrums:
    bark = bark_alg(spec)
    # print 'bark len:', len(bark)

    barks.append(bark)
print 'len barks', len(barks)

# divide one bark for 3 parts
red_bark = []
green_bark = []
blue_bark = []
print 'bark:', barks[5]
for i, num in enumerate(barks[5]):
    print i, num
    if i % 3 == 0:
        red_bark.append(num)
    elif i % 3 ==1:
        green_bark.append(num)
    else:
        blue_bark.append(num)
print 'red:', red_bark
print 'green', green_bark
print 'blue', blue_bark

# sys.exit(0)
# show part of signal
# plt.plot(audio1[: 30*44100])
# plt.title('audio')
# plt.show()
# sys.exit(0)

# calculate BeatTrackerDegara
# beats = beatTracker_alg(audio1)
# print 'len beats', len(beats)
# print beats
# plt.plot(beats)
# plt.title('beats')
# plt.show()
# sys.exit(0)

# calculate rhythm extractor
# bpm, ticks, confidence,estimates, bpmIntervals = rhythmExtractor2013_alg(audio1)
# plt.plot(estimates)
# plt.title('estimates')
# plt.show()
# sys.exit(0)




# calculate FrequencyBands
# frequencyBands = []
# for spec in spectrums:
#     freqBand = frequencyBands_alg(spec)
#     frequencyBands.append(freqBand)
#     # print 'len freqband:', len(freqBand)
# print 'frequencyBands len: ', len(frequencyBands)



# clculate noveltyCurve
# novelties = []
# for freq in frequencyBands:
#     novelty = noveltyCurve_alg(freq)
#     noveltiss.append(novelty)
#     print 'len novelty', len(novelty)
# print 'novelties len', len(novelties)

# plt.plot(novelties[5])
# plt.plot(novelties[0])
# plt.title('NoveltyCurve')
# plt.show()

# sys.exit(0)

# dispaly several specs and barks
plt.subplot(2,1,1)
for i, spec in enumerate(spectrums):
    if i % 1000 ==0:
        plt.plot(spec)
plt.title('spec')

plt.subplot(2,1,2)
for i, bark in enumerate(barks):
    if i % 1000 ==0:
        plt.plot(bark)
plt.title('bark')

plt.show()

# exit immediettly
sys.exit(0)

# print len(audio[1*44100:2*44100])
plt.subplot(2,1,1)
plt.plot(audio1[:44100*30])
plt.title('audio1')

plt.subplot(2,1,2)
plt.plot(audio2[:44100*30])
plt.title('audio2')

plt.show()
