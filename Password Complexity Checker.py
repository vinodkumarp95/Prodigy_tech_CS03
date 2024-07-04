import re


class PasswordChecker:
    def __init__(self, password):
        self.password = password
        self.min_length = 8
        self.score = 0
        self.feedback = []

    def check_length(self):
        if len(self.password) >= self.min_length:
            self.score += 1
        else:
            self.feedback.append(f"Password should be at least {self.min_length} characters long.")

    def check_uppercase(self):
        if re.search(r'[A-Z]', self.password):
            self.score += 1
        else:
            self.feedback.append("Password should include at least one uppercase letter.")

    def check_lowercase(self):
        if re.search(r'[a-z]', self.password):
            self.score += 1
        else:
            self.feedback.append("Password should include at least one lowercase letter.")

    def check_digit(self):
        if re.search(r'[0-9]', self.password):
            self.score += 1
        else:
            self.feedback.append("Password should include at least one number.")

    def check_special_char(self):
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', self.password):
            self.score += 1
        else:
            self.feedback.append("Password should include at least one special character.")

    def assess_strength(self):
        # Evaluate each criterion
        self.check_length()
        self.check_uppercase()
        self.check_lowercase()
        self.check_digit()
        self.check_special_char()

        # Assess strength based on score
        strength_levels = {
            0: "Very Weak",
            1: "Weak",
            2: "Fair",
            3: "Good",
            4: "Strong",
            5: "Very Strong"
        }

        return strength_levels[self.score], self.feedback


def main():
    print("Password Strength Checker")
    password = input("Enter a password to assess: ").strip()

    checker = PasswordChecker(password)
    strength, feedback = checker.assess_strength()

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("\nSuggestions for improvement:")
        for suggestion in feedback:
            print(f" - {suggestion}")
    else:
        print("Your password is strong and meets all criteria!")


if __name__ == "__main__":
    main()
