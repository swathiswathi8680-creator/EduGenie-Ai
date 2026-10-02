import google.generativeai as genai

def explain_topic(topic: str) -> str:
    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")
        prompt = f"Explain the concept of '{topic}' in a simple and clear way for a school student."
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error in Explanation: {e}"
