#I am going to orgnaize my code into 2 sections. One has the game. And the other has the helper functions/lists/dictionaries. 
# This way everything is much neater instead of being a mix of both!
############################################################################################################################################
#Code section:
import pygame 
import time
import sys
import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
#Made linebreak function to make code cleaner
def linebreak():
    print('~'*150)
#So the gemini terminal flash thing didn't work at all due to how my VS Code editor handles those commands. :(
#To try and still acheive that effect, I'm just going to make a rectangle of emojis in that color :(
def flash_white():
    clear()
    color = '⬜️'
    lines = 20 # apparently this is the standard number for now many rows terminal size if you don't know which os
    columns = 40 # this is apparantly the standard of columns for terminal size if you don't know the os
    white_block = (color*columns + '\n') * lines
    print(white_block)
    sys.stdout.flush()
    time.sleep(0.2)
#I'm making this function called restart so that if the player does want to play again they can. 
#For me, this is easier tha unsing a while loop so I don't have to reset all of the values of the variables
def restart():
    sys.stdout.flush()
    os.execv(sys.executable,[sys.executable]+sys.argv)
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
          'Transportation Transformation! Try to use less transportation today by walking, biking, or taking public transport. Think you have what it takes to go car free?',]
#Now, I will also be making a list of quest explanations, that give the user more information about the quest once they've completed it.
#Adding statistics to these messages will help the user better understand their positive impact!
quest_explanations = [f'Switching off the lights is a good start, but using energy-efficient LEDs is better, as they consume 75% less energy!',
                      'Collecting trash keeps the environment clean and prevents pollution. By 2050, an estimated 3.78 billion metric tons of trash will be produced.',
                      'Did you know that recycling 10 plastic bottles can generate enough electricity to power a laptop for a day?',
                      'Many appliances consume power even when turned off. Unplugging devices like TVs and chargers can conserve energy. ',
                      'Producing 1 kg of beef generates 60 kg of carbon dioxide, while root vegetables only generate 0.4 kg!',
                      'You can save 8 gallons of water by closing the tap while brushing and 45 gallons by taking a shower instead of a bath!',
                      f'Did you know that fast fashion significantly contributes to plastic waste, with 85% of items ending up in landfills?',
                      f'Walking and cycling produce little to no direct emissions and can reduce dependence on fossil fuels.',]
quests_completed = 0
garden = ['_','_','_','_','_','_','_','_']
#I do need to give them quest completeion messages. I'm going to use a list to give them a different message each time
complete_messages=['Awesome', 'Well done', 'You did it', 'Amazing work', 'Good job', 'Excellent work', 'Way to go', 'Congratulations']
#Now, I can make a function that will water the garden. They can only water the garden if they have completed an even number of quests, and if it is above 0.
def water_garden():
    if quests_completed > 0 and (quests_completed+1) %2 == 0:
        input('Press enter to water your garden! 💧💧💧')
        #playing watering sound effect here
        play_water_sound()
        print()
        for plant in garden:
            print(plant + '✨', end='')
        time.sleep(3)
        print('\n')
        print('Your garden is looking beautiful!')
    else:
        print()
        print('Your garden is looking great!')
#Now, I will make a function that "brews" a potion using the plants, since that's the next part of the story!
#So I'm using the same code I did in the flash white function, just changing it to flash purple for the potion making part
def flash_purple():
    clear()
    color = '🟪'
    lines = 20 # apparently this is the standard number for now many rows terminal size if you don't know which os
    columns = 40 # this is apparantly the standard of columns for terminal size if you don't know the os
    purple_block = (color*columns + '\n') * lines
    print(purple_block)
    sys.stdout.flush()
    time.sleep(0.2)

