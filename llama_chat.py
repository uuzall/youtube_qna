from transformers import AutoTokenizer, AutoModelForCausalLM
import torch 

def get_prompt(results, tokenizer, MAX_LEN=3000): 
  selected = '' 
  selected_len = 0 
  for i in results: 
    next_len = len(tokenizer(f'\n* {i}').input_ids)
    if selected_len + next_len < MAX_LEN: 
      selected += '\n* ' + i
      selected_len += next_len 
    else: 
      break
  return selected

def ask_llama(question, tokenizer, model, device): 
  inputs = tokenizer(question, return_tensors='pt')
  with torch.no_grad(): 
    out = model.generate(**inputs.to(device), max_length=4096, temperature=0.01, do_sample=True)
  return tokenizer.batch_decode(out)[0]