
class SymptomChecker:
    def __init__(self):
        self.symptom_database = {
    "Fever": ["Flu", "COVID-19", "Common Cold"],
    "Cough": ["Flu", "COVID-19", "Common Cold", "Bronchitis"],
    "Headache": ["Migraine", "Tension Headache", "Sinusitis"],
    "Fatigue": ["Chronic Fatigue Syndrome", "Anemia", "Depression"],
    "Sore Throat": ["Strep Throat", "Common Cold", "COVID-19"],
    "Shortness of Breath": ["Asthma", "Pneumonia", "COVID-19"],
    "Nausea": ["Food Poisoning", "Gastroenteritis", "Morning Sickness"],
    "Vomiting": ["Food Poisoning", "Gastroenteritis", "Norovirus"],
    "Diarrhea": ["Food Poisoning", "Gastroenteritis", "Irritable Bowel Syndrome"],
    "Chest Pain": ["Heart Attack", "Angina", "Gastroesophageal Reflux Disease"],
    "Abdominal Pain": ["Appendicitis", "Irritable Bowel Syndrome", "Gastritis"],
    "Joint Pain": ["Rheumatoid Arthritis", "Osteoarthritis", "Lupus"],
    "Back Pain": ["Herniated Disc", "Muscle Strain", "Osteoarthritis"],
    "Frequent Urination": ["Urinary Tract Infection", "Diabetes", "Enlarged Prostate"],
    "Constipation": ["Irritable Bowel Syndrome", "Hemorrhoids", "Colon Cancer"],
    "Dizziness": ["Vertigo", "Anemia", "Migraine"],
    "Rash": ["Allergies", "Eczema", "Psoriasis"],
    "Swelling": ["Edema", "Allergies", "Lymphedema"],
    "Chest Congestion": ["Pneumonia", "Bronchitis", "Asthma"],
    "Runny Nose": ["Common Cold", "Allergies", "Sinusitis"],
    "Frequent Urination": ["Urinary Tract Infection", "Diabetes", "Enlarged Prostate"],
    "Frequent Thirst": ["Diabetes", "Dehydration", "Kidney Disease"],
    "Unexplained Weight Loss": ["Hyperthyroidism", "Cancer", "Diabetes"],
    "Fainting": ["Vasovagal Syncope", "Low Blood Pressure", "Heart Arrhythmia"],
    "Seizures": ["Epilepsy", "Fever-induced Seizures", "Brain Tumor"],
    "Chest Tightness": ["Angina", "Asthma", "Panic Attack"],
    "Numbness or Tingling": ["Peripheral Neuropathy", "Multiple Sclerosis", "Pinched Nerve"],
    "Vision Changes": ["Cataracts", "Glaucoma", "Macular Degeneration"],
    "Shortness of Breath": ["Asthma", "Pneumonia", "COPD"],
    "Coughing Blood": ["Lung Cancer", "Tuberculosis", "Bronchitis"],
    "Bloody Stool": ["Hemorrhoids", "Colon Cancer", "Inflammatory Bowel Disease"],
    "Loss of Appetite": ["Depression", "Anorexia", "Cancer"],
    "Night Sweats": ["Tuberculosis", "Lymphoma", "Menopause"],
    "Chest Pain with Exertion": ["Angina", "Aortic Stenosis", "Coronary Artery Disease"],
    "Abdominal Bloating": ["Irritable Bowel Syndrome", "Ovarian Cancer", "Gastritis"],
    "Difficulty Swallowing": ["Esophageal Stricture", "GERD", "Throat Cancer"],
    "Pale Skin": ["Anemia", "Iron Deficiency", "Leukemia"],
    "Calf Pain": ["Deep Vein Thrombosis", "Muscle Cramp", "Peripheral Artery Disease"],
    "Increased Heart Rate": ["Anxiety", "Hyperthyroidism", "Panic Attack"],
    "Chest Wall Pain": ["Costochondritis", "Muscle Strain", "Rib Fracture"],
    "Mood Swings": ["Bipolar Disorder", "Depression", "Borderline Personality Disorder"],
    "Difficulty Breathing While Lying Down": ["Congestive Heart Failure", "Sleep Apnea", "Chronic Obstructive Pulmonary Disease"],
    "Yellowing of Skin and Eyes": ["Jaundice", "Hepatitis", "Liver Disease"],
    "Hair Loss": ["Alopecia", "Thyroid Disorder", "Chemotherapy"],
    "Irregular Menstrual Periods": ["Polycystic Ovary Syndrome", "Endometriosis", "Uterine Fibroids"],
    "Cold Hands and Feet": ["Raynaud's Disease", "Poor Circulation", "Hypothyroidism"],
    # Add more symptoms and associated diseases here
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
        print(result)
        
    else:
        print("No matching conditions found.")
