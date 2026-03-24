# Python ATM Simulation

> Completed as part of **Python ATM Simulation Essentials Mini Project** — LetsUpgrade Bootcamp Program

A console-based ATM simulation in Python. User enters a PIN to login (max 3 attempts), then gets a menu with Check Balance, Deposit, Withdraw, and Exit options. Validates inputs, prevents withdrawal above balance, and loops the menu until Exit is chosen. Demonstrates core Python programming concepts.

---

## Live Demo

[Add your live demo link here — deploy on Vercel or GitHub Pages]

**Note:** This project now has two versions:
- CLI version (`atm.py`) — original bootcamp assignment implementation
- Website-style version (`index.html`) — self-initiated enhancement by me for portfolio improvement (not part of LetsUpgrade required curriculum)

---

## Vercel Deployment Note (Way 1)

This project is currently a **CLI Python app**. Vercel cannot run interactive terminal sessions directly.

To make this project live on Vercel (Way 1):
- Build a frontend version (for example with React/Next.js) that replicates the same ATM flow.
- Move logic from terminal `input()`/`print()` interaction into UI forms, buttons, and state.
- Keep this Python script as reference for original assignment logic.

### Planned Vercel Setup

| Field | Value |
|---|---|
| GitHub repository | `https://github.com/AshishCherian15/react-mini-projcets` |
| Deployment model | One Vercel project per mini-project folder |
| Root directory | `ATM/` (web version folder) |
| Live URL | Not specified |
| Status | Website-style version completed, ready to deploy |

### Update Log

- README updated to include a production-ready deployment path.
- Website-style version created in `index.html`.
- Website-style enhancement clearly marked as self-learning outside bootcamp scope.
- Existing CLI implementation preserved.

---

## Screenshots

| View 1 | View 2 |
|---|---|
| ![Screenshot 1](screenshots/1.png) | ![Screenshot 2](screenshots/2.png) |

---

## Tech Used

- Python 3

---

## How to Run

```bash
python atm.py
```

### Website-style Run

- Open `index.html` in browser
- Or deploy `ATM/` on Vercel as independent project root

---

## Key Concepts

| Concept | Purpose |
|---|---|
| `variables` | balance=5000.0, CORRECT_PIN='1234', attempts=0 store program data |
| `while loop` | Main menu loops until user chooses Exit; login loops up to 3 times |
| `if/elif/else` | Checks menu choice (1/2/3/4), validates PIN, validates amounts |
| `input()` | Reads user's keyboard input as a string |
| `float()` | Converts string input to decimal number for money calculations |
| `try/except ValueError` | Catches error when user types letters instead of a number |
| `break` | Exits the while loop immediately when correct PIN or Exit chosen |
| `exit()` | Stops entire program if user fails PIN 3 times |
| `f-strings` | f'Balance: Rs.{balance:.2f}' formats number with 2 decimal places |
| `ALL_CAPS convention` | CORRECT_PIN in caps indicates it is a constant - Python convention |

---

## Core Code

```python
CORRECT_PIN = '1234'
balance = 5000.0

# Login with attempt limit
while attempts < 3:
    pin = input('Enter PIN: ')
    if pin == CORRECT_PIN:
        logged_in = True; break
    else:
        attempts += 1

# Main menu loop
while True:
    choice = input('Enter choice (1-4): ')
    if choice == '2':  # Deposit
        try:
            amount = float(input('Amount: '))
            if amount > 0: balance += amount
        except ValueError:
            print('Invalid input')
    elif choice == '4':
        break  # Exit
```

---

## Certificate

| Field | Details |
|---|---|
| Bootcamp | Python ATM Simulation Essentials Mini Project |
| Completed by | Ashish Cherian |
| Date | 10 February 2026 |
| Certificate No | LUEATMFEB126273 |
| Verify | [www.letsupgrade.in/verify](https://www.letsupgrade.in/verify) |
| In collaboration with | NSDC, ITM Edutech, GDG MAD |

---

## Project Structure

```
01-atm-simulation/
├── atm.py
├── README.md
└── certificate/
    └── LUEATMFEB126273.pdf
```

---
*Built during LetsUpgrade Bootcamp — 10 February 2026*
