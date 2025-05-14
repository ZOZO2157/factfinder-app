import streamlit as st
import random

st.set_page_config(page_title="FactFinder: The Misinformation Challenge", layout="centered")

# Sample Quiz Questions
questions = [
    {
        "text": "A tweet claims that drinking bleach cures COVID-19.",
        "options": ["True", "False", "Misleading"],
        "answer": "False"
    },
    {
        "text": "An article states that climate change is a hoax.",
        "options": ["True", "False", "Misleading"],
        "answer": "Misleading"
    },
    {
        "text": "WHO recommends washing hands to prevent virus spread.",
        "options": ["True", "False", "Misleading"],
        "answer": "True"
    }
]

# Shuffle questions once per session
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = random.sample(questions, len(questions))
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.quiz_complete = False

st.title("\U0001F9E0 FactFinder: The Misinformation Challenge")

st.markdown("""
**Purpose:** Improve students' ability to recognize and debunk misinformation through fun, interactive quizzes.
""")

if not st.session_state.quiz_complete:
    q = st.session_state.shuffled_questions[st.session_state.current_q]

    st.markdown(f"### Question {st.session_state.current_q + 1}")
    st.write(q["text"])

    choice = st.radio("Select the correct classification:", q["options"])

    if st.button("Submit Answer"):
        if choice == q["answer"]:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect. The correct answer was **{q['answer']}**.")

        st.session_state.current_q += 1

        if st.session_state.current_q >= len(st.session_state.shuffled_questions):
            st.session_state.quiz_complete = True
        st.experimental_rerun()
else:
    st.subheader("🎉 Quiz Complete!")
    st.markdown(f"**Your Score:** {st.session_state.score} / {len(questions)}")

    if st.session_state.score == len(questions):
        st.success("Excellent! You've mastered spotting misinformation.")
    elif st.session_state.score >= 2:
        st.info("Good job! But there's still room to improve.")
    else:
        st.warning("Keep practicing to sharpen your fact-checking skills.")

    if st.button("Restart Quiz"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()