def potion_brewing():
    print('\n꧁✮.....................................................✮꧂')
    #Testing potion brewing background sound here
    play_potion_brewing()
    print('"First, we need to gather some rare magic ingredients from my grotto!", says Master Oakley.')
    time.sleep(2)
    print('...')
    time.sleep(1)
    print('"Aha! I\'ve found what we need. Lets get started!"')
    time.sleep(2)
    print('"A touch of toadstool"')
    play_toad_stool() #added new toadstool sound effect here
    print('🍄🍄🍄')
    time.sleep(2)
    print('"A dash of lightning. Just a little!')
    play_lightning() #added new lightning sound effect here
    print('⚡️')
    time.sleep(2)
    print('"A pinch of fairy dust')
    play_fairy_dust() #added new fairy dust sound effect here
    print('✨✨✨✨')
    time.sleep(2)
    print('"And some unicorn hair!"')
    play_unicorn_hair() #added new unicorn hair sound effect here
    print('🦄🦄🦄')
    print('"And now, for the most important ingredient. Your garden!"\n')
    print('You see, those aren\'t just any plants. Together, they become a rare, powerful jewel called a Lux Roboris.\n')
    time.sleep(2)
    count = 0
    temp_garden = garden[:]
    while count <8:
        for i in temp_garden:
            print(i, end ="")
        print()
        del temp_garden[-1]
        time.sleep(1)
        count +=1
    print('⛧°. ⋆༺☾𖤓༻⋆. °⛧')
    play_gem() #added new gem sound effect here
    time.sleep(1)
    gem ='✨💎✨'
    print(gem)
    print('"Now, to brew the potion. 🪄"')
    time.sleep(3)
    print('\033[1;35mcigam noitop lleps '*5)
    time.sleep(1)
    print('cigam noitop LLEPS '*5)
    time.sleep(1)
    print('cigam NOITOP LLEPS '*5)
    time.sleep(1)
    print('CIGAM NOITOP LLEPS! '*5)
    flash_purple() #added new flash purple function here :)
    potion = '🔮💎🔮💎🔮'
    print(f'"\033[0mHere is your potion: {potion}.\n')
    print('You have to pour the potion on yourself to be teleported to the Briarwood.\n')
    time.sleep(2)
    stop_music()
    print(f'Remember, you will only have 3 chances to beat Nox. Good luck {player_name}!\n')
    time.sleep(3)
    print('꧁✮.....................................................✮꧂')
#The Final quiz will be a dictionary. The keys are the questions and the values are the answers.
lives = 3
quiz_questions = {
                'Q1':'LED\'s are more energy efficient than normal light bulbs (true/false)',
                'Q2':'Unplugging electronics when not in use wastes up to 10 percent of energy (true/false)',
                'Q3':'Fill in the blank: reduce, ________, recycle',
                'Q4':'Fill in the blank: Riding a ________ instead of driving reduces carbon emissions.',
                'Q5':'Type A or B: Which is more sustainable? A) Using a plastic water bottle. B) Using a reusable water bottle.',
                'Q6':'Type A or B: Which is more sustainable? A) Consuming large amounts of meat and animal products. B) Consuming produce and other vegetables',
                'Q7':'Which one does NOT belong in the recycling bin? A) Old batteries B) Cardboard boxes C) Glass jars',
                'Q8':'Which one is NOT a renewable energy source? A) Solar B) Hydroelectric C) Fossil fuels',  
                }
#This will check if the user's answer matches the correct answer in the dictionary
#I realise now that I should probably include more than one way of answering for some of these questions so the user doesn't feel misled. 
#To do this, I will be making another dictionary with the quiz answers
quiz_answers = {
                'Q1':['true','t'],
                'Q2':['false','f'],
                'Q3':['reuse','Reuse','REUSE','Re-use','re-use','RE-USE'],
                'Q4':['bike','BIKE','Bike','bicycle','Bicycle','BICYCLE','scooter','Scooter','SCOOTER','skateboard','Skateboard','SKATEBOARD'],
                'Q5':['b','B','B)'],
                'Q6':['b','B','B)'],
                'Q7':['a','A','A)'],
                'Q8':['c','C','C)'],
                }
