feedback = []

def add_feedback():
    name = input("Enter student name: ")
    rating = int(input("Enter rating (1-5): "))
    feedback.append({"name": name, "rating": rating})
    print("Feedback added!\n")

def analyze_feedback():
    if not feedback:
        print("No feedback available.\n")
        return
    
    total = sum(f["rating"] for f in feedback)
    avg = total / len(feedback)
    
    print(f"Average Rating: {avg:.2f}")
    
    if avg >= 4:
        print("Overall Feedback: Excellent\n")
    elif avg >= 3:
        print("Overall Feedback: Good\n")
    else:
        print("Overall Feedback: Needs Improvement\n")

while True:
    print("1. Add Feedback")
    print("2. Analyze Feedback")
    print("3. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_feedback()
    elif choice == '2':
        analyze_feedback()
    elif choice == '3':
        break
    else:
        print("Invalid choice\n")