# Q&A Bot for Network Security

This repository contains the Q&A Bot for Network Security, an AI-powered chatbot that allows users to ask questions on network security topics. The bot leverages documents stored in PDF format, vector embeddings, and the Groq API to generate responses. The project includes a web-based interface for users to interact with the bot.

## Project Description

The Q&A Bot assists users by providing answers to network security-related questions using natural language processing (NLP) and embeddings. The bot fetches answers based on relevant content from the provided documents (stored in PDF format). The responses also include sources for better context.

## System Architecture

1. **Frontend (HTML, CSS, JavaScript)**:
   - Displays the user interface, where users can enter questions and view answers.
   - Manages user input and response display in the chat format.

2. **Backend (Python, Flask)**:
   - Routes requests and processes queries.
   - Loads and manages the document embeddings in ChromaDB.
   - Handles the interaction with Groq API to retrieve relevant answers from the model.

3. **Database (Chroma)**:
   - Stores vector embeddings for faster retrieval.
   - Performs similarity searches on queries to fetch the most relevant document content.

## Prerequisites

- **Python**: Version 3.7 or higher
- **Flask**: Web framework for Python
- **Git**: Version control
- **Node.js**: Required if using additional JS libraries for enhanced front-end features.

## Requirements

1. **Python Libraries**:
   - Install Python dependencies using:
     ```bash
     pip install -r requirements.txt
     ```
     The requirements file should include:
     - `Flask`
     - `langchain`
     - `ChromaDB`
     - `HuggingFaceEmbeddings`
     - `Groq API`
   
2. **Environment Variables**:
   - Set your Groq API key as an environment variable:
     ```bash
     export GROQ_API_KEY="your_api_key_here"
     ```

3. **Folder Setup**:
   - Place PDF resources in the `pdfs` directory.
   - Store vector embeddings in the `chroma_db` directory.

## Adopted Libraries

- **Flask**: Provides server functionality.
- **LangChain**: Manages document embeddings and retrieval.
- **HuggingFaceEmbeddings**: Generates vector embeddings.
- **Chroma**: Serves as the vector store for fast retrieval.
- **Groq API**: Powers the LLM for answer generation.

## Flow of Execution

1. **Startup**:
   - Run the Flask application to initiate the server.
   - Loads or creates vector embeddings for all PDF documents in the `pdfs` directory.

2. **User Interaction**:
   - User enters a question via the web interface.
   - JavaScript sends an AJAX request to the Flask backend.

3. **Processing Query**:
   - The question is processed through the Groq-powered LLM, retrieving the most relevant response from the vector embeddings.

4. **Response**:
   - The bot returns the answer along with the source document, if available.

## Commands to Run the Code

