from transformers import WhisperProcessor, WhisperForConditionalGeneration
from transformers import pipeline
import requests
import soundfile as sf


class InferlessPythonModel:
    def initialize(self):
        self.asr_processor = WhisperProcessor.from_pretrained("openai/whisper-base.en")
        self.asr_model = WhisperForConditionalGeneration.from_pretrained(
            "openai/whisper-base.en"
        )

        self.translation_processor = pipeline(
            "translation", model="Helsinki-NLP/opus-mt-en-fr"
        )

    @staticmethod
    def download_audio_file(url, destination):
        final_destination = f"{destination}/audio.wav"
        response = requests.get(url)
        if response.status_code == 200:
            with open(final_destination, "wb") as f:
                f.write(response.content)

    def infer(self, inputs):
        filename = inputs["filename"]
        start_time = inputs["start_time"]
        end_time = inputs["end_time"]
        vad = inputs["vad"]
        vad_silence = inputs["vad_silence"]
        model = inputs["model"]
        target_lang = inputs["target_lang"]

        self.download_audio_file(filename, "/mnt/data/audio.wav")
        audio, sampling_rate = sf.read("audio.wav")

        input_features = self.asr_processor(
            audio, sampling_rate=16000, return_tensors="pt"
        ).input_features

        predicted_ids = self.asr_model.generate(input_features)

        transcription = self.asr_processor.batch_decode(
            predicted_ids, skip_special_tokens=True
        )[0]

        translation = self.translation_processor(transcription, target_lang)[0][
            "translation_text"
        ]

        return {"result_text": translation}

    def finalize(self):
        self.asr_model = None
        self.asr_processor = None
        self.translation_processor = None
