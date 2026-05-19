import streamlit as st
import docx
import io

# 1. Clean App Title Page Layout
st.set_page_config(page_title="AI Student Report Hub", page_icon="🎓")
st.title("🎓 AI Student Report Hub")
st.write("Enter student data and a topic below to generate a formatted Word document.")

# 2. Input Fields for Details
student_name = st.text_input("👤 Student Name", placeholder="e.g., Anusha")
roll_number = st.text_input("🆔 Roll Number / USN", placeholder="e.g., 1VT23CS000")
topic = st.text_input("📚 Enter the Report Topic:", placeholder="e.g., Blockchain Architecture")

# 3. Generate Actions
if st.button("Generate Academic Report"):
    if topic and student_name:
        st.success(f"Generating comprehensive report outline for: {topic}...")
        
        # Initialize the Document
        doc = docx.Document()
        
        # Add Header Styling
        doc.add_heading(f"Technical Report: {topic}", level=0)
        doc.add_paragraph(f"Prepared by: {student_name}")
        if roll_number:
            doc.add_paragraph(f"Roll Number/USN: {roll_number}")
            
        doc.add_heading("1. Introduction", level=1)
        doc.add_paragraph(f"This section introduces the foundational concepts surrounding {topic}. It analyzes the historical context and explains why this field is highly relevant to contemporary technological studies.")
        
        doc.add_heading("2. Core Core Analysis & Discussion", level=1)
        doc.add_paragraph(f"When examining {topic} deeper, several critical principles must be reviewed. This includes detailed structural layouts, implementation workflows, system requirements, and experimental test boundaries.")
        
        doc.add_heading("3. Conclusion & Summary", level=1)
        doc.add_paragraph(f"In summary, understanding the mechanics of {topic} provides strong strategic insights. Future iterations will focus on advancing efficiency parameters and integration protocols.")

        # --- THE MAGIC FIXED DOWNLOAD TRICK ---
        # Instead of saving locally, we convert it to memory bytes for web stream download
        bio = io.BytesIO()
        doc.save(bio)
        bio.seek(0)
        
        st.success("✨ Report built successfully!")
        
        # This will bring up the clear "Click here to download" banner right below the button
        st.download_button(
            label="📥 Click Here to Download Word (.docx) Document",
            data=bio.getvalue(),
            file_name=f"{topic.replace(' ', '_')}_Report.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
    else:
        st.warning("⚠️ Please fill in both the Student Name and Report Topic fields first!")
