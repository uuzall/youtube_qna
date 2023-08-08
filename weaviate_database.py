from torch.utils.data import DataLoader
from tqdm import tqdm 
from sentence_transformers import SentenceTransformer

# loading the embedding model used for adding and searching database
emb_model = SentenceTransformer('/mnt/sda1/hf_models/multi-qa-mpnet-base-dot-v1', device='cpu')


def add_data(client, database_name, data): 
  iters = 1
  for text in data: 
    embedded_text = emb_model.encode(text, convert_to_tensor=True, convert_to_numpy=False).cpu().tolist()
    for idx, i in (loop := tqdm(enumerate(text), total=len(text))): 
      properties = {'text': i}
      client.batch.add_data_object(properties, class_name=database_name, vector=embedded_text[idx])
      loop.set_description(f'Iterations: [{iters}/{len(data)}]')
    iters += 1

def add_data_to_db(client, database_name, data: DataLoader, new_db=True): 
  if new_db == False: 
    try: # see if the database exists before adding data to it
      client.schema.get(database_name)
      add_data(client, database_name, data)
    except: # happens when database does not exist. 
      raise Exception(f'add new db is set to {new_db} but there is no database named {database_name}.')
  else: # add == False; so no adding to old database
    try: # see if the database exists before creating a new one
      wv_schema = {
        "class": database_name,
        "description": "Contents",
        "properties": [
            {
							'dataType': ['string'],
							'description': 'Text', 
							'name': 'text'
						}],
            # In the final version, add the length after knowing what model you will use
						# {
						# 	'dataType': ['int'], 
						# 	'description': 'Length of tokens', 
						# 	'name': 'length'
						# }], 
						'vectorIndexConfig': {'distance': 'dot'}}
      client.schema.create_class(wv_schema)
      add_data(client, database_name, data)
    except: # if the database does not exist, create it and add the data. 
      raise Exception(f'add new db is set to "{new_db}" but there is already a database named "{database_name}"') 

def search_db(client, database_name, query): 
  emb_q = emb_model.encode(query)
  results = client.query.get(database_name, ['text']).with_near_vector({'vector': emb_q}).with_limit(20).do()
  return [i['text'] for i in results['data']['Get'][database_name]] 