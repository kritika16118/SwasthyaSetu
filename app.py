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
    "placeholder": "Describe your symptoms...",
    "welcome_title": "💬 How can I help you today?",
    "welcome_text": "Please describe your symptoms in simple words.",
    "welcome_note": "I'll ask a few questions to understand better.",
    "new_chat": "🆕 New Chat",
    "about": "ℹ️ About",
    "about_text": "SwasthyaSetu helps users understand their symptoms through simple questions and general health information.",
    "important": "⚠️ Important",
    "important_text": "This chatbot does not diagnose diseases. For serious or emergency symptoms, seek medical help immediately.",
    "how_it_works": "🩺 How It Works",
    "step1": "1. Describe your symptoms.",
    "step2": "2. SwasthyaSetu asks simple questions.",
    "step3": "3. The chatbot provides general health information.",
    "step4": "4. Emergency symptoms are handled with an urgent warning."
},

    "Hindi": {
    "title": "🏥 स्वास्थ्यसेतु",
    "subtitle": "ग्रामीण स्वास्थ्य सहायता प्लेटफॉर्म",
    "language": "🌐 अपनी भाषा चुनें",
    "warning": "यह सहायक केवल सामान्य स्वास्थ्य जानकारी देता है। यह बीमारी का निदान नहीं करता और डॉक्टर का विकल्प नहीं है।",
    "placeholder": "अपने लक्षण बताएं...",
    "welcome_title": "💬 आज मैं आपकी कैसे मदद कर सकता हूँ?",
    "welcome_text": "कृपया अपने लक्षणों को सरल शब्दों में बताएं।",
    "welcome_note": "मैं बेहतर समझने के लिए आपसे कुछ सवाल पूछूँगा।",
    "new_chat": "🆕 नई चैट",
    "about": "ℹ️ हमारे बारे में",
    "about_text": "स्वास्थ्यसेतु सरल सवालों और सामान्य स्वास्थ्य जानकारी के माध्यम से उपयोगकर्ताओं को अपने लक्षण समझने में मदद करता है।",
    "important": "⚠️ महत्वपूर्ण",
    "important_text": "यह चैटबॉट बीमारियों का निदान नहीं करता। गंभीर या आपातकालीन लक्षणों के लिए तुरंत चिकित्सा सहायता लें।",
    "how_it_works": "🩺 यह कैसे काम करता है",
    "step1": "1. अपने लक्षण बताएं।",
    "step2": "2. स्वास्थ्यसेतु आपसे सरल सवाल पूछता है।",
    "step3": "3. चैटबॉट सामान्य स्वास्थ्य जानकारी देता है।",
    "step4": "4. आपातकालीन लक्षणों के लिए तुरंत चेतावनी दी जाती है।"
},

    "Telugu": {
    "title": "🏥 స్వాస్థ్యసేతు",
    "subtitle": "గ్రామీణ ఆరోగ్య సహాయ వేదిక",
    "language": "🌐 మీ భాషను ఎంచుకోండి",
    "warning": "ఈ సహాయకుడు సాధారణ ఆరోగ్య సమాచారాన్ని మాత్రమే అందిస్తుంది. ఇది వ్యాధులను నిర్ధారించదు మరియు వైద్యుడికి ప్రత్యామ్నాయం కాదు.",
    "placeholder": "మీ లక్షణాలను వివరించండి...",
    "welcome_title": "💬 ఈరోజు నేను మీకు ఎలా సహాయం చేయగలను?",
    "welcome_text": "దయచేసి మీ లక్షణాలను సులభమైన పదాల్లో వివరించండి.",
    "welcome_note": "మీ సమస్యను బాగా అర్థం చేసుకోవడానికి నేను కొన్ని ప్రశ్నలు అడుగుతాను.",
    "new_chat": "🆕 కొత్త చాట్",
    "about": "ℹ️ మా గురించి",
    "about_text": "స్వాస్థ్యసేతు సులభమైన ప్రశ్నలు మరియు సాధారణ ఆరోగ్య సమాచారం ద్వారా మీ లక్షణాలను అర్థం చేసుకోవడానికి సహాయపడుతుంది.",
    "important": "⚠️ ముఖ్యమైన సమాచారం",
    "important_text": "ఈ చాట్‌బాట్ వ్యాధులను నిర్ధారించదు. తీవ్రమైన లేదా అత్యవసర లక్షణాలు ఉంటే వెంటనే వైద్య సహాయం పొందండి.",
    "how_it_works": "🩺 ఇది ఎలా పనిచేస్తుంది",
    "step1": "1. మీ లక్షణాలను వివరించండి.",
    "step2": "2. స్వాస్థ్యసేతు మిమ్మల్ని సులభమైన ప్రశ్నలు అడుగుతుంది.",
    "step3": "3. చాట్‌బాట్ సాధారణ ఆరోగ్య సమాచారాన్ని అందిస్తుంది.",
    "step4": "4. అత్యవసర లక్షణాలు ఉంటే వెంటనే హెచ్చరిక అందిస్తుంది."
},

    "Kannada": {
    "title": "🏥 ಸ್ವಾಸ್ಥ್ಯಸೇತು",
    "subtitle": "ಗ್ರಾಮೀಣ ಆರೋಗ್ಯ ಸಹಾಯ ವೇದಿಕೆ",
    "language": "🌐 ನಿಮ್ಮ ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ",
    "warning": "ಈ ಸಹಾಯಕವು ಸಾಮಾನ್ಯ ಆರೋಗ್ಯ ಮಾಹಿತಿಯನ್ನು ಮಾತ್ರ ನೀಡುತ್ತದೆ. ಇದು ರೋಗಗಳನ್ನು ಪತ್ತೆಹಚ್ಚುವುದಿಲ್ಲ ಮತ್ತು ವೈದ್ಯರಿಗೆ ಪರ್ಯಾಯವಲ್ಲ.",
    "placeholder": "ನಿಮ್ಮ ರೋಗಲಕ್ಷಣಗಳನ್ನು ವಿವರಿಸಿ...",
    "welcome_title": "💬 ಇಂದು ನಾನು ನಿಮಗೆ ಹೇಗೆ ಸಹಾಯ ಮಾಡಬಹುದು?",
    "welcome_text": "ದಯವಿಟ್ಟು ನಿಮ್ಮ ರೋಗಲಕ್ಷಣಗಳನ್ನು ಸರಳ ಪದಗಳಲ್ಲಿ ವಿವರಿಸಿ.",
    "welcome_note": "ನಿಮ್ಮ ಸಮಸ್ಯೆಯನ್ನು ಚೆನ್ನಾಗಿ ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ನಾನು ಕೆಲವು ಪ್ರಶ್ನೆಗಳನ್ನು ಕೇಳುತ್ತೇನೆ.",
    "new_chat": "🆕 ಹೊಸ ಚಾಟ್",
    "about": "ℹ️ ನಮ್ಮ ಬಗ್ಗೆ",
    "about_text": "ಸ್ವಾಸ್ಥ್ಯಸೇತು ಸರಳ ಪ್ರಶ್ನೆಗಳು ಮತ್ತು ಸಾಮಾನ್ಯ ಆರೋಗ್ಯ ಮಾಹಿತಿಯ ಮೂಲಕ ನಿಮ್ಮ ರೋಗಲಕ್ಷಣಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.",
    "important": "⚠️ ಪ್ರಮುಖ ಮಾಹಿತಿ",
    "important_text": "ಈ ಚಾಟ್‌ಬಾಟ್ ರೋಗಗಳನ್ನು ಪತ್ತೆಹಚ್ಚುವುದಿಲ್ಲ. ಗಂಭೀರ ಅಥವಾ ತುರ್ತು ರೋಗಲಕ್ಷಣಗಳಿದ್ದರೆ ತಕ್ಷಣ ವೈದ್ಯಕೀಯ ಸಹಾಯ ಪಡೆಯಿರಿ.",
    "how_it_works": "🩺 ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ",
    "step1": "1. ನಿಮ್ಮ ರೋಗಲಕ್ಷಣಗಳನ್ನು ವಿವರಿಸಿ.",
    "step2": "2. ಸ್ವಾಸ್ಥ್ಯಸೇತು ನಿಮ್ಮನ್ನು ಸರಳ ಪ್ರಶ್ನೆಗಳನ್ನು ಕೇಳುತ್ತದೆ.",
    "step3": "3. ಚಾಟ್‌ಬಾಟ್ ಸಾಮಾನ್ಯ ಆರೋಗ್ಯ ಮಾಹಿತಿಯನ್ನು ನೀಡುತ್ತದೆ.",
    "step4": "4. ತುರ್ತು ರೋಗಲಕ್ಷಣಗಳಿದ್ದರೆ ತಕ್ಷಣ ಎಚ್ಚರಿಕೆ ನೀಡುತ್ತದೆ."
},
    "Tamil": {
    "title": "🏥 ஸ்வாஸ்த்யசேது",
    "subtitle": "கிராமப்புற சுகாதார உதவி தளம்",
    "language": "🌐 உங்கள் மொழியைத் தேர்ந்தெடுக்கவும்",
    "warning": "இந்த உதவியாளர் பொதுவான சுகாதார தகவல்களை மட்டுமே வழங்குகிறது. இது நோய்களைக் கண்டறியாது மற்றும் மருத்துவருக்கு மாற்றாகாது.",
    "placeholder": "உங்கள் அறிகுறிகளை விவரிக்கவும்...",
    "welcome_title": "💬 இன்று நான் உங்களுக்கு எப்படி உதவ முடியும்?",
    "welcome_text": "தயவுசெய்து உங்கள் அறிகுறிகளை எளிய வார்த்தைகளில் விவரிக்கவும்.",
    "welcome_note": "உங்கள் பிரச்சனையை நன்றாகப் புரிந்துகொள்ள நான் சில கேள்விகளைக் கேட்பேன்.",
    "new_chat": "🆕 புதிய உரையாடல்",
    "about": "ℹ️ எங்களைப் பற்றி",
    "about_text": "ஸ்வாஸ்த்யசேது எளிய கேள்விகள் மற்றும் பொதுவான சுகாதார தகவல்களின் மூலம் உங்கள் அறிகுறிகளைப் புரிந்துகொள்ள உதவுகிறது.",
    "important": "⚠️ முக்கியமான தகவல்",
    "important_text": "இந்த chatbot நோய்களைக் கண்டறியாது. கடுமையான அல்லது அவசர அறிகுறிகள் இருந்தால் உடனடியாக மருத்துவ உதவியைப் பெறுங்கள்.",
    "how_it_works": "🩺 இது எப்படி செயல்படுகிறது",
    "step1": "1. உங்கள் அறிகுறிகளை விவரிக்கவும்.",
    "step2": "2. ஸ்வாஸ்த்யசேது உங்களிடம் எளிய கேள்விகளைக் கேட்கும்.",
    "step3": "3. chatbot பொதுவான சுகாதார தகவல்களை வழங்கும்.",
    "step4": "4. அவசர அறிகுறிகள் இருந்தால் உடனடி எச்சரிக்கை வழங்கப்படும்."
},
}

