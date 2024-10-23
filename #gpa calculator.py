import tkinter as tk

def calculate_gpa():
    g = grade_entry.get().upper().split(",")
    credits = credit_entry.get().split(",")
    tc = 0
    tgp = 0

    grade_point_dict = {
        'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0,
        'D-': 0.7, 'F': 0.0
    }
#loop thru grades adnd credits
    if len(g) != len(credits):
        gpa_label.config(text="Error: Match grades & credits!")
        return

    for i in range(len(g)):
        grade = g[i].strip()
        try:
            credit = float(credits[i].strip())
        except ValueError:
            gpa_label.config(text="Error: Invalid credit!")
            return

        if grade not in grade_point_dict:
            gpa_label.config(text=f"Error: Invalid grade '{grade}'")
            return

        tc += credit
        tgp += grade_point_dict[grade] * credit

    if tc > 0:
        gpa = tgp / tc
        gpa_label.config(text=f"GPA = {gpa:.2f}")
    else:
        gpa_label.config(text="No classes entered.")

#gui thing
root = tk.Tk()
root.title("GPA Calculator")

tk.Label(root, text="Enter Grades (comma-separated):").pack()
grade_entry = tk.Entry(root, width=30)
grade_entry.pack()

tk.Label(root, text="Enter Credits : ").pack()
credit_entry = tk.Entry(root, width=30)
credit_entry.pack()

# calc GPA
tk.Button(root, text="Calculate GPA", command=calculate_gpa).pack()

gpa_label = tk.Label(root, text="GPA = ", font=("Helvetica", 14))
gpa_label.pack(pady=10)
root.mainloop()
