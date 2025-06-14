import tkinter as tk
from tkinter import messagebox
import random

# Initialize data
routes = {
    "Route A": [],
    "Route B": [],
    "Route C": []
}

# Function to simulate ships on routes
def simulate_traffic():
    # Reset routes
    for r in routes:
        routes[r] = []

    # Add 10 random ships
    for i in range(1, 11):
        ship = f"Ship-{i}"
        route = random.choice(list(routes.keys()))
        routes[route].append(ship)
    
    update_display()

# Function to update UI
def update_display():
    result_text.delete(1.0, tk.END)
    overloaded = []

    result_text.insert(tk.END, "📊 Current Ship Distribution:\n\n")
    for route, ships in routes.items():
        line = f"{route}: {len(ships)} ships - {ships}\n"
        result_text.insert(tk.END, line)
    
    result_text.insert(tk.END, "\n⚠️ Route Status:\n")
    for route, ships in routes.items():
        if len(ships) > 4:
            result_text.insert(tk.END, f"🔴 {route} is overloaded\n")
            overloaded.append(route)
        else:
            result_text.insert(tk.END, f"🟢 {route} is clear\n")

    result_text.insert(tk.END, "\n✅ Suggestion:\n")
    if len(overloaded) == 3:
        result_text.insert(tk.END, "❌ All routes are busy. Wait for clearance.")
    else:
        for route in routes:
            if route not in overloaded:
                result_text.insert(tk.END, f"✅ Best route: {route}")
                break

# GUI setup
root = tk.Tk()
root.title("Marine Traffic Analyzer")
root.geometry("600x500")
root.configure(bg="#E0F7FA")

title = tk.Label(root, text="🚢 Marine Traffic Analyzer 🚢", font=("Helvetica", 18, "bold"), bg="#E0F7FA", fg="blue")
title.pack(pady=10)

simulate_btn = tk.Button(root, text="Simulate Ship Traffic", font=("Arial", 14), bg="lightgreen", command=simulate_traffic)
simulate_btn.pack(pady=10)

result_text = tk.Text(root, width=70, height=20, font=("Courier", 10))
result_text.pack(pady=10)

simulate_traffic()  # Initial call

root.mainloop()
