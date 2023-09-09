const readline = require('readline');

class SymptomChecker {
    constructor() {
        this.symptomDatabase = {
            "cough": ["Common Cold", "Flu", "COVID-19"],
            "fever": ["Flu", "COVID-19"],
            "headache": ["Migraine", "Tension Headache", "COVID-19"],
            "fatigue": ["Anemia", "Chronic Fatigue Syndrome", "COVID-19"],
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
        };
    }

    async checkSymptoms(symptoms) {
        const matchedConditions = new Set();
        for (const symptom of symptoms) {
            if (symptom in this.symptomDatabase) {
                this.symptomDatabase[symptom].forEach(condition => {
                    matchedConditions.add(condition);
                });
            }
        }

        if (matchedConditions.size > 0) {
            return Array.from(matchedConditions);
        } else {
            return ["No matching conditions found."];
        }
    }
}

// Example usage:
const symptomChecker = new SymptomChecker();
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter your symptoms (comma-separated): ", (userInput) => {
    const userSymptoms = userInput.split(",").map(symptom => symptom.trim());

    symptomChecker.checkSymptoms(userSymptoms).then(result => {
        console.log("Possible conditions based on your symptoms:");
        for (const condition of result) {
            console.log("- " + condition);
        }

        if (result.length > 0) {
            console.log("The most likely condition based on your symptoms:");
            console.log(result[0]);
        } else {
            console.log("No matching conditions found.");
        }

        rl.close();
    });
});