def good_ending():
    #make good ending here
    clear()
    linebreak()
    print()
    print('\033[0;31mNOOOOO! WHAT KIND OF TRICKERY IS THIS?\033[0m\n')
    time.sleep(3)
    print('You shake your head in disbelief.\n')
    time.sleep(3)       
    print('You did it!\n')
    time.sleep(3)
    print('\033[0;31mI\'LL BE BACK! DON\'T THINK THAT I\'VE FORGOTTEN THIS. YOU WILL RUE THE D-\033[0m\n')
    time.sleep(3)
    print('The inky blackness of the forest disspeared.\n')
    time.sleep(3)
    print('Lush green trees. Birds and bees. Flowers everywhere.\n')
     #Adding winning music here
    play_winning_theme()
    time.sleep(3)
    print('An old looking wizard stood where the shadow once was.\n')
    time.sleep(3)
    print('What. How. Who are you?\n')
    time.sleep(4)
    print(f'I\'m {player_name}. I\'ve come to free you.\n')
    time.sleep(3)
    print('Why?\n')
    time.sleep(3)
    print('I wanted to gain the wish, so I can go home.\n')
    time.sleep(3)
    print('Of course.\n')
    time.sleep(3)
    print('Why were you trapped in your own shadow Nox?\n')
    time.sleep(3)
    print('The earth spirit cursed me.\n')
    print('She said that when, and only when I can learn to love and protect the environment, I will be allowed to experience its beauty again.\n')
    time.sleep(6)
    print('I\'m forever grateful for you.\n')
    print('Now, let\'s send you home... \n')
    input('Press enter to return to the cottage...')
    print()
    linebreak()
    clear()
    time.sleep(3)
    linebreak()
    print()
    print('You and Nox walk back to Mossy Meadows in a comfortable silence.\n')
    time.sleep(3)
    print('You admire the fairytale world around you.\n')
    time.sleep(3)
    print('The lessons you\'ve learned here will stay with you forever\n')
    time.sleep(3)
    print(f'"{player_name}! You\'re back!" Poppy says as she runs up to hug you.\n')
    time.sleep(3)
    print('Master Oakley nods sagely. A smile on his face.\n')
    time.sleep(3)
    print('"I\'m going to miss you!" Poppy says.\n')
    time.sleep(3)
    print('You are always welcome here, Master Oakley and Nox say.\n')
    time.sleep(3)
    print('You\'re really doing this. You\'re finally going home.\n')
    time.sleep(3)
    print('Nox\'s eyes glow white as he conjures a spell.\n')
    flash_white()
    print('\033[1;34m🌀LATROP emoH nruter!🌀')
    print('🌀'*15)
    print('🌀'*15)
    print('🌀'*15)
    print('🌀'*15)
    print()
    print('\033[1;34mA blue and white swirly vortex appears in front of you.\n')
    time.sleep(3)
    stop_music()
    print('Thank you, for everything! You step inside.\n')
    time.sleep(3)
    print('A bright, white light welcomes you in.\033[0m\n')
    time.sleep(3)
    print('Home.')
    print()
    linebreak()

def sad_ending():
    #make sad ending here
    #playing sad ending music here
    play_losing_theme()
    clear()
    linebreak()
    print()
    print('It\'s over.\n')
    time.sleep(3)
    print('You\'re whooshed back to the edge of the Briarwood.\n')
    time.sleep(3)
    print('You\'re eyes are glued to the ground. You\'re legs won\'t budge.\n')
    time.sleep(3)
    print('Time stands still.\n')
    time.sleep(3)
    print('You sob. You\'re stuck here.\n')
    time.sleep(3)
    print('Forever.\n')
    time.sleep(3)
    print('If you just had one more chance.\n')
    time.sleep(3)
    print('You were so, so close.\n')
    time.sleep(3)
    print('You trudge back to Mossy Meadows.\n')
    time.sleep(3)
    print('You don\'t want to face Oakley or Poppy. She was so happy for you.\n')
    time.sleep(3)
    print('You\'ll be seeing them a lot, since that\'s where you\'ll live now.\n')
    time.sleep(3)
    print('If only things had gone differently.\n')
    time.sleep(2)
    #stopping music
    stop_music()
    print('If only.')
    linebreak()
