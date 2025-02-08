def start():
    portal = input("You find yourself in a Waffle House at 2am. You munch on a delicious waffle and "
               "hash browns. The waitress who took your order was definitely not sober, " 
               "and the cook has been giving you the stink eye. Feeling uncomfortable, you "
               "decide to enter the bathroom. Big mistake. You finish doing your business and "
               "try to flush, but the toilet shakes slightly and nothing happens. Slightly "
               "perturbed, you try again. The toilet shakes more violently, but it still doesn't "
               "flush. You try one more time, and the entire room shakes, causing you to fall "
               "on the ground. When you regain your bearings, you notice that three portals have "
               "suddenly materialized in front of you. Do you want to enter the RED portal, the "
               "BLUE portal, or the GREEN portal? ").lower()
    if portal == "red":
        red_portal()
    elif portal == "blue":
      blue_portal()
    elif portal == "green": 
       green_portal()
    else:
      invalid_choice()
      start()

def red_portal():
      door = input("You enter the red portal and find yourself in a hallway made completely of shiny metal "
          "sheets. To the left, you see three prison cells. The doors are made of glass, with a control " 
           "panel next to each one, and you can see a person in each cell. The first person is the " 
           "largest person you have ever seen, with muscles that look like they could crush a car. "
           "The second person is a little girl curled up in the corner of her cell. This third is "
           "a nondescript man, normal in every respect. He stands in the middle of his cell, blinking "
           "and looking around, seemingly taking in the scenery, although there is no scenery to "
           "take in. You notice two doors, one in FRONT of you and one BEHIND you. Which door do you "
           "enter? ").lower()
      if door == "front":
            front_door()
      elif door == "behind":
             behind()
      else:
            invalid_choice()
            red_portal()

def front_door():
      prisoner = input("You enter the door in front, and find yourself in the cockpit of the ship. The pilot remains "
              "completely focused on flying the ship. Through the window at the front, you can see "
              "various astral bodies passing by at blinding speed. The pilot weaves in and out of "
              "these bodies with inhuman skill and precision. You walk around front to look at his face "
              "and he appears to be human, except his eyes are abnormally large, clearly adapted to "
              "more easily see and adapt to the various obstacles one might find in the void of space. "
              "He continues to focus on his work in silence. When you start to leave, you notice that "
              "the entire floor is beginning to flood. A man in a crew uniform runs in panicking. "
              "'The toilets in the cells are overflowing!' he yelled. 'We've got to evacuate before "
              "the ship is completely flooded!' He runs out of the cockpit and you follow. He stops "
              "in front of the three cells and looks at you. 'We have to choose one to free if we're "
              "going to survive in space,' he says. 'The horrors of deep space are far too dangerous "
              "for us to face alone.' He gestures to the prisoners. 'Each of these specimens possesses "
              "unique abilites that may be helpful. Our goal now is to simply survive.' He nods toward "
              "the large man. 'We found this this one in a barfight on  the Broslod system.' He next "
              "gestures to the girl. 'We picked her up on our way back from the gas station. She's "
              "a Psionic, so naturally, the Galactic Imperium has to execute her.' He curled his lip "
              "in disgust at this. 'Nevertheless, she and he would both be great assets in defending "
              "us from whatever abberations await us in the cosmos.' You point towards the normal "
              "man. 'What about him?' you ask. 'Him?' the crewman chuckled. 'We found him "
              "in sector X4. A dirty, rotten scoundrel. He would have been severely punished, had the "
              "ship completed its course to the volcanic execution chambers of Ragnar.' Unable to "
              "tell if the man is being sarcastic about the atrocities of loitering, you continue "
              "to watch the apparent criminal, who continues to smile absentmindedly as the ship "
              "continues to fill with water, which has now passed the point of your waist. The "
              "loiterer is intently studying a butterfly that had somehow found its way into the ship "
              "wearing the same innocent smile. The crew member turns to you again. 'I don't know why, "
              "stranger, but I fell I should trust your judgment, and my gut is rarely wrong. Whom should "
              "we take with us, the LARGE MAN, the GIRL, or the LOITERER?").lower
      if prisoner == "large man":
                large_man()
      elif prisoner == "girl":
             girl()
      elif prisoner == "loiterer":
             loiterer()
      else:
            invalid_choice()
            front_door()

def large_man():
      direction = input("'Uhhhhh...the big guy,' you say. The crewman nods and uses the control "
                              "panel to open the cell. The burly man walks out with a wicked grin on his "
                              "face. 'Alright, spacesuits are over here,' the crewman says, leading you "
                              "to the back of the ship. He hands a suit to you and the large man,and you "
                              "both put them on. The crewman adjusts his suit and holds his hand over a "
                              "large, red button. 'There is no pod on this ship, so we'll be ejected "
                              "directly into the vacuum of space.' He looks at you. 'I'll follow you. "
                              "As for the brute, I'll make sure he follows,' he said , gesturing to a "
                              "device on his belt. Without any time to question the moral implications "
                              "of this statement, he presses the button. The floor drops and ejects all "
                              "three of you into the void. You turn, squinting your eyes. There appear to be "
                              "systems to the LEFT, RIGHT, and in FRONT of you. Which way will you go?").lower()
      if direction == "left": 
                    go_left_large()
      elif direction == "right":
                        go_right_large()
      elif direction == "front":
             go_front_large()
      else:
            invalid_choice()
            large_man()

def go_left_large():
      print("You head left, and the large man and crewman follow. As you fly forward, you start "
                          "to make out a creature in the distance. It is a massive, bulbous creature with five "
                          "long necks ending in hideously beautiful heads. Looking at the heads, you can tell "
                          "that each one resembles a different member of popular boy band, One Direction. "
                          "However, none of the heads have mouths. The creature's only mouth lies in the center "
                          "of its body, a huge maw that is grinning wickedly. Before you have a chance to ask "
                          "how you got into its gravitational pull, the creature opens its mouth and begins to "
                          "sing a conveniently expositional song called 'You Just Got Pulled Into My Gravity,' "
                          "which goes something like this: \n'Yeah, you just got pulled into my gravity, "
                          "\nIrresistibly and uncontrollably drawn to me. \nI wish we still had time to say hi, "
                          "\nBut unfortunately, you must die. \nThe creature finishes singing its song, the "
                          "only thing worse than its lyrics being its generic chord progression. You look over at the "
                          "crewman, who shakes his head. 'Man, their lyrics get worse every time.' Thinking that this "
                          "a bit of an odd sentiment for one to express when faced with their imminent death, you "
                          "suddenly see the burly man rush forward and deliver a space punch that sends the creature "
                          "flying far in the distance, shouting a G Major chord as it goes. With that threat out of "
                          "the way, you notice what appears to be a stapler slowly moving towards you. Even as you "
                          "watch, a staple-shaped spaceship emerges from the stapler, flying straight at you. "
                          "Before you have time to react, the ship fires a tractor beam at you, pulling you in. " 
                          "Once inside the spaceship, the captain greets you. 'Welcome to Staples Rescue Service,' "
                          "he says. 'After humanity's move to space, office supplies didn't seem to cut it for us "
                          "anymore. Anyway, it's time for you to go home.' He turns to the cockpit, when you realize "
                          "that you can't remember the way back to the Waffle House. You win!")
      restart()
     
def go_right_large():
      print("You head right, and before you know it, you've entered the atmosphere of another planet. "
                              "You land on the surface, and take in your surroundings. You're surrounded by humanoid "
                              "creatures who are completely covered with thick hair of various coolors. The creatures "
                              "are lazily bobbing their heads in perfect unison to Dark Side of the Moon, which is "
                              "playing from a nearby record player. 'Oh great,' says the crewman, as 'Time' swells into "
                              "its chorus. 'Space Hippies,' he says. Just then, the burly man lets out a roar and charges. "
                              "Before you or the crewman can object, the creatures turn on you and trample all three of you. "
                              "You lose.")
      restart()

