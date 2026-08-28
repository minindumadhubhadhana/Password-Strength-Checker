def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    for character in password:
        if character.isupper():
            return True
    return False

def check_lowercase(password):
    for character in password:
        if character.islower():
            return True
    return False 

def check_number(password):
    for character in password:
        if character.isdigit():
            return True
    return False 

SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{};:,.<>?/\\|"

def check_special_character(password):
    for character in password:
        if character in SPECIAL_CHARACTERS:
            return True
    return False

def calculate_score(password):
    score = 0

    if check_length(password):
        score +=1

    if check_lowercase(password):
        score +=1

    if check_uppercase(password):
        score +=1

    if check_number(password):
        score +=1

    if check_special_character(password):
        score +=1

    return score

def get_strength(score):
    if score <=2:
        return "Weak"
    if score <=4:
        return"Medium"
    else: 
        return"Strong"

def check_common_password(password):
    try:
        with open("commonpassword.txt","r") as file:
            common_passwords = {
                line.strip().lower()
                for line in file
            }
        return password.lower() in common_passwords

    except FileNotFoundError:
        return False

def has_repeated_characters(password):
    for i in range(len(password) - 2):
        if  password[i] == password[i + 1] == password[i + 2]:
            return True
    return False

def has_sequential_character(password):
    password = password.lower()

    for i in range(len(password) - 2):
        first = ord(password[i])
        second = ord(password[i + 1])
        third = ord(password[i + 2])

        if second == first + 1 and third == second + 1:
            return True
        
    return False

def generate_feedback(password):
        feedback = []
    
        if not check_length(password):
            feedback.append("Use at least 8 characters.")
        if not check_lowercase(password):
            feedback.append("Add a lowercase letter.")
        if not check_uppercase(password):
            feedback.append("Add an uppercase letter.")
        if not check_number(password):
            feedback.append("Add a number.")
        if not check_special_character(password):
            feedback.append("Add a special Character.")
        if not check_common_password(password):
            feedback.append("Avoid commonly used password.")
        if not has_repeated_characters(password):
            feedback.append("Avoid Repeated characters.")
        if not has_sequential_character(password):
            feedback.append("Avoid sequential character.")
        return feedback
        










