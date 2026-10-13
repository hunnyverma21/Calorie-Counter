"""
Calorie Counter
A beginner-friendly command-line app to log food and estimate daily calorie intake.
"""

from datetime import date

def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a number that is 0 or greater.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def main():
    entries = []
    print("=" * 38)
    print("         DAILY CALORIE COUNTER")
    print("=" * 38)
    print(f"Date: {date.today()}")
    goal = get_positive_number("Enter your daily calorie goal (kcal): ")

    while True:
        print("\n1. Add food")
        print("2. View today's summary")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            food = input("Food name: ").strip()
            if not food:
                print("Food name cannot be empty.")
                continue
            calories = get_positive_number("Calories for this serving (kcal): ")
            servings = get_positive_number("Number of servings: ")
            total = calories * servings
            entries.append({"food": food, "calories": total})
            print(f"Added {food}: {total:.0f} kcal")

        elif choice == "2":
            total = sum(item["calories"] for item in entries)
            print("\n--- TODAY'S SUMMARY ---")
            if not entries:
                print("No food entries yet.")
            else:
                for index, item in enumerate(entries, start=1):
                    print(f"{index}. {item['food']}: {item['calories']:.0f} kcal")
            print(f"Total consumed: {total:.0f} kcal")
            print(f"Daily goal:     {goal:.0f} kcal")
            remaining = goal - total
            if remaining > 0:
                print(f"Remaining:      {remaining:.0f} kcal")
            elif remaining < 0:
                print(f"Over goal by:   {abs(remaining):.0f} kcal")
            else:
                print("You have reached your daily goal!")

        elif choice == "3":
            print("Goodbye! Remember that calorie values are estimates.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
