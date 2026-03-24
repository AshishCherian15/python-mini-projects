# E-commerce Review Insights

> Completed as part of **E-commerce Review Insights Essentials: End-to-End Python Mini Project** — LetsUpgrade Bootcamp Program

A Python program that analyses e-commerce product reviews using keyword matching. Classifies each review as positive, negative, or neutral. Prints counts, percentages, categorized reviews, and 4 business insights. Includes bonus user input review classification. Demonstrates Python list operations, string methods, and any() function.

---

## Live Demo

[Add your live demo link here — deploy on Vercel or GitHub Pages]

**Note:** This project now has two versions:
- CLI version (`review_insights.py`) — original bootcamp assignment implementation
- Website-style version (`index.html`) — self-initiated enhancement by me for portfolio improvement (not part of LetsUpgrade required curriculum)

---

## Vercel Deployment Note (Way 1)

This project is currently a **CLI Python app**. Vercel cannot run interactive terminal sessions directly.

To make this project live on Vercel (Way 1):
- Build a frontend version (for example with React/Next.js) that replicates the review analysis flow.
- Move logic from terminal `input()`/`print()` interaction into browser input fields and result cards.
- Keep this Python script as reference for original assignment logic.

### Planned Vercel Setup

| Field | Value |
|---|---|
| GitHub repository | `https://github.com/AshishCherian15/react-mini-projcets` |
| Deployment model | One Vercel project per mini-project folder |
| Root directory | `Review/` (web version folder) |
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
python review_insights.py
```

### Website-style Run

- Open `index.html` in browser
- Or deploy `Review/` on Vercel as independent project root

---

## Key Concepts

| Concept | Purpose |
|---|---|
| `list` | reviews=[] stores all product review strings |
| `for loop` | Loops through every review to classify it |
| `str.lower()` | Converts review to lowercase so 'Great' and 'great' both match |
| `any()` | any(word in review for word in keywords) checks if any keyword found |
| `in operator` | word in review_lower checks if keyword substring exists in review string |
| `list.append()` | Adds review to positive_reviews or negative_reviews list |
| `len()` | Counts total, positive, and negative reviews |
| `round()` | Calculates clean percentage values |
| `enumerate()` | Loops with index for numbered display: for i,review in enumerate(reviews,1) |
| `f-strings` | Formats output: f'Positive: {count} ({percent}%)'  |

---

## Core Code

```python
reviews = ['Great product, very useful', 'Delivery was late', ...]
positive_keywords = ['good','great','excellent','useful','fast']
negative_keywords = ['not','bad','late','stopped','worst']

for review in reviews:
    review_lower = review.lower()  # bonus: case-insensitive
    found_pos = any(word in review_lower for word in positive_keywords)
    found_neg = any(word in review_lower for word in negative_keywords)
    if found_pos and not found_neg:
        positive_reviews.append(review)
    elif found_neg:
        negative_reviews.append(review)
    else:
        neutral_reviews.append(review)

pos_percent = round((len(positive_reviews)/len(reviews))*100)
```

---

## Certificate

| Field | Details |
|---|---|
| Bootcamp | E-commerce Review Insights Essentials: End-to-End Python Mini Project |
| Completed by | Ashish Cherian |
| Date | 22 January 2026 |
| Certificate No | LUEECRJAN12675 |
| Verify | [www.letsupgrade.in/verify](https://www.letsupgrade.in/verify) |
| In collaboration with | NSDC, ITM Edutech, GDG MAD |

---

## Project Structure

```
02-review-insights/
├── review_insights.py
├── README.md
└── certificate/
    └── LUEECRJAN12675.pdf
```

---
*Built during LetsUpgrade Bootcamp — 22 January 2026*
