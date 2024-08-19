import random

# Dictionary of states and their capitals
states_and_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata"
}

def quiz():
    score = 0
    total_questions = 5  # Set the number of questions to ask
    states = random.sample(list(states_and_capitals.keys()), total_questions)  # Randomly select states
    
    print("Welcome to the Indian States and Capitals Quiz!")
    print("Type the capital of the given state. Type 'exit' to quit the quiz.")
    
    for state in states:
        correct_capital = states_and_capitals[state]
        
        user_answer = input(f"What is the capital of {state}? ").strip()
        
        if user_answer.lower() == 'exit':
            break
        
        if user_answer.lower() == correct_capital.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_capital}.")
        
        print()  # Print a new line for better readability

    print(f"Quiz finished! Your score: {score}/{total_questions}")

if __name__ == "__main__":
    quiz()