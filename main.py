import streamlit as st

from utils import load_json, reset


st.title("Quiz de Culture Generale")


if "score" not in st.session_state:
    st.session_state.score = 0
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "feedback" not in st.session_state:
    st.session_state.feedback = None


file = load_json("questions.json")


if st.session_state.feedback:
    if st.session_state.feedback == "Correct":
        st.sidebar.success(st.session_state.feedback)
    else:
        st.sidebar.error(st.session_state.feedback)


if st.session_state.question_index < len(file):
    question = file[st.session_state.question_index]
    st.write(f"Question {st.session_state.question_index + 1} : ")
    st.write(question["question"])

    for option in question["options"]:
        if st.button(option):
            if option == question["correct"]:
                st.session_state.feedback = "Correct"
                st.session_state.score += 1
                st.session_state.question_index += 1
                st.rerun()

            else:
                st.session_state.feedback = f"Perdu ! La bonne réponse était {question["correct"]}"
                st.session_state.question_index += 1
                st.rerun()

else:
    st.write("Terminé !")
    st.write(f"Votre score est de {st.session_state.score} / {len(file)}")
    if st.button("Rejouer"):
        reset()


st.sidebar.write(f"Score actuel : {st.session_state.score}")
if st.sidebar.button("Recommencer"):
    reset()
