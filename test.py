# from dotenv import load_dotenv
# from os import environ as env

# import google.generativeai as genai

# load_dotenv()
# genai.configure(api_key=env['API_KEY'])

# ai = genai.GenerativeModel('gemini-1.5-flash')

# response = ai.generate_content('Write some gibberish.')
# print(response)
# print(response.text)

# from rich.console import Console
# from rich.markdown import Markdown

# text = '''
# I have just the right answers for you!
# ## Pickup Line:

# "Hey Devansh, you have a voice that could melt glaciers.  Mind if I stand a little closer to you, just to make sure I don't freeze to death?"

# ## Ridiculous Tips:

# 1. **The Shakespearean Approach:**  Learn a sonnet by heart. It doesn't have to be about him, just pick something dramatic about love or loss.  He'll be impressed by your literary knowledge (and possibly terrified by your dramatic delivery).
# 2. **The "Mysteriously Cool" Strategy:**  Start wearing a monocle and talking about existential philosophy.  He'll be intrigued by your enigma, even if you're just trying to impress him with the word "epistemology."
# 3. **The "I'm a Genius" Gambit:**  Start talking about how you're working on a new theory about the universe, like string theory, but add a completely made-up element, like "the fifth dimension of quantum gravity."  He'll be either amused or slightly concerned.
# 4. **The "Master of Disguise" Maneuver:**  Show up at a place he frequents, but with a completely different hairstyle,  wearing a disguise. Then, when he's wondering who you are, casually reveal yourself.  It's a risky play, but if he's intrigued, it'll be a memorable entrance.
# 5. **The "I'm a Master of Subtlety" Ploy:**  Find a way to casually drop that you know Morse code. When he's confused, act like it's an everyday thing and start tapping out a random message.  He'll be thinking, "Why do I even bother?" while secretly wondering if you're secretly an international spy.

# **Remember:**  Humour is subjective, so tailor these ideas to Devansh's personality and sense of humor.  And most importantly, be genuine and yourself – even if you're being a bit ridiculous.  Good luck!
# '''

# console = Console()
# markdown = Markdown(text)
# console.print(markdown)

from tqdm import tqdm
from time import sleep
import random

for i in tqdm(range(100)):
    pause = random.uniform(0, 0.5)
    sleep(pause)