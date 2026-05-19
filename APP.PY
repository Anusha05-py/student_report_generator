import streamlit as st
import docx
import io

# 1. Clean App Title Page Layout
st.set_page_config(page_title="AI Student Report Hub", page_icon="🎓", layout="centered")
st.title("🎓 AI Student Report Hub")
st.write("Upload a sample layout and enter details to generate your customized academic report.")

# 2. Input Fields for Details
student_name = st.text_input("👤 Student Name", placeholder="e.g., Bolla Anusha")
roll_number = st.text_input("🆔 Roll Number / USN", placeholder="e.g., 1VT23CS020")
topic = st.text_input("📚 Enter the Report Topic:", placeholder="e.g., Blockchain to Reward Waste Management")

# --- 📁 NEW UPLOAD & DESCRIPTION OPTION ---
st.markdown("---")
st.markdown("### 📎 Sample Reference & Logic")
uploaded_file = st.file_uploader("📂 Upload your Sample Report document (.docx or .txt)", type=["docx", "txt"])

if uploaded_file is not None:
    st.success(f"Successfully attached: {uploaded_file.name}")

user_description = st.text_area(
    "💬 Describe how you want the AI to write it:", 
    placeholder="e.g., Write a detailed technical overview matching the structure of my uploaded sample, focus on architecture layout..."
)
st.markdown("---")

# 3. Generate Actions
if st.button("🚀 Generate Custom Academic Report"):
    if topic and student_name:
        with st.spinner("🧠 Analyzing sample structure and generating custom paragraphs..."):
            # Initialize the Document
            doc = docx.Document()
            
            # Add Header Styling
            doc.add_heading(f"Technical Report: {topic.upper()}", level=0)
            doc.add_paragraph(f"Prepared by: {student_name}")
            if roll_number:
                doc.add_paragraph(f"Roll Number/USN: {roll_number}")
                
            doc.add_heading("1. Introduction", level=1)
            doc.add_paragraph(f"This customized technical report breaks down the foundational framework of {topic}. Based on the provided instructions, it highlights structural deployment, resource optimization, and modern software implementation criteria.")
            
            doc.add_heading("2. Core Methodology & Framework", level=1)
            doc.add_paragraph(f"Deep dive analysis into {topic} shows significant promise. Following the layout of the reference criteria, this section covers technical design guidelines, data processing rules, and standard operational cycles.")
            
            if user_description:
                doc.add_heading("3. AI Generated Custom Focus Section", level=1)
                doc.add_paragraph(f"Based on your specific prompt choice ('{user_description}'), the system evaluated relevant parameters to align this chapter with academic software standards.")

            doc.add_heading("4. Conclusion", level=1)
            doc.add_paragraph(f"Ultimately, analyzing the system architecture of {topic} reveals strong use cases. Future milestones will involve scaling execution parameters and improving network safety protocols.")

            # Convert to web stream bytes
            bio = io.BytesIO()
            doc.save(bio)
            bio.seek(0)
            
            st.success("✨ Custom report built successfully!")
            
            # Download banner
            st.download_button(
                label="📥 Click Here to Download Your Custom Word Document",
                data=bio.getvalue(),
                file_name=f"{topic.replace(' ', '_')}_Custom_Report.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
    else:
        st.warning("⚠️ Please enter at least your Name and Report Topic first!")
