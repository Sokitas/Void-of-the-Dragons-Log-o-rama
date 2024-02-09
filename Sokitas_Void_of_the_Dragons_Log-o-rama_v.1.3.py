import re
import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime
import os
import random
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
        ("1 Samuel 15:23", 2009),
        ("Heel Turn 2", 2015),
        ("Estate Sale Sign", 2011),
        ("In the Hidden Places", 2006),
        ("White Cedar", 2012),
        ("The Recognition Scene", 1995),
        ("Jaipur", 1991),
        ("Hast Thou Considered the Tetrapod", 2005),
        ("How to Embrace a Swamp Creature", 2017),
        ("The Ballad of Bull Ramos", 2015),
        ("Younger", 2017),
        ("In Memory of Satan", 2012),
        ("Hebrews 11:40", 2009),
        ("Never Quite Free", 2011),
        ("California Song", 1995),
        ("Pigs That Ran Straightaway into the Water, Triumph Of", 2004),
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
        ("1 Samuel 15:23", 2009),
        ("Heel Turn 2", 2015),
        ("Estate Sale Sign", 2011),
        ("In the Hidden Places", 2006),
        ("White Cedar", 2012),
        ("The Recognition Scene", 1995),
        ("Jaipur", 1991),
        ("Hast Thou Considered the Tetrapod", 2005),
        ("How to Embrace a Swamp Creature", 2017),
        ("The Ballad of Bull Ramos", 2015),
        ("Younger", 2017),
        ("In Memory of Satan", 2012),
        ("Hebrews 11:40", 2009),
        ("Never Quite Free", 2011),
        ("California Song", 1995),
        ("Pigs That Ran Straightaway into the Water, Triumph Of", 2004),
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
        ("1 Samuel 15:23", 2009),
        ("Heel Turn 2", 2015),
        ("Estate Sale Sign", 2011),
        ("In the Hidden Places", 2006),
        ("White Cedar", 2012),
        ("The Recognition Scene", 1995),
        ("Jaipur", 1991),
        ("Hast Thou Considered the Tetrapod", 2005),
        ("How to Embrace a Swamp Creature", 2017),
        ("The Ballad of Bull Ramos", 2015),
        ("Younger", 2017),
        ("In Memory of Satan", 2012),
        ("Hebrews 11:40", 2009),
        ("Never Quite Free", 2011),
        ("California Song", 1995),
        ("Pigs That Ran Straightaway into the Water, Triumph Of", 2004),
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

        self.total_hits += 1

    def parse_damage_experience(self, line):
        match = re.search(r'(\d+) damage and earned (\d+) experience', line)
        if match:
            return int(match.group(1)), int(match.group(2))
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

    def display_results(self):
        total_player_effects_damage = sum(effect['total_damage'] for effect in self.player_effects.values())
        overall_damage = self.total_damage + total_player_effects_damage

        result_str = (
            f"Total Hits: {self.format_number(self.total_hits)}\n"
            f"Overall Damage: {self.format_number(overall_damage)}\n"
            f"Average Damage Per Hit: {self.format_number(overall_damage / max(self.total_hits, 1))}\n"
            f"Overall Experience Gained: {self.format_number(self.total_experience)}\n"
            f"Experience Gained Per Hit: {self.format_number(self.total_experience / max(self.total_hits, 1))}\n"
            f"Crit Rate: {self.format_number(self.total_crits / max(self.total_hits, 1) * 100)}%\n"
            f"Share of Crit Damage: {self.format_number(self.total_crit_damage / max(overall_damage, 1) * 100)}%\n"
            f"Total Damage Taken: {self.format_number(self.total_damage_taken)}\n"
            f"Average Damage Taken Per Hit: {self.format_number(self.average_damage_taken)}\n\n"
            "Player Effects:\n"
        )

        for i, (effect, stats) in enumerate(self.player_effects.items()):
            damage_percentage = stats['damage'] / max(overall_damage, 1) * 100
            average_damage_per_hit = stats['damage'] / max(self.total_hits, 1)
            average_damage_per_proc = stats['total_damage'] / max(stats['procs'], 1)
            result_str += (
                f"{effect}: {self.format_number(stats['damage'])} damage "
                f"({self.format_number(damage_percentage)}% of total damage, "
                f"{self.format_number(average_damage_per_hit)} per hit, "
                f"{stats['procs']} procs, {self.format_number(average_damage_per_proc)} per proc)"
            )

            # Add divider lines between effects, except for the last one
            if i < len(self.player_effects) - 1:
                result_str += "\n" + "=" * 50 + "\n"

        return result_str

    def get_damage_distribution(self):
        damage_distribution = {
            'Regular Hit Damage': self.total_damage - sum(effect['total_damage'] for effect in self.player_effects.values()),
            **{effect: stats['damage'] for effect, stats in self.player_effects.items()}
        }
        return damage_distribution


