Sokitas' Void of the Dragons Log-o-rama 2.0

Overview

This Python script is designed to analyze combat logs from the game "Void of the Dragons." It provides insights into various statistics, including overall damage, crit rate, damage taken, and player effects.

Features

Combat Log Parsing: Parse combat logs to extract information about hits, damage, experience gained, and more.
Statistical Analysis: Calculate various statistics such as overall damage, average damage per hit, crit rate, and share of crit damage.
Player Effects: Track and analyze the impact of individual player effects, including damage dealt, procs, and total damage.
DotV Raid Manager Raid History Analysis: Know how much of each item you have looted. Easily see how many Stat Points you gained from a given group of looted raids. 

Getting Started

If you are on Windows, grab the newest binary from the RELEASES section.


Prerequisites

Python 3.x

Tkinter (usually included in Python installations)

Matplotlib

Installation

Clone the repository:

bash
Copy code
git clone https://github.com/your-username/CombatLogAnalyzer.git
cd CombatLogAnalyzer
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the script:

bash
Copy code
python combat_log_analyzer.py


Follow the on-screen instructions to input your combat log. The script will display parsed results, charts, and save them to a file.

Screenshots
![NVIDIA_Share_6LlqcZPS9t](https://github.com/Sokitas/Void-of-the-Dragons-Log-o-rama/assets/159527539/399ad38d-4a78-45be-8232-58753626ca3a)

![image](https://github.com/Sokitas/Void-of-the-Dragons-Log-o-rama/assets/159527539/0967fc3f-971e-4cca-95be-642fba13979a)


NOTICE

If you encounter any false positives from Windows Defender, claiming the file contains a Trojan, be aware that this is a common false positive associated with executables built with some versions of pyinstaller. 
It seems the way the application reads and writes the config file in its directory is seen as snooping around. I sent the 1.9 version to Microsoft for investigation and possible whitelisting. 
![image](https://github.com/Sokitas/Void-of-the-Dragons-Log-o-rama/assets/159527539/249d86d7-7cd8-4db8-a78d-407eebbc036c)






Contributing

Contributions are welcome! Please contact me to request a collaboration.

License

This project is licensed under a modified MIT license that explicitly restricts commercial use - see the LICENSE file for details.

Acknowledgments

Mountain Goat Song titles are all rights reserved to the band the Mountain Goats / MERGE Records and their respective rights holders 



Tips

You can grab me a coffee at Ko-fi. It's completely optional, though. I'd honestly prefer you use your money where it matters most for you.
 https://Ko-fi.com/sokitas
