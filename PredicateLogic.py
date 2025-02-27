class MedicalDiagnosisAI:
    def __init__(self):
        """ Initialize knowledge base with facts and rules """
        self.facts = {}  # Stores known symptoms for each patient
        self.rules = []  # Stores predicate logic rules

        self.stem = {"Introduction to Computer Science": "Prerequisite: None or Pre-Calculus",
                        "Data Structures and Algorithms" : "Prerequisite: Introduction to Computer Science",
                        "Linear Algebra" : "Prerequisite: Calculus I",
                        "Organic Chemistry" : "Prerequisite: General Chemistry I",
                        "Biomechanics" : "Prerequisite: Physics I, Anatomy & Physiology",
                        "Artificial Intelligence " : "Prerequisite: Data Structures, Probability & Statistics"}

        self.businessEcon = {"Principles of Finance" : "Prerequisite: Introduction to Business, College Algebra",
                                "Marketing Strategies" : "Prerequisite: Introduction to Marketing",
                                "Investment Analysis" : "Prerequisite: Principles of Finance",
                                "Entrepreneurship & Innovation" : "Prerequisite: Introduction to Business"}
                        
        self.artsHumanities = {"Creative Writing Workshop" : "Prerequisite: English Composition",
                            "Art History" : "Prerequisite: None",
                            "Digital Photography" : "Prerequisite: None or Basic Art Course",
                            "Film Production " : "Prerequisite: Introduction to Film Studies"}

        self.socialSciLaw = {"Introduction to Political Science" : "Prerequisite: None",
                        "Constitutional Law" : " Prerequisite: Introduction to Political Science",
                        "Abnormal Psychology" : "Prerequisite: Introduction to Psychology",
                        "Sociology of Race and Ethnicity" : "Prerequisite: Introduction to Sociology"}

        self.healthSportSci = {"Anatomy & Physiology" : "Prerequisite: Biology I",
                        "Principles of Nutrition" : "Prerequisite: None",
                        "Kinesiology" : "Prerequisite: Anatomy & Physiology",
                        "Sports Medicine" : "Prerequisite: Biology, Chemistry"}

        self.envSustainability = {"Environmental Science" : "Prerequisite: None",
                        "Climate Change and Policy" : "Prerequisite: Environmental Science",
                        "Renewable Energy Technologies" : "Prerequisite: Physics, Chemistry"}

        self.gamingMedia =  { "Game Design Fundamentals" : "Prerequisite: None",
                        "3D Modeling and Animation" : "Prerequisite: Introduction to Game Design",
                        " Game Development with Unity" : "Prerequisite: Programming I"}



    def add_fact(self, patient, symptom):
        """ Adds known symptoms (patient's reported symptoms) """
        if patient not in self.facts:
            self.facts[patient] = set()
        self.facts[patient].add(symptom)



    def add_rule(self, premise, conclusion):
        """ Adds inference rules for diagnosing diseases """
        self.rules.append((premise, conclusion))



    def suggestMajor(self, student):
        """ Uses Predicate Logic to infer diseases """
        majors = [] #instantiate array of diseases
        if student not in self.facts: #if the patient listed is not in the self.facts dictionary return message
            return ["No data available for patient"]

        studentInterests = self.facts[student]

        for premise, conclusion in self.rules:
            if premise & studentInterests:  # Sorts any arrangement of interest key words
                majors.append(conclusion)

        return majors if majors else ["No clear diagnosis"]



# Create Medical AI System
student_ai = MedicalDiagnosisAI()

# Define Disease Rules in Predicate Logic
student_ai.add_rule({"STEM", "Science", "Tech", "Engineering", "Math", "Computers", "Programming", "Cybersecurity", "AI", "Math", "Physics",
                    "Chemistry", "Biology", "Medicine", "Engineering", "Robotics", "Aerospace", "Electronics", "Data", "Analytics", "Astronomy", 
                    "Genetics"}, 
                    "STEM")

