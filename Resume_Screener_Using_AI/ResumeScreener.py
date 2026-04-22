import PyPDF2
# Import re(regular expression) library for text cleaning using patterns
import re
# Import nltk library for natural language processing
import nltk
# Import English stopwords from nltk
from nltk.corpus import stopwords
#import tf-idf vectorizer from sklearn for feature extraction
from sklearn.feature_extraction.text import TfidfVectorizer
#import cosine_similarity from sklearn for calculating similarity between resumes and job descriptions
from sklearn.metrics.pairwise import cosine_similarity
#download the stopwords from nltk
nltk.download('stopwords')
# Extract text from PDF file
def extTextFromPDF(file):
    # Initialize an empty string to store the extracted text
    text = ""

    #open the pdf using the PyPDF2 library
    reader = PyPDF2.PdfReader(file)

    # Loop through each page in the PDF and extract text
    for page in reader.pages:
        # Extract text from the page
        page_text = page.extract_text()

        if page_text:
            # Append the extracted text to the overall text variable
            text = text + page_text

            text = text + "\n"  # Add a newline after each page's text
    return text



#function to clean the extracted text
def clean_text(text):
    text = text.lower()  # Convert text to lowercase

    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', ' ', text)

    # Replace special characters with space
    text = re.sub(r'[^a-zA-Z0-9+#.\s]', ' ', text)

    # Replace multiple spaces with single space
    text = re.sub(r'\s+', ' ', text).strip()

    words = text.split()  # Split text into words
    # Get English stopwords like 'is' 'the'  'and' etc and remove them from the text
    stop_words = set(stopwords.words('english'))  
    
    #keep only the words that are not in the stopwords list
    flitered_words = [word for word in words if word not in stop_words]

    #cleaned text is the filtered words joined back into a string
    cleaned_text = ' '.join(flitered_words)

    return cleaned_text

# Function to calculate match score between resume and job description
def calculateMatchScore(resume_text , job_desc):
    #create a Tfidfvectorizer object to convert text to numerical features
    vect = TfidfVectorizer(stop_words='english')

    #convert the resume text and job description into tf-idf vectors
    vectors = vect.fit_transform([resume_text, job_desc])

    #calculate the cosine similarity between the resume vector and job description vector
    similarity = cosine_similarity(vectors[0:1] , vectors[1:2])

    return similarity[0][0]

# List of important technical skills to search for
# Dictionary to normalize different skill variations
skill_keywords = {
    "python": ["python"],
    "java": ["java"],
    "c#.net": ["c#", "c#.net", "csharp"],
    "sql": ["sql", "pl/sql", "mysql", "postgresql"],
    "backend": ["backend", "backend developer", "api"],
    "automation": ["automation", "automationscript", "scripting"],
    "git": ["git"],
    "github": ["github"]
}

# Function to extract normalized skills
def extract_skills(text, skill_keywords):
    text = text.lower()
    found_skills = set()

    for standard_skill, keywords in skill_keywords.items():
        for keyword in keywords:
            if keyword in text:
                found_skills.add(standard_skill)
                break

    return found_skills

# Function to calculate skill match percentage
def calculateSkillMatch(resume_skills, job_skills):
    # If job skills list is empty, return 0
    if len(job_skills) == 0:
        return 0.0  # Avoid division by zero if job skills are empty

     # Find common skills between resume and job description
    matched_skills = resume_skills.intersection(job_skills)

    # Calculate percentage of matched skills
    match_score = (len(matched_skills) / len(job_skills)) * 100  # Convert to percentage

    return match_score

# Function to calculate final combined score
def calculateOverallMatch(tfidf_score, skill_score):

    # Convert tfidf score from decimal to percentage
    Tfidf_per = tfidf_score * 100  # Convert to percentage

    # Combine both scores with weights
    overall_score = (0.4 * Tfidf_per) + (0.6 * skill_score)
    return overall_score
def main():

    
    file = input("Enter the path to the resume PDF file: ")

    print("Paste Job Description below.")
    print("Type END on a new line when finished:\n")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
    lines.append(line)

    job_description = "\n".join(lines)
    # Extract and preprocess resume text
    try:
        resume_text = extTextFromPDF(file)
        cleaned_resume_text = clean_text(resume_text)

        # Preprocess job description
        cleaned_job_description = clean_text(job_description)

        # Calculate similarity score
        score = calculateMatchScore(cleaned_resume_text, cleaned_job_description)

        # Extract skills from resume and job description
        resume_skills = extract_skills(cleaned_resume_text, skill_keywords)
        job_skills = extract_skills(cleaned_job_description, skill_keywords)

        # Find matched and missing skills
        matched_skills = resume_skills.intersection(job_skills)
        missing_skills = job_skills.difference(resume_skills)

        # Calculate skill match score
        skill_score = calculateSkillMatch(resume_skills, job_skills)

        # Calculate final combined score
        final_score = calculateOverallMatch(score, skill_score)

        # Print results
        print("Original Resume Text:\n", resume_text)
        print("\nCleaned Resume Text:\n", cleaned_resume_text)
        print("\nMatch Score:", round(score * 100, 2), "%")
        print("\nResume Skills:", resume_skills)
        print("\nJob Description Skills:", job_skills)
        print("\nMatched Skills:", matched_skills)
        print("\nMissing Skills:", missing_skills)
        print("\nSkill Match Score:", round(skill_score, 2), "%")
        print("\nFinal Combined Score:", round(final_score, 2), "%")
    except FileNotFoundError:
        print("Error: The Resume PDF file was not found. Please check the file path and try again.")
    except Exception as e:
        print("An error occurred:", str(e))



if __name__ == "__main__":
    main()