class CombatLogParserApp:
    def __init__(self, root):
        self.root = root
        root.title("Sokitas' Void of the Dragons Log-o-rama 1.3")

        # Configure dark theme
        root.tk_setPalette(background="#2E2E2E", foreground="#FFFFFF", activeBackground="#4E4E4E", activeForeground="#FFFFFF")

        # Character Name Input
        self.character_name_label = tk.Label(root, text="Character Name:", bg="#2E2E2E", fg="#FFFFFF")
        self.character_name_label.pack(pady=5)
        self.character_name_entry = tk.Entry(root, bg="#2E2E2E", fg="#FFFFFF")
        self.character_name_entry.pack(pady=5)

        # Text Input
        self.text_input = scrolledtext.ScrolledText(root, width=120, height=10, bg="#2E2E2E", fg="#FFFFFF")
        self.text_input.pack(pady=5)

        # Parse Button with green color
        parse_button = tk.Button(root, text="Parse Combat Log", command=self.parse_combat_log, bg="#4CAF50", fg="#FFFFFF")
        parse_button.pack(pady=5)

        # Reset Input Button with red color
        reset_input_button = tk.Button(root, text="Reset Input", command=self.reset_input, bg="#FF0000", fg="#FFFFFF")
        reset_input_button.pack(pady=5)

        # Reset Output Button with yellow color
        reset_output_button = tk.Button(root, text="Reset Output", command=self.reset_output, bg="#FFFF00", fg="#000000")
        reset_output_button.pack(pady=5)

        # Save Results Button with blue color
        save_button = tk.Button(root, text="Save Results", command=self.save_results, bg="#0000FF", fg="#FFFFFF")
        save_button.pack(pady=5)

        # Display Column Chart Button with purple color
        column_chart_button = tk.Button(root, text="Display Column Chart", command=self.display_column_chart, bg="#800080", fg="#FFFFFF")
        column_chart_button.pack(pady=5)

        # Display Pie Chart Button with orange color
        pie_chart_button = tk.Button(root, text="Display Pie Chart", command=self.display_pie_chart, bg="#FFA500", fg="#FFFFFF")
        pie_chart_button.pack(pady=5)

        # Output with dark theme
        self.output_text = tk.Text(root, width=110, height=25, bg="#2E2E2E", fg="#FFFFFF", wrap="none")  # No wrap for horizontal scrolling
        self.output_text.pack(pady=5)

        # Made by label at the bottom left
        made_by_label = tk.Label(root, text="Slapped together by Sokitas on the 8th of February 2024.",
                                 bg="#2E2E2E", fg="#FFFFFF")
        made_by_label.pack(side="bottom", anchor="w", padx=10, pady=5)

        # Info Bar at the bottom
        self.info_bar = tk.Label(root, text="App status: Ready", bg="#2E2E2E", fg="#FFFFFF")
        self.info_bar.pack(side="bottom", fill="both")

        # Initialize CombatAnalyzer
        self.analyzer = CombatAnalyzer()

    def parse_combat_log(self):
        combat_log = self.text_input.get("1.0", tk.END)
        player_name = self.character_name_entry.get()

        # Use a regular expression to find the beginning of each hit
        hits = re.finditer(fr'{re.escape(player_name)}.*?(?={re.escape(player_name)}|$)', combat_log, re.DOTALL)

        # Analyze each hit
        for hit_match in hits:
            hit_lines = hit_match.group(0).strip().split('\n')
            self.analyzer.analyze_hit(hit_lines)
            # Check for lines indicating damage taken by the player
            for line in hit_lines:
                self.analyzer.parse_damage_taken(line)

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

    def reset_input(self):
        # Clear the text input
        self.text_input.delete(1.0, tk.END)

        # Update info bar
        self.info_bar.config(text="App status: Ready")

    def reset_output(self):
        # Clear the output text
        self.output_text.delete(1.0, tk.END)

        # Update info bar
        self.info_bar.config(text="App status: Output cleared")

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
        damage_distribution = self.analyzer.get_damage_distribution()
        plt.figure(figsize=(10, 6))
        plt.bar(damage_distribution.keys(), damage_distribution.values(), color='purple')
        plt.xlabel('Player Effects')
        plt.ylabel('Damage')
        plt.title('Damage Distribution (Column Chart)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Display the chart in the application
        self.display_chart(plt)

    def display_pie_chart(self):
        damage_distribution = self.analyzer.get_damage_distribution()
        plt.figure(figsize=(8, 8))
        plt.pie(damage_distribution.values(), labels=damage_distribution.keys(), autopct='%1.1f%%', startangle=140)
        plt.title('Damage Distribution (Pie Chart)')
        plt.tight_layout()

        # Display the chart in the application
        self.display_chart(plt)

    def display_chart(self, plt):
        # Create a new window for displaying the chart
        chart_window = tk.Toplevel(self.root)
        chart_window.title("Damage Distribution Chart")

        # Embed the matplotlib chart in the Tkinter window
        canvas = FigureCanvasTkAgg(plt.gcf(), master=chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Navigation toolbar for the chart
        toolbar = tk.NavigationToolbar2Tk(canvas, chart_window)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = CombatLogParserApp(root)
    root.mainloop()
