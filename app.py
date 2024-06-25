from dotenv import load_dotenv
from os import environ as env
from rich.console import Console
from rich.markdown import Markdown
from tqdm import tqdm
from time import sleep

import random
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=env['API_KEY'])

console = Console()
ai = genai.GenerativeModel('gemini-1.5-flash')

print('Welcome to PATAOFY by Param and Medha!')
print('Using this app, you can patao the people around you easily!')

crush = input('Whom do you want to patao?\n > ')

print('Guessing gender...')
response = ai.generate_content(f'''
You have to guess the gender of the person with the following name.
Respond just in one word without punctuation.
Your response should be either male or female in lowercase.
							   
The name is: "{crush}"
''')

gender = response.text.strip()

is_correct_gender = input(f'I detected that they are "{gender}".\nAm I right? (Y/n) > ')

if is_correct_gender == '' or is_correct_gender.lower() == 'y':
	print('I\'m smart, I know. 😎')
else:
	gender = 'male' if gender == 'female' else 'female'
	print(f'I was just playing with you, I knew it. 😎')

title = 'jiju' if gender == 'male' else 'bhabhi'
print(f'Ohhoooooo, {crush} {title}! 😉')

pronoun = 'him' if gender == 'male' else 'her'

likes = input(f'What do you like the most about {pronoun}?\n > ')

print('Getting ready...')
response = ai.generate_content(f'''
I like a person named "{crush}" and I want to impress {pronoun}.
What I like the most about {pronoun} is the following: "{likes}"

Using the abovementioned data and employing some unique, slightly stereotypical, and preferably dry/dark humour or just plain funny thinking, recommend a nice pickup line and a few slightly ridiculous tips to impress {pronoun}.
''')

print('Generating advice...')
for i in tqdm(range(100)):
	pause = random.uniform(0, 0.5)
	sleep(pause)

tips = Markdown(response.text.strip())

print('I have just the right answers for you!')
console.print(tips)