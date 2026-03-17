# Dataset Overview
The dataset consists of AI failure cases which is used to populate our AI Failures Museum. It consists of exhibits which represent examples of AI failures and includes the context, cause and consequence of these failures. The data is manually curated and added to the museum for educational purposes. 

# Adding New Exhibits
To add a new exhibit:


# Data Model
The main entities include: 
- Exhibits: represents the exhibits being stored in the AI museum
- Artefacts: represents the evidence that an exhibit entry would be based on
- Ai_system_description: represents a section of information that describes the overall 
system for an exhibit
- Failure_description: represents a section of information that describes the failure of AI for 
an exhibit
- Lessons_learned: represents a section of information that describes what not to do in the 
future for an exhibit 
- Contributing_factors: represents a section of information that describes what key factors 
led to the AI failure for an exhibit 
- Book_marks: used to link exhibits and users so that users can keep track of exhibits they 
have viewed and interacted with 
- quiz: represents the quiz for each exhibit 
- question: represents each individual question in the quiz 
- answer: represents an answer to each question 
- result: used to represent a quiz attempt by a user

# Passport Schema
- Product: Each exhibit represents the main product being examined and the 
ai_system_description entity is where the information about the AI system is stored. 
- Nodes: The contributing elements within the system include the contributing_factors entity 
which holds the key, related components that motivated the AI-failures occurrence. 
- Stages: The stages of the AI system lifecycle are illustrated in the ai_system_descrption and 
failure_description entities which outline the development, deployment and failure 
occurrence for the exhibit. 
- Evidence: Entities such as artefacts, lessons_learned is where evidence is implemented. 
Also, the quiz, question, answer, result entities further support interactive evidence-based 
learning and reinforce the engagement needed with this topic to reflect and understand. 