def go_front_large():
      print("You head forward, and are closely followed by the crewman and the burly man. You aren't "
                              "able to make it very far when you see a massive, humanoid figure standing in space. "
                              "The creature is incomprehensibly huge. Its head is the size of a planet, but appears to "
                              "be human in every other respect. He's clutching a microphone the size of an asteroid field. "
                              "'Wonderful,' says the creature with a smile, his voice booming through the void. 'You're just in time "
                              "to hear me test out my karaoke machine.' Just then, the unmistakable opening notes of "
                              "'Sweet Caroline' echo throughout the void. As the creature begins to sing, the burly man audibly groans. "
                              "'Uh-oh,' says the crewman. The creature spins toward you. 'You DARE disrespect Neil Diamond?' "
                              "he bellows. Before you have time to react, the creature flares its nostrils, which fire two "
                              "massive beams of energy, incinerating all three of you. You lose.")
      restart()

def girl():  
      direction = input("'How about the girl?' you say. The crewman nods and uses the control "
                              "panel to open the cell. The girl walks out and nervously looks around. "
                              "'Alright, spacesuits are over here,' the crewman says, leading you "
                              "to the back of the ship. He hands a suit to you and the girl, and you "
                              "both put them on. The crewman adjusts his suit and holds his hand over a "
                              "large, red button. 'There is no pod on this ship, so we'll be ejected "
                              "directly into the vacuum of space.' He looks at you. 'I'll follow you. "
                              "As for the girl, I'll make sure she follows,' he said , gesturing to a "
                              "device on his belt. Without any time to question the moral implications "
                              "of this statement, he presses the button. The floor drops and ejects all "
                              "three of you into the void. You turn, squinting your eyes. There appear to be "
                              "systems to the LEFT, RIGHT, and in FRONT of you. Which way will you go?").lower()
      if direction == "left":
                    go_left_girl()
      elif direction == "right":
                    go_right_girl()
      elif direction == "front":
                    go_front_girl()
      else:
            invalid_choice()
            girl()

def go_left_girl():
      print("You head left and the girl and crewman follow. As you fly forward, you start"
                          "to make out a creature in the distance. It is a massive, bulbous creature with five"
                          "long necks ending in hideously beautiful heads. Looking at the heads, you can tell"
                          "that each one resembles a different member of popular boy band, One Direction."
                          "However, none of the heads have mouths. The creature's only mouth lies in the center"
                          "of its body, a huge maw that is grinning wickedly. Before you have a chance to ask"
                          "how you got into its gravitational pull, the creature opens its mouth and begins to"
                          "sing a conveniently expositional song called 'You Just Got Pulled Into My Gravity,'"
                          "which goes something like this: \n'Yeah, you just got pulled into my gravity,"
                          "\nIrresistibly and uncontrollably drawn to me. \nI wish we still had time to say hi,"
                          "\nBut unfortunately, you must die. \nThe creature finishes singing its song, the"
                          "only thing worse than its lyrics being its generic chord progression. You look over at the"
                          "crewman, who shakes his head. 'Man, their lyrics get worse every time.' Thinking that this"
                          "a bit of an odd sentiment for one to express when faced with their imminent death, you"
                          "suddenly hear the girl shout, 'I can't control all five brains at once!' The creature"
                          "grins more widely, and it rushes towards you, eating all three of you in a single gulp. You lose.")
      restart()

def go_right_girl():
      print("You head right, and before you know it, you've entered the atmosphere of another planet. "
                              "You land on the surface, and take in your surroundings. You're surrounded by humanoid "
                              "creatures who are completely covered with thick hair of various coolors. The creatures "
                              "are lazily bobbing their heads in perfect unison to Dark Side of the Moon, which is "
                              "playing from a nearby record player. 'Oh great,' says the crewman, as 'Time' swells into "
                              "its chorus. 'Space Hippies,' he says. You wait around for a bit, unsure how to react to the "
                              "situation. One of the creatures suddenly walks forward. It grunts and gestures toward a tube "
                              "in its hand. 'Teleportation powder,' says the crewman. 'If you snort it, it'll take "
                              "you home. You gratefully, albeit reluctantly, accept the teleportation powder "
                              "and inhale it with a mighty snort. Suddenly, you find yourself back in the Waffle House "
                              "bathroom. 'Darn it!' you shout. 'That's the third time this week that toilet's done that!' "
                              "With that, you turn and exit the bathroom to finish your hash browns. You win!")
      restart()

def go_front_girl():
      print("You head forward, and are closely followed by the crewman and the girl. You aren't "
                              "able to make it very far when you see a massive, humanoid figure standing in space. "
                              "The creature is incomprehensibly huge. Its head is the size of a planet, but appears to "
                              "be human in every other respect. He's clutching a microphone the size of an asteroid field. "
                              "'Wonderful,' says the creature with a smile, his voice booming through the void. 'You're just in time "
                              "to hear me test out my karaoke machine.' Just then, the unmistakable opening notes of "
                              "'Sweet Caroline' echo throughout the void. As the creature begins to sing, he sudennly "
                              "whips around to face the girl. 'You just tried to alter my mind!' he bellows. 'You'll "
                              "pay dearly for this!' With that, he lets out an incomprehensibly loud belch that shatters your "
                              "bones into dust. You lose.")
      restart()

def loiterer():
      direction = input("'The loiterer,' you say. The crewman nods and uses the control "
                              "panel to open the cell. The loiterer walks out and smiles at you. "
                              "'Alright, spacesuits are over here,' the crewman says, leading you "
                              "to the back of the ship. He hands a suit to you and the loiterer, and you "
                              "both put them on. The crewman adjusts his suit and holds his hand over a "
                              "large, red button. 'There is no pod on this ship, so we'll be ejected "
                              "directly into the vacuum of space.' He looks at you. 'I'll follow you. "
                              "As for the loiterer, I'll make sure he follows,' he said , gesturing to a "
                              "device on his belt. Without any time to question the moral implications "
                              "of this statement, he presses the button. The floor drops and ejects all "
                              "three of you into the void. You turn, squinting your eyes. There appear to be "
                              "systems to the LEFT, RIGHT, and in FRONT of you. Which way will you go?").lower()
      if direction == "left":
                    go_left_loiterer()
      elif direction == "right":
                    go_right_loiterer()
      elif direction == "front": 
                    go_front_loiterer()
      else: 
            invalid_choice()
            loiterer()

def go_left_loiterer():
      print("You head left and the loiterer and crewman follow. As you fly forward, you start "
                          "to make out a creature in the distance. It is a massive, bulbous creature with five "
                          "long necks ending in hideously beautiful heads. Looking at the heads, you can tell "
                          "that each one resembles a different member of popular boy band, One Direction. "
                          "However, none of the heads have mouths. The creature's only mouth lies in the center "
                          "of its body, a huge maw that is grinning wickedly. Before you have a chance to ask "
                          "how you got into its gravitational pull, the creature opens its mouth and begins to "
                          "sing a conveniently expositional song called 'You Just Got Pulled Into My Gravity,' "
                          "which goes something like this: \n'Yeah, you just got pulled into my gravity, "
                          "\nIrresistibly and uncontrollably drawn to me. \nI wish we still had time to say hi, "
                          "\nBut unfortunately, you must die. \nThe creature finishes singing its song, the "
                          "only thing worse than its lyrics being its generic chord progression. You look over at the "
                          "crewman, who shakes his head. 'Man, their lyrics get worse every time.' Thinking that this "
                          "a bit of an odd sentiment for one to express when faced with their imminent death, you "
                          "hear the loiterer. 'Wow guys, that was great!' he says. The creature turns toward him "
                          "and smiles widely. 'You really think so?' asked the creature, still speaking with five "
                          "voices at once. 'I mean, during rehearsals I thought I was kinda pitchy.' 'No, dude,' "
                          "continues the loiterer. 'You were great! I've always loved all you guys, especially "
                          "Harry!' The creature's smile widens. 'Did you hear that?' asked the creature, now speaking "
                          "only with one voice, the unmistakable voice of Harry Styles. 'He thought I was the best! "
                          "'Yeah, but clearly I'm better!' interjects Liam's voice. 'No way,' says Zayn. 'The girls' "
                          "'ALWAYS thought I was the best!' The creature continues to argue with itself while the loiterer "
                          "nervously attempts to retract his statement. Before he can, however, the creature seems to "
                          "decide it needs an outlet for its anger and eats all three of you. You lose.")
      restart()

