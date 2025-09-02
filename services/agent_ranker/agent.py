from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from prompt import promptMessage
from pydantic import BaseModel
load_dotenv()

class Idea(BaseModel):
    slug: str
    user: str
    
class Ideas(BaseModel):
    ideas: list[Idea]

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions = promptMessage,
    response_model=Ideas
)

def getArticlesIa(listArticles):
    message = agent.run(message=listArticles)
    return message.content.ideas