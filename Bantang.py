import tkinter as tk
from tkinter import ttk


class GradeTrackerApp:
   def __init__(self, root):
       self.root = root 
       self.root.title("Grade Tracker")
       self.root.configure(bg="#FFB6C1")
      


       # Initialize variables
       self.subjects = []
       self.grades = {}


       # Create widgets
       self.subject_label = ttk.Label(root, text="Subject:", background="#815ea4", foreground="white")
       self.subject_entry = ttk.Entry(root)
       self.grade_label = ttk.Label(root, text="Grade:", background="#815ea4", foreground="white")
       self.grade_entry = ttk.Entry(root)
       self.add_button = ttk.Button(root, text="Add Grade", command=self.add_grade, style="Purple.TButton")
       self.calculate_button = ttk.Button(root, text="Calculate GPA", command=self.calculate_gpa, style="Purple.TButton")
       self.delete_button = ttk.Button(root, text="Delete All", command=self.delete_all, style="Red.TButton")
       self.grade_text = tk.Text(root, height=10, width=30, background="#f0e5f2", foreground="#000000", insertbackground="black")


       # Add widgets to the grid
       self.subject_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
       self.subject_entry.grid(row=0, column=1, padx=5, pady=5)
       self.grade_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
       self.grade_entry.grid(row=1, column=1, padx=5, pady=5)
       self.add_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
       self.calculate_button.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
       self.delete_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
       self.grade_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")


       # Create a style for buttons
       self.root.style = ttk.Style()
       self.root.style.configure("Purple.TButton", foreground="black", background="#815ea4")
       self.root.style.configure("Red.TButton", foreground="black", background="#d32f2f")


   def add_grade(self):
       subject = self.subject_entry.get()
       grade = float(self.grade_entry.get())


       if subject in self.grades:
           self.grades[subject].append(grade)
       else:
           self.grades[subject] = [grade]


       self.update_grade_text()


   def calculate_gpa(self):
       total_credits = 0
       total_grade_points = 0


       for subject, grades in self.grades.items():
           credits = len(grades)
           total_credits += credits
           total_grade_points += sum(grades)


       if total_credits == 0:
           gpa = 0.0
       else:
           gpa = total_grade_points / total_credits


       self.grade_text.insert(tk.END, f"Total Credits: {total_credits}\n")
       self.grade_text.insert(tk.END, f"Total Grade Points: {total_grade_points}\n")
       self.grade_text.insert(tk.END, f"GPA: {gpa:.2f}\n")


   def delete_all(self):
       self.grades = {}
       self.update_grade_text()


   def update_grade_text(self):
       self.grade_text.delete(1.0, tk.END)


       for subject, grades in self.grades.items():
           self.grade_text.insert(tk.END, f"{subject}: ")
           self.grade_text.insert(tk.END, ", ".join(map(str, grades)) + "\n")


if __name__ == "__main__":
   root = tk.Tk()
   app = GradeTrackerApp(root)
   root.mainloop()    

