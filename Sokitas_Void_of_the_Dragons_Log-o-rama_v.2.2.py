import os
import random
import re
import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime
from tkinter import scrolledtext, messagebox, filedialog, font
import configparser
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class CombatAnalyzer:
    MOUNTAIN_GOAT_SONGS = [
        ("No Children", 2002),
        ("This Year", 2005),
        ("The Best Ever Death Metal Band in Denton", 2002),
        ("Up the Wolves", 2005),
        ("Dance Music", 2005),
        ("Going to Georgia", 1994),
        ("Love, Love, Love", 2005),
        ("Woke Up New", 2006),
        ("Cry for Judas", 2012),
        ("Fault Lines", 2011),
        ("Sax Rohmer #1", 2008),
        ("Old College Try", 2002),
        ("Amy AKA Spent Gladiator 1", 2012),
        ("The Grey King and the Silver Flame Attunement", 2015),
        ("Tallahassee", 2002),
        ("Damn These Vampires", 2011),
        ("Game Shows Touch Our Lives", 2002),
        ("This Magic Moment", 2005),
        ("Cotton", 2004),
        ("Foreign Object", 2015),
        ("In the Craters on the Moon", 2008),
        ("Lion's Teeth", 2005),
        ("Palmcorder Yajna", 2004),
        ("Harlem Roulette", 2012),
        ("Get Lonely", 2006),
        ("Cubs in Five", 1995),
        ("Southwood Plantation Road", 2002),
        ("Estate Sale Sign", 2011),
        ("Up the Wolves", 2005),
        ("Golden Boy", 2006),
        ("In Memory of Satan", 2012),
        ("Sax Rohmer #2", 1995),
        ("Have to Explode", 2017),
        ("The Mess Inside", 2002),
        ("Wear Black", 2017),
        ("Family Happiness", 2005),
        ("The Diaz Brothers", 2012),
        ("San Bernardino", 2008),
        ("Against Pollution", 2004),
        ("In the Hidden Places", 2006),
        ("Oceanographer's Choice", 2002),
        ("Shadow Song", 2000),
        ("Stabbed to Death Outside San Juan", 2004),
        ("Alpha Desperation March", 1994),
        ("Alpha Rats Nest", 2002),
        ("In the Shadow of the Western Hills", 1994),
        ("Broom People", 2005),
        ("Billy the Kid's Dream of the Magic Shoes", 2006),
        ("Rain in Soho", 2017),
        ("Linda Blair Was Born Innocent", 2000),
        ("Color in Your Cheeks", 2002),
        ("For Charles Bronson", 1991),
        ("Ezekiel 7 and the Permanent Efficacy of Grace", 2009),
        ("Grendel's Mother", 1994),
        ("Tianchi Lake", 2017),
        ("In League with Dragons", 2019),
        ("Jaipur", 1991),
        ("Song for Dennis Brown", 2005),
        ("Autoclave", 2008),
        ("Woke Up New", 2006),
        ("Cry for Judas", 2012),
        ("Fault Lines", 2011),
        ("Sax Rohmer #1", 2008),
        ("Old College Try", 2002),
        ("Amy AKA Spent Gladiator 1", 2012),
        ("The Grey King and the Silver Flame Attunement", 2015),
        ("Tallahassee", 2002),
        ("Damn These Vampires", 2011),
        ("Game Shows Touch Our Lives", 2002),
        ("This Magic Moment", 2005),
        ("Cotton", 2004),
        ("Foreign Object", 2015),
        ("In the Craters on the Moon", 2008),
        ("Lion's Teeth", 2005),
        ("Palmcorder Yajna", 2004),
        ("Harlem Roulette", 2012),
        ("Get Lonely", 2006),
        ("Cubs in Five", 1995),
        ("Southwood Plantation Road", 2002),
        ("Estate Sale Sign", 2011),
        ("Golden Boy", 2006),
        ("In Memory of Satan", 2012),
        ("Sax Rohmer #2", 1995),
        ("Have to Explode", 2017),
        ("The Mess Inside", 2002),
        ("Wear Black", 2017),
        ("Family Happiness", 2005),
        ("The Diaz Brothers", 2012),
        ("San Bernardino", 2008),
        ("Against Pollution", 2004),
        ("In the Hidden Places", 2006),
        ("Oceanographer's Choice", 2002),
        ("Shadow Song", 2000),
        ("Stabbed to Death Outside San Juan", 2004),
        ("Alpha Desperation March", 1994),
        ("Alpha Rats Nest", 2002),
        ("In the Shadow of the Western Hills", 1994),
        ("Broom People", 2005),
        ("Billy the Kid's Dream of the Magic Shoes", 2006),
        ("Rain in Soho", 2017),
        ("Linda Blair Was Born Innocent", 2000),
        ("Color in Your Cheeks", 2002),
        ("For Charles Bronson", 1991),
        ("Lovecraft in Brooklyn", 2008),
        ("Distant Stations", 1994),
        ("Your Belgian Things", 2004),
        ("Quito", 2004),
        ("Quetzalcoatl Eats Plums", 1994),
        ("See America Right", 2002),
        ("Genesis 30:3", 2002),
        ("Ezekiel 7 and the Permanent Efficacy of Grace", 2009),
        ("Grendel's Mother", 1994),
        ("Tianchi Lake", 2017),
        ("In League with Dragons", 2019),
        ("Jaipur", 1991),
        ("Song for Dennis Brown", 2005),
        ("Autoclave", 2008),
        ("The Young Thousands", 2004),
        ("Liza Forever Minnelli", 2002),
        ("High Hawk Season", 2011),
        ("Birth of Serpents", 2011),
        ("Quito", 2004),
        ("Quetzalcoatl Eats Plums", 1994),
        ("See America Right", 2002),
        ("Genesis 30:3", 2002),
        ("Ezekiel 7 and the Permanent Efficacy of Grace", 2009),
        ("Grendel's Mother", 1994),
        ("Tianchi Lake", 2017),
        ("In League with Dragons", 2019),
        ("Jaipur", 1991),
        ("Song for Dennis Brown", 2005),
        ("Autoclave", 2008),
        ("The Young Thousands", 2004),
        ("Liza Forever Minnelli", 2002),
        ("High Hawk Season", 2011),
        ("Birth of Serpents", 2011),
        ("1 Samuel 15:23", 2009),
        ("Heel Turn 2", 2015),
        ("The Recognition Scene", 1995),
        ("Hast Thou Considered the Tetrapod", 2005),
        ("How to Embrace a Swamp Creature", 2017),
        ("The Ballad of Bull Ramos", 2015),
        ("Younger", 2017),
        ("Hebrews 11:40", 2009),
        ("Never Quite Free", 2011),
        ("California Song", 1995),
        ("Pigs That Ran Straightaway into the Water, Triumph Of", 2004),
        ("Stabbed to Death Outside San Juan", 2004),
        ("Alpha Desperation March", 1994),
        ("Alpha Rats Nest", 2002),
        ("In the Shadow of the Western Hills", 1994),
        ("Broom People", 2005),
        ("Billy the Kid's Dream of the Magic Shoes", 2006)
    ]

    def __init__(self):
        self.total_damage = 0
        self.total_experience = 0
        self.total_hits = 0
        self.total_crits = 0
        self.total_crit_damage = 0
        self.total_damage_taken = 0
        self.average_damage_taken = 0
        self.player_effects = {}
        self.hits_data = []
        self.total_evaded_hits = 0
        self.evasion_chance = 0
        self.total_heals = 0
        self.total_healing = 0
        self.personal_best_hit = 0  # Initialize personal best hit
        self.total_commander_injuries = 0
        self.total_troop_losses = 0

        self.log_results_enabled = self.read_log_results_setting()

        self.font_family = "Arial"
        self.font_size = 10


    def read_log_results_setting(self):
        try:
            config = configparser.ConfigParser()
            config.read('config.ini')
            return config.getboolean('LoggingSettings', 'LogResultsEnabled', fallback=True)
        except (configparser.NoSectionError, configparser.NoOptionError):
            # Handle the case where the section or option is not found
            return True

    def reset_data(self):
        self.total_damage = 0
        self.total_experience = 0
        self.total_hits = 0
        self.total_crits = 0
        self.total_crit_damage = 0
        self.total_damage_taken = 0
        self.average_damage_taken = 0
        self.player_effects = {}
        self.hits_data = []
        self.total_evaded_hits = 0
        self.evasion_chance = 0
        self.total_heals = 0
        self.total_healing = 0
        self.personal_best_hit = 0  # Initialize personal best hit
        self.total_commander_injuries = 0
        self.total_troop_losses = 0


    def format_number(self, number):
        return f"{number:,.0f}"

    def analyze_hit(self, hit_lines):
        if len(hit_lines) < 2:
            return

        player_damage_line = hit_lines[0]
        player_effects_lines = hit_lines[1:]

        if len(player_effects_lines) < 1:
            return

        player_damage, experience = self.parse_damage_experience(player_damage_line)
        self.total_damage += player_damage
        self.total_experience += experience
        self.parse_effects(player_effects_lines, self.player_effects)

        if "crit" in player_damage_line.lower():
            self.total_crits += 1
            self.total_crit_damage += player_damage

        self.hits_data.append({
            'hit_number': self.total_hits + 1,
            'experience_gained': experience,
            'damage_done': player_damage
        })

        # Check for a new personal best hit
        if player_damage > self.personal_best_hit:
            self.personal_best_hit = player_damage

            self.save_config()

        self.total_hits += 1

        for line in player_effects_lines:
            if "restored" in line.lower() and "health" in line.lower():
                self.parse_healing(line)

    def parse_damage_experience(self, line):
        match = re.search(r'(\d{1,3}(?:,\d{3})*?) damage and earned (\d{1,3}(?:,\d{3})*?) experience', line)
        if match:
            player_damage = int(match.group(1).replace(',', ''))
            experience = int(match.group(2).replace(',', ''))
            return player_damage, experience
        return 0, 0

    def parse_effects(self, lines, effects_dict):
        for line in lines:
            match = re.search(r'(.+?) (contributed|added|dealt) (\d{1,3}(?:,\d{3})*?) damage', line)
            if match:
                effect_name, effect_damage = match.group(1).strip(), int(match.group(3).replace(',', ''))
                effects_dict[effect_name] = effects_dict.get(effect_name, {'damage': 0, 'procs': 0, 'total_damage': 0})
                effects_dict[effect_name]['damage'] += effect_damage
                effects_dict[effect_name]['procs'] += 1
                effects_dict[effect_name]['total_damage'] += effect_damage

    def parse_damage_taken(self, line):
        match = re.search(r'(\S+) strikes you for (\d+) damage!', line)
        if match:
            damage_taken = int(match.group(2))
            self.total_damage_taken += damage_taken
            self.average_damage_taken = self.total_damage_taken / max(self.total_hits, 1)

    def parse_healing(self, line):
        match = re.search(r'(.+?) restored (\d{1,3}(?:,\d{3})*?) of your Health', line)
        if match:
            heal_amount = int(match.group(2).replace(',', ''))
            self.total_heals += 1
            self.total_healing += heal_amount

    def calculate_evasion_chance(self):
        if self.total_hits > 0:
            self.evasion_chance = (self.total_evaded_hits / self.total_hits) * 100

    def parse_formation_damage(self, line):
        troop_loss_match = re.search(r'Your armies suffered Troop losses from that last attack!', line)
        commander_injury_match = re.search(r'Your Commanders were injured from that last attack!', line)

        if troop_loss_match:
            self.total_troop_losses += 1
        if commander_injury_match:
            self.total_commander_injuries += 1

    def display_results(self):
        total_player_effects_damage = sum(effect['total_damage'] for effect in self.player_effects.values())
        overall_damage = self.total_damage
        regular_hit_damage = self.total_damage - total_player_effects_damage

        result_str = (
            f"Total Hits: {self.format_number(self.total_hits)}\n"
            f"Overall Damage: {self.format_number(overall_damage)}\n"
            f"Average Damage Per Hit: {self.format_number(overall_damage / max(self.total_hits, 1))}\n"
            f"Regular Hit Damage: {self.format_number(regular_hit_damage)}\n"
            f"Total Player Effect Damage: {self.format_number(sum(effect['total_damage'] for effect in self.player_effects.values()))}\n\n"

            f"Overall Experience Gained: {self.format_number(self.total_experience)}\n"
            f"Experience Gained Per Hit: {self.format_number(self.total_experience / max(self.total_hits, 1))}\n\n"

            f"Crit Rate: {self.format_number(self.total_crits / max(self.total_hits, 1) * 100)}%\n"
            f"Total Crit Damage: {self.format_number(self.total_crit_damage)}\n\n"

            f"Total Damage Taken: {self.format_number(self.total_damage_taken)}\n"
            f"Average Damage Taken Per Hit: {self.format_number(self.average_damage_taken)}\n"
            f"Total Heals: {self.format_number(self.total_heals)}\n"
            f"Total Healing: {self.format_number(self.total_healing)}\n"
            f"Average Healing Per Heal: {self.format_number(self.total_healing / max(self.total_heals, 1))}\n\n"


            f"Total Evaded Hits: {self.format_number(self.total_evaded_hits)}\n"
            f"Evasion Chance: {self.format_number(self.evasion_chance)}%\n\n"

            f"Instances of Commander Damage taken: {self.format_number(self.total_commander_injuries)}\n"
            f"Instances of Troop Damage taken: {self.format_number(self.total_troop_losses)}\n\n"




            "Player Effects:\n"
        )

        for i, (effect, stats) in enumerate(self.player_effects.items()):
            damage_percentage = stats['damage'] / max(overall_damage, 1) * 100
            average_damage_per_hit = stats['damage'] / max(self.total_hits, 1)
            average_damage_per_proc = stats['total_damage'] / max(stats['procs'], 1)

            # Format percentages with two decimal places
            damage_percentage_str = f"{damage_percentage:.2f}"
            average_damage_per_hit_str = f"{average_damage_per_hit:.2f}"
            average_damage_per_proc_str = f"{average_damage_per_proc:.2f}"

            result_str += (
                f"{effect}: {self.format_number(stats['damage'])} damage "
                f"({damage_percentage_str}% of total damage, "
                f"{average_damage_per_hit_str} per hit, "
                f"{stats['procs']} procs, {average_damage_per_proc_str} per proc)"
            )

            # Add divider lines between effects, except for the last one
            if i < len(self.player_effects) - 1:
                result_str += "\n" + "=" * 50 + "\n"

        return result_str

    def get_damage_distribution(self, regular_hit_damage):
        damage_distribution = {
            'Regular Hit Damage': regular_hit_damage,
            **{effect: stats['damage'] for effect, stats in self.player_effects.items()}
        }
        return damage_distribution

    def get_damage_distribution_percentage(self, overall_damage, regular_hit_damage):
        total_player_effects_damage = sum(effect['total_damage'] for effect in self.player_effects.values())
        regular_hit_damage = self.total_damage

        damage_distribution_percentage = {
            'Regular Hit Damage': (regular_hit_damage / overall_damage * 100),
            **{effect: max(0, stats['damage'] / max(overall_damage, 1) * 100) for effect, stats in
               self.player_effects.items()}
        }

        # Adjust the 'Regular Hit Damage' percentage to ensure that the sum is 100%
        # total_percentage = sum(damage_distribution_percentage.values())
        # if total_percentage != 100:
        #    damage_distribution_percentage['Regular Hit Damage'] += 100 - total_percentage

        return damage_distribution_percentage

    def load_config(self):
        config = configparser.ConfigParser()
        if not os.path.exists('config.ini'):
            # If not, create it with default values
            config['PersonalBest'] = {'Value': '0'}
            config['FontSettings'] = {'FontFamily': 'Arial', 'FontSize': 10}
            config["LoggingSettings"] = {"LogResultsEnabled": "False"}
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        try:
            config.read('config.ini')
            self.personal_best_hit = int(config['PersonalBest']['Value'])
        except (configparser.NoSectionError, configparser.NoOptionError, ValueError):
            self.personal_best_hit = 0

    def save_config(self):
        config = configparser.ConfigParser()
        config['PersonalBest'] = {'Value': str(self.personal_best_hit)}
        config['FontSettings'] = {'FontFamily': self.font_family, 'FontSize': str(self.font_size)}
        config['LoggingSettings'] = {'LogResultsEnabled': str(self.log_results_enabled)}

        with open('config.ini', 'w') as configfile:
            config.write(configfile)



    def log_results(self, result_str):
        if not self.log_results_enabled:
            return

        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{date_str}\n{result_str}\n\n"

        try:
            with open("history.txt", "a") as log_file:
                log_file.write(log_entry)
        except FileNotFoundError:
            # Create the history.txt file if it doesn't exist
            with open("history.txt", "w") as log_file:
                log_file.write(log_entry)
        except Exception as e:
            print(f"Error writing to log file: {str(e)}")


