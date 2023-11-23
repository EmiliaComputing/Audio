#Import
from google.cloud import speech

#Input
print()
print("-"*50)
print('Enter link to file: ')
file = input('')
print("-"*50)
print()

audio = speech.RecognitionAudio(uri=file)

#Speech to text
def speech_to_text(config: speech.RecognitionConfig, audio: speech.RecognitionAudio) -> speech.RecognizeResponse:
    response = speech.SpeechClient().recognize(config=config, audio=audio)
    return response

#Print result
def print_final(response: speech.RecognizeResponse):
    for result in response.results:
        print_result(result)

def print_result(result: speech.SpeechRecognitionResult):
    print()
    print("-"*50)
    print(f"transcript:    {result.alternatives[0].transcript}")
    print(f"confidence:    {result.alternatives[0].confidence:.0%}")
    print("-"*50)
    print()

config = speech.RecognitionConfig(language_code="en", audio_channel_count=2)

#Print
print_final(speech_to_text(config, audio))
