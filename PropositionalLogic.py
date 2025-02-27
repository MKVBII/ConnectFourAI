class StudentCourseRecommendations:
    def __init__(self):
        """ Initialize knowledge base with inference rules """
        #self.facts = set()  # Stores known keywords
        self.rules = []  # Stores keyword groupings that lead to course suggestions
        self.preReqs = set() # Stores the prerequisites to each course suggestions
        self.facts = {}

        #Courses and their prerequisite(s)
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
                        

        # Key words to suggest
        self.stemKeyWords = ["STEM", "Science", "Tech", "Engineering", "Math", "Computers", "Programming", "Cybersecurity", "AI", "Math", "Physics",
                             "Chemistry", "Biology", "Medicine", "Engineering", "Robotics", "Aerospace", "Electronics", "Data", "Analytics", "Astronomy", 
                             "Genetics"]
        self.businessEconomicsKeyWords = ["Business", "Economics", "Finance", "Investing", "Marketing", "Entrepreneurship"]
        self.artsHumanitiesKeyWords = ["Arts", "Humanities", "Art", "Music", "Writing", "History", "Philosophy", "Theater", "Photography", "Film", "Humanities"]
        self.socialSciencesLawKeyWords = ["Social Sciences", "Law", "Politics", "Psychology", "Sociology", "Education"]
        self.environmentalSustainabilityKeyWords = ["Environmental Studies", "Sustainability", "Environment", "Agriculture", "Farming"]
        self.gamingInteractiveMediaKeyWords = ["Gaming", "Interactive Media", "Social Media", "Instagram", "TikTok", "SnapChat"]
        self.healthSportSciKeyWords = ["Medicine", "Healthcare", "Coaching", "Sports"]
        

    def add_fact(self, studentName, interests):
        """ Adds known interests (student's reported interests) """
        if studentName not in self.facts:
            self.facts[studentName] = set()
        self.facts[studentName].add(interests)


    def add_rule(self, premise, conclusion):
        """ Adds inference rules for suggesting courses """
        self.rules.append((premise, conclusion))


    def suggestMajor(self, studentName):

        suggestedMajors = set()

        studentInterests = self.facts[studentName]

        for premise, conclusion in self.rules:
            if premise & studentInterests:
                suggestedMajors.add(conclusion)

        return suggestedMajors if suggestedMajors else ["No Clear Suggestons"]

# Create Course Recommendation AI System
student_ai = StudentCourseRecommendations()

# Define Course Rules
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

# name = str(input("Greetings, what is your name?: "))
# print(f"Hello {name}, welome to the Merrimack College Course Recommendation AI! Below are some key words to help us recommend courses that best suit your interests: ")

# Display the keywords the student can use to express interests
for i in range(7):
    print(student_ai.rules[i][1], ":\n", student_ai.rules[i][0], "\n")


# Add Student's Interests
# studentInterests = set(input("Enter some of your interests from above in the following format; interest1, interest2, . . . : ").split(", "))

courseLists = {
    "STEM": student_ai.stem,
    "Business $ Economy": student_ai.businessEcon,
    "Arts & Humanities": student_ai.artsHumanities,
    "Social Sciences & Law": student_ai.socialSciLaw,
    "Environmental Studies & Sustainability": student_ai.envSustainability,
    "Gaming & Interactive Media": student_ai.gamingMedia,
    "Health & Sport Sciences": student_ai.healthSportSci
}

#STUDENT ONE : BILLY
studentName = "Billy"
s1Interests = ["STEM", "Tech", "Gaming"]
for interest in s1Interests:
    student_ai.add_fact(studentName, interest)

suggestion = student_ai.suggestMajor(studentName) 

print(f"{studentName}\nBased on your choices, the following courses are likely to suit your interests: ")
for major in suggestion:
    if major in courseLists:
        print(f"\n{major} : Here are some courses to discuss with your advisor along with prerequisites:")
        for course, prereq in courseLists[major].items():
            print(f"  {course}: {prereq}\n")
        print()
    else:
        print(f"\nNo course list available for {major}")



#STUDENT TWO : JOE
studentName = "Joe"
s2Interests = ["Art","Finance","TikTok"]

for interest in s2Interests:
    student_ai.add_fact(studentName, interest)

suggestion = student_ai.suggestMajor(studentName)

print(f"{studentName}\nBased on your choices, the following courses are likely to suit your interests: ")
for major in suggestion:
    if major in courseLists:
        print(f"\n{major} : Here are some courses to discuss with your advisor along with prerequisites:")
        for course, prereq in courseLists[major].items():
            print(f"  {course}: {prereq}\n")
        print()
    else:
        print(f"\nNo course list available for {major}")


#STUDENT THREE : STEWART
studentName = "Stewart"
s3Interests = ["Law", "Coaching", "Biology"]
for interests in s3Interests:
    student_ai.add_fact(studentName, interest)

suggestion = student_ai.suggestMajor(studentName)

print(f"{studentName}\nBased on your choices, the following courses are likely to suit your interests: ")
for major in suggestion:
    if major in courseLists:
        print(f"\n{major} : Here are some courses to discuss with your advisor along with prerequisites:")
        for course, prereq in courseLists[major].items():
            print(f"  {course}: {prereq}\n")
        print()
    else:
        print(f"\nNo course list available for {major}")