#I've realized that music would proably help enhance my storybook enviorment and help the user feel more comfortable between pauses.
#So, I've decided to add some small sound effects and some backgroud music to important scenes
pygame.mixer.init() #this initilaizes the mixer, which is what will be playing the music files!

#Now I'm gonna make a function for the entering mossy meadows music

#I should mention that NONE of this music is my own. ALL RIGHTS GO TO THE ORIGINAL CREATORS!!
#I just wanted to add some music to enhance the storybook enviorment of my game. :)
#I downloaded all of the music from Pixabay.

#These are all of the MAIN background music functions. I will add more for the sound effects later.
def play_mossy_meadows():
    mossy_meadows = 'game sounds/background music/mossy_meadows.mp3' #make variable for music file
    pygame.mixer.music.load(mossy_meadows) #name of music file variable
    pygame.mixer.music.set_volume(0.2) #sets volume to 20% since its a background track
    pygame.mixer.music.play(-1) #loops forever
#Now I need to make a function to stop playing the music. I want it to fade out.
def stop_music():
    pygame.mixer.music.fadeout(3000) #fades out in 3 seconds
#Now I'm making a function to play the background music for the potion making scene!
def play_potion_brewing():
    potion_brewing = 'game sounds/background music/potion_brewing.mp3'
    pygame.mixer.music.load(potion_brewing)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
#Adding a function for the player entering the briarwoods scene
def play_briarwood():
    entering_briarwood = 'game sounds/background music/entering_briarwood.mp3'
    pygame.mixer.music.load(entering_briarwood)
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)
#Make function to play music if user wins! 
def play_winning_theme():
    winning_theme = 'game sounds/background music/happy_ending.mp3'
    pygame.mixer.music.load(winning_theme)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
#Now I will make a function to play the losing theme if the user loses the game
def play_losing_theme():
    losing_theme = 'game sounds/background music/sad_ending.mp3'
    pygame.mixer.music.load(losing_theme)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

#These are the sound effects functions. I will add more as I go along.

#Now, to make a watering the garden sound effect. 
def play_water_sound():
    water_sound = 'game sounds/sound effects/water_dripping.mp3'
    water_sound = pygame.mixer.Sound(water_sound)
    water_sound.set_volume(0.3)
    water_sound.play(2)
#Now, I will make a magical flourish sound effect for the garden getting a new plant
def play_chime_sound():
    chime_sound = 'game sounds/sound effects/magical_chime.mp3'
    chime_sound = pygame.mixer.Sound(chime_sound)
    chime_sound.set_volume(0.3)
    chime_sound.play()
#Now I will make a correct sound effect
def play_correct_sound():
    correct_sound = 'game sounds/sound effects/correct_ding.mp3'
    correct_sound = pygame.mixer.Sound(correct_sound)
    correct_sound.set_volume(0.3)
    correct_sound.play()
#Now I will make an error sound effect 
def play_error_sound():
    error_sound = 'game sounds/sound effects/error_sound.mp3'
    error_sound = pygame.mixer.Sound(error_sound)
    error_sound.set_volume(0.3)
    error_sound.play()
#Now I'm gonna make a function for the potion brewing sound effect. I will use this when the potion is being brewed.
#Nevermind that didn't work. I will make separate sound effects for each of the ingredients being added to the potion.
def play_toad_stool():
    toadstool = 'game sounds/sound effects/potion_sound1.mp3'
    toadstool = pygame.mixer.Sound(toadstool)
    toadstool.set_volume(0.4)
    toadstool.play()
    time.sleep(1)
def play_lightning():
    lightning = 'game sounds/sound effects/potion_sound2.mp3'
    lightning = pygame.mixer.Sound(lightning)
    lightning.set_volume(0.4)
    lightning.play()
    time.sleep(1)
def play_fairy_dust():
    fairy_dust = 'game sounds/sound effects/potion_sound3.mp3'
    fairy_dust = pygame.mixer.Sound(fairy_dust)
    fairy_dust.set_volume(0.4)
    fairy_dust.play()
    time.sleep(1)
