import streamlit as st
from fastbook import load_learner
import gdown

url = 'https://drive.google.com/uc?id=1-5UNAwm2ZdMc-Vm0sPmoqwvgx30EdrrR'
output = 'export.pkl'
gdown.download(url, output, quiet=False)


#For Windows users

#import pathlib
#temp = pathlib.PosixPath
#pathlib.PosixPath = pathlib.WindowsPath

learn=load_learner("export.pkl")

def main():
    
    # ===================== Set page config and background =======================
    # Main panel setup
    # Set website details
    st.set_page_config(page_title ="Emmanuel's Spam Checker Demo", 
                       page_icon=':desktop_computer:', 
                       layout='centered')
    """## Emmanuel's Spam Checker Demo"""

    with st.expander("About"):
        st.write("This App is a basic demo of Artificial Intelligence for Automatic Spam detection in messages. In building this, we leverage deep learning (NLP) techniques, specifically the ULMfit Method introduced by the Facebook AI research Lab in the paper [here](https://arxiv.org/abs/1801.06146)")

    with st.expander("Settings"):
        model_option = st.selectbox('Kindly select preferred model',('ULMFiT',))
        # I used a slider to set-up an adjustable threshold
        demo = st.selectbox('Use Demo Texts',('None', 'Demo 1','Demo 2', 'Demo 3', 'Demo 4'))

    if demo == "Demo 1":
      demo_text = 'A redacted loan for 950,000 Naira is approved for you if you receive this SMS. 1 min verification & cash in 1 hr at www.emmamoney.com.ng to opt out reply stop'
    elif demo == "Demo 2":  
      demo_text = "There is an assignment that must be submitted tommorow in class, the lecturer will give 0 scores to those that do not do the assignment or attend the class"
    elif demo == "Demo 3":  
      demo_text = "Due to a new legislation by the Nigerian government, those struggling with debt can now apply to have it written off. For more information text the word INFO or to opt out text STOP"
    elif demo == "Demo 4":  
      demo_text = "Good day secretary, kindly schedule an interview for Emma today. he has to be employed effective immediately if she meets all our requirements"
    else:
      demo_text = ""

    with st.form(key = 'form1', clear_on_submit=False):
        Job_description1 = st.text_area("", value=demo_text)
        submit_button = st.form_submit_button(label="Check Message")

    if submit_button:
        st.success("I'm processing your request......")
        prediction = learn.predict(Job_description1)
        if prediction[0] == 'spam':
            st.warning("This is a spam message, I am {} percent sure about this".format(round(float(max(prediction[-1])),2)*100))
        elif prediction[0] == 'ham':
            st.success("This message is safe, I am {} percent sure about this".format(round(float(max(prediction[-1])),2)*100))

if __name__ == "__main__":
    main()
