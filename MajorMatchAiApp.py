
#cd C:\Users\lghoualm\OneDrive - University of Tennessee\Desktop\Tech meetings -Conferences\MajorMatchAiApp
# streamlit run MajorMatchAiApp.py

import openai
import pandas as pd
import streamlit as st
import os



# Load OpenAI API key from secrets file
os.environ['OPENAI_API_KEY'] = st.secrets['pass']
openai.api_key = os.environ['OPENAI_API_KEY']
#openai.api_key = st.secrets["pass"]



#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
st.sidebar.image("MyLogo.png")
st.sidebar.write("""
         ######  This application, developed in Python, utilizes Streamlit and OpenAI APIs to assist incoming freshmen at the University of Tennessee in selecting a major that aligns with their strengths, preferences, and career aspirations. By evaluating their comfort levels in subjects such as math, science, and arts, as well as their preferred work environments, the app generates personalized major recommendations and career insights, tailored to the available majors at UT.

         """)
st.sidebar.write("""
         ######  Created by Lamis Ghoualmi
         """)

st.sidebar.write("""
         ######   [Github](https://github.com/lamisghoualmi)
                  """)

st.sidebar.write("""
         ######  [Linkedin](https://www.linkedin.com/in/lamisghoualmi/)
                  """)

# Display the header

st.title('Major Match using AI')
st.markdown("<h3 style='font-size:18px; color:#FF8200;'> Discovering Your Path: Tailored Major Recommendations for University of Tennessee Freshmen Using AI", unsafe_allow_html=True)
st.text('App developped for the UT IT Symposium 2025.')

# Add some space between the title and the content
st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)  # Adds 3 line breaks

#----------------------------------------------------------------------------------------




# Define AI function to interact with GPT
def AI(message, question):
    messages = [
        {
            "role": "system",
            "content": question
        }
    ]

    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        
        chat = openai.ChatCompletion.create(
            model="gpt-4",#"gpt-3.5-turbo", 
            messages=messages,  
            temperature=0.5, 
            max_tokens=1000, 
            top_p=0.9
        )
        
        reply = chat.choices[0].message["content"]
        return reply



#_______________________________________GUI_______________________________________________

st.markdown("<h3 style='font-size:18px;'>Question 1: What is your GPA?</h3>", unsafe_allow_html=True)
gpa = st.slider('Rate your GPA on a scale from 0 to 4.0, where 0 means the lowest and 4.0 means the highest', value=2.5, min_value=0.0, max_value=4.0, step=0.1, key="gpa")



st.markdown("<h3 style='font-size:18px;'>Question 1: Rate your comfort in Math</h3>", unsafe_allow_html=True)
comfort_math =st.slider('Rate your comfort in Math on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable', value=2,  min_value=0, max_value=10,  key="comfort_math")
#st.write('Choosen value:', comfort_math )


st.markdown("<h3 style='font-size:18px;'>Question 2: Rate your comfort in Science </h3>", unsafe_allow_html=True)
comfort_science =st.slider('Rate your comfort in Science  on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable', value=2, min_value=0, max_value=10,  key="comfort_science")
#st.write('Choosen value:', comfort_art )


st.markdown("<h3 style='font-size:18px;'>Question 3: Rate your comfort in Geography  </h3>", unsafe_allow_html=True)
comfort_geography =st.slider('Rate your comfort in Geography  on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable', value=2, min_value=0, max_value=10,  key="comfort_geography")
#st.write('Choosen value:', comfort_art )

st.markdown("<h3 style='font-size:18px;'>Question 4: Rate your comfort in Physics </h3>", unsafe_allow_html=True)
comfort_physics =st.slider('Rate your comfort in Physics  on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable', value=2, min_value=0, max_value=10,  key="comfort_physics")


st.markdown("<h3 style='font-size:18px;'>Question 5: Rate your comfort in Technology</h3>", unsafe_allow_html=True)
interest_in_technology =st.slider('Rate your comfort in Technology  on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable',  value=2,min_value=0, max_value=10 ,  key="interest_in_technology")

