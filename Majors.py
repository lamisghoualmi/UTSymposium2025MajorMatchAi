import pandas as pd

# Data: List of programs
data = {
    'Program': [
        'Research and experimental psychology',
        'Logistics, materials, and supply chain management',
        'Biology/biological sciences',
        'Registered nursing/registered nurse',
        'Marketing/marketing management',
        'Kinesiology and exercise science',
        'Finance',
        'Business statistics',
        'Mechanical engineering',
        'Political science and government',
        'Speech communication and rhetoric',
        'Sport and fitness administration/management',
        'English language and literature',
        'Neuroscience',
        'Business administration and management',
        'Animal sciences',
        'Sociology',
        'Multi-/interdisciplinary studies',
        'Accounting',
        'Human development and family studies',
        'Journalism',
        'Computer science',
        'Public relations/image management',
        'Audiology/audiologist and speech-language pathology/pathologist',
        'Architecture',
        'Social work',
        'Civil engineering',
        'History',
        'Chemical engineering',
        'Bioengineering and biomedical engineering',
        'Anthropology',
        'Foreign languages and literatures',
        'Wildlife, fish and wildlands science and management',
        'Aerospace, aeronautical and astronautical/space engineering',
        'Mathematics',
        'Advertising',
        'Electrical and electronics engineering',
        'Construction management',
        'Industrial engineering',
        'Nuclear engineering',
        'Economics',
        'Music',
        'Human resources management/personnel administration',
        'Chemistry',
        'Plant sciences',
        'Hospitality administration/management',
        'Interior architecture',
        'Consumer economics',
        'Business/managerial economics',
        'Statistics',
        'Food science',
        'Geology/earth science',
        'Fine/studio arts',
        'Forestry',
        'Soil chemistry and physics',
        'Geography',
        'Materials engineering',
        'Physics',
        'Special education and teaching',
        'Computer engineering',
        'Nutrition sciences',
        'Philosophy',
        'Agricultural business and management',
        'Graphic design',
        'Drama and dramatics/theatre arts',
        'Sustainability studies',
        'Classics and classical languages, literatures, and linguistics',
        'Agricultural and extension education services',
        'Information science/studies',
        'Public administration',
        'Agricultural engineering',
        'Religion/religious studies',
        'International/global studies',
        'Art history, criticism and conservation',
        'Natural resource economics',
        'Film/cinema/video studies',
        'Clinical laboratory science/medical technology/technologist'
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)
# Replace `your_dataframe` with the name of your dataframe
df.to_csv(r"C:\Users\lghoualm\OneDrive - University of Tennessee\Desktop\Tech meetings -Conferences\UT Symposium - Jan 2025\Majors.csv", index=False)

# Display the DataFrame
print(df)


# Replace 'your_filepath.csv' with the path to your CSV file
df = pd.read_csv(r"C:\Users\lghoualm\OneDrive - University of Tennessee\Desktop\Tech meetings -Conferences\UT Symposium - Jan 2025\Majors.csv", index_col=None)



# Display data without index
print(df.to_string(index=False))
