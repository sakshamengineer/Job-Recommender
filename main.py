import streamlit as st
from Dataset.Assets.masterskills import MASTER_SKILLS
from models import predict_job_role,predict_salary
from Models.Assets.Role_columns import ROLE_COLUMNS
from Models.Assets.RequiredJobSkills import JOB_ROLE_SKILLS
from APICALL import Generate_Roadmap
from ResumeParsing import parse_resume

def reset_prediction_state():
    st.session_state.predicted_roles = None
    st.session_state.roadmap = None
    st.session_state.selected_role = None

def encode_skills(skills):
    for i in range(len(skills)):
        skills[i] = skills[i].lower()
    skill_enc = [1 if skill.lower() in skills else 0 for skill in MASTER_SKILLS]
    return skill_enc

if "predicted_roles" not in st.session_state:
    st.session_state.predicted_roles = None

def skillgap(cur_skills , required_skills):
    result = [x for x in required_skills if x not in cur_skills]
    per = 1 - (len(result)/len(required_skills))
    return result,per

st.title("RESUME BASED JOB RECOMMENDER")
st.subheader("Upload Your Resume or Enter Inputs Manually")

choice = st.radio("Choose An Option",["Upload Resume", "Choose Manual Inputs"],on_change=reset_prediction_state)

predict_disabled = choice == "Upload Resume"

role_input = []
salary_input = []
Experience = 0

if choice == "Upload Resume":
    pdf = st.file_uploader("Upload Your Resume",["pdf","docx"])
    if pdf is not None:
        predict_disabled = False
        data = parse_resume(pdf)
        skills = data["skills"]
        skill_enc = encode_skills(skills)
        Experience = data["experience"]
        role_input.append(skill_enc)
    else:
        predict_disabled = True
else :
    skills = st.multiselect("Select an Skills",options = MASTER_SKILLS,accept_new_options=True)
    skill_enc = encode_skills(skills)

    Education = st.multiselect("Enter Your Education ",["BA","Btech","Bsc","BCA"],accept_new_options=True)
    Experience = st.slider("Select your Experience",min_value=0,max_value = 40,value=0)
    role_input.append(skill_enc)


if st.button("Predict",disabled=predict_disabled):
    if role_input:
        st.session_state.predicted_roles = predict_job_role(role_input)

if st.session_state.predicted_roles:
    predict = st.session_state.predicted_roles

    exp_sal = []
    for i in predict:
        role_enc = [1 if i == role else 0 for role in ROLE_COLUMNS]
        role_enc.append(Experience)
        exp_sal.append(predict_salary(role_enc))

    output = list(zip(predict,exp_sal))
    output.sort(key = lambda x : x[1] , reverse=True)
    
    bestmatch = ""
    bestpercent = 0

    for role,salary in output:
        prettyrole = role.replace("_"," ").capitalize()
        st.markdown(f"### {prettyrole}")
        st.markdown(f"#### Expected Salary : {salary[0]}")
        skill_gap,percent = skillgap(skills,JOB_ROLE_SKILLS[role])
        st.text(f"Your Skill Gap : {', '.join(skill_gap)}")
        st.caption(f"Match Percentage : {round(percent*100,2)}%")
        st.progress(percent)
        if bestpercent < percent:
            bestpercent = percent
            bestmatch = prettyrole

    st.subheader(f"Best Match According to Your Skills is {bestmatch}")

    selection = st.selectbox("Select a Job For Roadmap",["Select An Option"] + predict)
    if selection != "Select An Option":
        with st.spinner("Generating roadmap..."):
            roadmap = Generate_Roadmap(selection)
            if roadmap:
                st.markdown(roadmap)
            else:
                st.error("Roadmap generation failed.")