st.markdown("<h3 style='font-size:18px;'>Question 6: Rate your comfort in Art </h3>", unsafe_allow_html=True)
interest_in_arts =st.slider('Rate your comfort in Art  on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable',  value=2,min_value=0, max_value=10 ,  key="interest_in_arts")

st.markdown("<h3 style='font-size:18px;'>Question 7: Rate your comfort in Social Sciences </h3>", unsafe_allow_html=True)
interest_in_social_sciences =st.slider('Rate your comfort in Social Sciences  on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable', value=2, min_value=0, max_value=10 ,  key="interest_in_social_sciences")

st.markdown("<h3 style='font-size:18px;'>Question 8: Rate your comfort in Healthcare </h3>", unsafe_allow_html=True)
interest_in_healthcare =st.slider('Rate your comfort in Healthcare  on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable', value=2, min_value=0, max_value=10,  key="interest_in_healthcare")

st.markdown("<h3 style='font-size:18px;'>Question 9: Rate your comfort in Business Management </h3>", unsafe_allow_html=True)
interest_in_business_management  =st.slider('Rate your comfort in Business Management   on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable',  value=2, min_value=0, max_value=10,  key="interest_in_business_management")


st.markdown("<h3 style='font-size:18px;'>Question 10: Rate your comfort in Engineering</h3>", unsafe_allow_html=True)
interest_in_engineering  =st.slider('Rate your comfort in Engineering   on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable', value=2, min_value=0, max_value=10,  key="interest_in_engineering ")

st.markdown("<h3 style='font-size:18px;'>Question 11: Rate your comfort in environmental issues</h3>", unsafe_allow_html=True)
interest_in_environmental_issues  =st.slider('Rate your comfort in environmental issues on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable', value=2, min_value=0, max_value=10,  key="interest_in_environmental_issues")

st.markdown("<h3 style='font-size:18px;'>Question 12: Rate your  communication skills </h3>", unsafe_allow_html=True)
communication_skills  =st.slider('Rate your communication skills  on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable', value=2, min_value=0, max_value=10,  key="communication_skills")

st.markdown("<h3 style='font-size:18px;'>Question 13: Rate your analytical skills </h3>", unsafe_allow_html=True)
analytical_skills  =st.slider('Rate your  analytical_skills  on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable', value=2, min_value=0, max_value=10,  key="analytical_skills ")

st.markdown("<h3 style='font-size:18px;'>Question 14: Rate your creativity </h3>", unsafe_allow_html=True)
creativity   =st.slider('Rate your  creativity   on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable',  value=2, min_value=0, max_value=10,  key="creativity")

st.markdown("<h3 style='font-size:18px;'>Question 15: Rate your  interest in research  solving  problem </h3>", unsafe_allow_html=True)
interest_in_problem_solving_research   =st.slider('Rate your  interest in research  solving  problem    on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable', value=2, min_value=0, max_value=10,  key="interest_in_problem_solving_research")

st.markdown("<h3 style='font-size:18px;'>Question 16: Rate your  interest in entrepreneurship </h3>", unsafe_allow_html=True)
interest_in_entrepreneurship  =st.slider('Rate your  interest in entrepreneurship on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable',  value=2, min_value=0, max_value=10,  key="interest_in_entrepreneurship")

st.markdown("<h3 style='font-size:18px;'>Question 17: Rate your  interest in hands on jobs </h3>", unsafe_allow_html=True)
prefers_hands_on_jobs =st.slider('Rate your  interest in  hands on jobs  on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable', value=2, min_value=0, max_value=10,  key="prefers_hands_on_jobs")

st.markdown("<h3 style='font-size:18px;'>Question 18: Rate your  interest in office based jobs </h3>", unsafe_allow_html=True)
prefers_office_based_jobs =st.slider('Rate your  interest in hands on jobs  on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable',  value=2, min_value=0, max_value=10,  key="prefers_office_based_jobs")

st.markdown("<h3 style='font-size:18px;'>Question 19: Rate your  interest in Working from Home </h3>", unsafe_allow_html=True)
prefers_working_from_home=st.slider('Rate your  interest in  Working from Home on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable', value=2, min_value=0, max_value=10,  key="prefers_working_from_home")


