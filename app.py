import streamlit as st
from utils.ai_service import get_ai_response
from modules.quiz import generate_quiz
from modules.career import generate_career_roadmap
from modules.skill_gap import analyze_skill_gap
from modules.interview import generate_interview
from utils.pdf_export import create_pdf
from utils.analytics import (
    increment_counter,
    get_analytics
)
from utils.study_tips import get_study_tip


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

/* Main page */
.main {
    padding-top: 0.5rem;
    padding-bottom: 1rem;
}

/* Hide Streamlit menu */
#MainMenu {
    visibility: hidden;
}

/* Hide footer */
footer {
    visibility: hidden;
}

/* Headings */
h1 {
    color: #4F46E5;
    font-weight: 700;
}

h2, h3 {
    color: #4338CA;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 3.2em;
    font-size: 16px;
    font-weight: 600;
}

/* Metric cards */
[data-testid="metric-container"] {
    border-radius: 15px;
    padding: 15px;
    border: 1px solid #E5E7EB;
}

/* Reduce extra page spacing */
.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
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
        "🎤 AI Mock Interview",
        "📊 Analytics Dashboard",
    ],
    index=[
        "🏠 Home",
        "📚 AI Study Tutor",
        "📝 Smart Quiz Generator",
        "🚀 Career Roadmap",
        "📊 Skill Gap Analyzer",
        "🎤 AI Mock Interview",
        "📊 Analytics Dashboard",
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
    data = get_analytics()

    st.subheader("Learn Smarter. Plan Better. Grow Faster.")

    st.write("""
Your personal AI-powered study and career assistant designed to help students learn, practice, and prepare for their future.
""")

    st.markdown("---")

    st.subheader("📈 FUTUREMIND AI Statistics")

    analytics = get_analytics()

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("📚 Tutor", analytics["tutor"])

    with col2:
        st.metric("📝 Quizzes", analytics["quiz"])

    with col3:
        st.metric("🚀 Roadmaps", analytics["roadmap"])

    with col4:
        st.metric("📊 Skills", analytics["skill_gap"])

    with col5:
        st.metric("🎤 Interviews", analytics["interview"])

    st.markdown(
    """
    ## 🚀 Begin Your Journey

    Choose any feature from the sidebar and start learning with AI.
        """
    )
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("📚 Open AI Study Tutor", use_container_width=True):
            st.session_state["feature"] = "📚 AI Study Tutor"
            st.rerun()

        if st.button("🚀 Open Career Roadmap", use_container_width=True):
            st.session_state["feature"] = "🚀 Career Roadmap"
            st.rerun()

        if st.button("📊 Open Skill Gap Analyzer", use_container_width=True):
            st.session_state["feature"] = "📊 Skill Gap Analyzer"
            st.rerun()

    with col2:

        if st.button("📝 Open Smart Quiz", use_container_width=True):
            st.session_state["feature"] = "📝 Smart Quiz Generator"
            st.rerun()

        if st.button("🎤 Open Mock Interview", use_container_width=True):
            st.session_state["feature"] = "🎤 AI Mock Interview"
            st.rerun()

        if st.button("📈 Open Analytics", use_container_width=True):
            st.session_state["feature"] = "📈 Analytics Dashboard"
            st.rerun()
    st.markdown("---")

    import random

    st.info(get_study_tip())
    st.markdown("---")

    st.subheader("🌟 Why Choose FUTUREMIND AI?")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("""
    ### ⚡ Fast AI

    Instant responses for studying, quizzes, career planning and interviews.
    """)

    with c2:
        st.info("""
    ### 🎯 Personalized

    Every response is customized according to your goals and learning level.
    """)

    with c3:
        st.warning("""
    ### 🚀 All-in-One

    Study, Practice, Career Planning and Interview Preparation in one platform.
    """)
    st.markdown("---")

    st.markdown(
    """
    > **"Success doesn't come from what you do occasionally. It comes from what you do consistently."**
    """
    )

    st.caption("🧠 FUTUREMIND AI v1.3")

    st.caption("Learn Smarter • Plan Better • Grow Faster")

    st.caption("Developed with ❤️ by Sristi")

# ==========================================
# AI STUDY TUTOR
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

    # Suggested prompts
    st.markdown("### 💡 Try asking:")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("📘 Explain Newton's Laws"):
            st.session_state.messages = [
                {
                    "role": "user",
                    "content": "Explain Newton's Laws in simple language."
                }
            ]
            st.rerun()

        if st.button("🧮 Solve a Math Problem"):
            st.session_state.messages = [
                {
                    "role": "user",
                    "content": "Solve x² + 5x + 6 = 0 step by step."
                }
            ]
            st.rerun()

    with col2:

        if st.button("💻 Learn Python"):
            st.session_state.messages = [
                {
                    "role": "user",
                    "content": "Teach me Python loops with examples."
                }
            ]
            st.rerun()

        if st.button("🧪 Explain Photosynthesis"):
            st.session_state.messages = [
                {
                    "role": "user",
                    "content": "Explain photosynthesis for Class 8 students."
                }
            ]
            st.rerun()

    st.caption(
        f"💬 Messages in this conversation: {len(st.session_state.messages)}"
    )

    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    prompt = st.chat_input(
        "💬 Ask anything about studies..."
    )

    if prompt:

        # Show user message
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        # Generate AI response
        with st.chat_message("assistant"):

            with st.spinner("🧠 FUTUREMIND AI is thinking..."):

                answer = get_ai_response(
                    st.session_state.messages
                )

                # Increment analytics
                increment_counter("tutor")

                st.markdown(answer)

                pdf_file = create_pdf(
                    "FUTUREMIND AI Study Tutor",
                    answer
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.download_button(
                        "💾 Download TXT",
                        data=answer,
                        file_name="futuremind_answer.txt",
                        mime="text/plain",
                        use_container_width=True
                    )

                with col2:

                    st.download_button(
                        "📄 Download PDF",
                        data=pdf_file,
                        file_name="study_answer.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )

        # Save assistant response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    st.markdown("---")

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):

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
                increment_counter("quiz")

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
                increment_counter("roadmap")


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
                increment_counter("skill_gap")


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
                increment_counter("interview")


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
# ANALYTICS DASHBOARD
# ==========================================

elif feature == "📊 Analytics Dashboard":

    st.title("📊 FUTUREMIND AI Analytics")

    data = get_analytics()

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "📚 Tutor Questions",
            data["tutor"]
        )

        st.metric(
            "🚀 Roadmaps",
            data["roadmap"]
        )

        st.metric(
            "🎤 Interviews",
            data["interview"]
        )

    with col2:

        st.metric(
            "📝 Quizzes",
            data["quiz"]
        )

        st.metric(
            "📊 Skill Analyses",
            data["skill_gap"]
        )

    st.markdown("---")

    total = (
        data["tutor"]
        + data["quiz"]
        + data["roadmap"]
        + data["skill_gap"]
        + data["interview"]
    )

    st.success(
        f"🚀 Total AI Tasks Generated: {total}"
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