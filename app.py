import streamlit as st
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load the Hugging Face token from .env
load_dotenv()

# Create Hugging Face client
client = InferenceClient(
    token=os.getenv("HF_TOKEN"),
    provider="auto"
)

# Page configuration
st.set_page_config(
    page_title="SwasthyaSetu",
    page_icon="🏥"
)
translations = {
    "English": {
        "title": "🏥 SwasthyaSetu",
        "subtitle": "Your Rural Healthcare Assistance Platform",
        "language": "🌐 Select your language",
        "warning": "This assistant provides general health information only. It does not diagnose diseases and does not replace a qualified healthcare professional.",
        "placeholder": "Describe your symptoms..."
    },

    "Hindi": {
        "title": "🏥 स्वास्थ्यसेतु",
        "subtitle": "ग्रामीण स्वास्थ्य सहायता प्लेटफॉर्म",
        "language": "🌐 अपनी भाषा चुनें",
        "warning": "यह सहायक केवल सामान्य स्वास्थ्य जानकारी देता है। यह बीमारी का निदान नहीं करता और डॉक्टर का विकल्प नहीं है।",
        "placeholder": "अपने लक्षण बताएं..."
    },

    "Telugu": {
        "title": "🏥 స్వాస్థ్యసేతు",
        "subtitle": "గ్రామీణ ఆరోగ్య సహాయ వేదిక",
        "language": "🌐 మీ భాషను ఎంచుకోండి",
        "warning": "ఈ సహాయకుడు సాధారణ ఆరోగ్య సమాచారాన్ని మాత్రమే అందిస్తుంది. ఇది వ్యాధులను నిర్ధారించదు మరియు వైద్యుడికి ప్రత్యామ్నాయం కాదు.",
        "placeholder": "మీ లక్షణాలను వివరించండి..."
    },

    "Kannada": {
        "title": "🏥 ಸ್ವಾಸ್ಥ್ಯಸೇತು",
        "subtitle": "ಗ್ರಾಮೀಣ ಆರೋಗ್ಯ ಸಹಾಯ ವೇದಿಕೆ",
        "language": "🌐 ನಿಮ್ಮ ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "warning": "ಈ ಸಹಾಯಕವು ಸಾಮಾನ್ಯ ಆರೋಗ್ಯ ಮಾಹಿತಿಯನ್ನು ಮಾತ್ರ ನೀಡುತ್ತದೆ. ಇದು ರೋಗಗಳನ್ನು ಪತ್ತೆಹಚ್ಚುವುದಿಲ್ಲ ಮತ್ತು ವೈದ್ಯರಿಗೆ ಪರ್ಯಾಯವಲ್ಲ.",
        "placeholder": "ನಿಮ್ಮ ರೋಗಲಕ್ಷಣಗಳನ್ನು ವಿವರಿಸಿ..."
    },

    "Tamil": {
        "title": "🏥 ஸ்வாஸ்த்யசேது",
        "subtitle": "கிராமப்புற சுகாதார உதவி தளம்",
        "language": "🌐 உங்கள் மொழியைத் தேர்ந்தெடுக்கவும்",
        "warning": "இந்த உதவியாளர் பொதுவான சுகாதார தகவல்களை மட்டுமே வழங்குகிறது. இது நோய்களைக் கண்டறியாது மற்றும் மருத்துவருக்கு மாற்றாகாது.",
        "placeholder": "உங்கள் அறிகுறிகளை விவரிக்கவும்..."
    }
}
# App title
st.title("🏥 SwasthyaSetu")
st.subheader("Your Rural Healthcare Assistance Platform")
# Select language
selected_language = st.selectbox(
    translations["English"]["language"],
    list(translations.keys())
)

# Get translations for selected language
t = translations[selected_language]

# App UI
st.title(t["title"])
st.subheader(t["subtitle"])

# Safety warning
st.warning(t["warning"])

# Create chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input(t["placeholder"])

def check_emergency(text):
    emergency_keywords = [
        "difficulty breathing",
        "can't breathe",
        "cannot breathe",
        "severe chest pain",
        "unconscious",
        "not responding",
        "heavy bleeding",
        "severe bleeding",
        "stroke",
        "seizure"
    ]

    text = text.lower()

    for keyword in emergency_keywords:
        if keyword in text:
            return True

    return False

