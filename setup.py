import setuptools
setuptools.setup(     
     name="rag-module",     
     version="0.0.1",
     python_requires=">=3.11",   
     packages=["rag_pkg"],
     install_requires=[
         "langchain>=0.3",
         "langchain-core>=0.3",
         "langchain-openai>=0.2",
         "langchain-pinecone>=0.2",
     ]
)