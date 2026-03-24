# Python ATM Simulation

> Completed as part of **Python ATM Simulation Essentials Mini Project** — LetsUpgrade Bootcamp Program

A console-based ATM simulation in Python. User enters a PIN to login (max 3 attempts), then gets a menu with Check Balance, Deposit, Withdraw, and Exit options. Validates inputs, prevents withdrawal above balance, and loops the menu until Exit is chosen. Demonstrates core Python programming concepts.

---

## Live Demo

🌐 **[View Live: https://01-atm.vercel.app/](https://01-atm.vercel.app/)**

**Note:** This project now has two versions:
- CLI version (`atm.py`) — original bootcamp assignment implementation
- Website-style version (`index.html`) — self-initiated enhancement by me for portfolio improvement (not part of LetsUpgrade required curriculum)

---

## Vercel Deployment

This project's website-style version is deployed live on Vercel!

### Deployment Details

| Field | Value |
|---|---|
| GitHub repository | `https://github.com/AshishCherian15/python-mini-projects` |
| Deployment model | One Vercel project per mini-project folder |
| Root directory | `ATM/` (web version folder) |
| Live URL | **[https://01-atm.vercel.app/](https://01-atm.vercel.app/)** |
| Status | ✅ Live & Active |

### Update Log

- README updated to include a production-ready deployment path.
- Website-style version created in `index.html`.
- Website-style enhancement clearly marked as self-learning outside bootcamp scope.
- Existing CLI implementation preserved.

---

## Preview & Screenshots

### � Website Version (Live Demo)

![ATM Website Interface](ATM.jpg)

*Above: Interactive ATM machine interface on Vercel — [Try it live](https://01-atm.vercel.app/)*

---

### �🖥️ CLI Version Preview

```
===================================
      Welcome to Simple ATM
===================================

Enter your PIN: 1234

✅ Login successful! Welcome.

-----------------------------------
         ATM Main Menu
-----------------------------------
  1. Check Balance
  2. Deposit Money
  3. Withdraw Money
  4. Exit
-----------------------------------
Enter your choice (1-4): 1

💰 Your current balance is: ₹5000.00

-----------------------------------
         ATM Main Menu
-----------------------------------
  1. Check Balance
  2. Deposit Money
  3. Withdraw Money
  4. Exit
-----------------------------------
Enter your choice (1-4): 2

Enter amount to deposit: ₹1000
✅ ₹1000.00 deposited successfully.
   Updated Balance: ₹6000.00

-----------------------------------
         ATM Main Menu
-----------------------------------
  1. Check Balance
  2. Deposit Money
  3. Withdraw Money
  4. Exit
-----------------------------------
Enter your choice (1-4): 3

Enter amount to withdraw: ₹500
✅ ₹500.00 withdrawn successfully.
   Updated Balance: ₹5500.00

-----------------------------------
         ATM Main Menu
-----------------------------------
  1. Check Balance
  2. Deposit Money
  3. Withdraw Money
  4. Exit
-----------------------------------
Enter your choice (1-4): 4

👋 Thank you for using Simple ATM. Goodbye!
```

### 🌐 Website Version Preview

**Realistic ATM Machine Interface**

```
┌─────────────────────────────────────────────────────────┐
│                  ASH BANK ATM                           │
│                  [● ONLINE]                            │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │                                                  │  │
│  │  CARD DETECTED                                  │  │
│  │  Enter PIN: ••••                                │  │
│  │  Attempts remaining: 3                          │  │
│  │                                                 │  │
│  │  [SYSTEM] Welcome! Choose a transaction type.  │  │
│  │  [SYSTEM] 1. Check Balance                      │  │
│  │  [SYSTEM] 2. Deposit Money                      │  │
│  │  [SYSTEM] 3. Withdraw Money                     │  │
│  │  [SYSTEM] Exit                                  │  │
│  │                                                 │  │
│  └──────────────────────────────────────────────────┘  │
│                                                         │
│  Hardware Panel:                                        │
│  [ 1 ][ 2 ][ 3 ][ 4 ]   ← Numeric Keypad             │
│  [ 5 ][ 6 ][ 7 ][ 8 ]                                 │
│  [ 9 ][ 0 ][ C ][ OK]                                 │
│                                                         │
│  [💳 CARD SLOT] [💵 CASH DISPENSER] [🧾 RECEIPT]    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Features:**
- Metallic frame with professional ATM styling
- Interactive screen panel showing transaction details
- Numeric keypad for PIN entry
- System log output for all transactions
- Hardware slot representations (card slot, cash dispenser, receipt printer)
- Responsive design for mobile and desktop

| Aspect | Details |
|---|---|
| **Interface** | Realistic physical ATM machine aesthetic |
| **Interactions** | Click buttons to perform transactions, system messages logged |
| **Responsiveness** | Adapts to screen size while maintaining ATM appearance |
| **Data Persistence** | Balance updates during session (demo mode) |

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
