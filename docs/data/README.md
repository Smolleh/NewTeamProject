# Dataset Overview
The dataset consists of AI failure cases which is used to populate our AI Failures Museum. 
It consists of exhibits which represent examples of AI failures, and sub-tables (AI_system_description,contributing_factors,lessons_learned,failure_description).  

The data is manually curated and added to the museum for educational purposes. 
The dataset is stored on db.sqlite3 - functional information relating to the museum's products/exhibits is stored in the entities described in the Data Model section. The SQLite Viewer extension is recommended/needed to view the database. We have 20 exhibits and 20 supporting artefacts. We have over 40 quizz questions each linked to varying exhibits as well as 5 different failure categories. 
Images relating to the artefacts are not stored in the sqlite database instead in the media file, configured and setup using standard django protocols. All data is seeded and stored locally in the database and is not generated/retrieved from any external sources at runtime.

# Adding New Exhibits
To add a new exhibit: The user must be a curator, on the curator dashboard there is a button that lets the user create a new exhibit and let them fill out key information related to the exhibit that is stored in the exhibit entity. From there going back to the curator dashboard the in-depth information about the exhibit (contributing factor etc.) and the artefacts can be created and edited.  


# Data Model
Link to UML diagram of the database 
https://lucid.app/lucidchart/9d295542-13b3-46d1-b445-6ed1b5858a51/edit?viewport_loc=-725%2C-348%2C1758%2C1465%2C0_0&invitationId=inv_e5671f90-a690-4788-b6ee-570c73ae2f5f - Jimi Mandeville 

The entities: 
- Exhibit: is used to represent the exhibits stored in the museum
    Attributes: 
    exhibitId - the primary key
    title - name/title will describe/summarise the exhibit and is what users will be able to see when searching for an exhibit
    domain - area of interest the exhibit belongs to, it also refers to the failure category.
    backgroundDeploymentContext - extra information about the exhibit that may provide the necessary context/information in regard to the failure
    intendedUse - information about what the AI was originally intended to be used for
    viewNumber - analytical data only accessible to curators

- Artefact: represents the evidence that an exhibit entry would be based on 
    Attributes:
        artefactId - the primary key
        exhibitId - the foreign key used to link artefacts back to the exhibit
        info - information about the artefact and may include a website link
        artefactDate - date of the artefacts creation
        artefactObjectPath - the image stored that would be shown on the website 
    Relationships: Artefact is many to one to exhibits as a single exhibit can have 0 or multiple artefacts.
- AI_system_description: represents a section of information that describes the overall system for an exhibit
    Attributes:
        systemDescriptionId - the primary key
        exhibitId - foreign key to exhibit 
        systemDescription
        systemPurpose
        systemOutputs 
- failure_description: represents a section of information that describes the failure of AI for an exhibit
    Attributes:
        failureDescriptionId - primary key
        exhibitId- foreign key to exhibit
        whatWentWrong
        howItWasDetected
        whatWasAffected
- lessons_learned: represents a section of information that describes what not to do in the future for an exhibit 
    Attributes:
        lessonsLearnedId - primary key
        exhibitId - foreign key to exhibit
        practicalRecommendations
        futureWarnings
- contributing_factors: represents a section of information that describes what key factors led to the AI failure for an exhibit 
    Attributes:
        contributingFactorsId - primary key
        exhibitId - foreign key to exhibit
        dataIssues 
        designChoices
        organisationalOrGovernanceIssues
The previous 4 entities are used to store additional, more in-depth/specific information about exhibits. The relationships between these entities and Exhibit is one to one as they are an extension of exhibit.

- book_marks: used to link exhibits and users so that users can keep track of exhibits they have viewed and chosen to bookmark
    Attributes:
        userId - primary key and foreign key to users
        exhibitId - primary key and foreign key to exhibit 
    Relationships: book_marks is many to one to users and exhibits 

- comments: is used to allow users to add comments/messages to exhibits expressing their opinions about an exhibit. Comments have to be approved by curators before they can be added.
    Attributes:
        commentId - primary key
        content - the message the user wrote 
        isApproved - whether or not the comment has been approved
        exhibitId - foreign key to link to an exhibit
        userId - foreign key to link to the user
    Relationships: is many to one to users and exhibits 


- quiz: represents the quiz for each exhibit 
- question: represents each individual question in the quiz 
- answer: represents an answer to each question 
- result: used to represent a quiz attempt by a user
- userAchievements: used to represent a users total amount of points gained (from doing quizzes) and the users badge 


# Passport Schema
- Product: Each exhibit represents the main product being examined and the AI_system_description entity is where the information about the AI system is stored. 

- Nodes: The contributing elements within the system include the contributing_factors entity which holds the key, related components
that motivated the AI-failures occurrence. 

- Stages: The stages of the AI system lifecycle are illustrated in the ai_system_description and failure_description entities which outline the development, deployment and failure occurrence for the exhibit. 

- Evidence: Entities such as artefacts,lessons_learned is where evidence is implemented. 

Also, the quiz, question, answer, result entities further support interactive evidence-based learning and reinforce the engagement needed with this topic to reflect and understand. 