student_ai.add_rule({"Business", "Economics", "Finance", "Investing", "Marketing", "Entrepreneurship"}, 
                    "Business $ Economy")

student_ai.add_rule({"Humanities", "Art", "Music", "Writing", "History", "Philosophy", "Theater", "Photography", "Film", "Humanities"}, 
                    "Arts & Humanities")

student_ai.add_rule({"Medicine", "Healthcare", "Coaching", "Sports"}, "Health & Sport Sciences") 
student_ai.add_rule({"Social Sciences", "Law", "Politics", "Law", "Psychology", "Sociology", "Education"}, 
                    "Social Sciences & Law")

student_ai.add_rule({"Environmental Studies", "Sustainability", "Environment", "Sustainability", "Agriculture", "Farming"}, 
                    "Environmental Studies & Sustainability")

student_ai.add_rule({"Gaming", "Interactive Media", "Social Media", "Instagram", "TikTok", "SnapChat"}, 
                    "Gaming & Interactive Media")

courseLists = {
    "STEM": student_ai.stem,
    "Business $ Economy": student_ai.businessEcon,
    "Arts & Humanities": student_ai.artsHumanities,
    "Social Sciences & Law": student_ai.socialSciLaw,
    "Environmental Studies & Sustainability": student_ai.envSustainability,
    "Gaming & Interactive Media": student_ai.gamingMedia,
    "Health & Sport Sciences": student_ai.healthSportSci
}

#STUDENT ONE : WALUIG
studentName = "WaLuigi"
studentInterests = ["Math", "STEM", "Farming"]
# student_ai.facts[studentName] = set()

for interest in studentInterests:
    student_ai.add_fact(studentName, interest)

# Perform Inference
suggestion = student_ai.suggestMajor(studentName)
print(f"\nRecommendations for {studentName}:", ", ".join(suggestion))
print(f"{suggestion[0]}, {suggestion[1]}")

print(f"\n\nBased on your choices, the following courses are likely to suit your interests: ")
for major in suggestion:
    if major in courseLists:
        print(f"\n{major} : Here are some courses to discuss with your advisor along with prerequisites:")
        for course, prereq in courseLists[major].items():
            print(f"  {course}: {prereq}\n")
    else:
        print(f"\nNo course list available for {major}")



#STUDENT ONE : OPTIMUS PRIME
studentName = "Optimus Prime"
studentInterests = ["Gaming", "Music", "Art"]
# student_ai.facts[studentName] = set()

for interest in studentInterests:
    student_ai.add_fact(studentName, interest)

# Perform Inference
suggestion = student_ai.suggestMajor(studentName)
print(f"\n\n\nRecommendations for {studentName}:", ", ".join(suggestion))
print(f"{suggestion[0]}, {suggestion[1]}")

print(f"\n\nBased on your choices, the following courses are likely to suit your interests: ")
for major in suggestion:
    if major in courseLists:
        print(f"\n{major} : Here are some courses to discuss with your advisor along with prerequisites:")
        for course, prereq in courseLists[major].items():
            print(f"  {course}: {prereq}\n")
    else:
        print(f"\nNo course list available for {major}")



#STUDENT ONE : HALF A DOLLAR 
studentName = "50 Cent"
studentInterests = ["Biology", "Psychology", "Investing"]
# student_ai.facts[studentName] = set()

for interest in studentInterests:
    student_ai.add_fact(studentName, interest)

# Perform Inference
suggestion = student_ai.suggestMajor(studentName)
print(f"\n\n\nRecommendations for {studentName}:", ", ".join(suggestion))
print(f"{suggestion[0]}, {suggestion[1]}")

print(f"\n\nBased on your choices, the following courses are likely to suit your interests: ")
for major in suggestion:
    if major in courseLists:
        print(f"\n{major} : Here are some courses to discuss with your advisor along with prerequisites:")
        for course, prereq in courseLists[major].items():
            print(f"  {course}: {prereq}\n")
    else:
        print(f"\nNo course list available for {major}")


