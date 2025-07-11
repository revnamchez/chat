import random
import streamlit as st


responses = {
            "svr": ["Has the symptom persisted for over 24 hours?"],
            "mld": ["Has the symptom persisted for over 24 hours?"],
            "beta": ["You may need some rest while you monitor the situation. ok? (Type ok)"],
            "sam": ["Watch it for some more hours, if it continues, please consult your doctor. ok? (Type ok)"],
            "wos": ["You really need urgent medical attention. See your doctor. ok? (Type ok)"],
            "affirm": ["Up till now, do you feel (Type: 'better', 'same' or 'worse')"],
            "naffirm": ["Please avoid self medication. See your doctor if it persists after 24 hours. ok? (Type ok)"],
            "often": ["How often do you fall sick? (Type: 'rarely', 'occasionally' or 'frequently')"],
            "rare": ["You seems to have a strong immune system. Wait and observe, but seek medical attention if symptoms persists after 48 hours. Thanks."],
            "ocassion": ["You seems to have an average immune system. Avoid stress, and seek medical attention if symptoms persists after 24 hours. Thanks."],
            "freq": ["Your immune system is probably weak. Please see your doctor at once. Thanks."],
            "semi": ["You are welcome. Take care of yourself and goodbye."],
            "end": ["🤖👋👋👋"]
        }
    
        #Keywords
keywords = {
            "svr": ["severe"],
            "mld": ["mild"],
            "beta": ["better"],
            "sam": ["same"],
            "wos": ["worse"],
            "affirm": ["yes"],
            "naffirm": ["no"],
            "often": ["ok", 'okay'],
            "rare": ["rarely"],
            "ocassion": ["occasionally"],
            "freq": ["frequently"],
            "semi": ["thanks", "thank you"],
            "end": ["goodbye", "bye"]
        }


def get_response(user_input):
    user_input = user_input.lower()
        
    for intent, keys in keywords.items():
        for key in keys:
            if key in user_input:
                if intent == "end":
                    return responses[intent][0] + " " + ""
                else:
                    return random.choice(responses[intent])
        
    return "Please type in lower case and follow my simple response guide."
    


# Frontend
def main():
        st.subheader("Get Advice - Mini ChatBot 🤖")
        st.write("Rate your Symptom (type: mild or severe)")
    
        user_input = st.text_input("type in small letters. (Type goodbye to exit):")
        
        if user_input:
            response = get_response(user_input)
            st.write("ChatBot:", response)
        

# Run the app
if __name__ == "__main__":
        main()


st.markdown(
            """ 
            --- 
            *Important Disclaimer:* 
            This is an AI-based prediction tool for educational purposes only. 
            Please consult with a qualified healthcare professional for proper medical diagnosis and treatment. 
            """
    )

