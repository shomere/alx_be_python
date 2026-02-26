#!/usr/bin/env python3

# prompt the user for single task

task = input("Enter your task: ")
priority = input("Priority(high/medium/low): ")
time_bound = input("Is it time-bound?(yes/no): ")

#process the task based on priority and time sensitivity

match priority:
    case "high":
        reminder = f"{task} is high priority task"
    case "medium":
        reminder = f"{task} is medium priority task"
    case "low":
        reminder = f"{task} is low priority task"
    case -:
        reminder = f"{task} is unknown priority"

# modify reminder if time-bound

if time-bound == "yes":
    reminder += "that require immediate attention today!"
    print(f"Reminder: {reminder}")
else:
    print(f"Note: {reminder}. Consider completing it when you have free time.")

print("\nWell done on completing this project! Let the world hear about this milestone achieved.")

