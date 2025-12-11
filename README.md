<h1><b> CustomTkinter Calculator </b></h1>

A modern, dark-themed calculator application built using Python and CustomTkinter (CTk).
This project includes basic arithmetic operations as well as additional scientific functions such as square root, log, percentage, and power.


---

🚀<b> Features</b>

✔ Modern dark UI using CustomTkinter<br>
✔ Clean layout styled like a mobile calculator<br>
✔ Supports:<br>
    Addition, subtraction, multiplication, division<br>
    Percentage<br>
    Power ( ^ )<br>
    Square root ( √ )<br>
    Log base 10 (Log)<br>
✔ Error handling (Division by zero, invalid input, etc.)<br>
✔ Responsive button grid layout



---

📸 <b>UI Preview</b>

<img width="282" height="516" alt="Calculator" src="https://github.com/user-attachments/assets/da409cc8-82c0-409c-941a-d4b29d927e4a" />


---

📂<b> Project Structure</b>

MiniProject.py   # Main application file (GUI + Logic)


---

🛠 <b>Requirements</b>

Install the required modules:

pip install customtkinter

Python's built-in math module is used for advanced calculations.


---

▶<b> How to Run</b>

1. Clone the repository:



git clone https://github.com/your-username/your-repo-name.git

2. Open the folder:



cd your-repo-name

3. Run the program:



python MiniProject.py


---

🔧<b><h3> Code Overview</b></h3>

CustomTkinter UI

<h3>The app uses:</h3>

CTkFrame for layout

CTkButton for buttons

StringVar for input/output

Grid system for auto-resizing


<h3>Calculation Logic</h3>

User input is captured in input_var.
Pressing "=" evaluates math expressions using Python’s eval() after formatting (^ → ** , % → /100).
Additional buttons use math.sqrt and math.log10.


---

🧑‍💻<b> Author</b><br>
H Hapukotuwa<br>
himahapukotuwa8219@gmail.com



---

📜 <b>License</b>

This project is licensed under the MIT License.<br>
Feel free to use, modify, and distribute.