def play_unicorn_hair():
    unicorn_hair = 'game sounds/sound effects/potion_sound4.mp3'
    unicorn_hair = pygame.mixer.Sound(unicorn_hair)
    unicorn_hair.set_volume(0.4)
    unicorn_hair.play()
    time.sleep(1)
def play_gem():
    gem = 'game sounds/sound effects/potion_sound5.mp3'
    gem = pygame.mixer.Sound(gem)
    gem.set_volume(0.4)
    gem.play()
    time.sleep(1)
############################################################################################################################################
#Game section:
linebreak()
print()
time.sleep(3)
flash_white()
#testing new mossy meadows background sound
play_mossy_meadows()
print('Friends. Yelling. Light. A portal.\n')
time.sleep(3)
print('You startle awake, wildly swinging at nothing as you stumble backwards into a tree trunk.\n')
time.sleep(2)
print('You\'re covered in mud and your breathing is ragged. You swear there was a portal behind you.\n')
time.sleep(2)
print('Where is it now?\n')
time.sleep(2)
print('You force your eyes open, taking in your surroundings.\n')
time.sleep(2)
print('A babbling brook. Tiny huts made of straw and twigs. Towering trees. Flowers everywhere.\n')
time.sleep(2)
print('Your panic fades as you stare at this storybook forest. It\'s like you\'ve fallen into a fairytale.\n')
time.sleep(2)
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
print('"It\'s awake!", a tiny mushroom squeals. You jolt upright. A talking mushroom? \n\n"Poppy! Stop frightening our guest!"\n')
time.sleep(3)
player_name = input('What is your name? \n>>> ')
print()
print(f'"I\'m Poppy! And this is Master Oakley!" \n\n"Welcome to Mossy Meadows, {player_name}", says Oakley. "I\'ve never seen you here before."\n')
time.sleep(2)
print('"I...don\'t know why I\'m here."\n')
time.sleep(2)
print('Oakley nods. "Rest for now, we can talk later"\n')
time.sleep(2)
print()
linebreak()
clear()
time.sleep(5)
linebreak()
print()
print('Later that afternoon, Master Oakley offers to show you the village.\n')
time.sleep(3)
print('The market is small, but lively. Frogs bid on flies. Snails buy new shells. Flowers are everywhere.\n')
#Since my game is very text based, the player doesn't really have a chance to customize their avatar. 
#So, I wanted to add the text based equivalent, but letting them choose and accessory from the market!
print('Poppy tugs at your arm, leading you to a small, candy colored street filled with vendors stalls.\n')
print('"Everyone needs something from Marsh Market." she says with a smile.\n')
time.sleep(2)
print('"What will it be?" asks the vendor.\n')
print('1. A light blue shawl\n2. A wooly green coat\n3. A purple wizard\'s hat with stars\n')
time.sleep(2)
player_item =input('Enter 1, 2, or 3 >>>').strip()
print()
if player_item == '1':
    print('"That so cute! Good choice.", Poppy exclaims.')
elif player_item == '2':
    print('"Ah, nights here can get chilly. I have one of my own.", Oakley says.')
elif player_item == '3':
    print('"You look like a real wizard!", Poppy joked.')
else:
    print('You nervously shake your head. "No thank you!", you say as you awkwardly shuffle back to the main road.\n')
