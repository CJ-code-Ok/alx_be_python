task = input("Describe your task:")
priority = input("What is the task's priority (high, medium, low)?:").lower()
time_bound = input("Is the task time-bound (yes or no)?:").lower()
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Please find  time to complete it ASAP!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task that whose deadline is slowly approaching!")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task but it requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
            
