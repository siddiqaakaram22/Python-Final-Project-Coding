import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz")
        self.root.geometry("500x300")
        self.root.configure(bg='grey')  # Set background color to grey

        self.question_number = 0
        self.score = 0

        self.questions = [
            {"question": "How do you define a function in Python?", "options": ["1. function_name():", "2. def function_name():", "3. define function_name():"], "answer": "2. def function_name():"},
            {"question": "What does WWW stand for?", "options": ["1. World Wide Web", "2. World Web Warriors", "3. Wide World Web"], "answer": "1. World Wide Web"},
            {"question": "What is the file extension for PowerPoint presentations?", "options": ["1. .docx", "2. .pdf", "3. .pptx"], "answer": "3. .pptx"},
            {"question": "In what year was Facebook founded?", "options": ["1. 2000", "2. 2004", "3. 2008"], "answer": "2. 2004"},
            {"question": "Which chapter of the Quran is known as the Heart of the Quran?", "options": ["1. Surah Al-Fatiha", "2. Surah Al-Baqarah", "3. Surah Yaseen"], "answer": "3. Surah Yaseen"},
            {"question": "What is the purpose of the if statement in Python?", "options": ["1. Conditional execution", "2. Looping", "3. Variable assignment"], "answer": "1. Conditional execution"},
            {"question": "In Disney's Frozen who has the power to control ice and snow?", "options": ["1. Anna", "2. Elsa", "3. Olaf"], "answer": "2. Elsa"},
            {"question": "Number of continents in the world?", "options": ["1. Eight", "2. Seven", "3. Six"], "answer": "2. Seven"},
            {"question": "What is the largest mammal on Earth?", "options": ["1. Camel", "2. Elephant", "3. Blue Whale"], "answer": "3. Blue Whale"},
            {"question": "In Python what data type is used to store a sequence of elements?", "options": ["1. list", "2. Tuple", "3. String"], "answer": "1. list"},
            {"question": "In which Animated movie the character name is Simba?", "options": ["1. Beauty and The Beast", "2. The lion king", "3. Snow white"], "answer": "2. The lion king"},
            {"question": "Which Microsoft Excel function is used to find the highest value in a range?", "options": ["1. MAX()", "2. HIGH()", "3. TOP()"], "answer": "1. MAX()"},
            {"question": "Which planet is known as the Red Planet?", "options": ["1. Venus", "2. Mars", "3. Jupiter"], "answer": "2. Mars"},
            {"question": "Which Flower is a national flower of Pakistan?", "options": ["1. Rose", "2. Sun Flower", "3. Jasmine"], "answer": "3. Jasmine"},
            {"question": "Which of the following is not a font style?", "options": ["1. Seuperscript", "2. Bold", "3. Italic"], "answer": "1. Seuperscript"},
            {"question": "What is the duration of the national Anthem of Pakistan?:" , "options": ["1. 70 sec", "2. 80 sec", "3. 90 sec"], "answer": "2. 80 sec"},
            {"question": "Globophobia is a fear of?", "options": ["1. Pooping balloons", "2. flying of height", "3. swimmming"], "answer": "1. Pooping balloons"},
            {"question": "How many minutes are in a full week?", "options": ["1. 10090", "2. 10010", "3. 10080"], "answer": "3. 10080"},
            {"question": "How many elements are in the periodic table?", "options": ["1. 119", "2. 118", "3. 111"], "answer": "2. 118"},
            {"question": "Which country has won the most world cups?", "options": ["1. Rome", "2. Brazil", "3. America"], "answer": "2. Brazil"},
            {"question": "How many hearts does an octopus have?", "options": ["1. 03", "2. 04", "3. 02"], "answer": "1. 03"},
            {"question": "What color are mickey mouse shoes?", "options": ["1. Red", "2. Blue", "3. Yellow"], "answer": "3. Yellow"},
            {"question": "What does zam zam means?", "options": ["1. Holy Water", "2. Drink", "3. Stop"], "answer": "3. Stop"},
            {"question": "How many gates of Jannah are there?", "options": ["1. 08", "2. 06", "3. 07"], "answer": "1. 08"},
            {"question": "Which fruit is mention in the Quran?", "options": ["1. Grapes", "2. Apple", "3. Orange"], "answer": "1. Grapes"},
        ]

        self.label_question = tk.Label(root, text="", font=("Georgia", 14), fg='white', bg='grey')  # Set label background color to grey
        self.label_question.pack(pady=20)

        self.radio_var = tk.StringVar()
        self.radio_var.set(None)

        self.radio_buttons = []
        for i in range(3):  # Use 3 instead of 4 options
            radio_btn = tk.Radiobutton(root, text="", variable=self.radio_var, value="", font=("Helvetica", 12), fg='white', bg='grey', indicatoron=0, selectcolor='grey')
            radio_btn.pack(anchor="w")
            self.radio_buttons.append(radio_btn)

        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("Helvetica", 12), fg='yellow', bg='grey', relief=tk.GROOVE)
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.question_number < len(self.questions):
            question_data = self.questions[self.question_number]
            # Display question number along with the question
            question_text = f"{self.question_number + 1}. {question_data['question']}"
            self.label_question.config(text=question_text)

            for i in range(3):  # Use 3 instead of 4 options
                self.radio_buttons[i].config(text=question_data["options"][i], value=question_data["options"][i], fg='white')  # Set font color to white

        else:
            self.show_result()

    def next_question(self):
        selected_option = self.radio_var.get()

        if selected_option == "":
            messagebox.showwarning("Warning", "Please select an option.")
            return

        correct_answer = self.questions[self.question_number]["answer"]
        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Well Done!", "Correct Answer! 😄")

        else:
            messagebox.showinfo("You Lose", f"Wrong Answer!\nCorrect Answer: {correct_answer} 😢")

        # Change font color of the selected option to yellow
        for i in range(3):
            if self.radio_buttons[i]['value'] == selected_option:
                self.radio_buttons[i].config(fg='yellow')

        self.question_number += 1
        self.radio_var.set(None)
        self.load_question()

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"You have completed the quiz!\nYour score: {self.score}/{len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