def go_right_loiterer():
      print("You head right, and before you know it, you've entered the atmosphere of another planet. "
                     "You land on the surface, and take in your surroundings. You're surrounded by humanoid "
                     "creatures who are completely covered with thick hair of various coolors. The creatures "
                     "are lazily bobbing their heads in perfect unison to Dark Side of the Moon, which is "
                     "playing from a nearby record player. 'Oh great,' says the crewman, as 'Time' swells into "
                     "its chorus. 'Space Hippies,' he says. 'You know,' says the loiterer, 'I never did like "
                     "Pink Floyd.' The crewman and you both look at him in shock. 'You...you MONSTER! You've "
                     "doomed us all!' The crewman shouts. Before you can react, the loiterer is suddenly trampled by "
                     "the creatures, who are now dancing to 'Money.' They don't seem to be picky about whom they trample, "
                     "and run you and the crewman down as well. You lose.")
      restart()

def go_front_loiterer():
      print("You head forward, and are closely followed by the crewman and the loiterer. You aren't "
                           "able to make it very far when you see a massive, humanoid figure standing in space. "
                            "The creature is incomprehensibly huge. Its head is the size of a planet, but appears to "
                            "be human in every other respect. He's clutching a microphone the size of an asteroid field. "
                            "'Wonderful,' says the creature with a smile, his voice booming through the void. 'You're just in time "
                            "to hear me test out my karaoke machine.' Just then, the unmistakable opening notes of "
                            "'Sweet Caroline' echo throughout the void. The creatures sings along, and as it swells into "
                            "its chorus, the loiterer joins in. Pretty soon, the loiterer and the creature are singing "
                            "in perfect two-part harmony. The song ends, and the creature lets out a deep breath. "
                            "'Wow!' it says. 'I haven't felt that good in millenia!' It lets out another breath. "
                            "'For this super dope collab, I will grant one wish to one of you.' The crewman turns to you. "
                            "'It should be you,' he says. 'Wish to go home.' The loiterer nods in agreement, even though "
                            "he has abosolutely no reason to do so whatsoever. You nod and use your spacesuit to move "
                            "forward. As you do so, your wish becomes clear in your mind. It becomes your sole desire "
                            "and the most important thing to you in the universe. 'I wish,' you say, 'to return "
                            "to the Waffle House bathroom.' The creature snorts. 'Seriously, dude?' it scoffs. 'You "
                            "could have had anything in the universe, and you choose Waffle House?' 'And a million "
                            "dollars!' you interject hastily. The creature snorts again. 'Sorry, buddy, no double "
                            "wishes in my house.' He snaps his fingers, and you find yourself back in the Waffle House "
                            "bathroom. 'You know,' you say, 'That's not the weirdest thing I've ever seen come out of this "
                            "toilet.' With that, you turn and return to your hash browns. You win!")
      restart()

def behind():
      save = input("You enter the door behind you and find a ladder leading downward. With bated breath, "
                          "you descend into the darkness. You reach the bottom and find yourself in a room "
                          "full of crates. You hear the sounds of someone voraciously eating. You poke your way through "
                          "the crates and suddenly see a man lying on the floor of the ship, munching on a dehydrated "
                          "chicken leg. His eyes are closed and he seems really into his chicken leg, so you kind of "
                          "just awkwardly stand there. However, he just continues to munch. Eventually, the awkward silence "
                          "becomes overwhelming, and you clear your throat. Bro continues to munch, so you clear your "
                          "throat more loudly. He finally looks up, sees you, and lets out a small yelp. 'Oh, I'm sorry!' "
                          "he says. 'I didn't see you there!' He drops his chicken leg, wipes his hands on his grease-stained "
                          "shirt, and extends his hand. You take it. Not only is it extremely greasy, but he's also sweating "
                          "profusely. 'Oh, I'm sorry!' he laughs. 'I always get this way when I eat chicken!' 'Okay... "
                          "you say. 'I'm Steve,' he says. 'Stowaway Steve. Or at least, that's what they call me. This "
                          "is the third time I've stowed away this week! I've had nothing but suckers for the past couple "
                          "of days. Hopefully, this ship is on course to a nice, rich system! I might get enough chicken "
                          "to last me a lifetime! The ship's destination is on the monitor over there,' he points to a "
                          "screen on the wall. 'I can't read it, though, but hopefully, it says something good! Can you "
                          "read, starnger?' You look at the monitor more closely. It says, 'Destination: The Volcaninc "
                          "Execution Chambers of Ragnar.' You look back at Steve, who is now looking at you with an expectant "
                          "smile. Not wanting to spoil his excitment, you say, 'Uh, yeah it's great.' He smiles more widely, "
                          "when all of a sudden, you see a puddle of water forming on the floor. The water level is rapidly "
                          "rising, and the need to escape becomes clear. 'Oh, great!' says Steve. 'The toilets must have "
                          "gotten clogged again!' He tries to free himself from the large walls of crates around him, but the "
                          "crates topple, forcing him backward and trapping him further. At this point, the water has reached "
                          "your waist. 'Don't leave me here!' Steve yells. 'I'll drown!' Do you want to save Steve, YES or NO?").lower()
      if save == "yes":
                    save_steve()
      elif save == "no":
                    leave_steve()
      else:
            invalid_choice()
            behind()

def save_steve():
      print("You rush to Steve's side and try to lift the crates off of him. However, they're too heavy "
                          "and the water is rising too quickly. You try to pull him out, but the water has reached your "
                          "chest at this point. Before you know it, you and Steve are completely submerged. You and he "
                          "both drown. Hey, don't blame me, man. You're the one who tried to be a hero. You lose.")
      restart()

def leave_steve():
      prisoner2 = input("You turn away as Steve continues to struggle behind you. 'No!' he yells. 'Don't leave me!' "
                                   "Ignorning him, you continue to make your way to the ladder. 'You'll pay for this!' he "
                                   "continues to yell. 'You hear me, One Who Reads? You'll PAY FOR THIS!!' You finally reach the ladder "
                                   "as the water reaches your chest. You hurriedly begin to climb the ladder, reach the top, and "
                                   "return to the hallway, where a man in a crew uniform is waiting for you. 'The ship is flooding!' "
                                   "he yells. 'Yeah, I noticed,' you reply. Ignoring this, he starts  speaking to you again. 'We have "
                                   "to evacuate the ship, but before we do, we should take a prisoner with us. They'll help us to survive "
                                   "the horrors of deep space. He gestures to the prisoners. 'Each of these specimens possesses "
                                   "unique abilites that may be helpful. Our goal now is to simply survive.' He nods toward "
                                   "the large man. 'We found this this one in a barfight on  the Broslod system.' He next "
                                   "gestures to the girl. 'We picked her up on our way back from the gas station. She's "
                                   "a Psionic, so naturally, the Galactic Imperium has to execute her.' He curled his lip "
                                   "in disgust at this. 'Nevertheless, she and he would both be great assets in defending "
                                   "us from whatever abberations await us in the cosmos.' You point towards the normal "
                                   "man. 'What about him?' you ask. 'Him?' the crewman chuckled. 'We found him loitering "
                                   "in sector X4. A dirty, rotten scoundrel. He would have been severely punished, had the "
                                   "ship completed its course to the volcanic execution chambers of Ragnar.' Unable to "
                                   "tell if the man is being sarcastic about the atrocities of loitering, you continue "
                                   "to watch the apparent criminal, who continues to smile absentmindedly as the ship "
                                   "continues to fill with water, which has now passed the point of your waist. The "
                                   "loiterer is intently studying a butterfly that had somehow found its way into the ship "
                                   "wearing the same innocent smile. The crew member turns to you again. 'I don't know why, "
                                   "stranger, but I fell I should trust your judgment, and my gut is rarely wrong. Whom should "
                                   "we take with us, the LARGE MAN, the GIRL, or the LOITERER?").lower
      if prisoner2 == "large man":
                       large_man2()
      elif prisoner2 == "girl":
                       girl2()
      elif prisoner2 == "loiterer":
                       loiterer2()
      else:
            invalid_choice()
            leave_steve()

