import random
import time

# --- Collection of programming jokes ---
jokes = [
    "Why do Python programmers wear glasses? Because they can't C!",
    "I told my code to go to sleep... but it just kept throwing exceptions.",
    "Why did the developer go broke? Because he used up all his cache!",
    "What do you call 8 hobbits? A hobbyte.",
    "Why was the JavaScript developer sad? Because he didn’t 'null' his feelings.",
    "Why do functions break up? Because they have too many arguments.",
    "Python: Where whitespace is not just a suggestion, it's the law!",
    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
    "Why don't programmers like nature? It has too many bugs.",
    "How many programmers does it take to change a light bulb? None – it’s a hardware problem."
]

# --- Display welcome message ---
def intro():
    print("\n🧠 Welcome to the Programmer's Laugh Zone 🧠")
    print("Get ready to giggle like a glitch in production...\n")

# --- Display random joke ---
def tell_joke():
    joke = random.choice(jokes)
    print("💡 Here's a random joke just for you:\n")
    print("😂 " + joke + "\n")

# --- Main function ---
def run_joke_machine():
    intro()
    tell_joke()
    print("Want more? Just run me again! 🐍\n")

# --- Entry point ---
if __name__ == "__main__":
    run_joke_machine()
