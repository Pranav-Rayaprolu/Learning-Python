import tkinter as tk
from tkinter import messagebox
import webbrowser

class PlayerNameInput:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Enter Player Names and Rounds")
        self.root.configure(background="black", padx=20, pady=20)

        self.player1_name = tk.StringVar()
        self.player2_name = tk.StringVar()
        self.rounds = tk.StringVar()

        label_player1 = tk.Label(self.root, text="Enter Player 1 Name:", foreground="white", background="black", font=("Helvetica", 12, "bold"))
        entry_player1 = tk.Entry(self.root, textvariable=self.player1_name, font=("Helvetica", 12))

        label_player2 = tk.Label(self.root, text="Enter Player 2 Name:", foreground="white", background="black", font=("Helvetica", 12, "bold"))
        entry_player2 = tk.Entry(self.root, textvariable=self.player2_name, font=("Helvetica", 12))

        label_rounds = tk.Label(self.root, text="Enter Number of Rounds:", foreground="white", background="black", font=("Helvetica", 12, "bold"))
        entry_rounds = tk.Entry(self.root, textvariable=self.rounds, font=("Helvetica", 12))

        submit_button = tk.Button(self.root, text="Submit", command=self.submit_names, foreground="black", background="white", padx=10, pady=10, bd=0, borderwidth=0, relief="solid", highlightthickness=0, overrelief="solid", font=("Helvetica", 12, "bold"))

        label_player1.grid(row=0, column=0, pady=5, padx=5, sticky="e")
        entry_player1.grid(row=0, column=1, pady=5, padx=5, sticky="w")

        label_player2.grid(row=1, column=0, pady=5, padx=5, sticky="e")
        entry_player2.grid(row=1, column=1, pady=5, padx=5, sticky="w")

        label_rounds.grid(row=2, column=0, pady=5, padx=5, sticky="e")
        entry_rounds.grid(row=2, column=1, pady=5, padx=5, sticky="w")

        submit_button.grid(row=3, columnspan=2, pady=10)

    def submit_names(self):
        player1_name = self.player1_name.get()
        player2_name = self.player2_name.get()
        rounds = self.rounds.get()

        if player1_name and player2_name and rounds.isdigit() and int(rounds) > 0:
            self.root.destroy()  # Close input window

            game = TicTacToe(player1_name, player2_name, int(rounds))
            game.run()
        else:
            messagebox.showwarning("Error", "Please enter valid names and a positive number of rounds.")

class TicTacToe:
    def __init__(self, player1_name, player2_name, rounds):
        self.root = tk.Tk()
        self.root.title("TIC-TAC-TOE")
        self.root.geometry("315x580")  # Fixed size
        self.root.resizable(False, False)  # Non-resizable
        self.root.configure(background="black", padx=20, pady=20)

        self.player1_name = player1_name
        self.player2_name = player2_name
        self.rounds = rounds
        self.current_player = "X"
        self.player_color = "red"
        self.board = [""] * 9
        self.scores = {"X": 0, "O": 0}
        self.round_counter = 1

        title_label = tk.Label(self.root, text="TIC-TAC-TOE", font=("Helvetica", 16, "bold"), foreground="lightblue", background="black", padx=10, pady=10, borderwidth=0, relief="solid")
        title_label.grid(row=0, columnspan=3, pady=(0, 10))

        self.buttons = [tk.Button(self.root, text="", width=10, height=5, command=lambda i=i: self.make_move(i), background="black", padx=5, pady=5) for i in range(9)]

        for i in range(3):
            for j in range(3):
                self.buttons[i * 3 + j].grid(row=i + 1, column=j, padx=2, pady=2)

        self.turn_label = tk.Label(self.root, text=f"Turn: {self.player1_name} ({self.current_player})", foreground=self.player_color,
                                   background="black", padx=10, pady=7, font=("Helvetica", 10, "bold"))
        self.turn_label.grid(row=4, columnspan=3)

        self.score_label = tk.Label(self.root, text=f"SCORES:\n\n{self.player1_name} - 0\n\n{self.player2_name} - 0", foreground="white", background="black", padx=10, pady=10, font=("Helvetica", 10, "bold"))
        self.score_label.grid(row=5, columnspan=3)

        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.reset_board, foreground="black", background="white", padx=10, pady=10, bd=0, borderwidth=0, relief="solid", highlightthickness=0, overrelief="solid", font=("Helvetica", 10, "bold"))
        self.play_again_button.grid(row=6, column=0,)

        self.reset_button = tk.Button(self.root, text="Restart", command=self.reset_game, foreground="black", background="white", padx=10, pady=10, bd=0, borderwidth=0, relief="solid", highlightthickness=0, overrelief="solid", font=("Helvetica", 10, "bold"))
        self.reset_button.grid(row=6, column=1 )

        
        self.source_code_button.grid(row=6, column=2)

        self.root.grid_rowconfigure(6, weight=1)  # Center buttons in the middle row

    def make_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            player_color = "red" if self.current_player == "X" else "green"
            self.buttons[index].config(foreground=player_color)

            if self.check_winner():
                messagebox.showinfo("TIC-TAC-TOE", f"{self.player1_name if self.current_player == 'X' else self.player2_name} wins Round {self.round_counter}!")
                self.scores[self.current_player] += 1
                self.update_scores()
                self.disable_buttons()

                if self.round_counter < self.rounds:
                    self.round_counter += 1
                    self.reset_board()
                else:
                    self.show_final_result()
            elif "" not in self.board:
                messagebox.showinfo("TIC-TAC-TOE", "It's a draw!")
                self.disable_buttons()

                if self.round_counter < self.rounds:
                    self.round_counter += 1
                    self.reset_board()
                else:
                    self.show_final_result()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.player_color = "green" if self.current_player == "O" else "red"

                self.turn_label.config(text=f"Turn: {self.player1_name if self.current_player == 'X' else self.player2_name} ({self.current_player})", foreground=self.player_color)

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def reset_board(self):
        for i in range(9):
            self.buttons[i].config(text="")
            self.board[i] = ""
            self.buttons[i].config(state="normal")  # Enable buttons
        self.current_player = "X"
        self.player_color = "red"
        self.turn_label.config(text=f"Turn: {self.player1_name} ({self.current_player})", foreground=self.player_color)

    def reset_game(self):
        self.reset_board()
        self.scores = {"X": 0, "O": 0}
        self.round_counter = 1
        self.update_scores()

    def show_final_result(self):
        result_message = f"Final Result:\n{self.player1_name} - {self.scores['X']}\n{self.player2_name} - {self.scores['O']}"
        messagebox.showinfo("TIC-TAC-TOE", result_message)

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state="disabled")  # Disable buttons after the game ends

    def update_scores(self):
        self.score_label.config(text=f"SCORES:\n\n{self.player1_name} - {self.scores['X']}\n\n{self.player2_name} - {self.scores['O']}")

    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    player_input = PlayerNameInput()
    player_input.root.mainloop()