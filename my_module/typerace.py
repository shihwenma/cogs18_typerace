#imports used
import time
import string
import random
import os

def generate_text():
    """ Generates a random text string to copy
    
        Parameters
        ----------
        None
        
        Returns
        -------
        text : string
            The generated random string to be copied
    """
    text = ""
    i = 0
    while i < 100:
        #choose to add either letter, punctuation, or number
        diff_type = ['letter', 'punctuation', 'number']
        choose_type = random.choice(diff_type)
        
        #choice is letter
        if choose_type == 'letter':
            add = random.choice(string.ascii_letters)
        #choice is punctuation
        elif choose_type == 'punctuation':
            add = random.choice(string.punctuation)
        #choice is numbers
        else:
            add = random.choice(string.digits)
            
        #adds what char we generated to the text and increments
        text = text + add
        i = i+1
    return text

def num_diff(msg, text):
    """ Finds how many incorrect charactersy
    
        Parameters
        ----------
        msg : string
            User answer/copy 
        text : string
            The message the user was supposed to copy
        
        Returns
        -------
        diff : int
            The number of different characters between the two strings
    """

    diff = 0
    #if different lengths, make same length
    if (len(msg) != len(text)):
        if (len(msg) > len(text)):
            text = text[0:len(msg)]
        else:
            msg = msg[0:len(text)]
    
    #compare each char
    for i, j in zip(msg, text):
        if i != j:
            diff += 1
    return diff

def score(msg, text):
    """ Calculates player score before time factored in
    
        Parameters
        ----------
        msg : string
            User answer/copy 
        text : string
            The message the user was supposed to copy
        
        Returns
        -------
        fin_score : int
            The player score based on accuracy
    """

    fin_score = len(msg) - num_diff(msg, text)
    return fin_score
   
def avg_score(scores_list):
    """ Calculates average score of games 
        
        Parameters
        ----------
        scores_list : list of all the game scores received
        
        Returns
        -------
        avg : average score of games
    """
    total = 0
    for score in scores_list:
        total = total + score
    avg = total /  len(scores_list)
    return avg

# from A3 but significantly modified to include typeracer feature  
# adapted code to be considered part of graded project code.
def lets_chat():  
    """ main function to chat with bot
    
        Parameters
        ----------
        None
        
        Returns
        -------
        None
    """
    start = 0
    total_scores = []
    chat = True
    instructions = True
    text = ''
    game_start = False
    while chat:
        # Get a message from the user
        msg = input('USER :\t')
         # Check for an end msg 
        if msg == 'quit':
            out_msg = 'Your average score is ' + str(avg_score(total_scores)) + '!'
            out_msg = out_msg + 'Thanks for playing'
            chat = False
        
        #gives instructions.
        elif instructions:
            instructions = False
            out_msg = "Hello. I am a typeracer chatbot. "
            out_msg = out_msg + "Your goal is to type exactly what is given. " 
            out_msg = out_msg + "If you take too long, you lose!"
            out_msg = out_msg + "You will be scored based on accuracy "
            out_msg = out_msg + "and timing. To begin, type start. "
            out_msg = out_msg + "If you'd like to stop, type quit."
        
        # Check if they want to start game
        elif msg == 'start':
            text = generate_text()
            out_msg = text
            start = time.time()
            game_start = True
        
        #round is over. Need to type start again to start another game
        elif not game_start:
            out_msg = "Please type start to start the game or quit to end the game."
            game_start = False
        
        #returns score
        else:     
            end = time.time()
            time_elapsed = end-start
            fin_score = score(msg,text) - time_elapsed
            game_start = False
            # normal case - provides score
            if (fin_score >= 0):
                out_msg = "Score: " + str(fin_score)
                out_msg = out_msg + ". To generate a new game, type start"
                total_scores.append(fin_score)
            elif (time_elapsed > 60):
                out_msg = "Score: 0 - Took too long!"
                total_scores.append(0)
            # if too many wrong - loses
            elif (fin_score < 0):
                out_msg = "Score: 0 - Too many incorrect! "
                out_msg = out_msg + "To generate a new game, type start"
                total_scores.append(0)

        print('BOT :\t', out_msg)