def large_man2():
      print("'Uhhhhh...the big guy,' you say. The crewman nods and uses the control "
                        "panel to open the cell. The burly man walks out with a wicked grin on his "
                        "face. Before anything else happens, the ship begins to emit a light ringing sound. 'That's "
                        "the radar!' the crewman says excitedly. 'Another ship is coming to save us!' Through the ship's "
                        "window, you can see the unmistakable shape of the Millenium Falcon. Soon, the ship is boarded by "
                        "a dashing, rougish scoundrel with a cool space vest toting a blaster pistol and his tall, hairy best "
                        "friend. 'No way!' you say. 'It's Han Solo!' The newcomers slowly turn to you, sharing the same "
                        "offended look. 'What did you just call me?' the rogue asks. 'The name's Dumbledore, kid. This "
                        "is my partner-in-crime, Frodo Baggins. You don't know much about Star Trek, do you?' 'Clearly "
                        "confused, he is,' says Frodo, sounding just like Kermit the Frog. 'Okay, what is going on?' you "
                        "ask. 'Oh, we're here to save you,' said Dumbledore. 'We were just on the run from Prince "
                        "Humperdinck. We were smuggling elacca that we harvested on Vulcan. Anyways, hop right on.' You, the "
                        "crewman, and the burly man all board the ship. Unsure what to call it, you turn to Dumbledore. 'What's' "
                        "this ship called anyway?' you ask. 'Chitty Chitty Bang Bang,' Dumbledore replies. 'Why do I even "
                        "ask?' you say to yourself. The ship detaches and begins to fly away. It isn't able to get very far, "
                        "however, when the ship begins to rock violently. 'Uh-oh,' says Frodo. 'Being boarded, we are!' "
                        "The ship shakes again, then stops moving altogether. 'Soemthing's grabbed us!' shouts the "
                        "crewman in distress. Suddenly, the ship is boarded by a familiar face: Stowaway Steve. He is "
                        "closely followed by two creatures, which resemble floating eyeballs with dozens of tentacles. "
                        "'Well, well,' Steve says. 'If it isn't the one who reads.' Dumbledore raises his pistol. 'I'm "
                        "warning you,' he says. 'You either step off this ship, or you get a blast between the eyes.' "
                        "'Stand down, Gandalf,' Steve says. 'The name's DUMBLEDORE!!' Dumbledore shouts, and fires three "
                        "blasts straight at Steve's face. With a lazy wave of his arm, the blasts stop in midair, and redirect "
                        "themselves into Dumbledore's chest, who falls backward. Frodo whimpers slightly. 'You know, "
                        "I never could get those two straight,' he said. 'If I remember correctly, Gandalf is currently "
                        "leading an army of Fremen on Tatooine.' 'How did you survive?' you ask. Steve chuckled. 'Oh, One "
                        "Who Reads,' he says. 'You were really naive enough to believe that I could be stopped by a little "
                        "water? I did end up drowning, but that's beside the point. I was resurrected by these creatures "
                        "here, turning me into a powerful being, bestowing great and terrible abilities upon me, including "
                        "the ability to read. That fateful day, 30 minutes ago, not only did you lie but you also left me to die.' "
                        "'Sensational rhyming, my lord,' one of the eye monsters says telepathically. 'Thank you, George,' Steve "
                        "replied. Suddenly, the burly man roared and charged. Steve easily dodged his approach, got the "
                        "burly man in a headlock, and gave him a noogie. The burly man falls to the ground, incapacitated. "
                        "'Your minions dare defy me, One Who Reads?' Steve roars. 'I have had it with your resistance!' "
                        "With that, he licks his finger and gives you a killer Wet Willie, which punctures through your "
                        "ear and into your brain. You lose.")
      restart()

def girl2():
      print("'How about the girl?' you say. The crewman nods and uses the control "
                        "panel to open the cell. The girl walks out and nervously looks around. "
                        "Before anything else happens, the ship begins to emit a light ringing sound. 'That's "
                        "the radar!' the crewman says excitedly. 'Another ship is coming to save us!' Through the ship's "
                        "window, you can see the unmistakable shape of the Millenium Falcon. Soon, the ship is boarded by "
                        "a dashing, rougish scoundrel with a cool space vest toting a blaster pistol and his tall, hairy best "
                        "friend. 'No way!' you say. 'It's Han Solo!' The newcomers slowly turn to you, sharing the same "
                        "offended look. 'What did you just call me?' the rogue asks. 'The name's Dumbledore, kid. This "
                        "is my partner-in-crime, Frodo Baggins. You don't know much about Star Trek, do you?' 'Clearly "
                        "confused, he is,' says Frodo, sounding just like Kermit the Frog. 'Okay, what is going on?' you "
                        "ask. 'Oh, we're here to save you,' said Dumbledore. 'We were just on the run from Prince "
                        "Humperdinck. We were smuggling elacca that we harvested on Vulcan. Anyways, hop right on.' You, the "
                        "crewman, and the burly man all board the ship. Unsure what to call it, you turn to Dumbledore. 'What's' "
                        "this ship called anyway?' you ask. 'Chitty Chitty Bang Bang,' Dumbledore replies. 'Why do I even "
                        "ask?' you say to yourself. The ship detaches and begins to fly away. It isn't able to get very far, "
                        "however, when the ship begins to rock violently. 'Uh-oh,' says Frodo. 'Being boarded, we are!' "
                        "The ship shakes again, then stops moving altogether. 'Soemthing's grabbed us!' shouts the "
                        "crewman in distress. Suddenly, the ship is boarded by a familiar face: Stowaway Steve. He is "
                        "closely followed by two creatures, which resemble floating eyeballs with dozens of tentacles. "
                        "'Well, well,' Steve says. 'If it isn't the one who reads.' Dumbledore raises his pistol. 'I'm "
                        "warning you,' he says. 'You either step off this ship, or you get a blast between the eyes.' "
                        "'Stand down, Gandalf,' Steve says. 'The name's DUMBLEDORE!!' Dumbledore shouts, and fires three "
                        "blasts straight at Steve's face. With a lazy wave of his arm, the blasts stop in midair, and redirect "
                        "themselves into Dumbledore's chest, who falls backward. Frodo whimpers slightly. 'You know, "
                        "I never could get those two straight,' he said. 'If I remember correctly, Gandalf is currently "
                        "leading an army of Fremen on Tatooine.' 'How did you survive?' you ask. Steve chuckled. 'Oh, One "
                        "Who Reads,' he says. 'You were really naive enough to believe that I could be stopped by a little "
                        "water? I did end up drowning, but that's beside the point. I was resurrected by these creatures "
                        "here, turning me into a powerful being, bestowing great and terrible abilities upon me, including "
                        "the ability to read. That fateful day, 30 minutes ago, not only did you lie but you also left me to die.' "
                        "'Sensational rhyming, my lord,' one of the eye monsters says telepathically. 'Thank you, George,' Steve "
                        "replied. Suddenly, the girl falls to the ground, whimpering. 'Poor girl,' Steve said. 'She just "
                        "tried to engage in a psychic battle with me. Foolish girl. No ordinary Psionic is a match for "
                        "my abilities.' He turns to you. 'Your minions have defied me for the last time, One Who Reads.' "
                        "With that, he grabs your arm and gives you the worst Indian burn you've ever received. The pain "
                        "is so great that you fall to the ground, and all goes black. You lose.")
      restart()