time.sleep(2)
print()
print('"Where are you from?" Poppy asks.\n')
time.sleep(3)
print('"Earth."\n')
time.sleep(3)
print('She blinks. "I\'ve never heard of it."\n')
time.sleep(3)
print('...\n')
time.sleep(2)
print('By the time you return to the cottage, only one thought fills your mind.\n')
time.sleep(3)
print('How do I get home?')
print()
linebreak()
clear()
time.sleep(3)
linebreak()
print()
print('That evening, Oakley knocks on your door.\n')
print('"I\'ve been thinking about what you told me."\n')
time.sleep(2)
print('You look up.\n')
time.sleep(2)
print('"There may be a way to return home."\n')
time.sleep(2)
print('"Really?"\n')
time.sleep(2)
print('He nods.\n')
time.sleep(2)
print('"Long ago, a wizard named Nox was cursed and trapped within his own shadow. Legend says that anyone who breaks his curse is granted one wish."\n')
time.sleep(2)
print('"So... if I help him..."\n')
time.sleep(3)
print('...\n')
time.sleep(3)
print('"...he may send you home."\n')
time.sleep(3)
print('"How?"\n')
time.sleep(3)
print('"You must restore the magical garden. Complete eight quests, and each one will reward you with a magical plant. \nWhen the garden is full, I\'ll brew a potion strong enough to enter the Briarwood. \n' \
'There, you can find and defeat Nox."\n')
time.sleep(3)
print('He smiles.\n')
#I also wnated to add more character choice here
print('"Are you ready?"\n')
print('1.Absolutely. Let\'s do this!\n2.I\'m not sure what to expect, but I\'ll try.\n')
starting = input('Press 1 or 2 to begin >>>').strip()
if starting == '1':
    print('\n"Excellent. You\'ll be done in no time!"')
elif starting == '2':
    print('\n"Poppy and I will be here every step of the way."')
else:
    print(f'\n"Don\'t be afraid! You can do this {player_name}!", Poppy says.')
time.sleep(2)
print()
linebreak()
#Well, first, I need to tell the user about sustainability, and how it is important to take care of the enviorment! 
clear()
linebreak()
print()
print('"Before you begin your quest, I want to tell you a little bit about sustainability." Oakley says.')
print()
time.sleep(3)
print('It focuses on making conscious choices to limit environmental impact that can be incorporated into your lifestyle.')
print()
time.sleep(3)
print('Sustainable living doesn\'t have to be difficult or expensive! You can make a big difference by making small changes in your daily life.')
print()
time.sleep(3)
input('Press enter to continue...')
print()
stop_music()
linebreak()
clear()
#Now, I can basically use a while loop to keep the game going until the user has finished all of the quests. 
while quests_completed < len(quests):
    linebreak()
    print()
    print(f'Quest {quests_completed+1}: {quests[quests_completed]}')
    print()
    done = input('Type "done" when you\'ve finished the quest! ').strip().lower()
    print()
    if done == 'done':
        play_correct_sound()
        print(f'{complete_messages[quests_completed]} {player_name}! You have completed the quest!')
        print()
        time.sleep(2)
        print(f'Here is some extra information about the quest: {quest_explanations[quests_completed]}')
        print()
        time.sleep(4)
        print(f'You have added a plant to your garden!')
        print()
        garden[quests_completed] = plants[quests_completed]
        for i in garden:
            print(i," ", end='')
        print('\n')
        water_garden()
        #playing magical chime sound effect here 
        play_chime_sound()
        print()
        if quests_completed == 3:
            print('You\'re halfway there! Keep going!')
        else:
            pass
        quests_completed +=1
        time.sleep(2)
        clear()
        stop_music() #I know that the music will stop, but just incase I missed it earlier
    else:
        print()
        print('Please type "done", when you are finished. You can do it! ')
        time.sleep(2)
        clear()
        continue
linebreak()
print()
print('Congratulations! You have finished all of the quests and filled your garden!')
for i in garden:
    print(i, end ="")
print()
time.sleep(3)
clear()

