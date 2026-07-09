import time
import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print('Friends. Yelling. Light. A portal. \nYou startle awake, wildly swinging at nothing as you stumble backwards into a tree trunk. \nYou\'re covered in mud and your breathing is ragged. You swear there was a portal behind you. \nWhere is it now?')
print('\nYou force your eyes open, taking in your surroundings. A babbling brook. Tiny huts made of straw and twigs. Towering trees. Flowers everywhere. ')
print('Your panic fades as you stare at this storybook forest. It\'s like you\'ve fallen into a fairytale. \nSomething rough brushed against your cheek. \n \nEverything fades to black.')
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
time.sleep(25)
clear()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print('"It\'s awake!", a tiny mushroom squeals. You jolt upright. A talking mushroom? \n"Poppy! stop frightening our guest!"')
time.sleep(3)
player_name = input('What is your name? \n>>> ')
print()
print(f'"I\'m Poppy! and this is Master Oakley!" \n"Welcome to Mossy Meadows, {player_name}", says Oakley. "I\'ve never seen you here before."')
time.sleep(5)
print('"I...don\'t know why I\'m here."')
time.sleep(3)
print('Oakley nods. "Rest for now, we can talk later"')
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
clear()
time.sleep(5)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print('Later that afternoon, Master Oakley offers to show you the village')
print('The market is small, but lively. Frogs bid on flies. Snails buy new shells. Flowers are everywhere.')
time.sleep(5)
print('"Where are you from?" Poppy asks.')
time.sleep(3)
print('"Earth."')
time.sleep(3)
print('She blinks. "I\'ve never heard of it."')
print('...')
time.sleep(8)
print('By the time you return to the cottage, only one though fills your mind. \nHow do I get home?')
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
clear()
time.sleep(5)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
print('That evening, Oakley knocks on your door.')
print('"I\'ve been thinking about what you told me."')
print('You look up.')
print('"There may be a way to return home."')
time.sleep(3)
print('"Really?"')
print('He nods.')
time.sleep(3)
print('"Long ago, a wizard named Nox was cursed and trapped within his own shadow. \nLegend says that anyone who breaks his curse is granted one wish."')
time.sleep(5)
print('"So... if I help him..."')
time.sleep(3)
print('...')
time.sleep(3)
print('"...he may send you home."')
time.sleep(3)
print('"How?"')
print('"You must restore the magical garden. Complete eight quests, and each one will reward you with a magical plant. \nWhen the garden is full, I\'ll brew a potion strong enough to enter the Briarwood."')
time.sleep(5)
print('He smiles.')
print('"Are you ready?"')
time.sleep(3)
print('Press Enter to begin your first quest...')
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#Now that I have given the play some expoistion, I will start making the quest structure, and some other helper functions to help the game move smoothly
#The loop should be quest, user input, quest comeplete, user see's garden, if even number fo quests comeplted, they water teh garden, new quest
#I'm going to start by making a list of emojis called plants. Then, once a quest is completed by the user, an emoji will be added to the garden. 
plants =['🌼', '🌳', '🌹', '🪻', '🌱','🌸', '🌵', '🍀']
#Next, I need to make a list of quests, and a quests_complete variable to keep track of how many quests have been completed.
quests = ['Lights Out! Try to see if you can always remember to turn the lights off when you leave a room. Think you can have 0 lights on by the end of the day?',
          'Trash Talk! Pick up at least 5 pieces of trash in your neighborhood or local park.',
          'Recycle Race! Make sure to recycle at least 5 items today. Think you can do more than 10?',
          'Energy Saver! Try to use less energy today by unplugging electronics when not in use.'
          'Market Madness! Try to buy at least 1 crop from a local farmer\'s market or local small business today. While you\'re at it, try to avoid buying any meat or animal products.',
          'Water Watch! Try to use less water today by taking showers instead of baths and turning off the faucet when brushing your teeth!',
          'Protest Plastic! Try to use less plastic today by using reusable utentils, straws, and bags. Think you can go plastic free for a whole day?',
          'Transportation Transformation! Try to use less transportation today by walking, biking, or taking public transport. Think you have what it takes to go car free?']
quests_completed = 0
garden = []
#Now, I can make a function that will water the garden. They can only water the garden if they have completed an even number of quests, and if it is above 0.
def water_garden():
    if quests_completed > 0 and quests_completed %2 == 0:
        print('Time to water your garden! 💧💧💧')
        for plant in garden:
            print(plant + '✨', end='')
        print('Your garden is looking beautiful!')
#Now, I can basically use a while loop to keep the game going until teh user has finished all of the quests. 

    
