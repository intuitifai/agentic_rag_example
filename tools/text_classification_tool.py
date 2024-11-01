from groq import Groq

groq_client = Groq(api_key="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")

def text_classification_tool_function(text):
    prompt = (
        f"Classify the following tweet as Positive, Negative or Neutral:\n\n"
        f"{text}\n\nClassification:"
    )
    response = groq_client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": prompt
        }],
        model="llama3-8b-8192",
        temperature=0.0
    )
    return response.choices[0].message.content