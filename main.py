
from getpass import getpass
from password_checker import(
    check_length,
    check_lowercase,
    check_uppercase,
    check_number,
    check_special_character,
    calculate_score,
    get_strength,
    check_common_password,
    has_repeated_characters,
    has_sequential_character,
    generate_feedback,
)
print("="*45)
print("SECURE PASSWORD ANALYSER")
print("="*45)

password = getpass("Enter your password")

score = calculate_score(password)
strength = get_strength(score)

print("\nPassword Analysis")
print("-" * 25)
print("Length:",len(password))
print("Uppercase:", "Yes" if check_uppercase(password) else "No")
print("Lowercase:", "Yes" if check_lowercase(password) else "No")
print("Number:" , "yes" if check_number(password) else "No")
print("Special Character:", "Yes" if check_special_character(password) else "No")
print("Common passwors:", "Yes" if check_common_password(password) else "No")
print("Repeated characters:", "Yes" if has_repeated_characters(password) else "No")
print("Sequential characters:", "Yes" if has_sequential_character(password) else "No")

print("\nSecurity Result")
print("-" * 25)

print("score:", score, "/5")
print("strength", strength)

feedback = generate_feedback(password)

if feedback:
    print("\nRecommendations:")
    for item in feedback:
        print("-", item)

else:
    print("\nNo major weekness detected.")

print("\n" + "=" * 45)