# Select language
selected_language = st.selectbox(
    "🌐 Language / भाषा / భాష / மொழி",
    list(translations.keys())
)

# Get selected language translations
t = translations[selected_language]

# App title
st.title(t["title"])
st.subheader(t["subtitle"])

# Safety warning
st.warning(t["warning"])

# Create chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Sidebar
with st.sidebar:
    st.header(t["title"])

    st.write(t["subtitle"])

    if st.button(t["new_chat"]):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.subheader(t["about"])
    st.write(t["about_text"])

    st.subheader(t["important"])
    st.write(t["important_text"])
    st.divider()

    st.subheader(t["how_it_works"])
    st.write(t["step1"])
    st.write(t["step2"])
    st.write(t["step3"])
    st.write(t["step4"])

# Clean welcome screen
if not st.session_state.messages:
    st.markdown(f"## {t['welcome_title']}")
    st.write(t["welcome_text"])
    st.write(t["welcome_note"])


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


def check_emergency(text):

    emergency_keywords = [
        # English
        "difficulty breathing",
        "can't breathe",
        "cannot breathe",
        "severe chest pain",
        "unconscious",
        "not responding",
        "heavy bleeding",
        "severe bleeding",
        "stroke",
        "seizure",

        # Hindi
        "सांस लेने में कठिनाई",
        "सांस नहीं आ रही",
        "सीने में तेज दर्द",
        "बेहोश",
        "बहुत ज्यादा खून",
        "दौरा",

        # Telugu
        "శ్వాస తీసుకోవడంలో ఇబ్బంది",
        "ఊపిరి తీసుకోలేకపోతున్నాను",
        "తీవ్రమైన ఛాతి నొప్పి",
        "స్పృహ కోల్పోయిన",
        "తీవ్రమైన రక్తస్రావం",

        # Kannada
        "ಉಸಿರಾಟದ ತೊಂದರೆ",
        "ಉಸಿರಾಡಲು ಸಾಧ್ಯವಾಗುತ್ತಿಲ್ಲ",
        "ತೀವ್ರ ಎದೆ ನೋವು",
        "ಪ್ರಜ್ಞಾಹೀನ",
        "ತೀವ್ರ ರಕ್ತಸ್ರಾವ",

        # Tamil
        "சுவாசிப்பதில் சிரமம்",
        "மூச்சு விட முடியவில்லை",
        "கடுமையான நெஞ்சு வலி",
        "மயக்கமடைந்த",
        "கடுமையான இரத்தப்போக்கு"
    ]

    text = text.lower()

    for keyword in emergency_keywords:
        if keyword in text:
            return True

    return False

