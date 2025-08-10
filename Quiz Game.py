import random

# --- Step 1: Define the quiz questions ---
questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "correct": "C"
    },
    {
        "question": "What movie features the quote: 'May the Force be with you'?",
        "options": ["A. Harry Potter", "B. Star Wars", "C. The Matrix", "D. Lord of the Rings"],
        "correct": "B"
    },
    {
        "question": "What does the 'len()' function do in Python?",
        "options": ["A. Converts to lowercase", "B. Finds length", "C. Repeats a loop", "D. Prints output"],
        "correct": "B"
    },
    {
        "question": "Who played Iron Man in the Marvel Cinematic Universe?",
        "options": ["A. Chris Hemsworth", "B. Chris Evans", "C. Robert Downey Jr.", "D. Mark Ruffalo"],
        "correct": "C"
    },
    {
        "question": "Which of these is NOT a Python data type?",
        "options": ["A. tuple", "B. dictionary", "C. arraylist", "D. list"],
        "correct": "C"
    },
    {
        "question": "What is the capital of Wakanda in Black Panther?",
        "options": ["A. Birnin Zana", "B. Zamunda", "C. Jabari", "D. Sokovia"],
        "correct": "A"
    },
    {
        "question": "In Python, which symbol is used for comments?",
        "options": ["A. //", "B. --", "C. #", "D. **"],
        "correct": "C"
    },
    {
        "question": "Which movie won Best Picture at the Oscars in 2023?",
        "options": ["A. The Fabelmans", "B. Top Gun: Maverick", "C. Everything Everywhere All At Once", "D. Avatar 2"],
        "correct": "C"
    }
]

# --- Step 2: Define the quiz function ---
def start_quiz():
    print("\n🎮 Welcome to the Python & Movie Fun Quiz! 🎬\n")
    score = 0
    total = len(questions)

    # Randomize question order
    random.shuffle(questions)

    # Ask each question
    for i, q in enumerate(questions, start=1):
        print(f"Q{i}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        # Get user answer
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        # Check correctness
        if answer == q["correct"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect. Correct answer: {q['correct']}\n")

    # Show result
    print("🏁 Quiz Finished!")
    print(f"🏆 Your Score: {score}/{total}")
    print("⭐" * score + "\n")

# --- Step 3: Play loop ---
def run_game():
    while True:
        start_quiz()
        retry = input("Do you want to play again? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("\n👋 Thanks for playing! See you next time!")
            break

# --- Entry Point ---
if __name__ == "__main__":
    run_game()
