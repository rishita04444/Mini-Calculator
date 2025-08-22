import tkinter as tk
from tkinter import messagebox
import random

class SimpleQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Quiz App")
        self.root.geometry("400x500")
        
        # Quiz questions
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                "answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "answer": "Mars"
            },
            {
                "question": "What is the largest mammal in the world?",
                "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
                "answer": "Blue Whale"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Van Gogh", "Picasso", "Da Vinci", "Michelangelo"],
                "answer": "Da Vinci"
            },
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Go", "Gd", "Au", "Ag"],
                "answer": "Au"
            }
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.create_welcome_screen()
    
    def create_welcome_screen(self):
        """Create the welcome screen"""
        self.clear_screen()
        
        welcome_label = tk.Label(self.root, text="Simple Quiz", font=("Arial", 20, "bold"))
        welcome_label.pack(pady=20)
        
        info_label = tk.Label(self.root, text="Answer 5 general knowledge questions\nTest your knowledge!", 
                             font=("Arial", 12))
        info_label.pack(pady=10)
        
        start_btn = tk.Button(self.root, text="Start Quiz", font=("Arial", 14),
                             command=self.start_quiz, bg="#4CAF50", fg="white")
        start_btn.pack(pady=30)
    
    def start_quiz(self):
        """Start the quiz"""
        self.current_question = 0
        self.score = 0
        self.show_question()
    
    def show_question(self):
        """Display the current question"""
        self.clear_screen()
        
        if self.current_question >= len(self.questions):
            self.show_results()
            return
        
        # Progress indicator
        progress_label = tk.Label(self.root, 
                                 text=f"Question {self.current_question + 1} of {len(self.questions)}",
                                 font=("Arial", 10))
        progress_label.pack(pady=5)
        
        # Question
        question_data = self.questions[self.current_question]
        question_label = tk.Label(self.root, text=question_data["question"], 
                                 font=("Arial", 14, "bold"), wraplength=350)
        question_label.pack(pady=20)
        
        # Options
        options = question_data["options"]
        random.shuffle(options)
        
        for option in options:
            btn = tk.Button(self.root, text=option, font=("Arial", 12),
                           command=lambda opt=option: self.check_answer(opt),
                           width=20, pady=5)
            btn.pack(pady=5)
    
    def check_answer(self, selected_option):
        """Check if the selected answer is correct"""
        question_data = self.questions[self.current_question]
        correct_answer = question_data["answer"]
        
        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Result", "Correct! ✅")
        else:
            messagebox.showinfo("Result", f"Incorrect ❌\nCorrect answer: {correct_answer}")
        
        self.current_question += 1
        self.show_question()
    
    def show_results(self):
        """Show the final results"""
        self.clear_screen()
        
        result_label = tk.Label(self.root, text="Quiz Completed!", font=("Arial", 18, "bold"))
        result_label.pack(pady=20)
        
        score_label = tk.Label(self.root, 
                              text=f"Your score: {self.score}/{len(self.questions)}",
                              font=("Arial", 16))
        score_label.pack(pady=10)
        
        percentage = (self.score / len(self.questions)) * 100
        performance_label = tk.Label(self.root, 
                                   text=f"Score: {percentage:.1f}%",
                                   font=("Arial", 14))
        performance_label.pack(pady=5)
        
        # Simple performance message
        if percentage >= 80:
            message = "Excellent work!"
            color = "green"
        elif percentage >= 60:
            message = "Good job!"
            color = "orange"
        else:
            message = "Keep practicing!"
            color = "red"
        
        message_label = tk.Label(self.root, text=message, font=("Arial", 12), fg=color)
        message_label.pack(pady=10)
        
        restart_btn = tk.Button(self.root, text="Play Again", font=("Arial", 12),
                               command=self.create_welcome_screen, bg="#2196F3", fg="white")
        restart_btn.pack(pady=20)
    
    def clear_screen(self):
        """Clear all widgets from the root window"""
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    app = SimpleQuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
