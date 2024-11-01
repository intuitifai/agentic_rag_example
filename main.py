from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from tools import calculator_tool, repl_tool, text_similarity_tool, text_summarization_tool, text_classification_tool
from langchain_groq import ChatGroq

tools = [
    Tool(name='REPL', func=repl_tool.repl_tool_function, description='Executes Code.'),
    Tool(name='Calculator', func=calculator_tool.calculator_tool_function, description='Performs Basic calculation'),
    Tool(name='Text Classification', func=text_classification_tool.text_classification_tool_function, description='Classifies the tweet'),
    Tool(name='Text Summarization', func=text_summarization_tool.text_summarization_tool_function, description='Summarizes the tweet'),
    Tool(name='Text Similarity', func=text_similarity_tool.text_similarity_tool_function, description='Finds similar text')
]

llm = ChatGroq(
    model="llama3-8b-8192",  # Ensure this model ID is correct
    temperature=0.7,
    api_key="YOUR_GROQ_API_HERE"
)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent='zero-shot-react-description',
    verbose=True,
    handle_parsing_errors=True,
)

def agent_pipeline(query):
    response = agent({"input": query})
    print(response['output'])
    
if __name__=='__main__':
    agent_pipeline("What would be the output of the code: sum(i for i in range(10))")
    agent_pipeline("What is the value of the multiplication: 108*1203")
    agent_pipeline("Is there any tweet where we team managed a last-minute save?")