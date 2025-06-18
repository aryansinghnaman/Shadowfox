total_jumping_jacks = 100
set_size = 10
completed = 0

while completed < total_jumping_jacks:
    completed += set_size
    print(f"\nYou completed {completed} jumping jacks.")

    # Check if user completed full workout
    if completed >= total_jumping_jacks:
        print("🎉 Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/no): ").strip().lower()
    
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"\nYou completed a total of {completed} jumping jacks.")
            break
        else:
            print(f"{total_jumping_jacks - completed} jumping jacks remaining.")
    else:
        print(f"{total_jumping_jacks - completed} jumping jacks remaining.")
