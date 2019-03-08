# Sequence to Sequence Models
## Machine Translation - Basic Model vs. Beam Search
### Basic Model
The most basic model for machine translation is an RNN encoder followed by an RNN decoder architecture. The two founding papers on this topic are:
* [Sutskever et al., 2014: Sequence to Sequence Learning with Neural Networks](https://papers.nips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks)
* [Cho et al., 2014: Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation](https://www.aclweb.org/anthology/D14-1179)

Along a similar line, we can use a CNN encoder (for example AlexNet) to encode an image and then use an RNN decoder to generate an image caption. (see ... for the introducing paper). This works reasonably well as long as the captions are not too long. 

### Beam Search

## Bleu Score (Bilingual Evaluation Understudy)

## Attention Model

## Speech Recognition
Traditionally, speech recognition has been done using phonems. However, using neural nets, the handling of speech via phonems is not necessary anymore. A typical academic dataset could consist of about 300 hrs of audio data, commercial datasets can comprise over 100.000 hrs.

We can distinguish between two approaches for speech recognition:
* Attention Models
* CTC (Connectionist Temporal Classification)

### CTC
CTC was originally introduced in [Graves et al 2006, Connectionist Temporal Classification: Labeling unsegmented sequence data with recurrent neural networks](). CTC uses a bi-directional RNN (such as GRU or LSTM) with the same number of output features as input features.  It outputs a letter at every position. However, it makes use of an additional "blank" character and used the basic rule that identical characters are collapsed should they not be separated by a blank. For example the "ddd__aa_t_aaaaa___" equals the output "data". This enables the architecture to have as many output as input features. 

### Trigger Word Detection
Whilst a full speech recognition algorithm is a considerable amount of effort, a trigger word detection algorithm can be achieved with less. 
For trigger word detection, we label the audio data in a way that at the end of the trigger word, we label it as 1 and as 0 otherwise. This works recently well. However, this leaves a quite unbalanced data set. One way around this is to label a few instances as 1 at the end of the trigger (instead of only a single one).
