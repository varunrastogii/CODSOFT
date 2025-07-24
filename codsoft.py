# import math
# import tkinter as tk
# from tkinter import messagebox

# # Constants
# HUMAN = 'X'
# AI = 'O'
# EMPTY = ' '

# # Game variables
# board = [[EMPTY for _ in range(3)] for _ in range(3)]
# buttons = [[None for _ in range(3)] for _ in range(3)]
# use_alpha_beta = True

# # Evaluation logic
# def evaluate():
#     for i in range(3):
#         if board[i][0] == board[i][1] == board[i][2] != EMPTY:
#             return 1 if board[i][0] == AI else -1
#         if board[0][i] == board[1][i] == board[2][i] != EMPTY:
#             return 1 if board[0][i] == AI else -1

#     if board[0][0] == board[1][1] == board[2][2] != EMPTY:
#         return 1 if board[0][0] == AI else -1
#     if board[0][2] == board[1][1] == board[2][0] != EMPTY:
#         return 1 if board[0][2] == AI else -1

#     return 0

# def is_moves_left():
#     return any(EMPTY in row for row in board)

# # Minimax with optional Alpha-Beta Pruning
# def minimax(depth, is_max):
#     score = evaluate()
#     if score != 0 or not is_moves_left():
#         return score

#     if is_max:
#         best = -math.inf
#         for i in range(3):
#             for j in range(3):
#                 if board[i][j] == EMPTY:
#                     board[i][j] = AI
#                     best = max(best, minimax(depth + 1, False))
#                     board[i][j] = EMPTY
#         return best
#     else:
#         best = math.inf
#         for i in range(3):
#             for j in range(3):
#                 if board[i][j] == EMPTY:
#                     board[i][j] = HUMAN
#                     best = min(best, minimax(depth + 1, True))
#                     board[i][j] = EMPTY
#         return best

# def minimax_ab(depth, is_max, alpha, beta):
#     score = evaluate()
#     if score != 0 or not is_moves_left():
#         return score

#     if is_max:
#         best = -math.inf
#         for i in range(3):
#             for j in range(3):
#                 if board[i][j] == EMPTY:
#                     board[i][j] = AI
#                     val = minimax_ab(depth + 1, False, alpha, beta)
#                     board[i][j] = EMPTY
#                     best = max(best, val)
#                     alpha = max(alpha, best)
#                     if beta <= alpha:
#                         break
#         return best
#     else:
#         best = math.inf
#         for i in range(3):
#             for j in range(3):
#                 if board[i][j] == EMPTY:
#                     board[i][j] = HUMAN
#                     val = minimax_ab(depth + 1, True, alpha, beta)
#                     board[i][j] = EMPTY
#                     best = min(best, val)
#                     beta = min(beta, best)
#                     if beta <= alpha:
#                         break
#         return best

# # AI Move
# def best_move():
#     best_val = -math.inf
#     move = (-1, -1)

#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == EMPTY:
#                 board[i][j] = AI
#                 move_val = (
#                     minimax_ab(0, False, -math.inf, math.inf)
#                     if use_alpha_beta else minimax(0, False)
#                 )
#                 board[i][j] = EMPTY
#                 if move_val > best_val:
#                     move = (i, j)
#                     best_val = move_val
#     return move

# # Handle player's click
# def on_click(i, j):
#     if board[i][j] != EMPTY:
#         return

#     board[i][j] = HUMAN
#     buttons[i][j]['text'] = HUMAN
#     buttons[i][j]['fg'] = 'blue'
#     buttons[i][j]['state'] = 'disabled'
#     buttons[i][j]['disabledforeground'] = 'blue'

#     if evaluate() == -1:
#         end_game("You win! 🎉")
#         return
#     if not is_moves_left():
#         end_game("It's a draw!")
#         return

#     # AI Move
#     ai_i, ai_j = best_move()
#     board[ai_i][ai_j] = AI
#     buttons[ai_i][ai_j]['text'] = AI
#     buttons[ai_i][ai_j]['fg'] = 'red'
#     buttons[ai_i][ai_j]['state'] = 'disabled'
#     buttons[ai_i][ai_j]['disabledforeground'] = 'red'

#     if evaluate() == 1:
#         end_game("AI wins! 🤖")
#     elif not is_moves_left():
#         end_game("It's a draw!")

# def end_game(msg):
#     messagebox.showinfo("Game Over", msg)
#     for i in range(3):
#         for j in range(3):
#             buttons[i][j]['state'] = 'disabled'

# def reset_game():
#     global board
#     board = [[EMPTY for _ in range(3)] for _ in range(3)]
#     for i in range(3):
#         for j in range(3):
#             btn = buttons[i][j]
#             btn.config(text=EMPTY, fg='black', state='normal')

