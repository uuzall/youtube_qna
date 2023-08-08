from transformers import pipeline 

def speech_recognition(data, file_path): 
	pipe = pipeline('automatic-speech-recognition', model='/mnt/sda1/hf_models/whisper-medium', chunk_length_s=30, device='cuda')
	prediction = pipe(data, batch_size=32) 
	with open(file_path, 'w') as file: 
		file.write(prediction['text'])

def slice_text(text): 
	all_text = list() 
	splitted_pred = text.split() 
	for i in range(512, len(splitted_pred), 512): 
		all_text.append(' '.join(splitted_pred[i-512:i]))
	return all_text