# ============================================
# PLANT CARE MANAGEMENT SYSTEM
# ============================================
# Features:
# - Secure Login System
# - Plant Information Management
# - Growth Tracking
# - Watering & Sunlight Scheduling
# - Reports & Analytics
# - CSV Storage
# - Modern GUI Design using Tkinter
# ============================================

import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from datetime import datetime

# ============================================
# DATA FILES
# ============================================

PLANT_FILE = "plants.csv"
USER_FILE = "users.csv"

# ============================================
# USER CLASS
# ============================================

class User:
    def __init__(self, username, password, role="User"):
        self.__username = username
        self.__password = password
        self.__role = role

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_role(self):
        return self.__role


# ============================================
# PLANT CLASS
# ============================================

class Plant:
    def __init__(self, name, species, plant_type,
                 growth_stage, watering, sunlight, health):

        self.name = name
        self.species = species
        self.plant_type = plant_type
        self.growth_stage = growth_stage
        self.watering = watering
        self.sunlight = sunlight
        self.health = health


# ============================================
# DATA MANAGER
# ============================================

class DataManager:

    @staticmethod
    def initialize_files():

        if not os.path.exists(PLANT_FILE):
            with open(PLANT_FILE, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "Name",
                    "Species",
                    "Type",
                    "Growth Stage",
                    "Watering",
                    "Sunlight",
                    "Health"
                ])

        if not os.path.exists(USER_FILE):
            with open(USER_FILE, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Username", "Password", "Role"])
                writer.writerow(["admin", "admin123", "Admin"])

    @staticmethod
    def save_plant(plant):

        with open(PLANT_FILE, "a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                plant.name,
                plant.species,
                plant.plant_type,
                plant.growth_stage,
                plant.watering,
                plant.sunlight,
                plant.health
            ])

    @staticmethod
    def load_plants():

        plants = []

        with open(PLANT_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                plants.append(row)

        return plants

    @staticmethod
    def validate_login(username, password):

        with open(USER_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                if row[0] == username and row[1] == password:
                    return True

        return False


# ============================================
# CARE SCHEDULER
# ============================================

class CareScheduler:

    @staticmethod
    def watering_message(schedule):
        return f"Next watering schedule: {schedule}"

    @staticmethod
    def sunlight_message(schedule):
        return f"Sunlight exposure: {schedule}"


# ============================================
# REPORT GENERATOR
# ============================================

class ReportGenerator:

    @staticmethod
    def generate_report():

        plants = DataManager.load_plants()

        total = len(plants)

        healthy = 0
        unhealthy = 0

        for plant in plants:
            if plant[6].lower() == "healthy":
                healthy += 1
            else:
                unhealthy += 1

        report = (
            f"Total Plants: {total}\n"
            f"Healthy Plants: {healthy}\n"
            f"Unhealthy Plants: {unhealthy}\n"
        )

        return report


# ============================================
# MAIN APPLICATION
# ============================================

class PlantCareApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Plant Care Management System")
        self.root.geometry("1200x700")
        self.root.configure(bg="#1e272e")

        DataManager.initialize_files()

        self.create_login_screen()

    # ========================================
    # LOGIN UI
    # ========================================

    def create_login_screen(self):

        self.clear_window()

        frame = tk.Frame(
        
           self.root,
            bg="#2f3640",
            padx=40,
            pady=40
        )

        frame.place(relx=0.5, rely=0.5, anchor="center")

        title = tk.Label(
            frame,
            text="Plant Care System",
            font=("Segoe UI", 24, "bold"),
            fg="white",
            bg="#2f3640"
        )

        title.pack(pady=20)

        tk.Label(
            frame,
            text="Username",
            fg="white",
            bg="#2f3640",
            font=("Segoe UI", 12)
        ).pack()

        self.username_entry = tk.Entry(
            frame,
            font=("Segoe UI", 12),
            width=30
        )

        self.username_entry.pack(pady=10)

        tk.Label(
            frame,
            text="Password",
            fg="white",
            bg="#2f3640",
            font=("Segoe UI", 12)
        ).pack()

        self.password_entry = tk.Entry(
            frame,
            show="*",
            font=("Segoe UI", 12),
            width=30
        )

        self.password_entry.pack(pady=10)

        login_button = tk.Button(
            frame,
            text="LOGIN",
            font=("Segoe UI", 12, "bold"),
            bg="#44bd32",
            fg="white",
            width=20,
            command=self.login
        )

        login_button.pack(pady=20)

    # ========================================
    # LOGIN FUNCTION
    # ========================================

    def login(self):

        username = self.username_entry.get()
        password = self.password_entry.get()

        try:

            if DataManager.validate_login(username, password):

                messagebox.showinfo(
                    "Success",
                    "Login Successful!"
                )

                self.create_dashboard()

            else:
                messagebox.showerror(
                    "Error",
                    "Invalid Username or Password"
                )

        except Exception as e:
            messagebox.showerror(
                "System Error",
                str(e)
            )

    # ========================================
    # DASHBOARD UI
    # ========================================

    def create_dashboard(self):

        self.clear_window()

        header = tk.Frame(
            self.root,
            bg="#10ac84",
            height=80
        )

        header.pack(fill="x")

        title = tk.Label(
            header,
            text="Plant Care Dashboard",
            font=("Segoe UI", 24, "bold"),
            bg="#10ac84",
            fg="white"
        )

        title.pack(pady=15)

        main_frame = tk.Frame(
            self.root,
            bg="#1e272e"
        )

        main_frame.pack(fill="both", expand=True)

        left_frame = tk.Frame(
            main_frame,
            bg="#2f3640",
            width=350,
            padx=20,
            pady=20
        )

        left_frame.pack(side="left", fill="y")

        right_frame = tk.Frame(
            main_frame,
            bg="#353b48",
            padx=20,
            pady=20
        )

        right_frame.pack(side="right", fill="both", expand=True)

        # ====================================
        # FORM TITLE
        # ====================================

        tk.Label(
            left_frame,
            text="Add New Plant",
            font=("Segoe UI", 18, "bold"),
            fg="white",
            bg="#2f3640"
        ).pack(pady=10)

        # ====================================
        # INPUT FIELDS
        # ====================================

        self.entries = {}

        fields = [
            "Plant Name",
            "Species",
            "Plant Type",
            "Growth Stage",
            "Watering Schedule",
            "Sunlight Schedule",
            "Health Status"
        ]

        for field in fields:

            tk.Label(
                left_frame,
                text=field,
                fg="white",
                bg="#2f3640",
                font=("Segoe UI", 11)
            ).pack(anchor="w", pady=5)

            entry = tk.Entry(
                left_frame,
                font=("Segoe UI", 11),
                width=30
            )

            entry.pack(pady=5)

            self.entries[field] = entry

        # ====================================
        # SAVE BUTTON
        # ====================================

        save_button = tk.Button(
            left_frame,
            text="SAVE PLANT",
            font=("Segoe UI", 12, "bold"),
            bg="#44bd32",
            fg="white",
            width=25,
            command=self.save_plant
        )

        save_button.pack(pady=20)

        report_button = tk.Button(
            left_frame,
            text="GENERATE REPORT",
            font=("Segoe UI", 12, "bold"),
            bg="#0984e3",
            fg="white",
            width=25,
            command=self.show_report
        )

        report_button.pack(pady=20)

        report_button = tk.Button(
            left_frame,
            text="GENERATE REPORT",
            font=("Segoe UI", 12, "bold"),
            bg="#0984e3",
            fg="white",
            width=25,
            command=self.show_report
        )

        report_button.pack(pady=10)

        # ====================================
        # TABLE
        # ====================================

        columns = (
            "Name",
            "Species",
            "Type",
            "Growth",
            "Watering",
            "Sunlight",
            "Health"
        )

        self.tree = ttk.Treeview(
            right_frame,
            columns=columns,
            show="headings",
            height=20
        )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        self.tree.pack(fill="both", expand=True)

        self.load_table()

    # ========================================
    # SAVE PLANT
    # ========================================

    def save_plant(self):

        try:

            values = []

            for field, entry in self.entries.items():

                value = entry.get().strip()

                if value == "":
                    raise ValueError(
                        f"{field} cannot be empty."
                    )

                values.append(value)

            plant = Plant(
                values[0],
                values[1],
                values[2],
                values[3],
                values[4],
                values[5],
                values[6]
            )

            DataManager.save_plant(plant)

            messagebox.showinfo(
                "Success",
                "Plant Saved Successfully!"
            )

            self.load_table()

            for entry in self.entries.values():
                entry.delete(0, tk.END)

        except Exception as e:

            messagebox.showerror(
                "Input Error",
                str(e)
            )

    # ========================================
    # LOAD TABLE
    # ========================================

    def load_table(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        plants = DataManager.load_plants()

        for plant in plants:
            self.tree.insert("", tk.END, values=plant)

    # ========================================
    # REPORT WINDOW
    # ========================================

    def show_report(self):

        report = ReportGenerator.generate_report()

        report_window = tk.Toplevel(self.root)
        report_window.title("Plant Report")
        report_window.geometry("400x300")
        report_window.configure(bg="#2f3640")

        tk.Label(
            report_window,
            text="Plant Health Report",
            font=("Segoe UI", 18, "bold"),
            fg="white",
            bg="#2f3640"
        ).pack(pady=20)

        tk.Label(
            report_window,
            text=report,
            font=("Segoe UI", 14),
            fg="#dcdde1",
            bg="#2f3640",
            justify="left"
        ).pack(pady=20)

    # ========================================
    # CLEAR WINDOW
    # ========================================

    def clear_window(self):

        for widget in self.root.winfo_children():
            widget.destroy()


# ============================================
# APPLICATION START
# ============================================

if __name__ == "__main__":

    root = tk.Tk()

    app = PlantCareApp(root)

    root.mainloop()