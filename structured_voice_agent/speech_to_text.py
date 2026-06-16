import whisper

model=whisper.load_model("tiny")


def transcribe(audio_file):
    result=model.transcribe(audio_file)
    return result["text"]
