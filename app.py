import streamlit as st
from utils.ai_service import get_ai_response
from modules.quiz import generate_quiz
from modules.career import generate_career_roadmap
from modules.skill_gap import analyze_skill_gap
from modules.interview import generate_interview
from utils.pdf_export import create_pdf


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="FUTUREMIND AI",
    page_icon="🧠",
    layout="wide"
)
st.markdown("""
<style>

/* Try to hide GitHub links only */
a[href*="github.com"] {
    display: none !important;
}

/* Hide Streamlit menu */
#MainMenu {
    visibility: hidden;
}

/* Hide footer */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)
# ==========================================
# CUSTOM CSS STYLING
# ==========================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

h1 {
    color: #4F46E5;
}

h2, h3 {
    color: #4338CA;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 3em;
    font-weight: 600;
}



</style>
""", unsafe_allow_html=True)
# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.markdown("""
# 🧠 FUTUREMIND AI

### Your AI Learning Partner
""")

if "feature" not in st.session_state:
    st.session_state["feature"] = "🏠 Home"

feature = st.sidebar.selectbox(
    "🚀 Explore Features",
    [
        "🏠 Home",
        "📚 AI Study Tutor",
        "📝 Smart Quiz Generator",
        "🚀 Career Roadmap",
        "📊 Skill Gap Analyzer",
        "🎤 AI Mock Interview"
    ],
    index=[
        "🏠 Home",
        "📚 AI Study Tutor",
        "📝 Smart Quiz Generator",
        "🚀 Career Roadmap",
        "📊 Skill Gap Analyzer",
        "🎤 AI Mock Interview"
    ].index(st.session_state["feature"])
)

st.session_state["feature"] = feature

st.sidebar.markdown("---")

st.sidebar.success(
    "✨ Learn • Practice • Grow"
)

st.sidebar.markdown("""
---
Developed with ❤️ by **Sristi**
""")


# ==========================================
# HOMEPAGE
# ==========================================

if feature == "🏠 Home":

    st.title("🧠 FUTUREMIND AI")

    st.subheader("Learn Smarter. Plan Better. Grow Faster.")

    st.write("""
Your personal AI-powered study and career assistant designed to help students learn, practice, and prepare for their future.
""")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.info("""
### 📚 AI Study Tutor
Understand difficult concepts with simple AI explanations.
""")

        st.success("""
### 📝 Smart Quiz Generator
Generate interactive quizzes and test your knowledge.
""")

        st.warning("""
### 🚀 Career Roadmap
Get a personalized path towards your dream career.
""")

    with col2:

        st.success("""
### 📊 Skill Gap Analyzer
Discover missing skills and improve yourself.
""")

        st.info("""
### 🎤 AI Mock Interview
Practice realistic interview questions confidently.
""")

    st.markdown("---")

    st.markdown(
    """
    ## 🚀 Begin Your Journey

    Choose any feature from the sidebar and start learning with AI.
        """
    )

# ==========================================
# AI STUDY TUTOR v1.1 (ChatGPT Style)
# ==========================================

elif feature == "📚 AI Study Tutor":

    st.title("📚 AI Study Tutor")

    st.markdown("""
Welcome to your AI Study Assistant! 🤖

Ask any academic question and continue the conversation naturally.
Your chat history will remain available during your session.
""")

    # Create chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])


    # User input
    prompt = st.chat_input(
        "Ask your study question here..."
    )


    # When user sends a message
    if prompt:

        # Show user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Save user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )


        # Generate AI response
        with st.chat_message("assistant"):

            with st.spinner(
                "🧠 FUTUREMIND AI is thinking..."
            ):

                answer = get_ai_response(st.session_state.messages)
                st.markdown(answer)
                pdf_file = create_pdf(
                    "FUTUREMIND AI Study Tutor",
                    answer
                )

                st.download_button(
                    "📄 Download PDF",
                    data=pdf_file,
                    file_name="study_answer.pdf",
                    mime="application/pdf"
                )

        # Save AI response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


    # Clear conversation button
    st.markdown("---")

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()
            # ==========================================
# SMART QUIZ GENERATOR
# ==========================================

elif feature == "📝 Smart Quiz Generator":

    st.title("📝 Smart Quiz Generator")

    st.markdown("""
