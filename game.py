import random
import sys

# Game variables
health = 100
stress_level = 0
knowledge_level = 0
social_level = 0

user_average = int(input("Enter your average in high school: "))
user_extracurricular_count = int(input("Enter how many extracurriculars you did in high school: "))


def choose_university():
    # Function to choose a university from the given list and print a congratulations message.
    if user_average >= 97 and user_extracurricular_count >= 3:
        accepted_university = input("You got accepted into both University of Waterloo and University of Toronto, which one would you like to go to? University of Waterloo or University of Toronto: ")
    if user_average >= 92:
        if user_extracurricular_count >= 5:
            # Nested condition based on extracurricular count
            accepted_university = random.choice(["University of Waterloo", "University of Toronto"])
        else:
            accepted_university = "University of Toronto"

    else:
        sys.exit("You were not accepted to any university.")
    print("You were accepted to", accepted_university, "Congrats!")
    return accepted_university


def explore_campus(university):
    # Function to simulate exploring the campus, offering choices based on the university selected.
    global health, stress_level, knowledge_level, social_level
    print("\nAfter getting settled into your dorm room, you decide to explore the ", university , " campus a bit.")
    if university == "University of Waterloo" or university == "Waterloo":
        print("As you wander, you come across a group of students gathered around a bulletin board having a conversation.")
    elif university == "University of Toronto" or university == "Toronto":
        print("As you wander through the iconic King's College Circle, you notice a group of students gathered around a bulletin board, engaged in a lively discussion.")

    choice = input("\nDo you:\nA) Approach the group and introduce yourself\nB) Continue exploring on your own\n").upper()

    if choice == "A":
        # Interacting with a group of students
        social_level += 10
        stress_level += 5
        approach_group(university)
    elif choice == "B":
        # Exploring alone
        stress_level += 10
        explore_alone(university)
    else:
        print("Invalid choice, please try again.")
        explore_campus(university)


def approach_group(university):
    # Function to simulate approaching a group of students, offering different choices based on the university selected.
    global knowledge_level, stress_level
    if university == "University of Waterloo":
        print("You approach the group of students.")
        # Interaction dialogues for University of Waterloo
        print("\nStudent 1: Hey there! You must be new here.")
        print("You: Yeah, I just got accepted into the computer science program. I'm excited but a little nervous too.")
        print("Student 2: Don't worry, we were all there once! This place can seem intimidating at first, but you'll get used to it.")
        print("Student 3: Have you had a chance to check out the computer labs yet? They're top-of-the-line, and perfect for working on projects.")
        print("Student 1: We were just about to head over to the lab to work on our latest assignment. You should come with us, we can show you around!")
    else:
        print("You approach the group of students.")
        # Interaction dialogues for University of Toronto
        print("\nStudent 1: Hey there, you must be new here!")
        print("You: Yeah, I just got accepted into the computer science program. I'm really excited to be here.")
        print("Student 2: Welcome to UofT! This is one of the best places to study computer science in the country.")
        print("Student 3: Have you had a chance to check out the libraries yet? They have some amazing resources for research and studying.")
        print("Student 1: We were just about to head over to the library to work on a group project. You should come with us, we can give you the insider's tour!")

    choice = input("\nDo you:\nA) Go with the group to the lab/library\nB) Thank them, but continue exploring on your own\n").upper()

    if choice == "A":
        # Going with the group to the lab/library
        if university == "University of Waterloo":
            knowledge_level += 10
            stress_level += 5
            lab_episode(university)
        else:
            knowledge_level += 10
            stress_level += 5
            library_episode(university)
    elif choice == "B":
        # Continuing exploration alone
        explore_alone(university)
    else:
        print("Invalid choice, please try again.")
        approach_group(university)


def explore_alone(university):
    # Function to simulate exploring the campus alone.
    print("You decide to continue exploring the ",university," campus on your own for now.")
    if university == "University of Waterloo":
        explore_waterloo_alone()
    else:
        explore_uoft_alone()


def explore_waterloo_alone():
    # Function to simulate exploring the Waterloo campus alone, offering choices for activities.
    print("\nAs you walk around the Waterloo campus, you're struck by the modern architecture and the vibrant tech scene.")
    print("You pass by the Student Life Centre, which is buzzing with activity. There's a group of students playing video games in the lounge area.")
    choice = input("\nDo you:\nA) Join the group and play some games\nB) Continue exploring the campus\n").upper()
    if choice == "A":
        # Joining the group for video games
        print("You decide to join the group and play some video games for a while. It's a great way to meet new people and take a break from exploring.")
        video_game_session()
    elif choice == "B":
        # Continuing exploration
        print("You continue your exploration of the Waterloo campus.")
        explore_waterloo_further()
    else:
        print("Invalid choice, please try again.")
        explore_waterloo_alone()


