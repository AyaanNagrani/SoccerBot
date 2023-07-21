import random
import time
import sys
import requests
import json
def get_prediction(season, name, matches_played):
  data={"season": season, "name":name,"matches played":matches_played}
  url = 'https://askai.aiclub.world/3b3e1c54-8ea0-4ef9-9316-13ac9ca37320'
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  predicted_label = json.loads(json.loads(response)['body'])['predicted_label']
  return predicted_label











def say(msg, sleepAfter=0):
  for char in msg:
    print(char, end='')
    time.sleep(0.03)
    sys.stdout.flush()
  print()
  time.sleep(sleepAfter)
  

say("Hello, I am SoccerBot. Ask me a soccer-related question, and I might be able to answer!")
time.sleep(2)
say("What is your name?")
question = input("")
say(f"Hello {question}, nice to meet you.")
time.sleep(2)
say("How can I help you? ")
mainq = input("")
if mainq == "Can you give me stats from the EPL?":
  say("Which statistic?")
  stat = input("")    
  if stat == "wins":
    say("Of course!")
    time.sleep(1)
    say("Enter the season you woud like statistics from: ")
    season = input("")
    say("Which team would you like the statistics from? ")
    team = input("")
    say("How many matches did this team play?")
    matches_played = input("")
    finalpredic = get_prediction(season,team,matches_played)
    say(f"{team} had {finalpredic} wins in the {season} season..")
    say("I hope this answered your question!")
  else:
    say("Sorry, the program cannot provide this information quite yet.") #add function

