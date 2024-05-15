import streamlit as st
import pickle
import base64

# Load the trained model
with open('model1.pkl', 'rb') as f:
    model = pickle.load(f)

# Function to convert an image to base64
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Convert image to base64
img = get_img_as_base64("imagee.jpg")

# CSS styling for background image and other elements
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://cdn.pixabay.com/photo/2016/11/19/16/52/dawn-1840298_1280.jpg");
    background-size: cover;  /* Ensure the background image covers the entire container */
    background-position: top right;  /* Adjust background image position */
    background-repeat: no-repeat;  /* Do not repeat the background image */
    background-attachment: fixed;  /* Fix the background image so it doesn't scroll with the content */
}}
[data-testid="stHeader"] {{
    background-color: transparent;  /* Make the header background transparent */
}}
[data-testid="stToolbar"] {{
    right: 2rem;  /* Position the toolbar to the right */
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Streamlit UI
st.title('Graduate Admission Prediction')

# Input fields
gre_score = st.number_input('GRE Score', min_value=260, max_value=340, value=300, step=1)
toefl_score = st.number_input('TOEFL Score', min_value=0, max_value=120, value=100, step=1)
university_rating = st.number_input('University Rating', min_value=1, max_value=5, value=3, step=1)
sop = st.number_input('Statement of Purpose (SOP)', min_value=0.0, max_value=5.0, value=3.0, step=0.5)
lor = st.number_input('Letter of Recommendation (LOR)', min_value=0.0, max_value=5.0, value=3.0, step=0.5)
cgpa = st.number_input('CGPA', min_value=0.0, max_value=10.0, value=7.5, step=0.1)
research = st.number_input('Research Experience (0 for No, 1 for Yes)', min_value=0, max_value=1, value=0)

# Prediction button
if st.button('Predict Admission Chance'):
    # Ensure that the model is fitted before making predictions
    prediction = model.predict([[gre_score, toefl_score, university_rating, sop, lor, cgpa, research]])
    st.markdown(f'<div style="background-color:#FFFFFF; padding: 10px; border-radius: 5px;">Chance of Admission: {prediction[0]:.2%}</div>', unsafe_allow_html=True)
