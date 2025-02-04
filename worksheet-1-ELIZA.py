import re
import random

# ----------------------------------------------------
# Utility function to read the entire shakes.txt file.
# ----------------------------------------------------

def read_shakespeare_text(file_path="shakes.txt"):

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text  # For demonstration, we'll only show the first 10000 characters

# ------------------------------------------------------------------------
# Question 1
# ------------------------------------------------------------------------

def question1_1_all_alphabetic(file_path="shakes.txt"):

    text = read_shakespeare_text(file_path)
    lines = text.splitlines()

    pattern = re.compile(r'[A-Za-z]')  # Entire line: one or more alphabetic chars

    print("\n--- Question 1.1: All Alphabetic Lines ---")
    for line in lines[:100]:
        if pattern.match(line):
            print(line)
    print("--- End Question 1.1 ---\n")

def question1_2_lowercase_ending_in_b(file_path="shakes.txt"):
   
    text = read_shakespeare_text(file_path)
    lines = text.splitlines()

    pattern = re.compile(r'[a-z]+b$')  # All lowercase, must end with 'b'

    print("\n--- Question 1.2: Lowercase Lines Ending in 'b' ---")
    for line in lines[:10000]:
        for word in line.split():
            if pattern.match(word):
                print(word)
    print("--- End Question 1.2 ---\n")

def question1_3_bab_condition(file_path="shakes.txt"):

    text = read_shakespeare_text(file_path)
    lines = text.splitlines()

    pattern = re.compile(r'(?:b|bab)')  # Only 'b' or 'babbbbbabbbbaab'

    print("\n--- Question 1.3: Strings Where Each 'a' Is Surrounded by 'b' ---")
    for line in lines:
        for word in line.split():
        # Before checking, ensure the line has only 'a'/'b' characters, otherwise skip
            if pattern.match(word):  
               print(word)
    print("--- End Question 1.3 ---\n")

# ------------------------------------------------------------------------
# Question 2
# ------------------------------------------------------------------------

def question2_1_two_consecutive_repeated_words(file_path="shakes.txt"):

    text = read_shakespeare_text(file_path)
    lines = text.splitlines()

    pattern = re.compile(r'\b([A-Za-z]+)\b\s+\1\b')

    print("\n--- Question 2.1: Lines with Two Consecutive Repeated Words ---")
    for line in lines[:10000]:
        if pattern.search(line):
            print(line)
    print("--- End Question 2.1 ---\n")

def question2_2_starts_with_integer_ends_with_word(file_path="shakes.txt"):
   
    text = read_shakespeare_text(file_path)
    lines = text.splitlines()

    pattern = re.compile(r'^[0-9]+\b.*\b[A-Za-z]+$')

    print("\n--- Question 2.2: Lines Starting with an Integer, Ending with a Word ---")
    for line in lines:
        if pattern.match(line):
            print(line)
    print("--- End Question 2.2 ---\n")

def question2_3_contain_grotto_and_raven(file_path="shakes.txt"):
 
    text = read_shakespeare_text(file_path)
    lines = text.splitlines()

    pattern = re.compile(r'(?=.*\bgrotto\b)(?=.*\braven\b)')

    print("\n--- Question 2.3: Lines Containing Both 'grotto' and 'raven' ---")
    for line in lines[:100]:
        if pattern.match(line):
            print(line)
    print("--- End Question 2.3 ---\n")

def question2_4_capture_first_word(file_path="shakes.txt"):
   
    text = read_shakespeare_text(file_path)
    lines = text.splitlines()

    pattern = re.compile(r'^[^A-Za-z]*([A-Za-z]+)')

    print("\n--- Question 2.4: Capturing the First Word in Each Line ---")
    for line in lines[:10]:
        match = pattern.match(line)
        if match:
            # match.group(1) is the first captured word
            captured_word = match.group(1)
            print(f"Line: {line}\n --> First word captured: '{captured_word}'\n")
    print("--- End Question 2.4 ---\n")

# -------------------------------------------------------------------------
# Question 3 -> Implement an ELIZA-like programme
# -------------------------------------------------------------------------