# # GUI Setup
# root = tk.Tk()
# root.title("Tic-Tac-Toe AI")
# root.configure(bg='#f0f0f0')

# frame = tk.Frame(root, bg='#f0f0f0', padx=10, pady=10)
# frame.pack()

# style = {
#     'font': ('Arial', 32),
#     'width': 5,
#     'height': 2,
#     'bg': '#ffffff',
#     'activebackground': '#dcdcdc',
#     'relief': 'raised',
#     'bd': 2
# }

# for i in range(3):
#     for j in range(3):
#         button = tk.Button(frame, text=EMPTY, **style,
#                            command=lambda i=i, j=j: on_click(i, j))
#         button.grid(row=i, column=j, padx=5, pady=5)
#         buttons[i][j] = button

# reset_button = tk.Button(root, text="Reset Game", font=('Arial', 14), bg='#4CAF50', fg='white',
#                          padx=10, pady=5, command=reset_game)
# reset_button.pack(pady=10)

# root.mainloop()


'.....................................................................................................................................................................'



# import tkinter as tk
# from tkinter import ttk, messagebox
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# movies = {
#     'title': [
#         'The Matrix', 'John Wick', 'Inception', 'The Dark Knight',
#         'Interstellar', 'Avengers: Endgame', 'The Prestige', 'Tenet',
#         'Memento', 'Dunkirk', '3 Idiots', 'PK', 'Dangal', 'Chak De! India',
#         'Zindagi Na Milegi Dobara', 'Taare Zameen Par', 'Barfi!', 'Queen',
#         'Lagaan', 'Swades'
#     ],
#     'description': [
#         'A computer hacker learns about the true nature of reality and his role in the war against its controllers.',
#         'An ex-hitman comes out of retirement to track down the gangsters that killed his dog.',
#         'A thief steals corporate secrets through dream-sharing technology.',
#         'Batman faces the Joker in a battle for Gotham\'s soul.',
#         'Explorers travel through a wormhole in space to save humanity.',
#         'The Avengers assemble once more to reverse Thanos\' snap and restore balance.',
#         'Two magicians engage in a dangerous rivalry full of tricks.',
#         'A secret agent manipulates time to prevent global disaster.',
#         'A man with short-term memory loss uses tattoos to hunt his wife\'s killer.',
#         'Allied soldiers are surrounded during WWII evacuation.',
#         'Three engineering students learn life lessons while dealing with academic pressure.',
#         'An alien lands on Earth and questions religious dogma in India.',
#         'A former wrestler trains his daughters to become world-class wrestlers.',
#         'A hockey coach trains a women\'s team to prove his loyalty to the nation.',
#         'Three friends take a road trip across Spain discovering themselves.',
#         'A teacher helps a dyslexic child discover his potential through art.',
#         'A mute man with autism falls in love in a bittersweet journey.',
#         'A woman rediscovers herself on a solo honeymoon trip.',
#         'A small village team takes on the British in a game of cricket.',
#         'A NASA scientist returns to rural India to bring development.'
#     ]
# }

# df = pd.DataFrame(movies)

# vectorizer = TfidfVectorizer(stop_words='english')
# tfidf_matrix = vectorizer.fit_transform(df['description'])
# cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# def get_recommendations(title, top_n=3):
#     if title not in df['title'].values:
#         return []
#     idx = df[df['title'] == title].index[0]
#     sim_scores = list(enumerate(cosine_sim[idx]))
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#     sim_scores = sim_scores[1:top_n + 1]
#     movie_indices = [i[0] for i in sim_scores]
#     return df.iloc[movie_indices][['title', 'description']].values.tolist()

# root = tk.Tk()
# root.title("🌟 Movie Recommendation System")
# root.geometry("750x600")
# root.configure(bg="#ffe6f0")

# TITLE_FONT = ('Comic Sans MS', 20, 'bold')
# LABEL_FONT = ('Verdana', 13)
# RESULT_FONT = ('Calibri', 12)

# style = ttk.Style()
# style.configure('TButton', font=('Verdana', 11), padding=6, foreground="#004d99")
# style.configure('TLabel', font=LABEL_FONT)
# style.configure('TCombobox', font=LABEL_FONT)

# title_label = tk.Label(root, text="🎬 Movie Recommendation System", font=TITLE_FONT, bg="#ffe6f0", fg="#cc0066")
# title_label.pack(pady=25)

# dropdown_label = tk.Label(root, text="🎯 Select a movie you like:", font=LABEL_FONT, bg="#ffe6f0", fg="#800000")
# dropdown_label.pack()

