import yt_dlp 
import librosa 

def download_audio(url, file): 
  yt_opts = {'outtmpl': file, 'format': 'bestaudio', 'noplaylist': True}

  with yt_dlp.YoutubeDL(yt_opts) as ydl: 
    ydl.download([url]) 
  
def read_audio(file):
  data, sr = librosa.load(file, sr=16000)
  return data, sr 

def main(url, file): 
  download_audio(url, file) 
  data, sr = read_audio(file) 
  return data, sr 