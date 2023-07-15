import tkinter as tk
from tkinter import filedialog
from difflib import SequenceMatcher

class PlagiarismChecker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Plagiarism Checker")
        
        # Create Labels
        self.label1 = tk.Label(self.window, text="Original File:")
        self.label1.pack(pady=10)
        
        self.label2 = tk.Label(self.window, text="Comparison File:")
        self.label2.pack(pady=10)
        
        # Create Text Boxes
        self.text_box1 = tk.Text(self.window, height=10, width=50)
        self.text_box1.pack()
        
        self.text_box2 = tk.Text(self.window, height=10, width=50)
        self.text_box2.pack()
        
        # Create Buttons
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(pady=20)
        
        self.load_button1 = tk.Button(self.button_frame, text="Load Original", command=self.load_original)
        self.load_button1.grid(row=0, column=0, padx=10)
        
        self.load_button2 = tk.Button(self.button_frame, text="Load Comparison", command=self.load_comparison)
        self.load_button2.grid(row=0, column=1, padx=10)
        
        self.check_button = tk.Button(self.button_frame, text="Check Plagiarism", command=self.check_plagiarism)
        self.check_button.grid(row=0, column=2, padx=10)
        
        # Run the GUI main loop
        self.window.mainloop()
        
    def load_original(self):
        original_file = filedialog.askopenfilename(initialdir='/', title='Select Original File',
                                                  filetypes=(('Text Files', '*.txt'),))
        with open(original_file, 'r') as file:
            self.text_box1.delete(1.0, tk.END)
            self.text_box1.insert(tk.END, file.read())
        
    def load_comparison(self):
        comparison_file = filedialog.askopenfilename(initialdir='/', title='Select Comparison File',
                                                    filetypes=(('Text Files', '*.txt'),))
        with open(comparison_file, 'r') as file:
            self.text_box2.delete(1.0, tk.END)
            self.text_box2.insert(tk.END, file.read())
        
    def check_plagiarism(self):
        original_text = self.text_box1.get(1.0, tk.END)
        comparison_text = self.text_box2.get(1.0, tk.END)
        
        similarity_ratio = SequenceMatcher(None, original_text, comparison_text).ratio()
        
        result = f"Similarity Ratio: {similarity_ratio:.2%}"
        
        tk.messagebox.showinfo("Plagiarism Check Result", result)

# Create an instance of the PlagiarismChecker class
checker = PlagiarismChecker()
