import cohere
from cohere.classify import Example
co = cohere.Client('ULmoY0tufNb8CTEEPUh8ZU8Q6MPTFYdXgW6LaU3K')

examples=[
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

def classification(str):
  response = co.classify(model='large', inputs=[str], examples=examples)
  print(response.classifications)

classification("I mean I can wait to do them if that's what you wanna")


