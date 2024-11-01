from groq import Groq

groq_client = Groq(api_key="YOUR_GROQ_API_HERE")

def text_summarization_tool_function(text):
    prompt = f"Summarize the following text:\n\n{text}\n\nSummary"
    response = groq_client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": prompt
        }],
        model="llama3-8b-8192",
        temperature=0.0
    )