#Now, to make the end sequence of the story before the character enters the Briarwood (fictional forest where the villan lives)
linebreak()
print()
time.sleep(2)
print('You did it! You\'re one step closer to finally going back home.\n')
time.sleep(3)
print('You wonder if your friends back home are looking for you.\n')
time.sleep(3)
print('Guess you\'ll find out soon enough.\n')
linebreak()
time.sleep(2)
clear()
linebreak()
print()
print('You excitedly tell Master Oakley that you have completed all of the quests and collected the plants.\n')
time.sleep(3)
print(f'"Well done {player_name}. I knew you could do it.", Master Oakley says, smiling.\n')
time.sleep(3)
print(f'"Now, I will brew a potion to help you enter the Briarwood, a dangerous, enchanted forest where Nox lives."\n')
time.sleep(3)
print(f'"Defeating Nox will not be easy. He will ask you some difficult questions that you must answer."\n')
time.sleep(3)
print(f'"The potion will give you three chances to answer all of the questions to defeat Nox."\n')
time.sleep(3)
print(f'"Should you succeed..."\n')
time.sleep(2)
print('...\n')
time.sleep(3)
print('...The wish will be mine. I can finally go home!\n')
time.sleep(3)
print(f'"Let\'s get to work"\n')
input('Press enter to brew the potion...\n')
clear()
potion_brewing()
print()
print(f'"I\'m gonna miss you! Be careful out there!" says Poppy.\n')
print()
input('Press enter to begin the final battle...')
linebreak()
clear()
#This is the scene where the character enters the Briarwood and finds Nox.
time.sleep(3)
linebreak()
print()
print('You hesitate for just a second.\n')
time.sleep(2)
print('Deep breaths.\n')
time.sleep(2)
print('You pour the potion on yourself.\n')
time.sleep(2)
print('It feels tingly.\n')
time.sleep(2)
print('The world is spinning.\n')
time.sleep(2)
print('You fall to the ground.\n')
print()
linebreak()
clear()
time.sleep(3)
linebreak()
print()
play_briarwood()
print('You hear something rustling.\n')
time.sleep(2)
print('You feel the dirt squelch in your palms.\n')
time.sleep(2)
print('You force yourself up, head still spinning.\n')
time.sleep(2)
print('You\'re in the Briarwood. You look around.\n')
time.sleep(2)
print('Dead trees, fog, and the unforgiving cold threaten to choke your resolve.\n')
time.sleep(3)
print('How do you find Nox?\n')
time.sleep(2)
print('Nox! You call out.\n')
time.sleep(2)
print('You wander some more, unsure of exactly how you\'re supposed to find him.\n')
time.sleep(4)
print('Nox! I\'ve come to free you!\n')
time.sleep(2)
print('I\'ve come to...\n')
time.sleep(2)
print('\033[0;31mWHO DARES TO ENTER MY HOME UNINVITED!\033[0m')
time.sleep(1)
print()
linebreak()
clear()
time.sleep(3)
linebreak()
print()
print('The ground shakes as you turn around.\n')
time.sleep(2)
print('An impossibly tall shadow looks down at you. Menacing green eyes, purple smoke.\n')
time.sleep(4)
print('Are those claws or teeth?\n')
time.sleep(2)
print('You shake.\n')
time.sleep(2)
print('\033[0;31mLEAVE. NOW!\033[0m\n')
time.sleep(2)
print('I\'ve come to free y-\n')
time.sleep(2)
print('\033[0;31mGET OUT!\033[0m\n')
time.sleep(2)
print('I can help you! I can free you from your curse! \n')
time.sleep(2)
print('\033[0;31mHA! HUMANS. DELUSIONAL. IMPULSIVE. I KNOW YOUR TYPE. YOU THINK YOU CAN BEST ME?\033[0m\n')
time.sleep(4)
print('\033[0;31mTHIS IS YOUR LAST CHANCE.\033[0m\n')
time.sleep(2)
print('I will free you.\n')
time.sleep(2)
print('\033[0;31mAND WHAT IS IT YOU WISH TO GAIN FROM RELEASING ME FROM MY SHADOW?\033[0m\n')
time.sleep(2)
#Here I want to add a bit more story so teh player can reveal their true motivations! 
#I think this will make the story feel more fun and interactive. 
print('1.I want to return home.\n2.I want to help you.\n3.I believe everyone deserves a second chance.\n')
climax_feeling = input('Press 1, 2, or 3 >>> ').strip()
print()
if climax_feeling == '1':
    print('\033[0;31mNOT AS NOBLE AS YOU SEEM TO THINK EH?\033[0m\n')
elif climax_feeling == '2':
    print('\033[0;31mYOU\'RE LYING. HUMANS. ALWAYS TRYING TO WEASEL THEIR WAY OUT OF THINGS!\n')