def loiterer2():
      print("'The loiterer,' you say. The crewman nods and uses the control "
                              "panel to open the cell. The loiterer walks out and smiles at you. "
                              "Before anything else happens, the ship begins to emit a light ringing sound. 'That's "
                        "the radar!' the crewman says excitedly. 'Another ship is coming to save us!' Through the ship's "
                        "window, you can see the unmistakable shape of the Millenium Falcon. Soon, the ship is boarded by "
                        "a dashing, rougish scoundrel with a cool space vest toting a blaster pistol and his tall, hairy best "
                        "friend. 'No way!' you say. 'It's Han Solo!' The newcomers slowly turn to you, sharing the same "
                        "offended look. 'What did you just call me?' the rogue asks. 'The name's Dumbledore, kid. This "
                        "is my partner-in-crime, Frodo Baggins. You don't know much about Star Trek, do you?' 'Clearly "
                        "confused, he is,' says Frodo, sounding just like Kermit the Frog. 'Okay, what is going on?' you "
                        "ask. 'Oh, we're here to save you,' said Dumbledore. 'We were just on the run from Prince "
                        "Humperdinck. We were smuggling elacca that we harvested on Vulcan. Anyways, hop right on.' You, the "
                        "crewman, and the burly man all board the ship. Unsure what to call it, you turn to Dumbledore. 'What's' "
                        "this ship called anyway?' you ask. 'Chitty Chitty Bang Bang,' Dumbledore replies. 'Why do I even "
                        "ask?' you say to yourself. The ship detaches and begins to fly away. It isn't able to get very far, "
                        "however, when the ship begins to rock violently. 'Uh-oh,' says Frodo. 'Being boarded, we are!' "
                        "The ship shakes again, then stops moving altogether. 'Soemthing's grabbed us!' shouts the "
                        "crewman in distress. Suddenly, the ship is boarded by a familiar face: Stowaway Steve. He is "
                        "closely followed by two creatures, which resemble floating eyeballs with dozens of tentacles. "
                        "'Well, well,' Steve says. 'If it isn't the One Who Reads.' Dumbledore raises his pistol. 'I'm "
                        "warning you,' he says. 'You either step off this ship, or you get a blast between the eyes.' "
                        "'Stand down, Gandalf,' Steve says. 'The name's DUMBLEDORE!!' Dumbledore shouts, and fires three "
                        "blasts straight at Steve's face. With a lazy wave of his arm, the blasts stop in midair, and redirect "
                        "themselves into Dumbledore's chest, who falls backward. Frodo whimpers slightly. 'You know, "
                        "I never could get those two straight,' he said. 'If I remember correctly, Gandalf is currently "
                        "leading an army of Fremen on Tatooine.' 'How did you survive?' you ask. Steve chuckled. 'Oh, One "
                        "Who Reads,' he says. 'You were really naive enough to believe that I could be stopped by a little "
                        "water? I did end up drowning, but that's beside the point. I was resurrected by these creatures "
                        "here, turning me into a powerful being, bestowing great and terrible abilities upon me, including "
                        "the ability to read. That fateful day, 30 minutes ago, not only did you lie but you also left me to die.' "
                        "'Sensational rhyming, my lord,' one of the eye monsters says telepathically. 'Thank you, George,' Steve "
                        "replied. 'Unfortunately, I must now take you prisoner. I have something very special in mind for "
                        "you,' he says, looking at you. The loiterer sighs and rolls his eyes. 'That's it,' he says. 'I'm "
                        "done with this.' With that, he waves his hand, and Steve and his minions disappear. You turn to "
                        "the loiterer. 'Wait,' you say. 'You could have done that this whole time, and you just didn't? You "
                        "let Dumbledore die?' 'I don't intervene unless absolutely necessary,' replies the loiterer. 'I "
                        "am the Loiterer. Since the beginning of time, I have been loitering everywhere, all the time, "
                        "all at once. I am both everywhere and nowhere.' 'How does that make any sense?' you ask. "
                        "'It doesn't,' he replies. 'At least, not to a lower mind such as your own. My termination would "
                        "disrupt the very fabric of the universe, and this man was certainly powerful enough to cause such "
                        "a rupture. I normally don't do this, but I'm feeling generous. Stranger, I know you're not from "
                        "around here,' he said, indicating you. 'I can send you back to your realm. It's one in which I've "
                        "loitered many times.' With a wave of his hand, all goes fuzzy, and you find yourself back in the "
                        "Waffle House bathroom. 'You know, I think I've had enough toilets for one day,' you say to yourself. With that, you "
                        "turn and return to your table, considering ordering a waffle with chocolate chips. You win!")
      restart()

def blue_portal():
      way = input("You enter the blue portal, and before you know it, you fall in the middle of a conference "
                      "room. The people in the room are well-dressed and are clearly in the middle of a session "
                      "The man at the head of the table speaks up. 'What are you doing in here?' he asks angrily. "
                      "'Sorry,' you say. 'I was just, uh, looking for the bathroom.' Everyone is staring at you, and the "
                      "room is dead silent. 'Oh, looking for the bathroom, were you? And you figured that this room with "
                      "a table and a bunch of people talking was a place you might find a toilet?' You mumble a word "
                      "of apology. 'Speak up!' the man commands. 'I'm sorry,' you say more clearly, waiting "
                      "for someone-anyone-in the room to come to your defense, but no one does. They just continue to look "
                      "at you in silence. 'Well?' the man at the front says. 'What are you waiting for? Get out of here!' "
                      "'Alright,' you say, noticing one door in front of you and one behind you. 'Which door do you want me "
                      "to-' 'Any door!' the man yells. You mumble another apology, and size up each door again. Do "
                      "you want to take the door in FRONT of you, or BEHIND you?").lower()
      if way == "front":
              front_way()
      elif way == "behind":
              behind_way()
      else:
            invalid_choice()
            blue_portal()

def front_way():
      print("You take the door in front of you, everyone watching as you leave. You find yourself in an "
                    "office hallway, and who should be waiting there but your high school math teacher. "
                    "'Well, well, well,' she says. 'If it isn't my worst student of all time.' she says, all "
                    "the while closing in on you, slowly pinning you against the wall. 'Your math skills were "
                    "simply pathetic, the most pathetic I've ever seen, as I recall.' She continues to close "
                    "in on you. You desperately look around for an out or a door of some kind, but the only door "
                    "you can access is the one that will take you back to the conference room, and heaven knows "
                    "you are NOT going back in there. Every step your former teacher takes seems to shake the ground, "
                    "emitting a loud BOOM. BOOM. She takes a step. 'Now look at you,' she said. BOOM. 'Look how far "
                    "you've come.' BOOM. 'Or should I say, how far you've fallen.' BOOM. 'You haven't amounted "
                    "to anything, have you?' BOOM. 'Everything you touch falls apart.' BOOM. 'You are SUCH' "
                    "BOOM. 'A' BOOM. 'FAILURE!!' At this point, she's nose to nose with you. 'Well? What do you "
                    "have to say for yourself?' 'I'm sorry, ma'am,' you offer weakly. 'LOUDER!' she screams, spraying your face with spittle. "
                    "'I'M SORRY!' you yell. 'Much better,' she says. 'What are you?' she asks. 'A failure!' you reply. 'What have "
                    "you amounted to?' 'Nothing!' 'Very good,' she says, although I don't really think this lesson is "
                    "sinking in.' She cracks her knuckles, and that same wicked smile that used to haunt you once again " 
                    "graces her lips.  'It's time for me to show just how pathetic you really are.' With that, she pummels "
                    "you in the stomach, and all goes black. You lose.")
      restart()

