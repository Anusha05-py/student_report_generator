import streamlit as st
import docx

st.title("🎓 AI Student Report Generator")
st.write("Welcome! Let's build your report generator.")

# A simple text input box
topic = st.text_input("Enter the Report Topic:", placeholder="e.g., Blockchain Architecture")

if st.button("Generate Report Outline"):
    if topic:
        st.success(f"Generating outline for: {topic}...")
        
        # Create a simple Word Document
        doc = docx.Document()
        doc.add_heading(f"Report: {topic}", level=0)
        doc.add_paragraph("This is a placeholder paragraph for your automated report.")
        
        # Save it
        doc.save("generated_report.docx")
        st.info("Saved a temporary 'generated_report.docx' to your folder!")
    else:
        st.warning("Please enter a topic first!")