1. **Initialize Git Repository and Push Changes**:
   ```bash
   git init
   git remote add origin <repository-url>
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   
2. **Run the Flask Application**:
 ```bash
     python app.py
     ```
By default, the app runs on localhost:5000.

4. **Testing the App**:
Access the application by opening a browser and navigating to http://127.0.0.1:5000.

## Training Data and Data Formats
**PDFs in pdfs Directory**:
Each PDF contains lecture notes or other resources.
PDF content is split and converted into vector embeddings using the RecursiveCharacterTextSplitter function, ensuring each document is indexed.

**Vector Database**:
Stored in chroma_db.
Used for quick access to content when processing user queries.


## Step-by-Step Instructions for Execution

1. **Set Up Virtual Environment**:
python -m venv env
source env/bin/activate  # Windows: .\env\Scripts\activate

2. **Install Required Libraries**:
pip install -r requirements.txt

3. **Load or Create Vector Embeddings**:
Run app.py to initialize the vector database or create embeddings from PDF files if they don’t exist.

4. **Start Flask Application**:
Run python app.py to start the web server.

5 **Navigate to Web Interface**:
Open http://localhost:5000 in a browser.
Enter a network security question and view the response in the chat window.


## Features
Question Answering: The bot provides answers based on documents in the pdfs directory.
Source Tracking: Each response includes the document source.
Interactive Web UI: Users can interact with the bot via a web-based chat interface.
Time-stamped Messages: Displays both user and bot messages with timestamps for clarity.

## Issues and Solutions
**Issue: Bot not responding correctly**
Solution: Ensure all dependencies are installed, and the GROQ_API_KEY environment variable is set.

**Issue: PDF Files Not Loading**
Solution: Check that PDFs are in the pdfs directory and have read permissions.

**Issue: Chat UI Errors**
Solution: Inspect the console in Developer Tools (F12) for errors in app.js.

## Suggestions and Feedback
Enhance Answer Accuracy: Add more network security-related documents to improve the bot’s knowledge base.
Improve UI: Customize style.css to make the chat interface more engaging.
Performance Tuning: Index larger files separately to improve load times.

## References

### Primary Documentation
- **[LangChain Documentation](https://langchain.com/docs/)**: Detailed documentation for LangChain, covering its use for NLP and document retrieval.
- **[Flask Documentation](https://flask.palletsprojects.com/)**: Official Flask documentation for understanding web server and routing features.
- **[Groq API Documentation](https://groq.com/docs/)**: Information on Groq API usage, authentication, and advanced capabilities.

### Additional Resources
- **[Hugging Face Models](https://huggingface.co/models)**: Repository for choosing embedding models, such as `sentence-transformers`, to improve embedding quality and relevance.
- **[Chroma Documentation](https://docs.trychroma.com/)**: Guide for configuring Chroma as a vector store for efficient similarity search.

### Tutorials and Guides
1. **[How to Build Your Own AI Chatbot With ChatGPT API (2023) | Beebom](https://beebom.com/how-to-build-your-own-ai-chatbot-with-chatgpt-api/)**: Step-by-step guide for setting up a chatbot using ChatGPT API.
2. **[How to Build Your Own AI Chatbot With ChatGPT API: a Step-by-Step Ultimate Guide | Softermii](https://www.softermii.com/blog/build-your-own-ai-chatbot-ultimate-guide)**: In-depth guide on creating a chatbot with personalized responses using custom knowledge.
3. **[Build a Chatbot Based on Your Own Documents with ChatGPT | Vasos Koupparis](https://vasos-koupparis.com/build-chatbot-chatgpt-documents/)**: Instructions for setting up a document-based chatbot, leveraging custom data.
4. **[Create a Powerful Chatbot with ChatGPT Using Your Documents | Analytics Vidhya](https://www.analyticsvidhya.com/blog/2023/02/create-powerful-chatbot-using-your-documents/)**: A walkthrough on using ChatGPT and document embeddings for a personalized chatbot.
5. **[How to Train an AI Chatbot With Custom Knowledge Base Using ChatGPT API | Beebom](https://beebom.com/how-to-train-ai-chatbot-custom-knowledge-base/)**: Techniques for training a chatbot with specific knowledge and deploying with ChatGPT API.
6. **[Create an Azure OpenAI, LangChain, ChromaDB, and Chainlit Chat App | Microsoft Community Hub](https://techcommunity.microsoft.com/t5/apps/create-azure-openai-langchain-chromadb-and-chainlit-chat-app/ba-p/3822022)**: Guide for integrating LangChain and ChromaDB in Azure for a scalable AI chatbot.
7. **[How to create a private ChatGPT that interacts with your local documents - TechTalks](https://bdtechtalks.com/2023/03/14/private-chatgpt-local-documents/)**: Steps for setting up a local document-interactive ChatGPT.
8. **[What Product People Need To Know About LangChain | CommandBar Blog](https://commandbar.com/blog/langchain-guide-product-people)**: Overview of LangChain for product developers building AI applications.
9. **[Host a Llama 2 API on GPU for Free | by Yuhong Sun | Medium](https://medium.com/@yuhongsun/host-llama-2-api-on-gpu-free/)**: Tutorial on hosting a free Llama 2 API with GPU support for resource-efficient applications.


### Other Relevant Resources
10. **[How to Build a Personalized Unlimited Quiz App in Minutes: ChatGPT API Edition - DEV Community](https://dev.to/devguy/how-to-build-personalized-quiz-app-using-chatgpt-api)**: Guide on building a quiz app using ChatGPT API.
11. **[How to Build a Multiple Choice Quiz with Chat GPT | by S713FF3N | Dev Genius](https://devgenius.io/how-to-build-a-multiple-choice-quiz-chat-gpt)**: Steps for building a multiple-choice quiz app leveraging ChatGPT's AI.

