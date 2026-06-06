"""
Day 12 — Combining Lists & Dictionaries
Problem: You have two lists:

subjects = ["Math", "Science", "English", "History", "PE"]
scores   = [88, 76, 92, 65, 80]
1. Combine them into a dictionary using zip().
2. Find the subject with the highest and lowest score.
3. Add a new subject "Art" with score 71.
4. Print subjects where score is above average.
5. Create a sorted list of (subject, score) tuples by score.
Concepts: zip(), dict(), tuples, combined data structures
"""
subjects = ["Math", "Science", "English", "History", "PE"]
scores   = [88, 76, 92, 65, 80]

# 1
subject_scores = dict(zip(subjects, scores))
print(subject_scores)

# 2
highest = max(subject_scores, key=subject_scores.get)
lowest = min(subject_scores, key=subject_scores.get)

print(f"Highest: {highest} ({subject_scores[highest]})")
print(f"Lowest: {lowest} ({subject_scores[lowest]})")

# 3
subject_scores["Art"] = 71
print(subject_scores)

# 4
avg = sum(subject_scores.values()) / len(subject_scores)
above_avg = {k: v for k, v in subject_scores.items() if v >= avg}
print(f"Average: {avg:.2f}")
print(f"Subjects above average: {above_avg}")

# 5
sorted_scores = sorted(subject_scores.items(), key=lambda item : item[1], reverse=True)
print(sorted_scores)