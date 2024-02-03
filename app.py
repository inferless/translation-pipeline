from transformers import WhisperProcessor, WhisperForConditionalGeneration
from transformers import pipeline
import requests

class InferlessPythonModel:
  def initialize(self):
    self.asr_processor = WhisperProcessor.from_pretrained("openai/whisper-base.en")
    self.asr_model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-base.en")

  @staticmethod
  def download_audio_file(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
      with open(destination, 'wb') as f:
        f.write(response.content)

  def infer(self, inputs):
    filename = inputs["filename"]
    start_time = inputs["start_time"]
    end_time = inputs["end_time"]



# load dummy dataset and read audio files
ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
sample = ds[0]["audio"]
input_features = processor(sample["array"], sampling_rate=sample["sampling_rate"], return_tensors="pt").input_features 

# generate token ids
predicted_ids = model.generate(input_features)
# decode token ids to text
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=False)

transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)
