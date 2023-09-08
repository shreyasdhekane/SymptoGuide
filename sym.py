class SymptomChecker:
    def __init__(self):
        self.symptom_database = {
            "cough": ["Common Cold", "Flu", "COVID-19"],
            "fever": ["Flu", "COVID-19"],
            "headache": ["Migraine", "Tension Headache","COVID-19"],
            "fatigue": ["Anemia", "Chronic Fatigue Syndrome","COVID-19"],
            "pain in ass": ["faisalitis","piles"],
            # Add more symptoms and associated conditions here
        }

    def check_symptoms(self, symptoms):
        matched_conditions = set()
        for symptom in symptoms:
            if symptom in self.symptom_database:
                matched_conditions.update(self.symptom_database[symptom])
        
        if matched_conditions:
            return matched_conditions
        else:
            return ["No matching conditions found."]

if __name__ == "__main__":
    symptom_checker = SymptomChecker()
    
    # Get user input for symptoms (comma-separated)
    user_input = input("Enter your symptoms (comma-separated): ")
    user_symptoms = [symptom.strip() for symptom in user_input.split(",")]

    # Check the symptoms
    result = symptom_checker.check_symptoms(user_symptoms)
    
    # Display the result
    print("Possible conditions based on your symptoms:")
    for condition in result:
        print("- " + condition)
class SymptomChecker:
    def __init__(self):
        self.symptom_database = {
            "cough": ["Common Cold", "Flu", "COVID-19"],
            "fever": ["Flu", "COVID-19"],
            "headache": ["Migraine", "Tension Headache","COVID-19"],
            "fatigue": ["Anemia", "Chronic Fatigue Syndrome","COVID-19"],
            "pain in ass": ["faisalitis","piles"],
            # Add more symptoms and associated conditions here
        }

    def check_symptoms(self, symptoms):
        matched_conditions = set()
        for symptom in symptoms:
            if symptom in self.symptom_database:
                matched_conditions.update(self.symptom_database[symptom])
        
        if matched_conditions:
            return matched_conditions
        else:
            return ["No matching conditions found."]

if __name__ == "__main__":
    symptom_checker = SymptomChecker()
    
    # Get user input for symptoms (comma-separated)
    user_input = input("Enter your symptoms (comma-separated): ")
    user_symptoms = [symptom.strip() for symptom in user_input.split(",")]

    # Check the symptoms
    result = symptom_checker.check_symptoms(user_symptoms)
    
    # Display the result
    print("Possible conditions based on your symptoms:")
    for condition in result:
        print("- " + condition)

    if result:
        print("The most likely condition based on your symptoms:")
        print(result[0])
        
    else:
        print("No matching conditions found.")
