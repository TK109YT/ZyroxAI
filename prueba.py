from IPython.display import Audio
from scipy.io.wavfile import write as write_wav
from bark import SAMPLE_RATE, generate_audio, preload_models


preload_models()

text_prompt = "¡Hola!, esto es una prueba de texto 1 2 3 4. Zyrox, ¿sabes quién es?"

audio_array = generate_audio(text_prompt)   #, history_prompt="./bark/bark/assets/prompts/v2/es_speaker_1.npz")

write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)

Audio(audio_array, rate=SAMPLE_RATE, filename='bark_generation.wav')

