import numpy as np
import streamlit as st
import pickle

#Import model
model=pickle.load(open(r"C:\Users\CORONA\Desktop\Deployment\Financial_Inclusion.pkl","rb"))

country_mapping = {
    'Kenya': 0, 
    'Rwanda': 1, 
    'Tanzania': 2,
    'Uganda': 3
    }

education_mapping ={
    'Secondary education': 3,
    'No formal education': 0,
    'Vocational/Specialised training': 5,
    'Primary education': 2,
    'Tertiary education': 4, 
    'Other/Dont know/RTA': 1
    }

job_mapping={
    'Self employed': 9 ,
    'Government Dependent': 4,
    'Formally employed Private': 3,
    'Informally employed': 5 ,
    'Formally employed Government': 2, 
    'Farming and Fishing': 1,
    'Remittance Dependent': 8, 
    'Other Income': 7,
    'Dont Know/Refuse to answer': 0,
    'No Income': 6
    }


def financial_inclusion(user_input):
    #convert data into an array
    input_array = np.asarray(user_input)

    
    #reshaped data into a two dimensional array
    reshaped_array = input_array.reshape(1, -1)

    #getting predicction
    prediction =model.predict(reshaped_array)
    if prediction==0:
        return"No,wont have a bank account"
    else:
        return"Yes,will have a bank account"
    


def main():
    st.title("Financial Inclusion in Africa Web App")

    country = st.selectbox("Select Country:", list(country_mapping.keys()))
    encoded_country = country_mapping[country]
    location_type=st.text_input("Location: Rural :0, Urban:1")
    cellphone_access=st.text_input("Access to a cellphone: Yes:1, No:0")
    age=st.text_input("Age")
    gender=st.text_input("Gender: Male:0, Female:1")
    education_level = st.selectbox("Select Education Level:", list(education_mapping.keys()))
    encoded_education = education_mapping[education_level]
    job_type = st.selectbox("Select Job Category:", list(job_mapping.keys()))
    encoded_job_type = job_mapping[job_type]

    performance=""
    
    if st.button("Predict"):

        prediction = financial_inclusion([(encoded_country), int(location_type), int(age), (encoded_education), (encoded_job_type), int(cellphone_access), int(gender)])
        st.success(prediction)


if  __name__== "__main__":
    main()    

