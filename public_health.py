import time
# display header for adventure game
print('+++++++++++++++++++++++++++++++++++++')
print('Welcome to the COVID Safety/Public Health Adventure Game')
time.sleep(1) 
# set language variable based on user input
language = input('Please pick a language, enter e for English or s for Spanish: ')
if language == 's': # create path for Spanish language version of game
    print('Hola') 
else:
    play_game = input('Are you ready to play? enter y or n: ')
    # start main game loop, continues until play_game set to n
    while play_game != 'n':
        print('Good morning, it is time to go to school')
        time.sleep(2)
        print ('Remember to be safe on your way to school because of the Pandemic')
        time.sleep(2)
        # player must choose an item to bring to school
        print ('It is time to go to the bus stop, you can bring one extra item to school')
        item = input('Do you want to bring a bandana (b), a fidget spinner (f), a mask (m) or a kazoo (k) :')
        while not (item == 'b' or item == 'f' or item == 'm' or item == 'k'): # error check inputs values
            item = input('Please enter b for bandana, f for fidget spinner, m for mask or k for kazoo: ') 
        # player goes to bus stop and is called over by friend
        print ('It is almost time for the bus, you better hurry to the bus stop!')
        time.sleep(2)
        print ('You arrive at the bus stop and see your friend Pat, they ask you to look at something')
        time.sleep(2)
        print ('They motion you to come closer')
        time.sleep(1)
        distance = input('How close should you get? enter the number of feet: ')
        distance = int(distance) # change input from text string to integer
        if distance < 6: # player loses game if distance less than 6
            print('Always remember to distance yourself from others')
            time.sleep(2)
            print ('Your friend might have COVID and now you are now a close contact, please Quarantine for two weeks')
            time.sleep(2)
            print ('Sorry, you did not win this time')
            play_game = input('Do you want to play again, y or n: ')
        else: # player enters 6 or greater
            print('You were smart to stay at least 6 feet away from your friend')
            time.sleep(2)
            print ('It is time to get on the bus, did you remember to bring a mask?')
            time.sleep(2)
            if item != 'm':
                print ('Sorry, you forgot to bring a mask and cannot get on the bus!')
                time.sleep(2)
                print ('You will need to return home to find a way to get to school')
                play_game = input('Do you want to play again, y or n: ')
            else:
                print ('Good thing you remembered to bring your mask')
                time.sleep(2)
                # bus brings students to school, they arrive and have hand sanitizer choice
                print ('The bus brings you to school and there is a line waiting for hand sanitizer')
                time.sleep(2)
                print ('Your friend Pat notices another open door and motions you to follow them into the school')
                time.sleep(2)
                choice = input ('Do you wait for hand sanitizer (s) or follow your friend (f)? :')
                while not (choice == 's' or choice == 'f'): # error checking to ensure correct input
                    choice = input('Please enter s for Sanitizer, f to follow your friend :')
                if choice == 'f': # bad choice, you lose
                    print ('Since you missed the hand sanitizer station, the Principal sends you to Quarantine')
                    play_game = input('Do you want to play again, y or n: ')
                else:
                    print('Smart choice to wait for hand sanitizer, frequent hand cleaning is important!')
                    time.sleep(2)
                    # students make it to classroom
                    print('You arrive in your classroom and get settled')
                    time.sleep(1)
                    print('Your teacher announces a very special field trip for the whole class') 
                    time.sleep(2)
                    print('However, only the whole class can go together, no one can be left out')
                    time.sleep(2)
                    # player makes vaccination choice
                    print('In order to go, everyone in the class needs to be vaccinated')
                    vax = input('Are you willing to be vaccinated for the field trip? y or n :')
                    if vax == 'n':
                        print('You are the only one in the class that refused the vaccine')
                        time.sleep(2)
                        print('The field trip is cancelled and the class is very sad')
                        play_game = input('Do you want to play again, y or n: ')
                    else: # path to victory!
                        print('Smart choice to get vaccinated!')
                        time.sleep(2)
                        print('Sometimes the choices we make for ourselves benefit others!')
                        time.sleep(2)
                        print('Everyone has an amazing time on the field trip')
                        time.sleep(2)
                        print('You made smart COVID safety and public health choices - YOU WIN!!')
                        play_game = 'n'
                    