def explore_uoft_alone():
    # Function to simulate exploring the UofT campus alone, offering choices for activities.
    print("\nAs you wander through the historic UofT campus, you're surrounded by grand architecture and a rich academic atmosphere.")
    print("You stumble upon the impressive Robarts Library, one of the largest academic libraries in the world.")
    choice = input("\nDo you:\nA) Enter the library and explore\nB) Continue exploring the campus\n").upper()
    if choice == "A":
        # Exploring the library
        print("You decide to enter the Robarts Library and explore its vast collections. The library is a true haven for knowledge and study.")
        library_exploration()
    elif choice == "B":
        # Continuing exploration
        print("You continue your exploration of the UofT campus.")
        explore_uoft_further()
    else:
        print("Invalid choice, please try again.")
        explore_uoft_alone()


def lab_episode(university):
    # Function to simulate a lab session, where the player works on a coding assignment with a group.
    global knowledge_level, stress_level
    print("You decide to tag along with the group to the computer lab...")
    print("The students show you around the lab, explaining the various workstations and software available.")
    print("After settling in, you start working on a coding assignment together, with the group members offering helpful tips and guidance.")
    print("You spend a few hours coding and debugging, feeling a sense of accomplishment as you make progress on the project.")
    knowledge_level += 10
    stress_level += 10


def library_episode(university):
    # Function to simulate a library study session, where the player works on a research project with a group.
    global knowledge_level, stress_level
    print("You decide to tag along with the group to the library...")
    print("The students give you a tour of the library, pointing out the different sections and study areas.")
    print("You find a quiet corner to work on your research project, with the group members helping you locate relevant books and resources.")
    print("After a productive study session, you feel more confident about navigating the library's vast collections.")
    knowledge_level += 10
    stress_level += 5


def video_game_session():
    # Function to simulate a video game session with a group of students.
    global health, stress_level, knowledge_level, social_level
    print("\nYou join the group of students playing video games in the lounge area.")
    games = ["Super Smash Bros.", "Fortnite", "Valorant"]
    selected_game = random.choice(games)
    print("The group is playing " + selected_game + ".")

    choice = input("Do you want to join the game? (Y/N): ").upper()
    if choice == "Y":
        print("You decide to join the group and play ",selected_game,".")
        stress_level -= 20
        social_level += 10
    else:
        print("You choose to continue exploring the campus.")
        return

    print("You spend a couple of hours playing ",selected_game," with the group, bonding with your new friends over shared interests.")
    print("It's a great way to take a break from studying and relieve some stress.")


def explore_waterloo_further():
    # Function to simulate further exploration of the Waterloo campus.
    print("\nYou continue exploring the Waterloo campus, taking in the sights and sounds.")
    print("You come across the Columbia Icefield, a popular hangout spot for students.")
    print("There's a lively atmosphere with music playing and people socializing on the green spaces.")
    print("You decide to grab a snack from one of the food trucks and soak in the vibrant campus life.")


def library_exploration():
    global knowledge_level
    print("\nYou spend some time exploring the different floors and sections of the Robarts Library.")
    library_sections = ["Reading Nooks", "Quiet Study Areas", "Cafe", "Special Collections"]

    for floor in range(1, 6):  # Example: iterating through different floors
        print("\nFloor",floor, ":")
        for section in library_sections:
            print("You explore the",section)
            knowledge_level += 2

    print("You make a mental note of the resources available, knowing this library will be a valuable asset for your studies.")


def explore_uoft_further():
    # Function to simulate further exploration of the UofT campus.
    print("\nYou continue your exploration of the UofT campus, marveling at its architectural beauty.")
    print("You stumble upon Hart House, a historic building that serves as a hub for cultural and recreational activities.")
    print("There are various events and clubs meeting inside, offering opportunities to engage with the campus community.")
    print("You decide to step inside and see what's happening.")


def end_game(stay):
    # Function to display the end game message based on whether the player chose to stay in university or dropped out
    if stay:
        print("\nCongratulations! You have decided to stay in university.")
        print("You've worked hard, made meaningful connections, and gained valuable knowledge.")
        print("Now, you're ready to embark on the next chapter of your life with confidence.")
    else:
        print("\nUnfortunately, you have dropped out of university.")
        print("It's important to reflect on what led to this outcome and consider your options moving forward.")
        print("Remember, setbacks are opportunities for growth, and there are many paths to success.")


def main():
    # Main function to run the game.
    global health, stress_level, knowledge_level, social_level
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



main()
