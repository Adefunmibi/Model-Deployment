import numpy as np
import pickle
import streamlit as st

#Loading the model
model=pickle.load(open("logistic_model_1.pkl", "rb"))

def performance_prediction(user_input):
    #convert data into array
    input_array=np.asarray(user_input)

    #reshape data intpo two dimensional array
    reshaped_array=input_array.reshape(1,-1)
    #getting prediction
    prediction=model.predict(reshaped_array)

    if prediction==0:
        return("This student did not pass")
    else:
        return("This student passed")



def main():
    st.title("Citrone Performance Web App")

    Quiz_Summary=st.text_input("Quiz Summary score")
    Assignment_summary=st.text_input("Assignment Summary score")
    Grade_point_Average=st.text_input("Learner's Grade point Average score")
    Age =st.text_input("Learner's Age")
    Children = st.text_input("Does learner have children? 1 for Yes/0 for No")
    
    Completed_Nysc=st.text_input("Completed Nysc? 1 for Yes/0 for No")
    Gender=st.text_input("What's your learners gender? 1 for Male,0 for Female")

    performance=""

    if st.button("Eligibility Result"):
        performance=performance_prediction([float(Quiz_Summary), float(Assignment_summary), float(Grade_point_Average), int(Age),int(Children),int(Completed_Nysc),int(Gender)])
        st.success(performance)

if __name__ == "__main__":
    main()



              