class CombatLogParserApp:
    def __init__(self, root):
        self.root = root
        root.title("Sokitas' Void of the Dragons Log-o-rama 2.1 - Electric Log-aloo 2: Log Harder")

        # Configure dark theme
        root.tk_setPalette(background="#2E2E2E", foreground="#FFFFFF", activeBackground="#4E4E4E",
                           activeForeground="#FFFFFF")

        self.config = configparser.ConfigParser()

        # Load the configuration file
        self.load_config()

        # Create a font style
        self.font_family = self.config.get('FontSettings', 'FontFamily', fallback='Arial')
        self.font_size = self.config.getint('FontSettings', 'FontSize', fallback=10)
        custom_font = font.Font(family=self.font_family, size=self.font_size)

        # Logging settings
        self.log_results_enabled = self.config.getboolean('LoggingSettings', 'LogResultsEnabled', fallback=False)

        # Create a centered frame with a custom style for background color
        style = ttk.Style()
        style.configure("CenterFrame.TFrame", background="#2E2E2E")

        center_frame = ttk.Frame(root, style="CenterFrame.TFrame")
        center_frame.grid(row=0, column=0, padx=2, pady=2)

        # Character Name Input
        self.character_name_label = tk.Label(center_frame, text="Character Name:", bg="#2E2E2E", fg="#FFFFFF")
        self.character_name_label.grid(row=0, column=0, pady=5, padx=1, sticky="e")

        # Combobox for Character Name
        self.character_names = self.load_character_names()
        self.character_name_combobox = ttk.Combobox(center_frame, values=self.character_names, state="write",
                                                    style="Dark.TCombobox")
        self.character_name_combobox.grid(row=0, column=1, pady=1, padx=10, sticky="w")

        # Button to add current character name
        add_button = tk.Button(center_frame, text="Add", command=self.add_character_name, bg="#2E7D32", fg="#FFFFFF")
        add_button.grid(row=0, column=2, pady=1, padx=5, sticky="e")

        # Text Input
        self.text_input = scrolledtext.ScrolledText(root, width=100, height=10, bg="#2E2E2E", fg="#FFFFFF",
                                                    font=custom_font)
        self.text_input.grid(row=1, column=0, columnspan=3, pady=5, padx=5)

        # Create a frame for the middle buttons
        middle_buttons_frame = tk.Frame(root)
        middle_buttons_frame.grid(row=2, column=0, columnspan=3, pady=5, padx=5)

        # Parse Button with green color
        parse_button = tk.Button(middle_buttons_frame, text="Parse Combat Log", command=self.parse_combat_log,
                                 bg="#2E7D32",
                                 fg="#FFFFFF")
        parse_button.grid(row=0, column=0, pady=1, padx=3, sticky="w")
        Tooltip(parse_button, "Click to parse combat log.")

        # Reset Input Button with red color
        reset_input_button = tk.Button(middle_buttons_frame, text="Reset Input", command=self.reset_input, bg="#731010",
                                       fg="#FFFFFF")
        reset_input_button.grid(row=0, column=1, pady=1, padx=3, sticky="w")
        Tooltip(reset_input_button, "Click to the input textbox.")
        # Reset Output Button with yellow color
        reset_output_button = tk.Button(middle_buttons_frame, text="Reset Output and internal Data",
                                        command=self.reset_output,
                                        bg="#ba9457", fg="#000000")
        reset_output_button.grid(row=0, column=2, pady=1, padx=3, sticky="w")
        Tooltip(reset_output_button, "Click to reset output textbox and and internally saved variables.")
        # Save Results Button with blue color
        save_button = tk.Button(middle_buttons_frame, text="Save Results", command=self.save_results, bg="#1565C0",
                                fg="#FFFFFF")
        save_button.grid(row=0, column=3, pady=1, padx=3, sticky="w")
        Tooltip(save_button, "Click to save results to a .txt file.")

        # Display Column Chart Button with purple color
        column_chart_button = tk.Button(middle_buttons_frame, text="Display Column and Timeline Chart",
                                        command=self.display_column_chart, bg="#6A1B9A", fg="#FFFFFF")
        column_chart_button.grid(row=0, column=4, pady=1, padx=3, sticky="w")
        Tooltip(column_chart_button, "Click to display column and timeline chart.")

        # Display Pie Chart Button with orange color
        pie_chart_button = tk.Button(middle_buttons_frame, text="Display Pie Charts", command=self.display_pie_chart,
                                     bg="#733112",
                                     fg="#FFFFFF")
        pie_chart_button.grid(row=0, column=5, pady=1, padx=3, sticky="w")
        Tooltip(pie_chart_button, "Click to display pie charts.")

        process_loot_logs_button = tk.Button(middle_buttons_frame, text="Process Loot Logs from RM",
                                             command=self.process_loot_logs, bg="#274e13", fg="#FFFFFF")
        process_loot_logs_button.grid(row=0, column=6, pady=1, padx=3, sticky="w")
        Tooltip(process_loot_logs_button, "Click to process loot logs after copying them over from the 'My Raid History' section of the Raid Manager.")

        # Output with dark theme
        self.output_text = tk.Text(root, width=130, height=40, bg="#2E2E2E", fg="#FFFFFF",
                                   wrap="none", font=custom_font)  # No wrap for horizontal scrolling
        self.output_text.grid(row=4, column=0, columnspan=3, pady=5, padx=5)

        # Made by label at the bottom left
        made_by_label = tk.Label(root, text="Slapped together by Sokitas on the 8th of February 2024; a Thursday.",
                                 bg="#2E2E2E", fg="#FFFFFF")
        made_by_label.grid(row=5, column=0, columnspan=3, pady=5, padx=5, sticky="w")

        # Info Bar at the bottom
        self.info_bar = tk.Label(root, text="App status: Ready", bg="#2E2E2E", fg="#FFFFFF")
        self.info_bar.grid(row=6, column=0, columnspan=3, pady=5, padx=5, sticky="w")

        # Initialize CombatAnalyzer
        self.analyzer = CombatAnalyzer()
        self.analyzer.load_config()  # Load personal best hit from the configuration file

        # Personal Best Label
        formatted_personal_best = "{:,}".format(self.analyzer.personal_best_hit)
        self.personal_best_label = ttk.Label(center_frame, text="Personal Best: {}".format(formatted_personal_best))
        self.personal_best_label.grid(row=0, column=4, pady=1, padx=5, sticky="e")
        self.update_personal_best_label()

    def load_config(self):
        try:
            self.config.read('config.ini')
        except configparser.Error as e:
            messagebox.showerror("Configuration Error", f"Error loading configuration: {str(e)}")
    def update_personal_best_label(self):
        formatted_personal_best = "{:,}".format(self.analyzer.personal_best_hit)
        self.personal_best_label.config(text="Personal Best: {}".format(formatted_personal_best))

        # Determine background color based on personal best value
        bg_color = self.get_bg_color(self.analyzer.personal_best_hit)
        self.personal_best_label.config(background=bg_color)

    def get_bg_color(self, value):
        # Define color range based on personal best value
        low_color = "#0000FF"  # Blue for low values
        high_color = "#FF0000"  # Red for high values

        # Normalize value to be between 0 and 1
        normalized_value = min(1, max(0, value / 10000000))

        # Interpolate between low and high colors based on normalized value
        r = int((1 - normalized_value) * int(low_color[1:3], 16) + normalized_value * int(high_color[1:3], 16))
        g = int((1 - normalized_value) * int(low_color[3:5], 16) + normalized_value * int(high_color[3:5], 16))
        b = int((1 - normalized_value) * int(low_color[5:], 16) + normalized_value * int(high_color[5:], 16))

        # Convert RGB to hexadecimal
        hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)

        return hex_color

    def add_character_name(self):
        new_name = self.character_name_combobox.get().strip()
        if new_name and new_name not in self.character_names:
            self.character_names.append(new_name)
            self.character_name_combobox["values"] = tuple(self.character_names)
            self.save_character_names()

    def load_character_names(self):
        try:
            with open("character_names.txt", "r") as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            return []

    def save_character_names(self):
        with open("character_names.txt", "w") as file:
            file.write("\n".join(self.character_names))

    def get_hits_data(self):
        return [(hit['hit_number'], hit['experience_gained'], hit['damage_done']) for hit in self.analyzer.hits_data]

    def parse_combat_log(self):
        combat_log = self.text_input.get("1.0", tk.END)
        player_name = self.character_name_combobox.get()

        # Count all occurrences of "nimbly evaded"
        self.analyzer.total_evaded_hits = combat_log.lower().count("nimbly evaded")

        # Use a regular expression to find the beginning of each hit
        hits = re.finditer(fr'{re.escape(player_name)}.*?(?={re.escape(player_name)}|$)', combat_log, re.DOTALL)

        # Analyze each hit
        for hit_match in hits:
            hit_lines = hit_match.group(0).strip().split('\n')
            self.analyzer.analyze_hit(hit_lines)
            # Check for lines indicating damage taken by the player
            for line in hit_lines:
                self.analyzer.parse_damage_taken(line)

            for line in hit_lines:
                self.analyzer.parse_formation_damage(line)

        self.analyzer.calculate_evasion_chance()

        # Display results
        result_str = self.analyzer.display_results()


        # Add Mountain Goats Song of the Parse
        mountain_goats_song, release_year = random.choice(CombatAnalyzer.MOUNTAIN_GOAT_SONGS)
        result_str += f"\n\nMountain Goats Song of the Parse: \"{mountain_goats_song}\" - Released in {release_year}"

        # Clear previous output
        self.output_text.delete(1.0, tk.END)

        # Update output
        self.output_text.insert(tk.END, result_str)

        # Update info bar
        self.info_bar.config(text="App status: Parsing complete")

        self.analyzer.log_results(result_str)

    def reset_input(self):
        # Clear the text input
        self.text_input.delete(1.0, tk.END)

        # Update info bar
        self.info_bar.config(text="App status: Ready")

    def reset_output(self):
        # Clear the output text
        self.output_text.delete(1.0, tk.END)

        # Reset the CombatAnalyzer instance
        self.analyzer.reset_data()

        # Update info bar
        self.info_bar.config(text="App status: Output cleared and data reset")

    def save_results(self):
        try:
            result_str = self.output_text.get(1.0, tk.END)

            # Remove the last line (Mountain Goats Song of the Parse) from the saved content
            lines = result_str.split('\n')
            lines = lines[:-3]  # Adjust the index based on the format of your output
            result_str = '\n'.join(lines)

            date_str = datetime.now().strftime("%Y.%m.%d")
            file_number = 1
            while True:
                file_name = f"combat_results_{date_str}_{file_number}.txt"
                if not os.path.exists(file_name):
                    break
                file_number += 1
            with open(file_name, "w") as file:
                file.write(result_str)
            messagebox.showinfo("Save Results", f"Results saved to {file_name} successfully.")
        except Exception as e:
            messagebox.showerror("Save Results", f"An error occurred: {str(e)}")

    def display_column_chart(self):

        overall_damage = (self.analyzer.total_damage - sum(
            effect['total_damage'] for effect in self.analyzer.player_effects.values()))
        regular_hit_damage = (self.analyzer.total_damage - sum(
            effect['total_damage'] for effect in self.analyzer.player_effects.values()))
        damage_distribution_percentage = self.analyzer.get_damage_distribution_percentage(self.analyzer.total_damage,
                                                                                          regular_hit_damage)

        plt.figure(figsize=(10, 6), facecolor='#c1c1c1')
        plt.bar(damage_distribution_percentage.keys(), damage_distribution_percentage.values(), color='purple')
        plt.xlabel('Player Effects')
        plt.ylabel('Damage Percentage')  # Updated ylabel to reflect percentage
        plt.title('Damage Distribution (Column Chart)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Display the chart in the application
        self.display_chart(plt)
        self.display_timeline_chart()

    def display_pie_chart(self):

        overall_damage = self.analyzer.total_damage - sum(
            effect['total_damage'] for effect in self.analyzer.player_effects.values())
        regular_hit_damage = (self.analyzer.total_damage - sum(
            effect['total_damage'] for effect in self.analyzer.player_effects.values()))
        damage_distribution_percentage = self.analyzer.get_damage_distribution_percentage(self.analyzer.total_damage,
                                                                                          regular_hit_damage)

        # Define a threshold for combining small slices
        threshold_percentage = 2.0
        small_slices = [label for label, percentage in damage_distribution_percentage.items() if
                        percentage < threshold_percentage]

        # Combine small slices into an "Other" category
        combined_percentage = sum(
            percentage for label, percentage in damage_distribution_percentage.items() if label in small_slices)
        damage_distribution_percentage = {label: percentage for label, percentage in
                                          damage_distribution_percentage.items() if label not in small_slices}
        damage_distribution_percentage['Other'] = combined_percentage

        explode = [0.5 if label in small_slices else 0.3 for label in damage_distribution_percentage.keys()]

        plt.figure(figsize=(12, 8), facecolor='#c1c1c1')

        # First pie chart for general damage distribution
        plt.subplot(1, 2, 1)

        plt.pie(damage_distribution_percentage.values(), labels=damage_distribution_percentage.keys(),
                autopct='%1.1f%%', startangle=140, explode=explode)
        plt.title('Damage Distribution')

        # Second pie chart for crit damage distribution

        plt.subplot(1, 2, 2)

        crit_damage_percentage = self.analyzer.total_crit_damage / max(self.analyzer.total_damage, 1) * 100
        total_damage = self.analyzer.total_damage
        non_crit_damage_percentage = 100 - crit_damage_percentage
        crit_label = f'Crit Damage\n({self.analyzer.format_number(self.analyzer.total_crit_damage)} damage)'
        non_crit_label = f'Non-Crit Damage\n({self.analyzer.format_number(total_damage - self.analyzer.total_crit_damage)} damage)'

        labels = [crit_label, non_crit_label]
        percentages = [crit_damage_percentage, non_crit_damage_percentage]
        plt.pie(percentages, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Crit Damage Distribution')

        plt.tight_layout()
        # Display the chart in the application
        self.display_chart(plt)

    def display_timeline_chart(self):
        hits_data = self.get_hits_data()  # You need to implement get_hits_data method
        if not hits_data:
            messagebox.showwarning("Timeline Chart", "No hits data available.")
            return

        # Extract data for timeline chart
        hits, experience, damage = zip(*hits_data)

        # Create a new window for displaying the chart
        timeline_chart_window = tk.Toplevel(self.root)
        timeline_chart_window.title("Timeline Chart")

        # Plot the timeline chart
        plt.figure(figsize=(10, 6), facecolor='#c1c1c1')
        plt.plot(hits, experience, label="Experience", marker='o')
        plt.plot(hits, damage, label="Damage", marker='o')
        plt.xlabel('Hits')
        plt.ylabel('Value')
        plt.title('Timeline Chart')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        # Save chart button for the timeline chart
        save_button = tk.Button(timeline_chart_window, text="Save Chart", command=lambda: self.save_chart(plt),
                                bg="#4CAF50", fg="#FFFFFF")
        save_button.pack(side=tk.BOTTOM, pady=10)

        # Embed the matplotlib chart in the Tkinter window
        canvas = FigureCanvasTkAgg(plt.gcf(), master=timeline_chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def display_chart(self, plt):
        # Create a new window for displaying the chart
        chart_window = tk.Toplevel(self.root)
        chart_window.title("Damage Distribution Chart")

        # Embed the matplotlib chart in the Tkinter window
        canvas = FigureCanvasTkAgg(plt.gcf(), master=chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Navigation toolbar for the chart
        toolbar_frame = tk.Frame(chart_window)
        toolbar_frame.pack(side=tk.TOP, fill=tk.BOTH)

        # Save chart button
        save_button = tk.Button(toolbar_frame, text="Save Chart", command=lambda: self.save_chart(plt), bg="#4CAF50",
                                fg="#FFFFFF")
        save_button.pack(side=tk.LEFT, padx=5)

    def save_chart(self, plt):
        try:
            file_types = [('PNG files', '*.png'), ('All files', '*.*')]
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=file_types)
            if file_path:
                plt.savefig(file_path, format='png')
                messagebox.showinfo("Save Chart", f"Chart saved to {file_path} successfully.")
        except Exception as e:
            messagebox.showerror("Save Chart", f"An error occurred: {str(e)}")

    def process_loot_logs(self):
        loot_logs = self.text_input.get("1.0", tk.END)
        loot_items = {}
        raid_hits = {}
        raid_stat_points = {}

        for log_line in loot_logs.splitlines():
            # Extracting raid name and difficulty
            raid_match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+([\w\s]+ \/ [A-Za-z]+)\s+(\d+)', log_line)

            if raid_match:
                timestamp, raid_info, _ = raid_match.groups()
                raid_hits[raid_info] = raid_hits.get(raid_info, 0) + 1

                # Extracting stat points gained
                stat_points_match = re.search(r'Stat Points: (\d+)', log_line)
                if stat_points_match:
                    stat_points = int(stat_points_match.group(1))
                    raid_stat_points[raid_info] = raid_stat_points.get(raid_info, []) + [stat_points]



                # Extracting items dropped
                items_dropped_match = re.findall(r'(\w[ \w\']*): (\d+)', log_line)
                if items_dropped_match:
                    for item, quantity in items_dropped_match:
                        loot_items[item.strip()] = loot_items.get(item.strip(), 0) + int(quantity)

        # Calculate average stat points for each raid
        average_stat_points = {raid: sum(points) / len(points) for raid, points in raid_stat_points.items()}

        # Sort raid hits by the number of hits in descending order
        sorted_raid_hits = sorted(raid_hits.items(), key=lambda x: x[1], reverse=True)

        # Sort average stat points by the value in descending order
        sorted_avg_stat_points = sorted(average_stat_points.items(), key=lambda x: x[1], reverse=True)

        # Sort loot items by the number of drops in descending order
        sorted_loot_items = sorted(loot_items.items(), key=lambda x: x[1], reverse=True)

        result_str = "Raids hit Tally (Sorted by number of Raids):\n"
        avg_stat_points_str = "Average Stat Points (Sorted by value in descending order):\n"
        items_per_line = 5  # Number of items per line for better readability

        for raid_info, hit_count in sorted_raid_hits:
            result_str += f"{raid_info}: {hit_count}\n"

        for raid_info, avg_stat in sorted_avg_stat_points:
            # Add average stat points information
            avg_stat_points_str += f"{raid_info}: {avg_stat:.2f}\n"

        result_str += "\n\nLoot Tally (Sorted by Total Drops):\n"

        for idx, (item, count) in enumerate(sorted_loot_items, start=1):
            result_str += f"{item}: {count}\t"

            # Add newline after a certain number of items
            if idx % items_per_line == 0:
                result_str += "\n"

        # Clear previous output
        self.output_text.delete(1.0, tk.END)

        # Update output
        self.output_text.insert(tk.END, result_str + "\n" + avg_stat_points_str)

        # Update info bar
        self.info_bar.config(text="App status: Loot Logs and Raids hit processed")
class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text, justify='left', background="#000000", relief='solid', borderwidth=1)
        label.pack(ipadx=1)

    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

if __name__ == "__main__":
    root = tk.Tk()
    app = CombatLogParserApp(root)
    root.mainloop()
