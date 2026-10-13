# Calorie Counter

A beginner-friendly Python command-line project to record food, estimate calorie intake, and compare the total with a daily calorie goal.

## Features
- Set a daily calorie goal.
- Add food items with calories per serving and number of servings.
- View each logged item and total calories consumed.
- See calories remaining or how far the total is above the goal.
- Validate numeric input.

## Requirements
- Python 3.8 or newer
- No external libraries required

## How to run
1. Download and extract this project ZIP.
2. Open a terminal or command prompt in the project folder.
3. Run:

   ```bash
   python calorie_counter.py
   ```

## Example
If you log a meal with 250 kcal per serving and 2 servings, the app adds 500 kcal to your daily total.

## Limitations
Entries are kept only while the program is running; they are not saved after exit. Calorie values depend on portion size and the accuracy of the values you enter. This tool is for general tracking, not medical advice.