def behind_way():
      next = input("You exit the conference room through the door behind you, the entire room watching as you "
                           "do. When you close the door behind you, you turn and find yourself in a labyrinthine "
                           "office hallway, with no map or reference point in sight. You start walking down the hallway: "
                           "first you take a left, then a right, right again, left again, straight across. 'Hold "
                           "on,' you think to yourself. 'Didn't I pass that potted plant already?' You begin to "
                           "panic when you see a man walking down the hallway. 'Excuse me,' you begin. 'Could you "
                           "help me find the way down from here?' The man, pauses, looks at you for a moment, then "
                           "laughs out loud. 'Oh man, that's a good one. You really had me going.' 'But, I really "
                           "need your help,' you start to say, but the man cuts you off. 'Look, this joke is getting "
                           "pretty tired. These halls are some of the easiest to navigate in the world. Everyone "
                           "knows that! At least, everyone who isn't a complete idiot.' He walks off, shaking his head "
                           "as he goes. Feeling just a little offended, you continue trying to navigate the halls, each "
                           "and every wall lacking any kind of map or reference. Finally, you find an elevator and press "
                           "the down button. The elevator doors open, and you get in, standing next to a man in an "
                           "overcoat with graying hair. He regards you for a bit, then speaks. 'How goes it today?' he "
                           "asks you politely. This being the only remotely normal interaction you've had today, you "
                           "let down your guard. 'Honestly,' you say, 'I don't know where I am, what this place is, or "
                           "why everyone here is so mean.' The man's eyes widen. 'Oh, I see,' he says. 'You're lost.' "
                           "'Yeah, basically,' you say. 'In that case, follow me,' the man says as the eleveator doors "
                           "open again. He leads you down the hall into an empty office. He sits behind the desk and "
                           "indicates a seat in front of the desk for you to take. You sit, and he begins to speak. 'Allow "
                           "me to explain,' he says. 'There are different worlds all throughout the multiverse that are each "
                           "pure, physical manifestations of one particular human emotion. Sadness, greed, anger, to name "
                           "a few. The one you've wound up in is 'Awkward.'' 'Awkward?' you ask. 'I just feel like everyone's "
                           "been calling me an idiot all day.' 'Ah, yes,' the man says. 'You do feel quite awkward when "
                           "one makes you feel stupid.' 'Why did I have to end up in the awkward place, anyway?' you ask. "
                           "'Why couldn't I have gone to, oh, I don't know, the happy place or something?' At this, the man "
                           "scoffed. 'You want to get into Joy?' he asked. 'Good luck. That place's waitlist is completely "
                           "packed. Whatever the case, you have wound upn in Awkward, and it's my job to bring you home. "
                           "'Why's that?' you ask. 'I'm a dimensional guide,' the man replies. 'It's our duty to help lost "
                           "individuals like yourself to find their homeworld again. The trouble is, we don't know if and "
                           "when you will return. As we see it, the best way to go about it is to follow your will and "
                           "your decisions. After all, those are what made you wind up here in the first place.' 'Seriously?' "
                           "you ask. 'You can't just push a button or something and send me back home now?' The man shakes his "
                           "head. 'I don't have the coordinates for your world. Many animals rely on instinct to find their way back home "
                           "again. Perhaps the same will work for you. It's worked for many others in the past. Others... "
                           "have not been so lucky,' he says. 'Wait. So you're telling me that you have no idea how to get me "
                           "home?' you ask. 'That is correct,' says the man. 'If anyone knows how to help you find your way "
                           "out of here, it would be you.' 'Wait,' you say, 'if you can't even get me out of here, what's even "
                           "the point of you being here at all?' The man leaned forward. 'To make certain that you don't fall "
                           "prey to this world. I know it far better than you do. Well, anyways, we should get going. The "
                           "most effective way for one to find their way back home is to start moving and travel somewhere. "
                           "'Okay, great,' you say. 'Would you like to take the BUS or the TRAIN?' the man asks.").lower()
      if next == "bus":
                   bus()
      elif next == "train":
                   train()
      else:
            invalid_choice()
            behind_way()

def bus():
      print("'Let's take the bus,' you say. The guide nods. 'You got it. Follow me.' He gets up from his chair."
                   "You follow him out the office door. 'Remember,' he says as you approach the elevator, 'expect awkward"
                   "situations. I can't tell you how many times I've run into my ex-wife.' With that, the eleveator doors"
                   "open, and the two of you walk in, exchanging brief pleasantries with the man already inside. The doors"
                   "close, and you begin your descent. You stand there quietly, humming to yourself and looking around the"
                   "elevator, anywhere but at the other guy in the elevator. You keep waiting for the elevator to finish"
                   "descending, but it seemingly never does, and the silence becomes all the more suffocating. Finally, you"
                   "give in. 'So, do you-' you start to say, but the man says something at the same time. 'Oh, sorry,' both"
                   "of you say simultaneously before starting to say something, then stopping, fearful that the other person"
                   "will talk first. 'I guess-' 'What?' I'll go first?' you submit. 'Oh, yeah,' the man says. 'So, do you, uh,"
                   "come here often?' you ask. 'The man gives you a weird look. 'What kind of question is that?' The elevator"
                   "doors finally open, and he gets off, continuing to stare at you with that weird look on his face as he goes."
                   "Your guide steps off the elevator, and you follow. He leads you to a bus stop near the office building. The"
                   "bus doesn't take long to arrive, and you and your guide board it. You choose a seat and wait for the bus to"
                   "start moving. Suddenly, you feel something warm and wet on your upper lip. Your nose has started to run."
                   "Suddenly, everyone on the bus turns toward you. 'Look!' the guy sitting in front of you shouts. 'They have"
                   "a runny nose! Isn't that so gross?' Everyone on the bus shudders and turns away from you. You look at the"
                   "at the aisle across from you, and your crush is sitting there, looking at you with disgust. The pain becomes"
                   "too much, and you pull out a knife and stab yourself. You lose.")
      restart()

def train():
      stop = input("'Let's take the train,' you say. The guide nods. 'You got it. Follow me.' He gets up from his chair. "
                   "You follow him out the office door. 'Remember,' he says as you approach the elevator, 'expect awkward "
                   "situations. I can't tell you how many times I've run into my ex-wife.' With that, the eleveator doors "
                   "open, and the two of you walk in, exchanging brief pleasantries with the man already inside. The doors "
                   "close, and you begin your descent. You stand there quietly, humming to yourself and looking around the "
                   "elevator, anywhere but at the other guy in the elevator. You keep waiting for the elevator to finish "
                   "descending, but it seemingly never does, and the silence becomes all the more suffocating. Finally, you "
                   "give in. 'So, do you-' you start to say, but the man says something at the same time. 'Oh, sorry,' both "
                   "of you say simultaneously before starting to say something, then stopping, fearful that the other person "
                   "will talk first. 'I guess-' 'What?' 'I'll go first?' you submit. 'Oh, yeah,' the man says. 'So, do you, uh, "
                   "come here often?' you ask. 'The man gives you a weird look. 'What kind of question is that?' The elevator "
                   "doors finally open, and he gets off, continuing to stare at you with that weird look on his face as he goes. "
                   "Your guide steps off the elevator, and you follow. He leads you to a nearby train station, and approaches the "
                   "booth to buy two tickets. The lady at the booth hands you the tickets. 'Enjoy you trip,' she says. 'You too,' "
                   "you say before you can stop yourself. You close your eyes and grit your teeth. The lady in the booth looks "
                   "directly at you. 'What did you just say?' she asks in an offended tone. 'Nothing,' you say hastily. 'I'm "
                   "not going on a trip. How could you be so insensitive?' she demands. 'Sorry,' you mutter to yourself. The lady "
                   "sniffs indignantly and waves you off. You and your guide board the train. After a while, it arrives "
                   "at its first stop. 'What do you think?' your guide asks. 'Should we get off at THIS stop or the NEXT?").lower()
      if stop == "this":
            this_stop()
      elif stop == "next":
            next_stop()
      else:
            invalid_choice()
            train()

def this_stop():
      hide = input("'Let's get off here,' you say. Your guide nods, and leads you off the train. You walk around the "
                        "station, and as you do, you must have run into about eight of your old babysitters, who all talk "
                        "about how cute you were when you were younger, how you used to wet the bedy, and every other "
                        "well-kept and mortifying secret of your childhood that you had endeavored to suppress. Eventually, "
                        "you run into your ex, who is hanging out with their new androgynous romantic partner. 'Hey!' they "
                        "call out to you. Before you can escape, they walk over. 'It's so great to see you! By the way, this "
                        "is my androgyonus romantic partner, Sam.' You shake Sam's hand, endeavoring to crush their fingers "
                        "as much as possible. 'How have you been?' your ex asks. 'Oh, same old, same old,' you reply.' 'That's "
                        "great! Are you dating anyone right now?' At this, you excuse yourself and pull your guide aside. 'What "
                        "is going on here?' you ask. 'Well,' your guide replies, 'the story has to work whether the player is male "
                        "or female.' 'No, not that,' you say. 'Why are there actual people that I know here? Are they actually here "
                        "too?' 'No,' your guide says, 'the world is awkwardness incarnate, meaning it'll distort itself to fit "
                        "the mold of what you find awkward. If anyone else was here, you wouldn't be able to interact with them. "
                        "The world would be doing the same thing to them as it is to you: changing itself to become as awkward "
                        "as it can be for that specific person.' Still a little confused, you turn back to your ex. 'What in the "
                        "world could that be?' you ask, pointing off in the distance. Sam and your ex look where you're pointing, "
                        "and you take off running, towing your guide along behind you. You see a building while you're running. "
                        "Do you want to HIDE or continue to RUN?").lower()
      if hide == "hide":
            choose_hide()
      elif hide == "run":
            choose_run()
      else:
            invalid_choice()
            this_stop()

