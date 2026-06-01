"""
Day 3 — Loops Over Lists
Problem: You have a list of student scores: [78, 92, 55, 88, 73, 61, 95, 49, 83, 70]

Print all scores above 75.
Count how many students passed (score ≥ 60).
Find the highest and lowest score without using max() or min().
Calculate the class average.
Concepts: for loops, conditionals, accumulators
"""
import statistics

scores = [78, 92, 55, 88, 73, 61, 95, 49, 83, 70]
high_scores = []
mid_scores = []
sixty = 0
highest_score = 0
lowest_score = 0

def high_score(high_scores: list):
    for score in scores:
        if score > 75:
            high_scores.append(score)
    #print(high_scores)
    return high_scores

def mid_score(mid_scores: list):
    global sixty
    for score in scores:
        if score > 60:
            sixty += 1
        # print(high_scores)
    return sixty

def highest_scores(high_scores: list):
    global highest_score
    for score in scores:
        if score > highest_score:
            highest_score = score
        # print(high_scores)
    return highest_score

def lowest_scores(lowest_scores: list):
    lowest_score = scores[0]
    for score in scores:
        if score < lowest_score:
            lowest_score = score
    return lowest_score

def class_average(class_average: list):
    average = 0
    total = 0
    for score in scores:
        total += score
    average = total/len(scores)
    return average


high_score = high_score(high_scores)
print(f"Print all scores above 75 {high_score}")
score_above_sixty = mid_score(sixty)
print(f"Count how many students passed (score ≥ 60) : {score_above_sixty}")
highest = highest_scores(highest_score)
print(f"Find the highest : {highest}")
lowest = lowest_scores(lowest_score)
print(f"find the lowest : {lowest}")
caverage = class_average(class_average)
print(f"Class Average : {caverage}")

print(f"Average score : {statistics.mean(scores)}")