if user_input:
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    if check_emergency(user_input):

      emergency_messages = {
        "English": "⚠️ Your symptoms may require urgent medical attention. Please contact a qualified healthcare professional or emergency service immediately.",
        "Hindi": "⚠️ आपके लक्षणों के लिए तुरंत चिकित्सा सहायता की आवश्यकता हो सकती है। कृपया तुरंत किसी योग्य स्वास्थ्य पेशेवर या आपातकालीन सेवा से संपर्क करें।",
        "Telugu": "⚠️ మీ లక్షణాలకు తక్షణ వైద్య సహాయం అవసరం కావచ్చు. దయచేసి వెంటనే అర్హత కలిగిన ఆరోగ్య నిపుణుడిని లేదా అత్యవసర సేవలను సంప్రదించండి.",
        "Kannada": "⚠️ ನಿಮ್ಮ ರೋಗಲಕ್ಷಣಗಳಿಗೆ ತುರ್ತು ವೈದ್ಯಕೀಯ ಸಹಾಯ ಬೇಕಾಗಬಹುದು. ದಯವಿಟ್ಟು ತಕ್ಷಣ ಅರ್ಹ ಆರೋಗ್ಯ ವೃತ್ತಿಪರರನ್ನು ಅಥವಾ ತುರ್ತು ಸೇವೆಯನ್ನು ಸಂಪರ್ಕಿಸಿ.",
        "Tamil": "⚠️ உங்கள் அறிகுறிகளுக்கு உடனடி மருத்துவ உதவி தேவைப்படலாம். தயவுசெய்து உடனடியாக தகுதியான சுகாதார நிபுணரை அல்லது அவசர சேவையை தொடர்பு கொள்ளுங்கள்."
    }

    ai_response = emergency_messages.get(
        selected_language,
        emergency_messages["English"]
    )

else:
    # Your existing Hugging Face AI code

    # Instructions for the AI
    system_prompt = f"""

You are SwasthyaSetu, an AI assistant that helps collect health symptoms
and provides general health information.

IMPORTANT: You are NOT a doctor and must not diagnose diseases.

Your primary task is to understand the user's symptoms and collect relevant
information BEFORE giving general advice.

CONVERSATION RULES:

1. First identify the main symptom.

2. If the user mentions a symptom but does not provide enough information,
ask ONE relevant follow-up question.

3. For example, if the user says "I have fever", first ask about duration,
such as:
"How long have you had the fever?"

4. Do NOT immediately recommend random home remedies, foods, drinks,
medicines, or treatments.

5. Do NOT recommend coconut water, herbal remedies, or specific medication
unless the information is part of approved, trusted medical guidance.

6. Do NOT immediately tell every user to visit a doctor.

7. Ask about important warning signs when relevant.

8. If the user describes potentially serious warning signs, such as severe
difficulty breathing, unconsciousness, severe chest pain, or other obvious
emergencies, clearly advise immediate emergency medical help.

9. Ask only ONE question at a time.

10. Use simple language and respond in the user's selected language.

EXAMPLE:

User: I have fever
Assistant: I'm sorry you're feeling unwell. How long have you had the fever?

User: 3 days
Assistant: Have you measured your temperature? If yes, what was the highest temperature?

Do not invent medical facts. Keep responses focused on symptom collection.

The user's selected language is: {selected_language}

IMPORTANT RULES:
- Always reply in the selected language.
- Use very simple language that rural users can understand.
- Do not diagnose diseases.
- Do not pretend to be a doctor.
- Ask one relevant question at a time.
- Do not give random home remedies or medicines.
- Do not immediately tell every user to visit a doctor.
- If the symptoms could indicate an emergency, clearly advise the user to seek immediate medical help.
- Do not invent medical facts.

If the user gives a symptom but there is not enough information,
ask one useful follow-up question before giving advice.

For example:
If the user says "I have fever", ask:
"How long have you had the fever?"

Keep your response short and easy to understand.
"""


    try:
        # Send message to Hugging Face model
        recent_messages =st.session_state.messages[-10:]

        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3-0324",
            messages=[
                {"role": "system", "content": system_prompt},
                *recent_messages
            ],
            max_tokens=150
        )

        # Get AI response
        ai_response = response.choices[0].message.content

    except Exception as e:
        ai_response = f"Error connecting to AI: {str(e)}"

    # Save AI response
    st.session_state.messages.append(
        {"role": "assistant", "content": ai_response}
    )

    # Display AI response
    with st.chat_message("assistant"):
        st.write(ai_response) 