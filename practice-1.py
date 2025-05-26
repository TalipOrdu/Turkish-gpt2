"""
turkish-gpt2 model poem generation in turkish
"""
#import libs
from transformers import AutoTokenizer, GPT2LMHeadModel
import torch
from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#tokenizer and model
model_name = "ytu-ce-cosmos/turkish-gpt2-large-750m-instruct-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

#starting text
text = """
Şiir:
Kenetlenmişsin kalbime, ilmek ilmek,
"""

#tokenization and encoding
inputs = tokenizer.encode(text, return_tensors="pt")
#text generation
outputs = model.generate(
    inputs,
    max_length=100,
    num_return_sequences=1,
    top_k=40,
    top_p=0.9,
    temperature=0.8,
    repetition_penalty=1.2,
    do_sample=True)

#generated tokens convert numbers to words
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True) 

#printing and save .txt file
print("Input Text:", text)
print("Generated Text:", generated_text)

with open("poem.txt", "a", encoding="utf-8", newline="") as f:
    f.write("\n" + "="*50 + "\n")
    f.write(f"Generated Time: " + str(current_time + "\n"))
    f.write("Input Text: " + text + "\n")
    f.write("Generated Text: " + generated_text + "\n")
f.close()
print("Poem saved to poem.txt")