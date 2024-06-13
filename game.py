import random

# Game variables
health = 100
stress_level = 0
knowledge_level = 0
social_level = 0

def main():
    print("Welcome to the University Exploration Simulator!")
    university = choose_university()
    explore_campus(university)
    print("\nCongratulations on completing your first day of exploration at your university!")
    print("Here's how you did:")
    print("Health: ", health)
    print("Stress Level: ", stress_level)
    print("Knowledge Level: ", knowledge_level)
    print("Social Level: ", social_level)

    # Determine the outcome based on knowledge level and stress level
    stay = knowledge_level >= 15 and stress_level <= 25
    end_game(stay)

def choose_university():
    # Function to choose a university from the given list and print a congratulations message.
    user_average = int(input("Enter your average in high school: "))
    user_extracurricular_count = int(input("Enter how many extracurriculars you did in high school: "))

    if user_average >= 97 and user_extracurricular_count >= 3:
        accepted_university = input("You got accepted into both University of Waterloo and University of Toronto, which one would you like to go to? University of Waterloo or University of Toronto: ")
    if user_average >= 92:
        if user_extracurricular_count >= 5:
            # Nested condition based on extracurricular count
            accepted_university = random.choice(["University of Waterloo", "University of Toronto"])
        else:
            accepted_university = "University of Toronto"

    else:
        raise Exception("You were not accepted to any university.")
    print("You were accepted to", accepted_university, "Congrats!")
    return accepted_university

def explore_campus(university):
    # Function to simulate exploring the campus, offering choices based on the university selected.
    print("\nAfter getting settled into your dorm room, you decide to explore the ", university , " campus a bit.")
    if university == "University of Waterloo" or university == "Waterloo":
        print("As you wander, you come across a group of students gathered around a bulletin board having a conversation.")
    elif university == "University of Toronto" or university == "Toronto":
        print("As you wander through the iconic King's College Circle, you notice a group of students gathered around a bulletin board, engaged in a lively discussion.")

    choice = input("\nDo you:\nA) Approach the group and introduce yourself\nB) Continue exploring on your own\n").upper()

    if choice == "A":
        approach_group(university)
    elif choice == "B":
        explore_alone(university)
    else:
        print("Invalid choice, please try again.")
        explore_campus(university)

def approach_group(university):
    # Function to simulate approaching a group of students, offering different choices based on the university selected.
    if university == "University of Waterloo":
        print("You approach the group of students at Waterloo.")
    else:
        print("You approach the group of students at UofT.")

def explore_alone(university):
    # Function to simulate exploring the campus alone.
    if university == "University of Waterloo":
        print("You decide to explore the Waterloo campus alone.")
    else:
        print("You decide to explore the UofT campus alone.")

def end_game(stay):
    # Function to display the end game message based on whether the player chose to stay in university or dropped out
    if stay:
        print("\nCongratulations! You have decided to stay in university.")
    else:
        print("\nUnfortunately, you have dropped out of university.")

if __name__ == "__main__":
    main()
