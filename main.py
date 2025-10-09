from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor

# Load environment variables from a .env file
load_dotenv()

# Define the response model using Pydantic
class ResponseModel(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

parser = PydanticOutputParser(pydantic_object=ResponseModel)

prompt = ChatPromptTemplate.from_messages([
    ("system", 
     """
     You are a helpful assistant that provides concise summaries on given topics.
     Answer the query and use the necessary tools to gather information.
     Wrap the output in this format and provide no other text \n{format_instructions}
     """,
     ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=[]
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[],
    verbose=True
)

raw_response = agent_executor.invoke({"query": "What is the impact of climate change on global agriculture?"})
print("--- Raw Response ---")
print(raw_response)

output_string = raw_response.get('output', '')

# Parse the output string into the structured response model
structured_response = parser.parse(output_string)
print(structured_response.topic)