def choose_hide():
      print("You run to the building to hide. It's a laundromat, and people are coming and going with loads of "
                                   "of laundry. You see your ex running by the building through the window. 'Come one, Sam! "
                                   "they say. 'We have to find them and tell them how great our life is!' After they're gone, you "
                                   "let out a sigh of relief. Suddenly, you hear a familiar voice come from behind you: the voice "
                                   "of your grandmother. 'Sweetie?' she says. 'Is that really you? It's been so long since you've "
                                   "called!' 'Yeah, I know grandma,' you say awkwardly. 'Are you just a terrible person?' your grandma "
                                   "asks. 'You know how lonely I am, and yet you continue to put off calling me. Do you even love me?' "
                                   "'Yes, grandma, I promise.' 'LIES!!' grandma yells and lunges at you. You easily dodge her advance "
                                   "(she is an old woman after all) and you run out of the laundromat. As you run, you see a portal "
                                   "open. 'That's it!' you say in relief. 'That's my way back!' With that, you hop in the portal and find "
                                   "yourself back in the Waffle House bathroom. 'I did it!' you think to yourself. 'I made it back! "
                                   "You walk back to your table and finish your food. When your finish, you walk to the cashier and pay. "
                                   "The cashier hands you a receipt. 'Thank you sir,' you say. 'It's MA'AM!' the cashier says. You mumble "
                                   "an apology and as you do, you see a man who looks just like your guide sitting at one of the tables. "
                                   "He winks at you, then looks out the window, as if thinking about something. 'Wait...did I make it back?' "
                                   "You exit the Waffle House, more confused than ever. You win?")
      restart()

def choose_run():
      print("You run away from your ex, trying to take as many weird turns as possible to lose her. You wind "
                                   "up in a park. You stop on the grass to catch your breath when your guide catches up to you. 'Hey, "
                                   "look,' he says, pointing at a gray-haired woman. 'That's my ex-wife. Isn't she gorgeous?' You look "
                                   "over at him. 'I think that would be a weird question for me to answer. After all she's old enough to "
                                   "be my mom. Suddenly, you hear someone clear their throat behind you and feel them tap you on the shoulder. "
                                   "You slowly turn around, and see your mom standing their. 'What's the deal?' she asks. 'You don't "
                                   "think I'm THAT old, do you?' 'I mean, I-' you sputter, trying to recover. 'Don't talk to me with that "
                                   "tone!' she yells. 'You know, it's almost your bedtime, so I think I'll put you to sleep for good!' With "
                                   "that, she clobbers you with a killer right hook. You fall to the ground and don't get up again. You lose.")
      restart()

def next_stop():     
      print("'Let's get off at the next stop,' you say. Your guide nods and sits back, resting in "
                              "his seat. When you arrive at the next stop, you and he get off the train. After exiting the "
                              "station, you see that you're on a bridge. You head down the bridge, and along the way you hear "
                              "a voice call out to you. You turn towards it, and see one of your old high school friends running "
                              "towards you. You exchange pleasantries and ask about each other's lives. Soon enough, the two of you "
                              "run out of things to talk about. You start to look around at the scenery, but that doesn't make "
                              "the awkwardness any less palpable. You look for an out, but people are crowding around the bridge to "
                              "look out at the scenery. You try your best to ignore your old friend, but they're standing right "
                              "next to you. That cerainly doesn't help matters. The silence becomes more oppresive than if someone "
                              "were yelling loudly in your ear. You need something, anything, to end your suffering. You look "
                              "out over the bridge, surmise that you might survive the fall, and jump off. The wind whistles in "
                              "your ears as you fall. When you hit the water, you break every bone in your body. You lose.")
      restart()

def green_portal():
      fire = input("You go through the green portal, and the next thing you know, you're sitting in the stands in an Adele "
                      "concert. She's singing 'Set Fire to the Rain.' Pretty soon, it starts actually raining fire. People "
                      "are screaming and running all over the place, but Adele continueas to sing, ostensibly unbothered by "
                      "the rather odd weather. Do you want to RUN or STAY where you are?").lower()
      if fire == "run":
            go_run()
      elif fire == "stay":
            go_stay()
      else:
            invalid_choice()
            green_portal()

def go_run():
      print("You run from the fire, weaving in and out of fiery raindrops. You run towards the doors at the "
                    "end of the concert hall and burst through them. You find yourself in a seemingly endless hallway "
                    "lit by white flourescent lights. You run down the hallway, seemingly never reaching the end. "
                    "In a panic, you burst through one of the doors on the side of the hallway, and find yourself in an "
                    "identical hallway. Confused, you run for a time before going through another door, finding yourself "
                    "in another identical hallway. You start to panic, continuiung to go through various doors, each time "
                    "finding yourself in an identical, nondescript hallway. Eventually, you sink to the floor in resignation "
                    "and remain there for what seems like eternity. You lose.")
      restart()     

def go_stay():
      choice = input("You decide to stay in the concert hall. After all, it would be rude to leave in the "
                             "middle of one of Adele's songs. You get to enjoy the epic experience of listening to "
                             "'Set Fire to the Rain' while it's actually raining fire. People may be running "
                             "around screaming, but hey, you came here to have fun. Adele's leaving everything "
                             "on the stage and you're having a great time. Flaming raindrops start falling around "
                             "you, but in this state of pure bliss, you don't notice. Eventually, you're completely "
                             "surrounded by fire, but there's no escaping now. You start to burn in the flames "
                             "and Adele's voice starts to fade. Your vision goes blurry, and you fall backward into "
                             "the flames. All goes black...and then you wake up with a start. You find yourself in the "
                             "passenger seat of a car that is speeding down Rainbow Road from Mario Kart. Trying "
                             "to gather your bearings given the surrealism of the situation, you look towards the driver, "
                             "and who should it be but Joseph Gordon-Levitt. 'Good,' he says, 'You're awake. We must "
                             "be several layers deep in this dream.' Still a little dazed, you look in the mirror, "
                             "and realize that the car is being chased by a giant Monopoly man made of glass. "
                             "'Wait,' you say, 'You're telling me that I'm dreaming right now?' Joseph Gordon-Levitt "
                             "nodded. 'So it's like Inception!' you say excitedly. 'How come it's just you? Where's "
                             "Leonardo DiCaprio?' Joseph Gordon-Levitt shakes his head. 'We didn't have the budget for "
                             "Leo. We had to leave out Elliot Page for continuity's sake. The producers didn't realize "
                             "that Michael Caine is still alive. As for Tom Hardy, we didn't have the budget for him "
                             "either. So it's just me.' 'What about Dileep Rao?' you ask. Joseph Gordon-Levitt scoffs. "
                             "'What? Is he even in Inception?' You fall silent, unsure of that fact yourself. 'Anyways,' "
                             "Joseph Gordon-Levitt says, 'I don't know who's trying to trap us here, but their archtects "
                             "sure know how to craft endless loops. This track is an easy example: we go around and "
                             "around, stuck here forever. Fortunately,' he continues, 'your projections have other ideas "
                             "about us staying here, me specifically.' When he finishes, your car is passed by your high "
                             "school bully, who sticks his tongue out at you as he pummels you with a green shell. "
                             "Joseph Gordon-Levitt grits his teeth as he starts to lose control of the car. 'I just "
                             "wish your projections were a little more direct when they try to kill us. If we go over "
                             "the edge, we may never come back. Falls are one of the easiest things for architects to "
                             "loop.' He regains control of the car as he continues. 'That's why I'm worried about that thing "
                             "catching up to us,' he says, gesturing toward the Monopoly man. 'He could send us over the "
                             "edge. What do you think we should do? Should we WAIT and let him catch up, or should "
                             "we continue to DRIVE?'").lower()
      if choice == "wait": 
            choose_wait()
      elif choice == "drive":
            choose_drive()
      else:
            invalid_choice()
            go_stay()