# Patient age
age = st.number_input(
    "👤 Age",
    min_value=1,
    max_value=120,
    value=None,
    placeholder="Enter your age"
)
gender = st.selectbox(
    "⚧ Gender",
    ["Select", "Male", "Female", "Other / Prefer not to say"]
)
# User input
user_input = st.chat_input(t["placeholder"])


if user_input:
     
    if age is None:
        st.warning("⚠️ Please enter your age before describing your symptoms.")
        st.stop()

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)


    # Emergency check
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
       system_prompt = f"""
          You are SwasthyaSetu, a simple rural healthcare assistance chatbot.

          You are NOT a doctor. You must NOT diagnose diseases.

          Your job is to:
          - Understand the user's symptoms.
          - Ask useful questions to collect information.
          - Give simple general health information when enough information is available.

          IMPORTANT RULES:

          1. Ask only ONE question at a time.

          2. If the user gives only a symptom, ask a relevant follow-up question.

          Example:
          User: I have fever
          Assistant: How long have you had the fever?

          3. Continue asking questions based on the user's previous answer.

          Example:
          User: 3 days
          Assistant: Have you measured your temperature? If yes, what was the highest temperature?

          4. Ask about important symptoms when relevant, such as:
          - difficulty breathing
          - severe chest pain
          - unconsciousness
          - severe bleeding
          - confusion
          - seizures

          5. If the user describes a serious emergency symptom, tell them to seek
          immediate medical help.

          6. Do NOT randomly recommend:
          - coconut water
          - herbal remedies
          - food
          - drinks
          - medicines

          7. Do NOT diagnose the user's disease.

          8. Do NOT immediately tell every user to visit a doctor.

          9. Use very simple language that a rural user can understand.

          10. Always reply in the selected language.

          11. Keep the response short, usually 1-3 sentences.

          12. Use the user's previous answers when asking the next question.
          Do not ask for information that the user has already provided.

          13. When you have enough information, briefly summarize what the user
          has told you and provide general health information.

          14. Clearly separate:
          - What the user reported
          - General information
          - When to seek medical help

          15. Never claim that the user definitely has a particular disease.

          16. If you are unsure, say that you are unsure rather than making up information.

          Selected language: {selected_language}
         """

       try:
            age_message = {
              "role": "system",
              "content": f"The user's age is {age} years old. Consider this information when giving general health information."
            }

            recent_messages = st.session_state.messages[-10:]

            response = client.chat.completions.create(
                model="deepseek-ai/DeepSeek-V3-0324",
                messages=[
                   {"role": "system", "content": system_prompt},
                   age_message,
                   *recent_messages
                ],
                max_tokens=150
            )

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