from tkinter import * 
import random 
def main():

    # global to keep track the current player
    global current_player

    def next_turn(row,column):
        # global to keep track the current player
        global current_player
        #'text' means content in row and column
        if buttons[row][column]['text']== ""and not check_winner():
            buttons[row][column]['text'] = current_player

            if check_winner() == True:
                label.config(text=f"{current_player} Wins !")
            elif check_winner() == "Draw":
                label.config(text="Draw!")
            else:
                if current_player == players[0]:
                    current_player = players[1]
                else:
                    current_player = players[0]

                label.config(text=f"{current_player} Turn")

    def check_winner():
        #Check for the row and column for a win 
        for i in range(3):
            if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
                for j in range(3):
                    buttons[i][j].config(bg="green")
                return True
            
        for i in range(3):
            if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
                for j in range(3):
                    buttons[j][i].config(bg="green")
                return True
            
        #Check for the diagonal for a win
        if buttons[0][0]['text']== buttons[1][1]['text']== buttons[2][2]['text'] != "":
            for i in range (3):
                buttons[i][i].config(bg="green")
            return True
        
        elif buttons[0][2]['text']== buttons[1][1]['text']== buttons[2][0]['text'] != "":
            for i in range (3):
                buttons[i][2-i].config(bg="green")
            return True
        
        # If no winner and the board is full it is a draw
        elif not empty():
            for row in range (3):
                for column in range (3):
                    buttons[row][column].config(bg="yellow")
            return "Draw"
        
        #No winner and the board is not full
        else:
            return False
        
    def empty():
        #Check if any button in the board is empty
        return any(buttons[row][column]['text']=='' for row in range(3) for column in range(3))
    
    def restart_game():
        #Restart the game and reset the current player
        global current_player
        current_player = random.choice(players)
        label.config(text=current_player + " Turn")
        for row in range(3):
            for column in range(3):
                #reset all the buttons to start a new game
                buttons[row][column].config(text="",bg="white")

    def quit_game():
        window.quit()

    #Initialize the Tkinter window
    window =Tk()
    window.title("Tic-Tac-Toe")
    players = ["X","O"]
    current_player = random.choice(players) 
    buttons = [["","",""],
              ["","",""],
              ["","",""]]
    
    # Create a label to display the turn 
    label =Label(text=current_player +" Turn ", font=('Arial',40))
    label.pack(side="top")

    # Container to display the button
    button_frame=Frame(window)
    button_frame.pack()

    # Command is the function that should be called when the button is clicked
    reset_button = Button(button_frame,text="Restart", font=('Arial',20),width=6,height=2,command=restart_game)
    quit_button = Button(button_frame,text="Quit",font=('Arial',20),width=6,height=2,command=window.destroy)
    # Padx is space
    reset_button.pack(side="left",padx=25)
    quit_button.pack(side="left",padx=25)

    # Creating a frame to add to window
    frame= Frame(window)
    frame.pack()
    for row in range(3):
        for column in range(3):
            # button in the frame is empty at every row and column with a certain width and height , when the button is clicked then the command will execute
            # lambda is used to create function
            buttons[row][column]= Button(frame, text="",font=('Arial',40),width=5,height=2,command= lambda row=row,column=column: next_turn(row,column))
            # grid is the button placed 
            buttons[row][column].grid(row=row,column=column)

    window.mainloop()