# selected_movie = tk.StringVar()
# movie_dropdown = ttk.Combobox(root, textvariable=selected_movie, values=df['title'].tolist(), state="readonly", width=55)
# movie_dropdown.pack(pady=10)
# movie_dropdown.current(0)

# result_frame = tk.Frame(root, bg="#ffffff", bd=4, relief="ridge", highlightbackground="#ff66b3", highlightthickness=3)
# result_frame.pack(pady=25, padx=30, fill="both", expand=True)

# result_title = tk.Label(result_frame, text="🍿 Top 3 Recommendations", font=('Arial Black', 14), bg="#ffffff", fg="#cc0066")
# result_title.pack(pady=(15, 10))

# result_label = tk.Text(result_frame, wrap='word', font=RESULT_FONT, bg="#ffffff", fg="#333", height=15, width=70)
# result_label.pack(padx=10, pady=5)

# def show_recommendations():
#     movie = selected_movie.get()
#     recommendations = get_recommendations(movie)
#     result_label.delete("1.0", tk.END)
#     if recommendations:
#         for i, (title, desc) in enumerate(recommendations, 1):
#             result_label.insert(tk.END, f"⭐ {i}. {title}\n📖 {desc}\n\n")
#     else:
#         messagebox.showinfo("⚠️ Not Found", "Movie not found in database.")

# button_frame = tk.Frame(root, bg="#ffe6f0")
# button_frame.pack()

# recommend_button = ttk.Button(button_frame, text="🎥 Recommend Movies", command=show_recommendations)
# recommend_button.grid(row=0, column=0, padx=15, pady=10)

# def reset():
#     movie_dropdown.current(0)
#     result_label.delete("1.0", tk.END)

# reset_button = ttk.Button(button_frame, text="🔄 Reset", command=reset)
# reset_button.grid(row=0, column=1, padx=15, pady=10)

# root.mainloop()



'.....................................................................................................................................................................'


import tkinter as tk
from tkinter import scrolledtext
import datetime

def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking 😊"
    elif "name" in user_input:
        return "I'm JARVIS – your Python chatbot buddy 🤖"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Take care! 👋"
    elif "help" in user_input:
        return "Ask me about the weather, time, jokes, or just say hi!"
    elif "creator" in user_input or "who made you" in user_input:
        return "I was crafted by VARUN RASTOGI, a passionate coder ❤️ using Python and Tkinter!"
    elif "time" in user_input:
        return "The current time is " + datetime.datetime.now().strftime("%I:%M %p")
    elif "date" in user_input:
        return "Today is " + datetime.datetime.now().strftime("%A, %d %B %Y")
    elif "joke" in user_input:
        return "Why do programmers prefer dark mode? Because light attracts bugs! 😄"
    elif "weather" in user_input:
        return "I'm not connected to live data, but I hope it's sunny where you are! ☀️"
    else:
        return "Sorry, I didn't get that. Could you rephrase?"

def send_message():
    user_input = entry.get().strip()
    if not user_input:
        return
    current_time = datetime.datetime.now().strftime("%H:%M")

    chat_area.insert(tk.END, f"You [{current_time}]: {user_input}\n", 'user')
    response = get_bot_response(user_input)
    chat_area.insert(tk.END, f"ChatWiz [{current_time}]: {response}\n\n", 'bot')
    chat_area.see(tk.END)
    entry.delete(0, tk.END)

def clear_chat():
    chat_area.delete(1.0, tk.END)

root = tk.Tk()
root.title("💬 ChatWiz - Rule-Based Chatbot")
root.geometry("600x600")
root.configure(bg="#2c3e50")

chat_area = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, font=("Segoe UI", 12),
    bg="#ecf0f1", fg="#2c3e50", padx=12, pady=12
)
chat_area.tag_config('user', foreground='#2980b9', font=('Segoe UI Semibold', 12, 'bold'))
chat_area.tag_config('bot', foreground='#27ae60', font=('Segoe UI', 12))
chat_area.pack(padx=12, pady=12, fill=tk.BOTH, expand=True)

entry_frame = tk.Frame(root, bg="#2c3e50")
entry_frame.pack(pady=8, fill=tk.X)

entry = tk.Entry(entry_frame, font=("Segoe UI", 13), width=40, bg="#ffffff", fg="#2c3e50", bd=2)
entry.pack(side=tk.LEFT, padx=10, pady=5)

send_button = tk.Button(entry_frame, text="➤ Send", command=send_message,
                        bg="#2980b9", fg="white", font=("Segoe UI Semibold", 11), width=10)
send_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(root, text="🧹 Clear Chat", command=clear_chat,
                         bg="#c0392b", fg="white", font=("Segoe UI", 10))
clear_button.pack(pady=8)

entry.bind("<Return>", lambda event: send_message())

root.mainloop()
