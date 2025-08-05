# LLM-Powered-PDF-Q-A-Assistant_final

# LLM-Powered PDF Q&A Assistant

🤖 A Streamlit web app that allows users to upload PDF documents and ask questions about their content using Large Language Models (LLMs) via OpenAI.

---

## Features

- Upload one or more PDF files via a web interface.
- Extract and index PDF text for semantic search.
- Answer user questions based on PDF content using OpenAI’s GPT models.
- Display retrieved relevant text passages alongside generated answers.
- Interactive and user-friendly Streamlit UI.

---

## Demo

*Add a link to a live demo here if available*

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- An OpenAI API key with available quota ([Get it here](https://platform.openai.com/account/api-keys))
- `pip` package manager

### Installation

1. Clone this repository:
    ```
    git clone https://github.com/yourusername/llm-pdf-qa.git
    cd llm-pdf-qa
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install required packages:
    ```
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root with your OpenAI API key:
    ```
    OPENAI_API_KEY=sk-your-openai-api-key
    ```

---

### Running the App

Start the Streamlit app with this command:


Open the local URL shown in your terminal (usually `http://localhost:8501`) to use the app. Upload PDFs and start asking questions!

---

## Project Structure

- `app.py`: Main Streamlit application script.
- `ingest.py`: Handles PDF ingestion and text extraction.
- `qa_chain.py`: Contains the logic for question answering using LLMs.
- `.env`: Stores environment variables such as OpenAI API key (not committed).
- `requirements.txt`: Python dependencies.
- Other helper modules & assets as needed.

---

## Troubleshooting

- **ModuleNotFoundError for some packages:**
  Ensure all dependencies are installed from `requirements.txt`.
  
- **OpenAI API key errors:**
  Make sure `.env` file is present **in the same folder as `app.py`** and contains a valid `OPENAI_API_KEY`.

- **Quota or rate limit exceeded:**
  Check your OpenAI dashboard for usage and billing status.

---

## Deploying to the Cloud

You can deploy this app easily to platforms like [Streamlit Community Cloud](https://streamlit.io/cloud), [Heroku](https://www.heroku.com/), or [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/).

### Example: Deploy to Streamlit Community Cloud

1. Push your repository to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and sign in.
3. Click **New app**, select your GitHub repo and branch.
4. Set the environment variable `OPENAI_API_KEY` in the Streamlit Cloud settings.
5. Deploy and share the live URL.

For Heroku or AWS, you will need additional setup like `Procfile`, Docker, or Elastic Beanstalk configs.

---

## License

Specify your license here, e.g., MIT License.

---

## Acknowledgements

- Built with [Streamlit](https://streamlit.io/)
- Powered by [OpenAI GPT](https://openai.com/)
- Uses [python-dotenv](https://pypi.org/project/python-dotenv/) for environment variable management.

---

## Contact

Yamini-datascientist – [yamini.rc59@gmail.com] 
Project Link: https://github.com/yourusername/llm-pdf-qa
