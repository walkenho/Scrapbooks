# setup deepspeech and prerequistes and anaconda environment
./deepspeech_setup.sh


## Enable anaconda environment
. ./activate_conda_env.sh

### Generating a language model
./generate_lm.sh 
Usage: ./generate_lm.sh <transcription files location> <trasncription files extension> <language model target directory location>

Example: 
If you already have a single file: good
If not:
mkdir language_model
./generate_lm.sh data_voip_en/dev trn language_model
Produces two files:
	• Lm.binary (the one we need)
	• Arpa
	• These are the same files, but in different standards
	• Also produces transcriptions.txt
	

### Deepspeeech requires csv describing dataset
./produce_csv.sh


Usage: produce_csv.sh <audio files directory> <CSV file target path and name (optional)>
./produce_csv.sh data_voip_en/dev/ test.csv
(this also does a cleaning step for the transciption files (which it expects to have the ending .wav.trn and the same filename as the .wav files)
	• Walks through the whole folder with subfolders to find all .wav files and then looks for corresponding .wav.trn
	• Wav's should be:
		○ Single channel
		○ 16k sample rate
		○ 16 bits per sample sample encoding
		○ You can check using soxi  filename.wav to find all these three pieces of information




./DeepSpeech-0.5.1/DeepSpeech.py --test_files data_voip_en/dev/test.csv \
  --lm_binary_path deepspeech-0.5.1-models/lm.binary  \
  --alphabet_config_path deepspeech-0.5.1-models/alphabet.txt \
  --checkpoint_dir deepspeech-0.5.1-checkpoint \
  --test_batch_size 8   --report_count 100   | tee  test_results.txt
(You can feed in your own trie model, if you don't it will generate the trie model from the language model)
(alternatively we can also use /DeepSpeech-0.5.1/evaluate.py  )

./DeepSpeech-0.5.1/DeepSpeech.py \
  --train_files  data_voip_en/dev/test.csv --dev_files  data_voip_en/dev/test.csv --test_files  data_voip_en/dev/test.csv \
 --lm_binary_path deepspeech-0.5.1-models/lm.binary  \
  --alphabet_config_path deepspeech-0.5.1-models/alphabet.txt \
  --checkpoint_dir deepspeech-0.5.1-checkpoint \
  --train_batch_size 8 --dev_batch_size 8 --test_batch_size 8 \
  --epochs 1 --learning_rate 0.0001 --display_step 0 --validation_step 1 --dropout_rate 0.15 --checkpoint_step 1 \
  --n_hidden 2048 --lm_alpha 0.75 --lm_beta 1.85
# --lm_trie_path DeepSpeech/data/lm/trie


