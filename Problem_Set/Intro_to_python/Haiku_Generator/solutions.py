# this is just the raw solutions, you can customize it however you wanted!

def input():
  username = input("Enter your name: ")
  topic = input("Enter a topic: ")
  print("Creating your haiku... \n")

def processing(username:str, topic:str):
  prompt_1 = "Make me a brief 'haiku' that gives me a quiet, thoughtful feeling. "
  prompt_2 = "Be sure to follow the rules where: the first line has 5 syllables, the second has 7 syllables, the third has 5 syllables. "
  prompt_3 = f"Add these also: My name: {username} My preferred topic: {topic}"
  
  complete_haiku_prompt = prompt_1 + promp_2 + prompt_3
  
  generated_response = call_gpt(complete_haiku_prompt)

  # at the end just print out the generated_responses like this or adds a new functions, it's all up to you...
  print(generated_responses)
