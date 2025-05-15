from kokoro import KPipeline
from IPython.display import display, Audio
import soundfile as sf 
import torch

class Speak:
    def __init__(self, voice, text):
        self.voice = voice
        self.text = text

    def speak(self):
        pipeline = KPipeline(lang_code='a')
        generator = pipeline(self.text, voice=self.voice)
        for i, (gs, ps, audio) in enumerate(generator):
            display(Audio(data=audio, rate=24000, autoplay=i==0))
            sf.write(f'{i}.wav', audio, 24000)
