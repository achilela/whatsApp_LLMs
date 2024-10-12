import warnings
warnings.filterwarnings("ignore")

!pip install --upgrade --quiet langchain
!pip install --quiet langchain-community
!pip install --upgrade --quiet langchain-together

## setting up the language model
from langchain_together import ChatTogether
import api_key

llm = ChatTogether(api_key=api_key.api,temperature=0.0, model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo")

! pip install youtube_transcript_api
! pip install pytube

## import the youtube documnent loader from LangChain
from langchain_community.document_loaders import YoutubeLoader

video_url = 'https://www.youtube.com/watch?v=gaWxyWwziwE'
loader = YoutubeLoader.from_youtube_url(video_url, add_video_info=False)
data = loader.load()

# show the extracted page content
data[0].page_content

# This code creates a list of messages for the language model:
# 1. A system message with instructions on how to summarize the video transcript
# 2. A human message containing the actual video transcript

# The messages are then passed to the language model (llm) for processing
# The model's response is stored in the 'ai_msg' variable and returned

messages = [
    (
        "system", 
        """Read through the entire transcript carefully.
           Provide a concise summary of the video's main topic and purpose.
           Extract and list the five most interesting or important points from the transcript. For each point: State the key idea in a clear and concise manner.

        - Ensure your summary and key points capture the essence of the video without including unnecessary details.
        - Use clear, engaging language that is accessible to a general audience.
        - If the transcript includes any statistical data, expert opinions, or unique insights, prioritize including these in your summary or key points.""",
    ),
    ("human", data[0].page_content),
]
ai_msg = llm.invoke(messages)
ai_msg

# Set up a prompt template for summarizing a video transcript using LangChain

# Import necessary classes from LangChain
from langchain.prompts import PromptTemplate
from langchain import LLMChain

# Define a PromptTemplate for summarizing video transcripts
# The template includes instructions for the AI model on how to process the transcript
product_description_template = PromptTemplate(
    input_variables=["video_transcript"],
    template="""
    Read through the entire transcript carefully.
           Provide a concise summary of the video's main topic and purpose.
           Extract and list the five most interesting or important points from the transcript. 
           For each point: State the key idea in a clear and concise manner.

        - Ensure your summary and key points capture the essence of the video without including unnecessary details.
        - Use clear, engaging language that is accessible to a general audience.
        - If the transcript includes any statistical data, expert opinions, or unique insights, 
        prioritize including these in your summary or key points.
    
    Video transcript: {video_transcript}    """
)

## invoke the chain with the video transcript 
chain = LLMChain(llm=llm, prompt=product_description_template)

# Run the chain with the provided product details
summary = chain.invoke({
    "video_transcript": data[0].page_content
})

summary['text']

from Ipython.display import Markdown, display

display(Markdown(summary['text']))




