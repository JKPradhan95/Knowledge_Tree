from django.shortcuts import render
from google import generativeai
import re

# Create your models here.


def clean_topic(raw_input):
    topic = raw_input.strip()
    phrases_to_remove = [
        r"^i want to ", r"^i would like to ", r"^my goal is to ", r"^i aim to ",
        r"^i plan to ", r"^i wish to ", r"^to "
    ]

    for pattern in phrases_to_remove:
        topic = re.sub(pattern, "", topic, flags=re.IGNORECASE)

    topic = topic.strip(" .!?").strip()
    return topic

def smart_goal_formatter(topic):
    topic = topic.strip()

    fixes = {
        r"\b be master in\b": "become a master in",
        r"\b mastery of\b": "master",
        r"\b expert in\b": "gain expertise in",
        r"\b be an expert in\b": "become an expert in",
        r"\b my skills in\b": "improve my skills in"
    }

    for pattern, replacement in fixes.items():
        topic = re.sub(pattern, replacement, topic, flags=re.IGNORECASE)

    topic = re.sub(r'\bpython\b', 'Python', topic, flags=re.IGNORECASE)
    topic = re.sub(r'\bai\b', 'AI', topic, flags=re.IGNORECASE)
    topic = re.sub(r'\bml\b', 'ML', topic, flags=re.IGNORECASE)

    return topic

# Gemini AI API key
generativeai.configure(api_key="")
model = generativeai.GenerativeModel(model_name="gemini-1.5-pro")
chat = model.start_chat(history=[])

def chatbot(user_input):
    response = chat.send_message(user_input)
    return response.text


def topic_input_view(request):  # Layer1
    if request.method == "POST":
        topic = request.POST.get("topic")
        w_questions = [
                        f"What is {topic}?",
                        f"When did {topic} originate or become relevant?",
                        f"Where is {topic} used or applied?",
                        f"Who is involved in or benefits from {topic}?",
                        f"Why is {topic} important or needed?",
                        f"How does {topic} work or how can it be done?"
                    ]
        request.session['topic'] = topic
        request.session['layer1_questions'] = w_questions
        return render(request, "layer1.html", {"topic": topic, "questions": w_questions})
    return render(request, "topic_input.html")


def layer2_view(request):
    if request.method == "POST":
        question = request.POST.get("question")
        topic = request.session.get("topic", "")
        try:
            answer = chatbot(question)
        except:
            answer = "Could not fetch answer."

        nested_questions = [
                            f"What is meant by {topic}?",
                            f"When does it matter {topic}?",
                            f"Where can we see {topic}?",
                            f"Who is related to {topic}?",
                            f"Why is it important to ask {topic}?",
                            f"How to explore or understand {topic}?"
                        ]

        request.session['layer2_question'] = question
        request.session['layer2_answer'] = answer
        request.session['layer2_questions'] = nested_questions

        return render(request, "layer2.html", {
            "question": question,
            "answer": answer,
            "nested_questions": nested_questions
        })


def layer3_view(request):
    if request.method == "POST":
        question = request.POST.get("question")
        topic = request.session.get('topic')

        try:
            answer = chatbot(question)
        except:
            answer = "Gemini failed to respond."

        nested_questions = [f"What needs to be done to {topic}?", 
                            f"When is India aiming to become {topic}?", 
                            f"Where we are now {topic}?", 
                            f"Who is involved in {topic}?", 
                            f"Why is necessary {topic}?", 
                            f"How is the planning to achieve the goal of becoming {topic}?"
                            ]

        return render(request, "layer3.html", {
            "question": question,
            "answer": answer,
            "nested_questions": nested_questions
        })

def layer4_view(request):
    if request.method == "POST":
        question = request.POST.get("question")
        topic = request.session.get('topic')
        try:
            answer = chatbot(question)
        except:
            answer = "Gemini failed to respond."

        nested_questions = [f"What specific actions and strategies need to be implemented to {topic}?", 
                            f"When should these actions be taken to {topic}?", 
                            f"Where in India should the key initiatives and infrastructure development efforts be focused to {topic}?", 
                            f"Who needs to be involved in the effort to{topic}?",
                            f" Why is it beneficial to {topic}?", 
                            f"How can we overcome challenges to  {topic}?"]

        return render(request, "layer4.html", {
            "question": question,
            "answer": answer,
            "nested_questions": nested_questions
        })


def layer5_view(request):
    if request.method == "POST":
        question = request.POST.get("question")
        topic = request.session.get('topic')
        try:
            answer = chatbot(question)
        except:
            answer = "Gemini failed to respond."

        nested_questions = [f" What detailed technological roadmaps need to be developed to {topic}?", 
                            f"When expect first Indian advanced node test chips {topic}?", 
                            f"What criteria for new chip manufacturing cluster locations need to be met {topic}?", 
                            f"Who relates to {topic}?", 
                            f"Why is reduced reliance on specific chip import countries a national security issue  {topic}?", 
                            f"How will the Semiconductor Leadership Council ensure timely decisions to  {topic}?"]

        return render(request, "layer5.html", {
            "question": question,
            "answer": answer,
            "nested_questions": nested_questions
        })
    
def layer6_view(request):
    if request.method == "POST":
        question = request.POST.get("question")
        topic = request.session.get('topic')
        try:
            answer = chatbot(question)
        except:
            answer = "Gemini failed to respond."

        nested_questions = [f"What criteria for new chip manufacturing cluster locations need to be met {topic}?", 
                            f"When expect first Indian advanced node test chips for {topic}?", 
                            f"Where should new chip manufacturing cluster locations be located that sweatable for {topic}?", 
                            f"Who in MeitY oversees semiconductor tech collaborations can help to {topic}?", 
                            f"Why would a chip export disruption cripple India's defense and infrastructure maintenance on its path to {topic}?", 
                            f"How will the Council's structure speed up chip project approvals in the mission to{topic}?"]

        return render(request, "layer6.html", {
            "question": question,
            "answer": answer,
            "nested_questions": nested_questions
        })
    
def layer7_view(request):
    if request.method == "POST":
        question = request.POST.get("question")
        topic = request.session.get('topic')
        try:
            answer = chatbot(question)
        except:
            answer = "Gemini failed to respond."

        nested_questions = [f"What percent and duration of R&D tax breaks for indigenous high-performance chip IP to support {topic}?", 
                            f"When is the projected date for the first sub-10nm test chip production in India on its journey to {topic}?", 
                            f"Where in India are the primary regions being developed for new chip fabs in the effort to {topic}?", 
                            f"Who are the key MeitY officials leading the US/EU advanced chip tech transfer talks to {topic}?", 
                            f"Why are specific advanced chips from limited suppliers a critical vulnerability for India's defense and communication in its pursuit to {topic}?", 
                            f"How will the Council's direct reporting or fast-track committees speed up chip project approvals to {topic}?"]

        return render(request, "layer7.html", {
            "question": question,
            "answer": answer,
            "nested_questions": nested_questions
        })
