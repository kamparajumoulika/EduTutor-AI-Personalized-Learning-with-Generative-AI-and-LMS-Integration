import gradio as gr

# Feature 1: Concept Clarifier
def clarify_concept(topic, age):
    # This simulates an explanation tailored to the child's age
    return (f"Here's a simple explanation of '{topic}' suitable for a {age}-year-old:\n\n"
            f"{topic} is an important concept that you can understand by thinking about it like this...")

# Feature 2: Mood-based Learning Method
def mood_based_learning(topic, mood):
    # Suggests a learning method based on mood with realistic text
    suggestions = {
        "😓 Tired": f"If you're tired, try quick visual summaries and simple examples of {topic} to keep it light.",
        "😐 Okay": f"Since you're feeling okay, let's do a short quiz of 5 questions on {topic} to test your understanding.",
        "😊 Ready": f"You're ready to dive deep! Here's a detailed explanation and practice problems on {topic}."
    }
    return suggestions.get(mood, f"Let's explore {topic} in a simple way.")

# Feature 3: Voice to Concept
def voice_input_concept(voice_text):
    # Converts voice transcription into a clear concept explanation
    return (f"Based on your input, here's a clear explanation of the topic:\n\n{voice_text}\n\n"
            "This is a key idea you should focus on when learning this topic.")

# Feature 4: Quick Quiz Generator
def generate_quiz(topic):
    # Generates example quiz questions (static placeholders)
    quiz = (
        f"Quiz on {topic}:\n"
        "1. What is the main idea of this topic?\n"
        "2. Can you give an example related to it?\n"
        "3. Why is it important?\n"
        "4. How can you apply it in real life?\n"
        "5. What is one challenge when learning this topic?"
    )
    return quiz

# Feature 5: Summary Generator
def generate_summary(topic):
    # Provides a short summary of the topic (static placeholder)
    return (f"{topic} is a fundamental subject that involves understanding the key principles and applying them "
            "in various situations. Mastering this topic helps build a strong foundation for advanced learning.")

# Feature 6: Study Tips Generator
def study_tips(topic):
    # Provides generic but useful study tips
    tips = (
        f"Study Tips for {topic}:\n"
        "- Break your study time into focused sessions.\n"
        "- Use visual aids like charts and diagrams.\n"
        "- Practice with quizzes and flashcards.\n"
        "- Teach someone else what you learned.\n"
        "- Take regular breaks to stay fresh."
    )
    return tips

# Gradio UI Setup
with gr.Blocks() as app:
    gr.Markdown("# 🎓 EduTutor AI: Personalized Learning")

    with gr.Tab("1. Concept Clarifier"):
        topic1 = gr.Textbox(label="Enter Topic")
        age1 = gr.Slider(8, 18, step=1, label="Choose Age Level")
        btn1 = gr.Button("Clarify Concept")
        out1 = gr.Textbox(label="Explanation")
        btn1.click(clarify_concept, inputs=[topic1, age1], outputs=out1)

    with gr.Tab("2. Mood-to-Method Learning"):
        topic2 = gr.Textbox(label="Enter Topic")
        mood = gr.Radio(["😓 Tired", "😐 Okay", "😊 Ready"], label="Your Mood")
        btn2 = gr.Button("Get Learning Method")
        out2 = gr.Textbox(label="AI Suggestion")
        btn2.click(mood_based_learning, inputs=[topic2, mood], outputs=out2)

    with gr.Tab("3. Voice to Concept"):
        voice = gr.Textbox(label="Type or Paste Voice Transcription")
        btn3 = gr.Button("Generate Explanation")
        out3 = gr.Textbox(label="Explanation")
        btn3.click(voice_input_concept, inputs=voice, outputs=out3)

    with gr.Tab("4. Quick Quiz Generator"):
        topic4 = gr.Textbox(label="Enter Topic")
        btn4 = gr.Button("Generate Quiz")
        out4 = gr.Textbox(label="Quiz Questions")
        btn4.click(generate_quiz, inputs=topic4, outputs=out4)

    with gr.Tab("5. Summary Generator"):
        topic5 = gr.Textbox(label="Enter Topic")
        btn5 = gr.Button("Generate Summary")
        out5 = gr.Textbox(label="Summary")
        btn5.click(generate_summary, inputs=topic5, outputs=out5)

    with gr.Tab("6. Study Tips Generator"):
        topic6 = gr.Textbox(label="Enter Topic")
        btn6 = gr.Button("Get Study Tips")
        out6 = gr.Textbox(label="Study Tips")
        btn6.click(study_tips, inputs=topic6, outputs=out6)

app.launch()