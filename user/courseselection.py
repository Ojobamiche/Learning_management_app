# Assuming you have a list of available courses
available_courses = [
    "Mathematics",
    "Physics",
    "Computer Science",
    "Biology",
    "Chemistry",
    "History",
    "Literature"
]

# Define a function to display available courses and get user input
def select_courses():
    print("Available courses:")
    for i, course in enumerate(available_courses, start=1):
        print(f"{i}. {course}")

    # Get user input for selected courses
    selected_courses = input("Enter the numbers of your preferred courses (comma-separated): ")
    selected_courses = selected_courses.split(",")

    # Convert selected course numbers to actual course names
    preferred_courses = []
    for num in selected_courses:
        try:
            index = int(num.strip()) - 1
            preferred_courses.append(available_courses[index])
        except (ValueError, IndexError):
            print(f"Invalid input: {num} is not a valid course number.")

    return preferred_courses

# Call the function to get user's preferred courses
user_courses = select_courses()

# Print the selected courses
print(f"Your preferred courses: {', '.join(user_courses)}")
