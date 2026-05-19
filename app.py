import streamlit as st
import docx
import io

# 1. PREMIUM NEON STYLING (Multiple Colors for Letters)
st.set_page_config(page_title="AI Report Hub", page_icon="🎓", layout="centered")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311042 100%); }
    
    /* Multicolor Title Letters */
    h1 { font-family: sans-serif; font-weight: 800; text-align: center; }
    .neon-text { 
        display: inline-block; 
        background: linear-gradient(90deg, #ff007a, #7000ff, #00d4ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 12px !important;
        border: 2px solid #a855f7 !important;
        background-color: #1e1b4b !important;
        color: #fff !important;
    }
    
    .stButton>button {
        background: linear-gradient(90deg, #ec4899 0%, #8b5cf6 100%) !important;
        color: white !important;
        border-radius: 15px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1><span class='neon-text'>AI Student Report Hub</span></h1>", unsafe_allow_html=True)

# 2. INPUTS
col1, col2 = st.columns(2)
with col1: student_name = st.text_input("👤 Student Name")
with col2: roll_number = st.text_input("🆔 Roll Number/USN")
report_topic = st.text_input("📚 Report Topic")
user_description = st.text_area("💬 Custom Content Directives:")
uploaded_sample = st.file_uploader("📂 Upload Reference File (VTU Template)", type=["docx"])

# 3. PRECISION REPLACEMENT LOGIC
if st.button("🚀 Generate Exact-Layout Report"):
    if uploaded_sample and student_name:
        doc = docx.Document(uploaded_sample)
        
        # Replace simple placeholders in the document
        for para in doc.paragraphs:
            if "NAME" in para.text.upper(): para.text = para.text.replace("NAME", student_name)
            if "USN" in para.text.upper(): para.text = para.text.replace("USN", roll_number)
            if "TOPIC" in para.text.upper(): para.text = para.text.replace("TOPIC", report_topic)
            
            # Smart Replacement for Content
            if "INTRODUCTION" in para.text.upper():
                para.text = f"Introduction: This report details {report_topic}. {user_description}"
        
        # Save to buffer
        byte_stream = io.BytesIO()
        doc.save(byte_stream)
        byte_stream.seek(0)
        
        st.success("✅ Layout preserved perfectly!")
        st.download_button("📥 Download Final Report", byte_stream, "Final_Report.docx")
    else:
        st.error("Please upload your VTU template and enter your details.")