Create personalized quizzes, test your knowledge,
and track your performance.
""")

    # Create session state
    if "quiz_data" not in st.session_state:
        st.session_state.quiz_data = None


    topic = st.text_input(
        "Enter quiz topic:",
        placeholder="Example: Python Programming"
    )


    difficulty = st.selectbox(
        "Select difficulty level:",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )


    number_of_questions = st.slider(
        "Number of Questions:",
        min_value=1,
        max_value=10,
        value=5
    )


    if st.button("📝 Generate Quiz"):

        if topic.strip():

            with st.spinner(
                "🧠 Creating your personalized quiz..."
            ):

                st.session_state.quiz_data = generate_quiz(
                    topic,
                    difficulty,
                    number_of_questions
                )

        else:

            st.warning(
                "⚠️ Please enter a quiz topic."
            )


    # Show generated quiz
    if st.session_state.quiz_data:

        st.markdown("---")
        st.subheader("🧩 Answer the Questions")


        user_answers = []


        for i, question in enumerate(
            st.session_state.quiz_data
        ):

            st.write(
                f"### Question {i + 1} of {len(st.session_state.quiz_data)}"
            )


            # Progress bar
            progress = (i + 1) / len(st.session_state.quiz_data)
            st.progress(progress)


            st.write(
                question["question"]
            )


            answer = st.radio(
                "Choose your answer:",
                options=list(question["options"].keys()),
                format_func=lambda x, q=question:
                    f"{x}. {q['options'][x]}",
                index=None,
                key=f"quiz_question_{i}"
            )


            user_answers.append(answer)


        if st.button("📊 Submit Quiz"):


            if None in user_answers:

                st.warning(
                    "⚠️ Please answer all questions before submitting."
                )


            else:

                score = 0

                st.markdown(
                    "# 🎯 Quiz Results"
                )


                for i, question in enumerate(
                    st.session_state.quiz_data
                ):

                    correct_answer = question["answer"]


                    if user_answers[i] == correct_answer:

                        score += 1

                        st.success(
                            f"Question {i + 1}: Correct ✅"
                        )

                    else:

                        st.error(
                            f"Question {i + 1}: Incorrect ❌"
                        )


                    st.write(
                        f"Your Answer: {user_answers[i]}"
                    )

                    st.write(
                        f"Correct Answer: {correct_answer}"
                    )


                    st.info(
                        f"Explanation: {question['explanation']}"
                    )


                    st.markdown("---")


                percentage = (
                    score / len(st.session_state.quiz_data)
                ) * 100


                st.header(
                    f"🏆 Final Score: {score}/{len(st.session_state.quiz_data)}"
                )


                if percentage >= 80:

                    st.balloons()

                    st.success(
                        "🌟 Excellent performance! Keep it up."
                    )

                elif percentage >= 50:

                    st.info(
                        "👍 Good job! Practice a little more to improve."
                    )

                else:

                    st.warning(
                        "📚 Keep learning and try again. You can do it!"
                    )


        if st.button("🔄 Start New Quiz"):

            st.session_state.quiz_data = None
            st.rerun()
            # ==========================================
# CAREER ROADMAP
# ==========================================

elif feature == "🚀 Career Roadmap":

    st.title("🚀 AI Career Roadmap")

    st.markdown("""