def choose_wait():
      step = input("'Let's wait,' you say. Joseph Gordon-Levitt nods and brings the car to a stop. The "
                   "Monopoly man catches up and raises its glass arm. It brings its arm down, and you "
                   "close your eyes, bracing for impact. When you open your eyes, you find yourself "
                   "standing on the sidewalk in the middle of a city. You see Joseph Gordon-Levitt standing "
                   "next to you, and he starts walking. You follow, doing your best to keep up, both with "
                   "his pace, and with the reality of your situation. 'Does this mean we've reached the real "
                   "world?' you ask. 'Not necessarily,' Joseph Gordon-Levitt replies. 'The closer we get "
                   "to the real world, the more the architects will try to mess with our heads to make us "
                   "think that we've finally woken up. Since they couldn't get us trapped inside a loop, "
                   "this is Plan B. It fools some people, but I'm not just anyone. Even when I think I've won, I ALWAYS investigate. Then again, if they "
                   "bring you into consciousness early, they could trick you into killing yourself.' "
                   "He pauses on the sidewalk for a moment and points at a building. 'There. You see that?' "
                   "You look towards the building. 'What am I supposed to be seeing?' you ask. 'I've seen "
                   "it before,' he says to himself. 'What, the building?' you ask. 'No,' he says. 'I've "
                   "seen that brick before, the one on the very left. Man, this architect is sloppy.' You "
                   "shake your head, still trying to take it all in, when you see Ronald McDonald walking "
                   "down the street. 'Uhhhh...did I just see what I think I saw?' you ask. 'Ah, yes,' "
                   "Joseph Gordon-Levitt replies. 'I saw it too. That's another, more obvious sign that we're "
                   "still dreaming: your projections, the one thing the architect can't control, will "
                   "continue to have surreal or odd forms.' As he finished talking, you see a very long-legged " 
                   "Pinocchio walk by. 'Okay,' you say, 'So how do we get out of here?' 'Well,' Joseph "
                   "Gordon-Levitt begins, 'In this scenario, the easiest way would be to anger the projections. "
                   "You're lucky that I'm here; the projections won't attack their host, so I'll have to be "
                   "the one to provoke them. The trick is to get them to inadvertently attack both me and you.' "
                   "You look over and see that he's holding a gun, something he definitely didn't have before. "
                   "'Why don't you just shoot both of us with your own gun?' you ask him. 'It woudldn't "
                   "work,' he replies. 'The source of death has to come from the dreamer's subconscious.' "
                   "With that, he starts shooting at your projections and ducks behind a car. 'If we escalate "
                   "the situation, there's a good chance that your projections will start to use heavy weaponry. "
                   "When that happens, there's a better chance that they'll kill both of us.' Your projections start "
                   "closing in, raining heavy fire on you and Joseph Gordon-Levitt. 'This isn't good,' he says. "
                   "I'm the one they want. If they hit me and not you, that's game over. You'll have a lot more "
                   "trouble getting out of here, especially with the architect controlling everything.' Suddenly, "
                   "you feel the ground shake. Pretty soon, it's vibrating so violently that you and Joseph "
                   "Gordon-Levitt fall to the ground. A fissure opens in the middle of the street as the ground "
                   "continues to shake, providing you with a potential out. Do you want to JUMP into the newly "
                   "formed pit, or do you want to STAY where you are?").lower()
      if step == "jump":
            jump_off()
      elif step == "stay":
            stay_here()
      else: 
             invalid_choice()
             choose_wait()

def jump_off():
        print("You run towards the pit and hurl yourself off. Behind you, you can hear Joseph Gordon-Levitt "
              "screaming at you to stop, when it hits you: the architect created this fissure as a way "
              "to bait you into jumping, and now that you have, they can trap you in an endless loop. "
              "This thought doesn't do you much good, however. You're still stuck falling for eternity. You "
              "lose.")
        restart()

def stay_here():
        home = input("You decide to hold your position. Bullets keep hammering into the front of the car."
                     "All of a sudden, you see Harry Potter apporach your position with a grenade launcher."
                     "He fires, and a grenade lands between you and Joseph Gordon-Levitt. It explodes, and"
                     "for a moment, you're blinded by the explosion. When you can finally see again, you're"
                     "standing in front of your house. The sights and smells are so familiar, so nostalgic."
                     "Joseph Gordon-Levitt still looks on edge. 'Where are we?' he asks. 'I'm...home,' you"
                     "reply solemnly. 'Careful now,' he says. 'This could be a ploy by the architect to"
                     "keep you here.' 'I know,' you say, but with everything that's happened today, and with"
                     "the acres of text you've been forced to read, every force within you compels you"
                     "to stay here and let it all come to an end. Do you want to STAY here, or try to"
                     "LEAVE?").lower()
        if home == "stay":
            go_home()
        elif home == "leave":
            leave_here()

def go_home():
       print("'I want to stay here,' you say. Joseph Gordon-Levitt gestures toward your front door. "
             "You walk up to it, content to return home, somewhere familiar, real or not. You "
             "open the front door and walk inside. You look back at Joseph Gordon-Levitt, who "
             "waves at you and walks away. With a smile, you pull your head inside and close the door. "
             "You win!")
       start()
def leave_here():
       real = input("'Let's get out of here,' you tell Joseph Gordon-Levitt. He grins. 'You don't "
                    "have to tell me twice.' With that, he yanks you out into the street, and the "
                    "two of you are struck by an oncoming car. You black out again (you're getting "
                    "quite sick of the sensation) and wake up in the Waffle House bathroom. You "
                    "blink once. You blink again. You take in the scenery: the rusting sink, the dirty "
                    "toilet, the awful smell. You can't believe it. You actually made it back. It "
                    "may not be pretty, but it's reality. You win! \nDo you want to play again?"
                    "(YES/NO)").lower()
       if real == "investigate":
              print("Unless...it's not real. Something Joseph Gordon-Levitt said comes back to you: "
                    "'Even when I think I've won, I ALWAYS investigate.' You decide to look a little "
                    "closer. You start walking through the Waffle House, taking a closer look at "
                    "the people in the booths. You walk past someone who looks vaguely familiar... "
                    "You decide to look closer. You realize with a start that you do recognize this person: "
                    "it's Elliot Page. Elliot sees you looking at him, and bolts for the door. You run after "
                    "him and tackle him to the ground. You pick him up and throw him against the wall. "
                    "'So,' you say, 'you've been the architect this whole time.' Elliot laughs, but "
                    "gives no confirmation. 'Why?' you ask. 'Why are you doing this?' Elliot finally "
                    "speaks up. 'You're asking me why? I've got a question for you: I presented you with "
                    "the perfect reality, a number of realities actually, that are totally free from "
                    "pain and strife. Why didn't you take them?' 'Because I actually care about what is "
                    "real and what isn't!' you reply. 'NONE OF THIS IS REAL!!' Elliot shouts. 'Tell me, how "
                    "did you get to Waffle House?' 'I-' you start to say. 'I...don't...remember.' I "
                    "created this world as an escape from reality! I made three completely different worlds "
                    "so that you could forget about the troubles of the world, even for a moment! You only "
                    "won when I said so. You only lost when I said so. And now, I have you trapped here! "
                    "If you didn't want the utopia I provided for you, so be it. You can stay in Waffle "
                    "House. Forever.' At this, you look out the window. Where the outside should be, you "
                    "see the interior of another Waffle House. Elliot laughs maniacally. 'How do you "
                    "plan on returning to reality now?' You think about his question for a moment. And "
                    "then the answer comes to you. 'I could walk away.' Elliot's smile fades. 'What?' 'I "
                    "'could just walk away. I know this world isn't real. I've always known that. It, just "
                    "like you, is nothing more than text on a screen. I can walk away right now end enjoy "
                    "reality.' Elliot is quiet for a minute. Then he speaks. 'Alright then. Go. If it's "
                    "that easy, walk away. Finally wake up. If you want to play again, I'll be here. Just do "
                    "it. Walk away. But first, I have a question: '")
              final_restart()
       elif real == "yes":
              start()
       else:
              print("Thanks for playing!")

def choose_drive():
      print("'Let's keep driving,' you say. Joseph Gordon-Levitt nods and keeps driving. Suddenly, "
            "disaster strikes in the form of a red shell, this time thrown by Bugs Bunny, who "
            "taunts you as he passes. Joseph Gordon-Levitt is unable to regain control this time, "
            "and the car goes careening over the edge of Rainbow Road. You and he fall into the void and "
            "continue to fall forever. You lose.")
      restart()

def invalid_choice():
        print()
        print("Nice try, smart guy, but that's an invalid input. Try again. ")
        print()

def restart():
       play = input("Do you want to play again? (YES/NO)").lower()
       if play == "yes":
            start()
       else:
            print("Thanks for playing!")

def final_restart():
       replay = input("Do you want to play again? (YES/NO)").lower()
       if replay == "yes":
            start()
       else: 
            print("'Thanks for playing!' Elliot says. 'If you ever want to escape from reality,"
                    "I'll be here, waiting. Always.'")
start()