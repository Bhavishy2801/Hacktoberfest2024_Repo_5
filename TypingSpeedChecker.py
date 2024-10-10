import time
import random

def get_random_prompt():
    prompts = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a great programming language.",
        "Typing speed tests are fun and useful.",
        "Practice makes perfect.",
        "Real-time typing tests help improve your skills."
    ]
    return random.choice(prompts)

def typing_speed_test():
    print("Welcome to the Typing Speed Test!")
    prompt = get_random_prompt()
    print("\nType the following prompt as quickly as you can:\n")
    print(f'"{prompt}"\n')

    input("Press Enter to start...")
    start_time = time.time()
    
    typed_text = input("\nStart typing here:\n")
    end_time = time.time()
    
    time_taken = end_time - start_time
    calculate_speed(typed_text, prompt, time_taken)

def calculate_speed(typed_text, prompt, time_taken):
    if typed_text == prompt:
        words_count = len(prompt.split())
        typing_speed = (words_count / time_taken) * 60  # words per minute
        print(f"\nYour typing speed: {typing_speed:.2f} WPM")
    else:
        print("\nThe text you typed did not match the prompt.")
        print(f'You typed: "{typed_text}"')
        print(f'Expected: "{prompt}"')

if __name__ == "__main__":
    typing_speed_test()
