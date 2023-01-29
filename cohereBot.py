import cohere
from cohere.classify import Example
co = cohere.Client('ULmoY0tufNb8CTEEPUh8ZU8Q6MPTFYdXgW6LaU3K')

def classification(prompt):
  examples = [
    Example("Can you get that done by tonight?", "professional"),
    Example("Make sure to submit your report by the weekend", "professional"),
    Example("Want to go out this weekend?", "casual"),
    Example("Preliminary testing begins tomorrow", "professional"),
    Example("We'll be holding a meeting", "professional"),
    Example("Let's meet to go over this tomorrow", "professional"),
    Example("Yo what's up", "casual"),
    Example("That's wild", "casual"),
    Example("I'll pull up tomorrow", "casual"),
    Example("Please just let me sleep bro", "casual"),
    Example("Please review the meeting notes for next week", "professional"),
    Example("Nice to meet you", "professional"),
    Example("That's so cringe bruh", "casual"),
    Example("I got a lotta people I hang out with", "casual"),
    Example("Made wonton soup the other day", "casual"),
  ]

  response = co.classify(model='large', inputs=[prompt], examples=examples)

  result = 'This message is '+ response.classifications[0].prediction + ' with ' + str(response.classifications[0].confidence) + ' confidence'
  return result
  #print(response.classifications[0].prediction)

#classification("I mean I can wait to do them if that's what you wanna")

def summarize(prompt):
  buffer_prompt = f"""Jake: Hey Vincent how are you? \n Vincent: I\'m good, how are you? \n Jake: I just finished walking my dog at 4pm, he seemed really happy which made me happy too \n Vincent: Wow!
  Summary: Jake greets Vincent and tells him about walking his happy dog. Vincent is excited.
  -- 
  Taran: Hey, did you want to meet up before class today? \n Steve: Yeah, sure. When were you thinking? \n Taran: Maybe about 3pm, before math class \n Steve: Sure, do you want to get lunch first? \n Taran: Yeah
  Summary: Taran and Steve decide to meet up and get lunch together before math class.
  --
  Mike: Hey, I need help on this physics question. \n George: What have you tried so far? \n Mike: I set the static energy equal to the kinetic energy. \n George: Bro that's so wrong I don't know how to help you.
  Summary: Mike asks George for help on a physics question but George is unable to help.
  --
  
  """
  bot_prompt = buffer_prompt + prompt + "\nSummary: "
  response = co.generate(model='xlarge', prompt=bot_prompt, max_tokens=50, temperature=0.8, end_sequences=["--"])
  return response.generations[0].text


print(summarize('Jake: Hey Vincent how are you? \n Vincent: I\'m good, how are you? \n Jake: I just finished walking my dog at 4pm, he seemed really happy which made me happy too \n Vincent: Wow!'))