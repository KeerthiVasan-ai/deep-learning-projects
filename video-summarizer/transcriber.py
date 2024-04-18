import whisper

whisper_model = whisper.load_model("tiny")

def transcribe_process(file_path: str) -> str:
  transcription = whisper_model.transcribe(file_path, fp16=False)
  return transcription['text']