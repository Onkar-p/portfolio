import os
import sys
import subprocess

# Ensure reportlab is installed
try:
    import reportlab
except ImportError:
    print("Installing reportlab...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
    import reportlab

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_resume():
    pdf_path = os.path.join(os.path.dirname(__file__), "Onkar_Purjalkar_Resume.pdf")
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=40,
        rightMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    story = []

    # Custom Color Palette
    primary_color = colors.HexColor("#0f172a") # Slate Navy
    secondary_color = colors.HexColor("#4f46e5") # Indigo/Purple
    text_dark = colors.HexColor("#334155") # Charcoal
    accent_color = colors.HexColor("#0d9488") # Teal

    # Typography Styles
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=primary_color,
        spaceAfter=4
    )

    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=secondary_color,
        spaceAfter=8
    )

    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=text_dark,
        alignment=0 # Left aligned
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=primary_color,
        spaceBefore=12,
        spaceAfter=4
    )

    bold_body = ParagraphStyle(
        'BoldBody',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=primary_color
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=text_dark,
        spaceAfter=4
    )

    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=text_dark,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=3
    )

    # 1. Header (Name, Title, Contact Info)
    story.append(Paragraph("ONKAR PURJALKAR", name_style))
    story.append(Paragraph("Machine Learning Engineer & Software Developer", title_style))

    contact_text = (
        "<b>Email:</b> onkarpurjalkar90.40@gmail.com | "
        "<b>LinkedIn:</b> linkedin.com/in/onkar-purjalkar-b63b74391 | "
        "<b>GitHub:</b> github.com/onkar-p | "
        "<b>Mobile-no:</b> +91 9421785743| "
        "<b>Location:</b> India"
    )
    story.append(Paragraph(contact_text, contact_style))
    story.append(Spacer(1, 10))

    # Decorative Line
    story.append(HRFlowable(width="100%", thickness=2, color=secondary_color, spaceAfter=15))

    # 2. Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey, spaceAfter=8))
    summary_text = (
        "Passionate B.Tech student and aspiring Machine Learning Engineer & Software Developer with hands-on "
        "experience building intelligent applications, predictive systems, and conversational agents. Proficient "
        "in Python, Machine Learning, data science and full-stack web development. Proven capability in "
        "developing end-to-end applications from model engineering to interactive UI dashboards, with practical internship "
        "experience in software quality assurance."
    )
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 10))

    # 3. Education
    story.append(Paragraph("EDUCATION", section_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey, spaceAfter=8))
    
    edu_data = [
        [
            Paragraph("<b>Bachelor of Technology (B.Tech)-MGM's college of Engineering , Nanded </b><br/> Major in Information Technology & Minor in Artificial Intelligence & Machine learning", body_style),
            Paragraph("<font color='#4f46e5'><b>Expected Graduation: 2028</b></font>", ParagraphStyle('RightText', parent=body_style, alignment=2))
            
        ],
        [
            Paragraph("<b>Diploma in Information Technology</b><br/> Government Polytechnic, Nanded", body_style),
            Paragraph("<font color='#4f46e5'><b>Completed: 2025</b></font>", ParagraphStyle('RightText2', parent=body_style, alignment=2))
        ]
    ]
    t = Table(edu_data, colWidths=[380, 150])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))

    # 4. Work Experience
    story.append(Paragraph("WORK EXPERIENCE", section_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey, spaceAfter=8))
    
    exp_header = [
        [
            Paragraph("<b>JOBITO</b> — Software Quality Assurance (SQA) Intern", bold_body),
            Paragraph("<b>2 Months</b>", ParagraphStyle('RightTextBold', parent=bold_body, alignment=2))
        ]
    ]
    t_exp = Table(exp_header, colWidths=[380, 150])
    t_exp.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_exp)
    story.append(Spacer(1, 4))
    story.append(Paragraph("• Executed manual testing and developed test plans to ensure functionality, reliability, and security of web applications.", bullet_style))
    story.append(Paragraph("• Collaborated with core developer teams to document, track, and verify resolution of bugs in a database-driven system.", bullet_style))
    story.append(Paragraph("• Gained hands-on insights into software development life cycles (SDLC) and QA best practices.", bullet_style))
    story.append(Spacer(1, 10))

    # 5. Core Projects
    story.append(Paragraph("PROJECTS", section_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey, spaceAfter=8))

    # Project 1: AIVICS
    proj1_header = [
        [
            Paragraph("<b>AIVICS — AI-Enhanced Virtual Interaction & Control System</b>", bold_body),
            Paragraph("<font color='#0d9488'><b>Python, OpenCV, Streamlit, APIs</b></font>", ParagraphStyle('RightTextAccent', parent=body_style, fontName='Helvetica-Bold', alignment=2))
        ]
    ]
    t_p1 = Table(proj1_header, colWidths=[350, 180])
    t_p1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_p1)
    story.append(Spacer(1, 3))
    story.append(Paragraph("• Engineered an AI-powered desktop virtual assistant with voice activation, computer vision gesture control, and automation features.", bullet_style))
    story.append(Paragraph("• Implemented <b>Hotword Detection</b> for hands-free wake commands and <b>Air Canvas</b> using hand-tracking and OpenCV for in-air writing.", bullet_style))
    story.append(Paragraph("• Integrated <b>Eye Mouse Control</b> via face landmarks, voice search activation, automatic system volume controls, and network speed testing.", bullet_style))
    story.append(Paragraph("• Designed automated messaging systems triggering WhatsApp, Email, SMS via python-based libraries and APIs.", bullet_style))
    story.append(Spacer(1, 8))

    # Project 2: AQI Predictor
    proj2_header = [
        [
            Paragraph("<b>Air Quality Monitoring & Predictor</b>", bold_body),
            Paragraph("<font color='#0d9488'><b>Random Forest, Streamlit, Pandas</b></font>", ParagraphStyle('RightTextAccent2', parent=body_style, fontName='Helvetica-Bold', alignment=2))
        ]
    ]
    t_p2 = Table(proj2_header, colWidths=[350, 180])
    t_p2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_p2)
    story.append(Spacer(1, 3))
    story.append(Paragraph("• Built an end-to-end machine learning system using <b>Random Forest Regression</b> to forecast historical and future Air Quality Index (AQI) values.", bullet_style))
    story.append(Paragraph("• Developed an interactive web interface using <b>Streamlit</b> to plot real-time pollution metrics, trends, and generate automated hazard warnings.", bullet_style))
    story.append(Paragraph("• Preprocessed complex environmental datasets using NumPy and Pandas to optimize model accuracy and training efficiency.", bullet_style))
    story.append(Spacer(1, 8))

    # Project 3: Multiagent Chatbot
    proj3_header = [
        [
            Paragraph("<b>Multiagent Chatbot System</b>", bold_body),
            Paragraph("<font color='#0d9488'><b>Python, LLMs, Streamlit, NLP</b></font>", ParagraphStyle('RightTextAccent3', parent=body_style, fontName='Helvetica-Bold', alignment=2))
        ]
    ]
    t_p3 = Table(proj3_header, colWidths=[350, 180])
    t_p3.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_p3)
    story.append(Spacer(1, 3))
    story.append(Paragraph("• Developed a conversational AI architecture where multiple specialized LLM agents collaborate to resolve user queries.", bullet_style))
    story.append(Paragraph("• Implemented task-routing algorithms separating research assistance, general chat agents.", bullet_style))
    story.append(Spacer(1, 10))

    # 6. Technical Skills
    story.append(Paragraph("TECHNICAL SKILLS", section_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey, spaceAfter=8))
    
    skills_data = [
        [Paragraph("<b>Programming & Web:</b>", bold_body), Paragraph("Python, PHP, JavaScript, SQL, HTML5, CSS3", body_style)],
        [Paragraph("<b>Machine Learning & Data:</b>", bold_body), Paragraph("Random Forest, Scikit-Learn, NumPy, Pandas, OpenCV, NLP", body_style)],
        [Paragraph("<b>Frameworks & Databases:</b>", bold_body), Paragraph("Streamlit, Flask, MySQL, SQLite", body_style)],
        [Paragraph("<b>Tools & Concepts:</b>", bold_body), Paragraph("Git & GitHub, API Integrations, Software Testing (QA), System Automation", body_style)]
    ]
    t_skills = Table(skills_data, colWidths=[160, 370])
    t_skills.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_skills)
    story.append(Spacer(1, 10))

    # 7. Certifications
    story.append(Paragraph("CERTIFICATIONS", section_heading))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey, spaceAfter=8))
    story.append(Paragraph("• Machine Learning with Python — <b>IBM</b>", bullet_style))
    story.append(Paragraph("• Python, NumPy and Pandas — <b>Infosys Springboard</b>", bullet_style))
    story.append(Paragraph("• The Complete Full Stack Web Development Bootcamp — <b>Udemy</b>", bullet_style))
    story.append(Paragraph("• PHP and MySQL — <b>Spoken Tutorial</b>", bullet_style))

    doc.build(story)
    print("Resume generated successfully!")

if __name__ == "__main__":
    create_resume()