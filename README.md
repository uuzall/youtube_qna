# YouTube Video QnA Bot 

In this repo, I wanted to experience creating something new using LLaMA-2. I read somewhere about making a bot that takes in YouTube videos and embeds them in a vector database. Everything after that is basic QnA using context, where you search the database using the embedding for the questions asked. Then, the question and the context are sent to LLaMA-2 who gives an answer. 

It worked amazingly, especially for video essays where a person talks extensively about one topic. However I found some weird quirks, like, 
* If you have a podcast or a video where 2+ people talk then there is no way to tell them apart just from the video transcript, so, LLaMA-2 gets incredibly confused as to who is talking and gives weird answers sometimes. Not too weird that what it says is wrong but it mixes the personalities of the multiple people talking into 1 person. Also, a future project inspiration is to solve this by using audio classifier to classify different voices into "person1", "person2", and so on. 
* There are some peculiar differences between GPT-3.5/4 and LLaMA-2. The most important of which is that LLaMA loves to talk, like a lot. It generates a lot of words and it paraphrases the context given to it. On the other hand, GPT is very short and succinct when replying (maybe because it saves OpenAI a lot of money when it generates less text). GPT's outputs are all to the point and does not diverge from the context provided by the user.

I have included some test outputs in this [file](output/answers.txt) file. You can check them out. 
If you want to run this by yourself then just clone it and "docker-compose up" to create a Weaviate server. Then it should work. If there are problems, I'm sure you can figure it out (you're very smart).