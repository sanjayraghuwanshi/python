"""
Day 21 — Week 3 Mini Project: Quiz Game
Project: Build a quiz game using functions and dictionaries.

Structure:
=========
1. Store questions as a list of dictionaries: {"question": "...", "options": [...], "answer": "..."}
2. Create at least 8 questions on any topic you like.
3. Functions to write:
    display_question(q) — shows the question and options.
    check_answer(user_ans, correct_ans) — returns True/False.
    run_quiz(questions) — runs through all questions, tracks score.
    show_result(score, total) — prints final score with a message (Excellent/Good/Try Again).
Shuffle questions each time using random.shuffle().
"""

space_trivia = [
    {
        "question": "Which planet in our solar system has the most moons?",
        "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
        "answer": "Saturn"
    },
    {
        "question": "What is the hottest planet in our solar system?",
        "options": ["Mercury", "Venus", "Mars", "Jupiter"],
        "answer": "Venus"
    },
    {
        "question": "Roughly how long does it take for light from the Sun to reach Earth?",
        "options": ["8 seconds", "8 minutes", "8 hours", "8 days"],
        "answer": "8 minutes"
    },
    {
        "question": "Which galaxy is the closest major galaxy to the Milky Way?",
        "options": ["Andromeda", "Triangulum", "Sombrero", "Whirlpool"],
        "answer": "Andromeda"
    },
    {
        "question": "What is the name of the first artificial Earth satellite launched into space?",
        "options": ["Apollo 11", "Voyager 1", "Sputnik 1", "Hubble"],
        "answer": "Sputnik 1"
    },
    {
        "question": "Who was the first human to journey into outer space?",
        "options": ["Neil Armstrong", "Yuri Gagarin", "Buzz Aldrin", "John Glenn"],
        "answer": "Yuri Gagarin"
    },
    {
        "question": "Which element makes up the vast majority of the Sun's mass?",
        "options": ["Oxygen", "Helium", "Hydrogen", "Carbon"],
        "answer": "Hydrogen"
    },
    {
        "question": "What is the name of the rover that landed on Mars in February 2021?",
        "options": ["Curiosity", "Perseverance", "Opportunity", "Spirit"],
        "answer": "Perseverance"
    }
]

def display_question(q):
    """Shows the question and a numbered list of options."""
    print(f"\nQues. {q['question']}")
    for i, option in enumerate(q['options'], 1):
        print(f"  {i}. {option}")

def check_answer(user_ans, correct_ans):
    return str(user_ans).strip().lower() == str(correct_ans).strip().lower()


def show_result(score, total):
    """Prints final score and a performance message."""
    percentage = (score / total) * 100
    print(f"\n--- Final Results ---")
    print(f"Score: {score}/{total} ({percentage}%)")

    if percentage == 100:
        print("Result: Excellent!")
    elif percentage >= 70:
        print("Result: Good!")
    else:
        print("Result: Try Again.")


def run_quiz(questions):
    """Loops through questions, collects input, and tracks the score."""
    current_score = 0
    for q in questions:
        display_question(q)
        choice = input("Your answer: ")

        # Check against the string answer
        if check_answer(choice, q['answer']):
            print("Correct!")
            current_score += 1
        else:
            print(f"Wrong! The correct answer was: {q['answer']}")

    show_result(current_score, len(questions))

run_quiz(space_trivia)