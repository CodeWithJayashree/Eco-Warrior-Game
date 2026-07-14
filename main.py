import time
import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
#Made linebreak function to make code cleaner
def linebreak():
    print('~'*150)
linebreak()
print()
time.sleep(3)
print('Friends. Yelling. Light. A portal.\n')
time.sleep(3)
print('You startle awake, wildly swinging at nothing as you stumble backwards into a tree trunk.\n')
time.sleep(4)
print('You\'re covered in mud and your breathing is ragged. You swear there was a portal behind you.\n')
time.sleep(4)
print('Where is it now?\n')
time.sleep(5)
print('You force your eyes open, taking in your surroundings.\n')
time.sleep(4)
print('A babbling brook. Tiny huts made of straw and twigs. Towering trees. Flowers everywhere.\n')
time.sleep(4)
print('Your panic fades as you stare at this storybook forest. It\'s like you\'ve fallen into a fairytale.\n')
time.sleep(4)
print('Something rough brushed against your cheek.\n')
time.sleep(2)
print('Everything fades to black.')
print()
linebreak()
time.sleep(3)
clear()
time.sleep(3)
linebreak()
print()
print('"It\'s awake!", a tiny mushroom squeals. You jolt upright. A talking mushroom? \n"Poppy! Stop frightening our guest!"')
time.sleep(3)
player_name = input('What is your name? \n>>> ')
print()
print(f'"I\'m Poppy! And this is Master Oakley!" \n"Welcome to Mossy Meadows, {player_name}", says Oakley. "I\'ve never seen you here before."')
time.sleep(5)
print('"I...don\'t know why I\'m here."')
time.sleep(4)
print('Oakley nods. "Rest for now, we can talk later"')
time.sleep(4)
print()
linebreak()
clear()
time.sleep(5)
linebreak()
print()
print('Later that afternoon, Master Oakley offers to show you the village.')
time.sleep(5)
print('The market is small, but lively. Frogs bid on flies. Snails buy new shells. Flowers are everywhere.')
time.sleep(5)
print('"Where are you from?" Poppy asks.')
time.sleep(3)
print('"Earth."')
time.sleep(3)
print('She blinks. "I\'ve never heard of it."')
time.sleep(3)
print('...')
time.sleep(8)
print('By the time you return to the cottage, only one thought fills your mind.')
time.sleep(3)
print('How do I get home?')
print()
linebreak()
clear()
time.sleep(5)
linebreak()
print()
print('That evening, Oakley knocks on your door.')
print('"I\'ve been thinking about what you told me."')
time.sleep(4)
print('You look up.')
time.sleep(4)
print('"There may be a way to return home."')
time.sleep(3)
print('"Really?"')
time.sleep(3)
print('He nods.')
time.sleep(3)
print('"Long ago, a wizard named Nox was cursed and trapped within his own shadow. Legend says that anyone who breaks his curse is granted one wish."')
time.sleep(8)
print('"So... if I help him..."')
time.sleep(3)
print('...')
time.sleep(3)
print('"...he may send you home."')
time.sleep(3)
print('"How?"')
time.sleep(3)
print('"You must restore the magical garden. Complete eight quests, and each one will reward you with a magical plant. \nWhen the garden is full, I\'ll brew a potion strong enough to enter the Briarwood. \n' \
'There, you can find and defeat Nox."')
time.sleep(8)
print('He smiles.')
print('"Are you ready?"')
time.sleep(3)
input('Press enter to begin your first quest...')
print()
linebreak()
#Now that I have given the player some expoistion, I will start making the quest structure, and some other helper functions to help the game move smoothly
#The loop should be quest, user input, quest comeplete, user see's garden, if even number fo quests comeplted, they water teh garden, new quest
#I'm going to start by making a list of emojis called plants. Then, once a quest is completed by the user, an emoji will be added to the garden. 
plants =['🌼', '🌳', '🌹', '🪻', '🌱','🌸', '🌵', '🍀']
#Next, I need to make a list of quests, and a quests_complete variable to keep track of how many quests have been completed.
quests = ['Lights Out! Try to see if you can always remember to turn the lights off when you leave a room. Think you can have 0 lights on by the end of the day?',
          'Trash Talk! Pick up at least 5 pieces of trash in your neighborhood or local park.',
          'Recycle Race! Make sure to recycle at least 5 items today. Think you can do more than 10?',
          'Energy Saver! Try to use less energy today by unplugging electronics when not in use.',
          'Meat Madness! Try to avoid buying or consuming any meat or animal products for a day by swapping them out with plant based substitutes.',
          'Water Watch! Try to use less water today by taking showers instead of baths and turning off the faucet when brushing your teeth!',
          'Protest Plastic! Try to use less plastic today by using reusable utentils, straws, and bags. Think you can go plastic free for a whole day?',
          'Transportation Transformation! Try to use less transportation today by walking, biking, or taking public transport. Think you have what it takes to go car free?']
