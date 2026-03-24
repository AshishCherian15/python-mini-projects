# ============================================================
#   E-commerce Review Insights — Python Mini Project
#   Made by: CSE Final Year Student
# ============================================================

# ── Step 1 & 2: Review Data — stored in a list ──
reviews = [
    "Great product, very useful and easy to use",
    "The quality is good but delivery was late",
    "Not satisfied, product stopped working after one week",
    "Excellent quality and fast delivery",
    "Average experience, nothing special"
]

# ── keyword lists for sentiment detection ──
positive_keywords = ["good", "great", "excellent", "useful", "fast", "easy", "happy", "best"]
negative_keywords = ["not", "bad", "late", "stopped", "worst", "poor", "unsatisfied", "broken"]

# ── Step 2: Display all reviews ──
print("=" * 60)
print("        E-COMMERCE PRODUCT REVIEW ANALYSIS")
print("=" * 60)
print("\n📋 ALL REVIEWS:")
print("-" * 60)
for i, review in enumerate(reviews, start=1):
    print(f"  {i}. {review}")

# ── Step 3: Analyse each review ──

total_reviews    = len(reviews)
positive_reviews = []
negative_reviews = []
neutral_reviews  = []

for review in reviews:
    # convert to lowercase for better keyword matching (bonus)
    review_lower = review.lower()

    found_positive = any(word in review_lower for word in positive_keywords)
    found_negative = any(word in review_lower for word in negative_keywords)

    if found_positive and not found_negative:
        positive_reviews.append(review)
    elif found_negative:
        negative_reviews.append(review)
    else:
        neutral_reviews.append(review)

positive_count = len(positive_reviews)
negative_count = len(negative_reviews)
neutral_count  = len(neutral_reviews)

# ── sentiment percentages (bonus) ──
pos_percent = round((positive_count / total_reviews) * 100)
neg_percent = round((negative_count / total_reviews) * 100)
neu_percent = round((neutral_count  / total_reviews) * 100)

# ── Step 3: Print counts ──
print("\n📊 REVIEW COUNTS:")
print("-" * 60)
print(f"  Total Reviews    : {total_reviews}")
print(f"  Positive Reviews : {positive_count}  ({pos_percent}%)")
print(f"  Negative Reviews : {negative_count}  ({neg_percent}%)")
print(f"  Neutral Reviews  : {neutral_count}   ({neu_percent}%)")

# ── Print categorised reviews ──
print("\n✅ POSITIVE REVIEWS:")
print("-" * 60)
if positive_reviews:
    for r in positive_reviews:
        print(f"  + {r}")
else:
    print("  None found.")

print("\n❌ NEGATIVE REVIEWS:")
print("-" * 60)
if negative_reviews:
    for r in negative_reviews:
        print(f"  - {r}")
else:
    print("  None found.")

print("\n😐 NEUTRAL REVIEWS:")
print("-" * 60)
if neutral_reviews:
    for r in neutral_reviews:
        print(f"  ~ {r}")
else:
    print("  None found.")

# ── Step 4: Simple Insights ──
print("\n" + "=" * 60)
print("        INSIGHTS")
print("=" * 60)

# Insight 1: Overall sentiment
if positive_count > negative_count:
    sentiment = "Mostly Positive 😊"
elif negative_count > positive_count:
    sentiment = "Mostly Negative 😞"
else:
    sentiment = "Mixed 😐"

print(f"\n  Insight 1 — Overall Customer Sentiment : {sentiment}")

# Insight 2: Common complaints
complaints = []
complaint_keywords = {
    "late"    : "Late delivery",
    "stopped" : "Product stopped working",
    "bad"     : "Bad quality",
    "not"     : "Dissatisfied customers",
    "poor"    : "Poor experience",
}
for review in reviews:
    review_lower = review.lower()
    for keyword, complaint in complaint_keywords.items():
        if keyword in review_lower and complaint not in complaints:
            complaints.append(complaint)

print("\n  Insight 2 — Common Complaints:")
if complaints:
    for c in complaints:
        print(f"             * {c}")
else:
    print("             No major complaints found.")

# Insight 3: What customers like the most
likes = []
like_keywords = {
    "quality"  : "Product quality",
    "delivery" : "Fast delivery",
    "useful"   : "Usefulness of product",
    "easy"     : "Ease of use",
    "great"    : "Overall greatness",
    "excellent": "Excellent experience",
}
for review in reviews:
    review_lower = review.lower()
    for keyword, like in like_keywords.items():
        if keyword in review_lower and like not in likes:
            likes.append(like)

print("\n  Insight 3 — What Customers Like Most:")
if likes:
    for l in likes:
        print(f"             * {l}")
else:
    print("             No specific likes identified.")

# Insight 4: Recommendation
print("\n  Insight 4 — Recommendation:")
if pos_percent >= 60:
    print("             Product is well-received. Keep up the quality!")
elif neg_percent >= 60:
    print("             Product needs improvement. Address complaints urgently.")
else:
    print("             Mixed feedback. Focus on resolving delivery and quality issues.")

print("\n" + "=" * 60)

# ── Bonus: Accept user review input ──
print("\n📝 ADD YOUR OWN REVIEW (Bonus Feature)")
print("-" * 60)
user_review = input("  Enter a review (or press Enter to skip): ").strip()

if user_review:
    user_lower = user_review.lower()
    is_pos = any(word in user_lower for word in positive_keywords)
    is_neg = any(word in user_lower for word in negative_keywords)

    if is_pos and not is_neg:
        label = "Positive ✅"
    elif is_neg:
        label = "Negative ❌"
    else:
        label = "Neutral 😐"

    print(f"\n  Your review sentiment: {label}")
    print(f"  Review added: \"{user_review}\"")
else:
    print("  No review entered. Skipping.")

print("\n" + "=" * 60)
print("  Analysis complete. Thank you!")
print("=" * 60)
