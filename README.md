# Q&A Bot for Network Security

This repository contains the Q&A Bot for Network Security, an AI-powered chatbot that allows users to ask questions on network security topics. The bot leverages documents stored in PDF format, vector embeddings, and the Groq API to generate responses. The project includes a web-based interface for users to interact with the bot.

---
# Execution Demo
![Execution Demo](./Screen%20Recording%20-%20Nov%208,%202024-VEED.gif)

---

## Project Description

The Q&A Bot assists users by providing answers to network security-related questions using natural language processing (NLP) and embeddings. The bot fetches answers based on relevant content from the provided documents (stored in PDF format). The responses also include sources for better context.

---

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

---

## Prerequisites

- **Python**: Version 3.7 or higher
- **Flask**: Web framework for Python
- **Git**: Version control
- **Node.js**: Required if using additional JS libraries for enhanced front-end features.

---

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

---

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
  
---

## Commands to Run the Code

1. **Initialize Git Repository and Push Changes**:
   ```bash
   git init
   git remote add origin <repository-url>
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   
2. **Run the Flask Application**:
     python app.py

     By default, the app runs on localhost:5000.

3. **Testing the App**:
Access the application by opening a browser and navigating to http://127.0.0.1:5000.

## Training Data and Data Formats

**PDFs in `pdfs` Directory**:
- Each PDF file contains lecture notes or other network security resources relevant to the Q&A bot.
- The PDFs are loaded into the system and processed using the `PyPDFLoader` class.
- Each document is divided into manageable chunks with the `RecursiveCharacterTextSplitter` function, creating smaller segments for more efficient processing and indexing.
- These chunks are transformed into vector embeddings and stored for later retrieval, ensuring that each document's contents are searchable based on user queries.

**Vector Database (`chroma_db`)**:
- All document embeddings are stored in the `chroma_db` directory using **Chroma**, a vector database optimized for similarity search.
- This vector store enables fast access to relevant content by performing similarity searches against the user’s query.
- During each query, Chroma retrieves the top matches from this database, ensuring responses are relevant and accurate.

---


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

---

## Features

- **Question Answering**: The bot provides answers based on content from documents stored in the `pdfs` directory, leveraging NLP for accurate retrieval.

- **Source Tracking**: Each response includes the source document’s name, offering users traceability and context for the provided answers.

- **Interactive Web UI**: Users interact with the bot via an intuitive web-based chat interface designed for seamless Q&A interactions.

- **Time-Stamped Messages**: Both user and bot messages display timestamps, providing a clear timeline of the conversation.

- **Dynamic Chat Interface**:
  - The chat interface uses JavaScript (in `app.js`) to create a dynamic user experience, allowing users to see messages appear in real-time without refreshing the page.
  - The chat area autoscrolls with each new message for user convenience.

- **Error Handling and User Feedback**:
  - If the bot encounters an error (e.g., API issues), it displays a user-friendly message and suggests actions, ensuring a smooth user experience.

- **Real-Time Query Processing**:
  - The app utilizes the Groq API for processing queries in real-time, ensuring responses are both quick and relevant.

- **Efficient Document Embedding**:
  - Leveraging Hugging Face’s embedding models, the bot stores pre-processed document embeddings for efficient similarity search during queries.

---

## Issues and Solutions

### Issue: API Connection Errors
- **Solution**: Check that the `GROQ_API_KEY` is correctly set and has not expired. If the API connection continues to fail, verify internet connectivity and review the console for detailed error messages.

### Issue: Bot Responses are Slow or Delayed
- **Solution**: Ensure the `chroma_db` vector database is properly optimized, especially if using large or numerous documents. Consider increasing server resources or using a faster embedding model if delays persist.

### Issue: PDF File Parsing Errors
- **Solution**: Verify that all PDF files in the `pdfs` directory are intact and have compatible formats. Use the `PyPDF2` library to troubleshoot parsing issues by testing individual files.

### Issue: Chat UI Display Issues
- **Solution**: Check the browser console (F12) for JavaScript errors in `app.js`. Ensure all static files (`style.css`, `app.js`) load correctly and confirm no conflicts with the HTML structure in `index.html`.

### Real-Time Issues You May Face

- **Memory Usage**: Processing large PDF files and storing embeddings can increase memory usage significantly, leading to performance degradation.
  - **Solution**: Break down large files into smaller chunks or limit the number of PDFs processed simultaneously.

- **Rate Limits with Groq API**: Exceeding rate limits may disrupt query processing.
  - **Solution**: Monitor API usage, optimize queries, and consider upgrading the API plan if rate limits are frequently hit.

- **Difficulty Debugging Errors in Embedding Models**:
  - **Solution**: Start with simpler models from Hugging Face or log detailed error messages during embedding to isolate issues.

---


## Suggestions and Feedback

### Suggestions for Further Development

- **Enhanced NLP Model**: To improve answer relevance, consider training a custom model with more network security-specific documents. This would refine the bot’s ability to answer complex questions accurately.

- **UI/UX Enhancements**:
  - Update `style.css` to make the chat interface more interactive, potentially incorporating animations or additional styling to create a more engaging user experience.
  - Provide options for dark and light modes for better accessibility.

- **Performance Optimization**:
  - Split and pre-process large PDF documents to reduce load times. Store embeddings in batches and periodically retrain Chroma database for optimal efficiency.
  - Consider indexing large documents or frequently accessed documents separately to reduce query time.

### Feedback for Future Improvements

- **Improve API Resilience**: Implement fallback mechanisms in case the Groq API is temporarily unavailable, allowing the bot to return an informative message rather than failing.

- **Data Privacy**: If using sensitive documents, consider implementing data encryption for all stored embeddings and implementing user authentication to restrict access.

- **Extending Functionality**:
  - Allow users to upload custom PDFs temporarily, enabling a more personalized Q&A experience.
  - Integrate with cloud storage services like AWS S3 or Google Cloud Storage for scalable document storage.

- **Deployment Recommendations**:
  - For wider accessibility, consider deploying on cloud platforms such as AWS or Azure. This will also allow scaling resources dynamically based on usage.

## References

### Primary Documentation
- **[LangChain Documentation](https://langchain.com/docs/)**: Detailed documentation for LangChain, covering its use for NLP and document retrieval.
- **[Flask Documentation](https://flask.palletsprojects.com/)**: Official Flask documentation for understanding web server and routing features.
- **[Groq API Documentation](https://groq.com/docs/)**: Information on Groq API usage, authentication, and advanced capabilities.

### Additional Resources
- **[Hugging Face Models](https://huggingface.co/models)**: Repository for choosing embedding models, such as `sentence-transformers`, to improve embedding quality and relevance.
- **[Chroma Documentation](https://docs.trychroma.com/)**: Guide for configuring Chroma as a vector store for efficient similarity search.

### Tutorials and Guides
1. **[How to Build Your Own AI Chatbot With ChatGPT API (2023) | Beebom]**: Step-by-step guide for setting up a chatbot using ChatGPT API.
2. **[How to Build Your Own AI Chatbot With ChatGPT API: a Step-by-Step Ultimate Guide | Softermii]**: In-depth guide on creating a chatbot with personalized responses using custom knowledge.
3. **[Build a Chatbot Based on Your Own Documents with ChatGPT | Vasos Koupparis]**: Instructions for setting up a document-based chatbot, leveraging custom data.
4. **[Create a Powerful Chatbot with ChatGPT Using Your Documents | Analytics Vidhya]**: A walkthrough on using ChatGPT and document embeddings for a personalized chatbot.
5. **[How to Train an AI Chatbot With Custom Knowledge Base Using ChatGPT API | Beebom]**: Techniques for training a chatbot with specific knowledge and deploying with ChatGPT API.
6. **[Create an Azure OpenAI, LangChain, ChromaDB, and Chainlit Chat App | Microsoft Community Hub]**: Guide for integrating LangChain and ChromaDB in Azure for a scalable AI chatbot.
7. **[How to create a private ChatGPT that interacts with your local documents - TechTalks]**: Steps for setting up a local document-interactive ChatGPT.
8. **[What Product People Need To Know About LangChain | CommandBar Blog]**: Overview of LangChain for product developers building AI applications.
9. **[Host a Llama 2 API on GPU for Free | by Yuhong Sun | Medium]**: Tutorial on hosting a free Llama 2 API with GPU support for resource-efficient applications.


### Other Relevant Resources
10. **[How to Build a Personalized Unlimited Quiz App in Minutes: ChatGPT API Edition - DEV Community]**: Guide on building a quiz app using ChatGPT API.
11. **[How to Build a Multiple Choice Quiz with Chat GPT | by S713FF3N | Dev Genius]**: Steps for building a multiple-choice quiz app leveraging ChatGPT's AI.

