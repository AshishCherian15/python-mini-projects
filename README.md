# 🎓 LetsUpgrade Python Mini Projects Portfolio

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1100&color=38BDF8&center=true&vCenter=true&width=980&lines=Python+Mini+Projects+Portfolio;CLI+Assignments+%2B+Website-Style+Enhancements;Recruiter-Ready+Repository+with+Vercel+Deployment+Plan" alt="Typing SVG" />
</p>

![Version](https://img.shields.io/badge/version-1.0.0-3498DB?style=flat-square)
![Status](https://img.shields.io/badge/status-active%20development-27AE60?style=flat-square)
![Tech](https://img.shields.io/badge/tech-Python%20%7C%20HTML%20%7C%20CSS-blue?style=flat-square)
![Deployment](https://img.shields.io/badge/deployment-Vercel-black?style=flat-square)
![Program](https://img.shields.io/badge/program-LetsUpgrade-purple?style=flat-square)

## 📋 Project Overview

This repository contains two Python mini-projects completed from LetsUpgrade workshop assignments.

Each project now includes:
- ✅ Original **CLI assignment version** (as submitted logic)
- ✅ **Website-style enhancement** (self-initiated portfolio improvement, outside bootcamp requirement)

## ✨ Learning Outcomes

- Python control flow with `if/elif/else`, loops, and input validation
- Error handling with `try/except` and robust user interaction
- Basic sentiment analysis using keyword matching and list operations
- Converting CLI workflows into browser-based UI experiences
- Structuring one repository for multiple independent Vercel deployments

## 🚀 Featured Projects

### 🏧 Project 1: Python ATM Simulation

**Bootcamp Assignment:** Build a Simple ATM Simulation Using Python

**Description:**
PIN-based login (3 attempts), check balance, deposit, withdraw, and exit flow with amount validation and insufficient-funds protection.

**Key Concepts:**

| Concept | Use in Project |
|---|---|
| Variables & constants | Store PIN, balance, attempts |
| `while` loop | Login attempts + repeating menu |
| `if/elif/else` | Choice handling and validation |
| `try/except` | Prevent crash on invalid numeric input |

**Tech Stack:**
- Python 3 (CLI)
- HTML/CSS/JavaScript (website-style UI enhancement)

![ATM Website Interface](ATM/ATM.jpg)

**Live Link:** [🔗 https://01-atm.vercel.app/](https://01-atm.vercel.app/)

[📖 View ATM Project Details](ATM/14_Python_ATM_Simulation_README.md)

### 🛍️ Project 2: E-commerce Review Insights

**Bootcamp Assignment:** E-commerce Review Insights Essentials: End-to-End Python Mini Project

**Description:**
Analyzes product reviews, classifies positive/negative/neutral sentiment, computes percentages, and displays practical business insights.

**Key Concepts:**

| Concept | Use in Project |
|---|---|
| Python lists | Store reviews and categories |
| `any()` + keyword matching | Sentiment classification |
| `lower()` normalization | Case-insensitive matching |
| Insight generation logic | Sentiment summary + recommendations |

**Tech Stack:**
- Python 3 (CLI)
- HTML/CSS/JavaScript (website-style UI enhancement)

![Review Analytics Dashboard](Review/REVIEW.jpg)

**Live Link:** [🔗 https://02-review.vercel.app/](https://02-review.vercel.app/)

[📖 View Review Project Details](Review/15_Ecommerce_Review_Insights_README.md)

Both projects are now live on Vercel! Each deploys independently from the same repository using project-specific root directories.

| Project | Vercel Root Directory | Live URL | Status |
|---|---|---|---|
| ATM Website-style | `ATM/` | **[https://01-atm.vercel.app/](https://01-atm.vercel.app/)** | ✅ Live |
| Review Insights Website-style | `Review/` | **[https://02-review.vercel.app/](https://02-review.vercel.app/)** | ✅ Live |

## 🛠️ Local Development

### Prerequisites
- Python 3.10+
- VS Code (recommended)
- PowerShell terminal (Windows)

### Setup

```powershell
cd C:\Users\ASHISH\Downloads\python-mini-projects
.\.venv\Scripts\Activate.ps1
```

### Run CLI Versions

```powershell
python ATM\atm.py
python Review\review_insights.py
```

### Run Website-style Versions

Open directly in browser:
- `ATM/index.html`
- `Review/index.html`

## 📁 Folder Structure

```text
python-mini-projects/
│
├── ATM/
│   ├── atm.py
│   ├── index.html
│   └── 14_Python_ATM_Simulation_README.md
│
├── Review/
│   ├── review_insights.py
│   ├── index.html
│   └── 15_Ecommerce_Review_Insights_README.md
│
├── LU.txt
└── README.md
```

## 🏆 Bootcamp Context

**Program:** LetsUpgrade Python Workshop Track  
**Focus:** Python fundamentals through assignment-driven mini-projects  
**Scope in this repo:** ATM Simulation + E-commerce Review Insights

## ✅ LetsUpgrade Certificate Verification

**Certificate Holder:** Ashish Cherian  
**Organizer:** LetsUpgrade  
**Verification Link:** https://www.letsupgrade.in/verify

### Verified Workshop Mapping

| Workshop / Project | Completion Date | Issue Date | Certificate / Credential ID | Collaborators | Verification Status |
|---|---|---|---|---|---|
| Python ATM Simulation Essentials Mini Project | 10 February 2026 | Not specified | LUEATMFEB126273 | NSDC, ITM Edutech, GDG MAD | ✅ Completed |
| E-commerce Review Insights Essentials: End-to-End Python Mini Project | 22 January 2026 | Not specified | LUEECRJAN12675 | NSDC, ITM Edutech, GDG MAD | ✅ Completed |

> Note: Workshop assignment descriptions were cross-checked from `LU.txt`. Any unavailable field is marked as **Not specified**.

## 🚀 Deployment Plan (Vercel)

1. Import this GitHub repository in Vercel.
2. Create two separate Vercel projects from the same repo.
3. Set root directory to `ATM/` for ATM web UI and `Review/` for Review web UI.
4. Deploy both and collect generated URLs.
5. Replace “Not specified” live links in this README.

## ✉️ Connect

- GitHub: [AshishCherian15](https://github.com/AshishCherian15)
- Repository: `python-mini-projects`

---

Last Updated: March 2026 | Status: Documentation Standardized ✅
