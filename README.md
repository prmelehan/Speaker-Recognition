# Speaker-Recognition
Speaker Recognition using Deep Convolutional Neural Networks

### Background

When with friends, family, or others we know very well, figuring out who is speaking is no problem. If we know people well enough, we can even recognize them by their walk. For computers, this has been a challenge. To recognize what a computer is saying, that has been done, and very well I might add. Speaker Recognition is just another form of biometric authentication computers can use for security, or for convenience.

The goal of this project is to use CNNs in Keras to decipher who is talking when presented an audio clip. The accuracy doesn't have to be 100%, but the goal is to be able to detect who is speaking with a non random probability.


### Approach

To train the network, I will be using Keras, an open source high level Machine Learning framework with a tensorflow backend. I will take audio clips and convert them into spectrograms, and run convolution on those spectrograms to train the network.

Training & Testing:

`Audio File --> Spectrogram --> Network --> Classification`