st.markdown("<h3 style='font-size:18px;'>Question 20: Rate your  interest in interacting with people </h3>", unsafe_allow_html=True)
interaction_level_with_people =st.slider('Rate your interest in interacting with people on a scale from 1 to 10, where 1 means least comfortable and 10 means very comfortable',  value=2, min_value=0, max_value=10,  key="interaction_level_with_people")




if st.button('Discover Your Path!'):
        # Output message
    message = f"""
    A freshman student has provided the following information for advising:
    - Comfort with Math (0-4): {gpa}
    - Comfort with Math (1-10): {comfort_math}
    - Comfort with Science (1-10): {comfort_science}
    - Comfort with Geography (1-10): {comfort_geography}
    - Comfort with Physics (1-10): {comfort_physics}

    - Interest in Technology (1-10): {interest_in_technology}
    - Interest in Arts (1-10): {interest_in_arts}
    - Interest in Social Sciences (1-10): {interest_in_social_sciences}
    - Interest in Healthcare (1-10): {interest_in_healthcare}
    - Interest in Business/Management (1-10): {interest_in_business_management}
    - Interest in Engineering (1-10): {interest_in_engineering}
    - Interest in Environmental Issues (1-10): {interest_in_environmental_issues}

    - Communication and Presentation skills (1-10): {communication_skills}
    - Analytical skills (1-10): {analytical_skills}
    - Creativity (1-10): {creativity}
    - Passion for problem-solving or research (1-10): {interest_in_problem_solving_research}
    - Interest in entrepreneurial ventures or self-employment (1-10): {interest_in_entrepreneurship}

    - Preference for hands-on or physical jobs (1-10): {prefers_hands_on_jobs}
    - Preference for office-based jobs (1-10): {prefers_office_based_jobs}
    - Preference for working from home (1-10): {prefers_working_from_home}
    - Interaction level with people (1-10): {interaction_level_with_people}
    """

    #___________ STEP 01: recommended majors

    question = "Based on the information provided,  including  your  GPA (on a scale from 0.0 to 4.0, where 0 represents the lowest performance and 4.0 represents the highest achievement) and comfort in Math, Science, Geography, Physics, and other factors (where 1 indicates low comfort/interest and 10 indicates high comfort/interest),  recommend at least five suitable college majors for the student, ordered from most suitable to least suitable."
    response = AI(message, question)

    #_____________ STEP 02: available  recommended programs at UT based on the recommended majors
    question = "Extract only the major names please."
    Recommended_Majors = AI(response, question)
    print('Major names')
    print(Recommended_Majors)

    # Load UT programs data
    df = pd.read_csv(r"Majors.csv", index_col=None)
    ListOfprograms = df.to_string(index=False)


    question = f"Based on the available list of programs: {ListOfprograms}, recommend the most suitable programs from this list that align closely with the previously recommended majors: {Recommended_Majors}."

    #
    ProgramsRecommended = AI(response, question)

    # Print the output
    print('Programs Recommended:')
    print(ProgramsRecommended)

    #_____________ STEP 03: Recommended jobs and career path
    st.markdown("<h3 style='font-size:18px; color:#FF8200;'> Recommended Majors </h3>", unsafe_allow_html=True)     
    st.write(response)

    st.markdown("<h3 style='font-size:18px; color:#FF8200;'> List of Programs Available at the University of Tennessee for the Recommended Majors </h3>", unsafe_allow_html=True)   
    st.write(ProgramsRecommended)

    #_____________ STEP 04: List of suitable jobs:
    st.markdown("<h3 style='font-size:18px; color:#FF8200;'>Recommended Jobs That a Student Could Pursue After Completing One of These Programs</h3>", unsafe_allow_html=True) 
    question = f"Based on the recommended list of programs: {ProgramsRecommended}, suggest at least 10 potential career paths or job roles that a student could pursue after completing these programs, to help guide their future career choices."
    RecommendedJobs = AI(ProgramsRecommended ,   question)
    st.write(RecommendedJobs )
        







 