#Now, I will also be making a list of quest explanations, that give the user more information about the quest once they've comepleted it.
#Adding statistics to these messages will help the user better understand their positive impact!
quest_explanations = [f'Switching off the lights is a good start, but using energy-efficient LEDs is better, as they consume 75% less energy!',
                      'Collecting trash keeps the environment clean and prevents pollution. By 2050, an estimated 3.78 billion metric tons of trash will be produced.'
                      'Did you know that recycling 10 plastic bottles can generate enough electricity to power a laptop for a day?',
                      'Many appliances consume power even when turned off. Unplugging devices like TVs and chargers can conserve energy. ',
                      'Producing 1 kg of beef generates 60 kg of carbon dioxide, while root vegetables only generate 0.4 kg!',
                      'You can save 8 gallons of water by closing the tap while brushing and 45 gallons by taking a shower instead of a bath!',
                      f'Did you know that fast fashion significantly contributes to plastic waste, with 85% of items ending up in landfills?',
                      f'In addition to reducing carbon emissions on average by 67%, biking and walking are great sources of exercise!']
quests_completed = 0
garden = ['_','_','_','_','_','_','_','_']
#I do need to give them quest completeion messages. I'm going to use a list to give them a different message each time
complete_messages=['Awesome', 'Well done', 'You did it', 'Amazing work', 'Good job', 'Excellent work', 'Way to go', 'Congratulations']
#Now, I can make a function that will water the garden. They can only water the garden if they have completed an even number of quests, and if it is above 0.
def water_garden():
    if quests_completed > 0 and (quests_completed+1) %2 == 0:
        input('Press enter to water your garden! 💧💧💧')
        print()
        for plant in garden:
            print(plant + '✨', end='')
        time.sleep(3)
        print('\n')
        print('Your garden is looking beautiful!')
    else:
        print()
        print('Your garden is looking great!')
#Well, first, I need to tell the user about sustainability, and how it is important to take care of the enviorment! 
linebreak()
print()
print('"Before you begin your quest, I want to tell you a little bit about sustainability." Oakley says.')
print()
time.sleep(3)
print('Sustainable living refers to making lifestyle choices that leave minimal negative effects on environment. ')
print()
time.sleep(3)
print('It focuses on making conscious choices to limit environmental impact that can be incorporated into your lifestyle.')
print()
time.sleep(3)
print('Sustainable living doesn\'t have to be difficult or expensive! You can make a big difference by making small changes in your daily life.')
print()
time.sleep(4)
input('Press enter to continue...')
print()
linebreak()
clear()
#Now, I can basically use a while loop to keep the game going until the user has finished all of the quests. 
while quests_completed < len(quests):
    linebreak()
    print()
    print(f'Quest {quests_completed+1}: {quests[quests_completed]}:')
    print()
    done = input('Type "done" when you\'ve finished the quest! ').strip().lower()
    print()
    if done == 'done':
        print(f'{complete_messages[quests_completed]} {player_name}! You have completed the quest!')
        print()
        time.sleep(5)
        print(f'Here is some extra information about the quest: {quest_explanations[quests_completed]}')
        print()
        time.sleep(5)
        print(f'You have added a plant to your garden!')
        print()
        garden[quests_completed] = plants[quests_completed]
        for i in garden:
            print(i," ", end='')
        print()
        time.sleep(3)
        print()
        water_garden()
        print()
        if quests_completed == 3:
            print('You\re halfway there! Keep going!')
        else:
            pass
        quests_completed +=1
        time.sleep(10)
        clear()
    else:
        print()
        print('Please type "done", when you are finished. You can do it! ')
        time.sleep(5)
        clear()
        continue
linebreak()
print()
print('Congratulations! You have finished all of the quests and filled your garden!')
time.sleep(2)
print(garden)
linebreak()
#Main quests sequence is comeplete! Now, I will make the final boss battle sequence. It will be an 8 question quiz, user has 3 lives. 
#The Final quiz will be a dictionary. The keys are the questions and the values are the answers.
player_lives = 3
final_quiz {}






        

        

    

    