def question3_eliza():
    print("\n--- Question 3: ELIZA-Like Chatbot ---")

    # Fallback responses to add variety when no rule matches
    fallbacks = [
        "Could you elaborate on that?",
        "Please, go on.",
        "I see. Tell me more about that.",
        "Hmm, that’s interesting. Can you say more?",
    ]

    # Rules: a list of regex–response pairs
    rules = [
        (re.compile(r"\bI\s*(?:am\s*)?feeling\b\s*(.*)", re.IGNORECASE),  # "I am feeling ___"
         "Why do you think you're feeling{0}?"),

        (re.compile(r"\bI\s*feel\s+(.*)", re.IGNORECASE),                 # "I feel ___"
         "Why do you feel {0}?"),

        (re.compile(r"\bI\s*want\s+(.*)", re.IGNORECASE),                # "I want ___"
         "What would having {0} mean to you?"),

        (re.compile(r"\bmy name is (.*)", re.IGNORECASE),                # "My name is ___"
         "Hello {0}, lovely to meet you. How are you feeling today?"),

        (re.compile(r"\byou are (.*)", re.IGNORECASE),                   # "You are ___"
         "Why do you think I am {0}?"),

        (re.compile(r"\bI'?m not sure about (.*)", re.IGNORECASE),       # "I'm not sure about ___"
         "What makes you uncertain about {0}?"),

        (re.compile(r"\bI can'?t (.*)", re.IGNORECASE),                  # "I can't ___"
         "What do you suppose might happen if you could {0}?"),

        (re.compile(r"\bI cannot (.*)", re.IGNORECASE),                  # "I cannot ___"
         "What leads you to believe you cannot {0}?"),

        (re.compile(r"\bI wonder (.*)", re.IGNORECASE),                  # "I wonder ___"
         "That's quite interesting. Have you tried to explore {0} further?"),

        (re.compile(r"\bI remember (.*)", re.IGNORECASE),                # "I remember ___"
         "What significance does {0} hold for you?"),

        (re.compile(r"\bI used to (.*)", re.IGNORECASE),                 # "I used to ___"
         "How do you feel now, looking back on {0}?"),

        (re.compile(r"\bI wish (.*)", re.IGNORECASE),                    # "I wish ___"
         "Why do you wish {0}?"),

        (re.compile(r"\bI love (.*)", re.IGNORECASE),                    # "I love ___"
         "What makes you love {0} so much?"),

        (re.compile(r"\bI hate (.*)", re.IGNORECASE),                    # "I hate ___"
         "Why does {0} bother you so greatly?"),

        (re.compile(r"\bIt hurts when (.*)", re.IGNORECASE),             # "It hurts when ___"
         "Have you discussed how it hurts when {0} with anyone else?"),

        (re.compile(r"\bI dream about (.*)", re.IGNORECASE),             # "I dream about ___"
         "What do you think your dream about {0} might mean?"),

        (re.compile(r"\bMy (father|mother) is (.*)", re.IGNORECASE),     # "My father/mother is ___"
         "How do you feel about your {0} being {1}?"),

        (re.compile(r"\bPeople (.*)", re.IGNORECASE),                    # "People ___"
         "What do you think causes people to {0}?"),

        (re.compile(r"\bNobody (.*)", re.IGNORECASE),                    # "Nobody ___"
         "How does it make you feel that nobody {0}?"),

        (re.compile(r"\bI often think about (.*)", re.IGNORECASE),       # "I often think about ___"
         "What sorts of thoughts do you have about {0}?"),

        (re.compile(r"\bI don'?t know (.*)", re.IGNORECASE),             # "I don't know ___"
         "What do you think might happen if you did know {0}?"),

        (re.compile(r"\bI feel (guilty|ashamed) about (.*)", re.IGNORECASE),  # "I feel guilty/ashamed about ___"
         "Why do you suppose you feel {0} about {1}?"),

        (re.compile(r"\bI can'?t decide whether (.*)", re.IGNORECASE),   # "I can't decide whether ___"
         "What might help you make a decision about {0}?"),

        (re.compile(r"\bI'?m confused about (.*)", re.IGNORECASE),       # "I'm confused about ___"
         "What do you think is the main source of your confusion about {0}?"),
    ]

    # Pronoun reflection function
    def reflect_pronouns(text):
        reflections = {
            r"\byou\b": "I",
            r"\byour\b": "my",
            r"\bare\b": "am",
            r"\bmy\b": "your",
            r"\bme\b": "you",
            r"\bI\b": "you",
            r"\bI'm\b": "you're",
        }
        for pattern, replacement in reflections.items():
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        return text

    # Main response function
    def eliza_respond(user_input):
        user_input = user_input.strip()
        for pattern, response_template in rules:
            match = pattern.search(user_input)
            if match:
                groups = match.groups()  # Capture all groups
                reflected_groups = [reflect_pronouns(g) for g in groups]  # Reflect pronouns in each group
                return response_template.format(*reflected_groups)
        return random.choice(fallbacks)

    # Demonstration
    sample_inputs = [
        "I want a pet unicorn that does taxes",
        "My name is Batman, but you can call me Bruce",
        "You are terrible at listening to my pizza problems",
        "I’m not sure if I’m a genius or just lucky",
        "I feel guilty about eating the last slice of cake",
        "I can’t decide whether to nap or to eat snacks",
        "I often think about what dogs dream of",
        "People keep asking me if I'm a wizard",
        "I wish I could speak fluent penguin",
        "I remember the time I tried to teach my cat yoga",
        "It hurts when I step on Lego pieces in the dark",
        "I dream about flying to the moon in a paper airplane",
]

    print("\nDemonstration of ELIZA-like responses:\n")
    for sample in sample_inputs:
        print(f"User: {sample}")
        print(f"Bot:  {eliza_respond(sample)}\n")

    # Interactive loop
    print("Now let's chat! Type 'quit' or 'exit' to leave.\n")
    while True:
        user_input = input(">> ")
        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye!\n")
            break
        print(f"User: {user_input}")
        print(f"Bot:  {eliza_respond(user_input)}\n")

    print("--- End Question 3 ---\n")

# -------------------------------------------------------------------------
# Main section to demonstrate each function in turn.
# -------------------------------------------------------------------------

if __name__ == "__main__":
    
    #question1_1_all_alphabetic()
    #question1_2_lowercase_ending_in_b()
    # question1_3_bab_condition()

    #question2_1_two_consecutive_repeated_words()
    #question2_2_starts_with_integer_ends_with_word()
    #question2_3_contain_grotto_and_raven()
    #question2_4_capture_first_word()

    question3_eliza()