Get a personalized step-by-step roadmap to achieve your dream career.
""")

    career_goal = st.text_input(
        "What is your dream career?",
        placeholder="Example: Data Scientist"
    )


    current_level = st.selectbox(
        "Select your current level:",
        [
            "School Student",
            "1st Year College Student",
            "2nd Year College Student",
            "3rd Year College Student",
            "Final Year Student",
            "Graduate",
            "Working Professional"
        ]
    )


    if st.button("🚀 Generate Roadmap"):

        if career_goal.strip():

            with st.spinner(
                "🧠 Creating your personalized career roadmap..."
            ):

                roadmap = generate_career_roadmap(
                    career_goal,
                    current_level
                )


            if "⚠️" in roadmap:

                st.error(roadmap)

            else:

                st.success(
                    "🎉 Your career roadmap is ready!"
                )

                
                st.markdown("## 🗺️ Your Roadmap")

                st.write(roadmap)

                pdf_file = create_pdf(
                    "Career Roadmap",
                    roadmap
                )

                st.download_button(
                    "📄 Download Roadmap PDF",
                    data=pdf_file,
                    file_name="career_roadmap.pdf",
                    mime="application/pdf"
                )

        else:

            st.warning(
                "⚠️ Please enter your dream career."
            )


# ==========================================
# SKILL GAP ANALYZER
# ==========================================

elif feature == "📊 Skill Gap Analyzer":

    st.title("📊 AI Skill Gap Analyzer")

    st.markdown("""
Analyze your current skills and discover what you need to learn next.
""")


    target_career = st.text_input(
        "Target Career:",
        placeholder="Example: Software Engineer"
    )


    current_skills = st.text_area(
        "Your Current Skills:",
        placeholder="Example: Python, HTML, CSS, JavaScript"
    )


    if st.button("📈 Analyze Skills"):


        if target_career.strip() and current_skills.strip():

            with st.spinner(
                "🧠 Analyzing your skills and preparing recommendations..."
            ):

                analysis = analyze_skill_gap(
                    target_career,
                    current_skills
                )


            if "⚠️" in analysis:

                st.error(analysis)

            else:

                st.success(
                    "🎯 Skill analysis completed!"
                )

                st.markdown("## 📚 Your Improvement Plan")

                st.write(analysis)

                pdf_file = create_pdf(
                    "Skill Gap Analysis",
                    analysis
                )

                st.download_button(
                    "📄 Download Analysis PDF",
                    data=pdf_file,
                    file_name="skill_gap_analysis.pdf",
                    mime="application/pdf"
                )

        else:

            st.warning(
                "⚠️ Please fill in both fields."
            )


# ==========================================
# MOCK INTERVIEW
# ==========================================

elif feature == "🎤 AI Mock Interview":

    st.title("🎤 AI Mock Interview")

    st.markdown("""
Practice realistic interview questions and improve your confidence.
""")


    job_role = st.text_input(
        "Target Job Role:",
        placeholder="Example: Software Engineer"
    )


    experience = st.selectbox(
        "Experience Level:",
        [
            "School Student",
            "College Student",
            "Fresher",
            "Experienced Professional"
        ]
    )


    if st.button("🎤 Generate Interview Questions"):


        if job_role.strip():

            with st.spinner(
                "🧠 Preparing your AI mock interview..."
            ):

                interview = generate_interview(
                    job_role,
                    experience
                )


            if "⚠️" in interview:

                st.error(interview)

            else:

                st.success(
                    "🎉 Your interview questions are ready!"
                )

                st.markdown("## 💼 Practice Questions")

                st.write(interview)

                pdf_file = create_pdf(
                    "Mock Interview Questions",
                    interview
                )

                st.download_button(
                    "📄 Download Interview PDF",
                    data=pdf_file,
                    file_name="mock_interview.pdf",
                    mime="application/pdf"
                )

        else:

            st.warning(
                "⚠️ Please enter a job role."
            )


# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown(
    """
<div style='text-align: center; color: grey;'>

### 🧠 FUTUREMIND AI

Learn Smarter • Plan Better • Grow Faster

Made with ❤️ by Sristi 

</div>
""",
    unsafe_allow_html=True
)