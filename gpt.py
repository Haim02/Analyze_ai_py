import os
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
import pandas as pd

os.environ["OPENAI_API_KEY"] = "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"

path = "DEQA - Exam"
os.chdir(path)

for file in os.listdir():
    with open(file, 'r') as f:
        df = pd.read_json(file)

pd_agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=True)

pd_agent.run("what is the product")
pd_agent.run("Analyze the product and compare it to similar products")