elif climax_feeling == '3':
    print('...')
    time.sleep(2)
    print('\033[0;31mYOU\'RE WASTING YOUR TIME.\033[0m\n')
time.sleep(3)
print('\033[0;31mVERY WELL.\033[0m\n')
time.sleep(2)
print('\033[0;31mI WILL ASK YOU 8 QUESTIONS. SHOULD YOU ANSWER THEM CORRECTLY, YOU CAN HAVE YOUR WISH.\033[0m\n')
time.sleep(2)
print('...\n')
time.sleep(2)
print('And if I don\'t?\n')
time.sleep(3)
print('\033[0;31mWHEN YOU FAIL, I WILL FEAST ON YOUR SOUL. IT\'S BEEN QUITE SOMETIME SINCE I HAD A NICE MEAL.\033[0m\n')
time.sleep(2)
print('You remember Master Oakley. And Poppy. They believed in you.\n')
time.sleep(2)
print('Alright. I\'ll do it.\n')
time.sleep(3)
print('\033[0;31mEXCELLENT.\033[0m')
print()
time.sleep(1)
linebreak()
clear()
time.sleep(3)
linebreak()
#Main quests sequence is comeplete! Now, I will make the final boss battle sequence. It will be an 8 question quiz, user has 3 lives. 
for question in quiz_questions:
    print()
    print(f'Question: {quiz_questions[question]}')
    user_answer = input('Type answer here: ').strip().lower()
    if user_answer in quiz_answers[question]:
        play_correct_sound()
        print('\033[0;32mCorrect ✅\033[0m')
    else:
        play_error_sound()
        print('\033[0;31mIncorrect ❌\033[0m')
        lives -=1
        if lives == 0:
            print('You lost! The potion is wearing off, you must retreat!\n')
            time.sleep(3)
            print('\033[0;31mI\'VE ENTERTAINED YOU LONG ENOUGH. TIME TO FEAST.\033[0m\n')
            print()
            input('Press enter to flee the Briarwood:')
            break
        if lives == 1:
            print('You are down to your last life! Be careful! Lives: ❤️ \n')
            time.sleep(1)
            print()
            print(f'\033[0;31mNOT SO CONFIDENT NOW ARE YOU {player_name}! YOU\'LL TASTE DELICIOUS.\033[0m')
        if lives >=2:
            print(f'You now have {lives} lives:', end ='')
            print(lives*'❤️ ')
    time.sleep(4)
    clear()
    print()
stop_music()
#Now We need to check how many lives the player has left. As long as they have more than 0, they get the happy ending. 
if lives> 0:
    good_ending()
    print()
    print('\033[0;32mYou are the Eco_Warrior ⚔️🌎⚔️ ! Our world needs you now more than ever! Use what you\'ve learned to help our environment! 🌎\033[0m')
    print()
    for i in garden:
        print(i, end ="")
    print()
else:
    sad_ending()
    print()
    print('\033[0;32mHello. I\'m a magic forest sprite.\033[0m\n')
    time.sleep(2)
    print('\033[0;32mI can give you another chance.\033[0m\n')
    time.sleep(2)
    print('\033[0;32mYou can erase the past and try to change fate. Do you want to?\033[0m\n')
    print()
    play_again = input('\033[0;32mType "yes" to play again. Type no to stay in Mossy Meadows.\033[0m\n>>> ').strip().lower()

    while play_again != 'yes' and play_again != 'no':
        print('\033[0;32mInvalid input. Please type "yes" or "no".\033[0m')
        play_again = input('\033[0;32mType "yes" to play again. Type no to stay in Mossy Meadows.\033[0m\n>>> ').strip().lower()

    if play_again == 'yes':
        stop_music()
        print('\033[0;32mLearn from your mistakes. You have another chance, make the most of it!\033[0m')
        time.sleep(3)
        restart()
    else:
        print('\033[0;32mI understand. But one defeat does not define you. Never stop learning, Eco-Warrior!\033[0m')
        stop_music()