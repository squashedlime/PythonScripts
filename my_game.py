from sys import exit
prompt = "-->"

def gold():
    print "The king shows you his treasure room take as much as you can carry my boy!"
    print "But don't be greedy!!"
    print "How much do you take??"
    
    choice = raw_input(prompt)
    #need to fix this bit!! first choice for how much then assess it!
    if choice <= 10:
        print "Take som more that won't get you very far!"
    elif choice <= 100:
        print "Go and have a good life!"
        exit(0)
    elif choice > 100:
        print "your greedy lite pig!!"
        dead("The king makes himself a new football with your head!")
 
def palace():
    print "The whole castle is amazed to see you riding in on a moose!"
    print "The king greets you and because you are a friend of the moose.."
    print "He offers you his daughter and as much gold as you can carry"
    print "what do you say to the king?"
    
    choice = raw_input(prompt)
    
    if "no" in choice or "not" in choice:
        dead("The king take this as an insult and has your head as a royal football!")
    elif "yes" or "nice" or "thanks" in choice:
        gold()
    else:
        print "try again"
        palace()
        

def clearing():
    print "You come to a clearing in the woods"
    print "On a stone in the middle is moose"
    print "The moose looks your way and you hear him say \"Hello\""
    print "what do you do? say hello or flee?"
    
    choice = raw_input(prompt)
    
    if "hello" in choice:
        print "The moose like you and give you a ride to the kings place"
        palace()
    elif "flee" in choice:
        dead("The moose chases you down and impales you on his antlers!!")   
    else:
        print "The moose said \"Hello\" aren't you going to answer him??\n"
        clearing()
         
        
 
def dead(why):
    print why, "Nice one!"
    exit(0)
           
def entrance():
    print "you're standing at the edge of a wood"
    print "It looks dark in there!"
    print "You have three ways to go"
    print "path through the woods, write woods"
    print "knock on the green litle round door, write knock"
    print "Take the path around the woods, write around wood"
    
    choice = raw_input(prompt)
    
    if choice == "woods":
        clearing()
    elif choice == "knock":
        elf_house()
    elif next == "around wood":
        around_wood()
    else:
        print "Sorry I didn't understand try again, woods, knock or around wood"
        entrance()


entrance()
        
# try doing an empty list and adding things to is how could I do this in the game??
#finish off the other rooms
#try importing more relivant modules like..... os, or argv or log or sys think up some ways of using them.

