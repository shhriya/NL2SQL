# 🎧 NL2SQL Spotify Dataset Assistant (BigQuery + Gemini)

This is an interactive terminal-based chatbot that answers natural language questions about the **Spotify 2023 dataset** using:

- 🧠 Google Gemini 1.5 Pro
- 🗃️ Google BigQuery
- 📦 Python + Docker

---

## 📂 Folder Structure

nl2sql_spotify_project/
│
├── main.py                  # Entry point
├── .env                     # API and auth secrets
├── requirements.txt         # Python dependencies
├── Dockerfile               # Container setup
├──service-account.json
│
├── data/
│ └── spotify-2023.csv       # csv data
│
├── prompts/
│ └── system_prompt.txt      # Prompt to guide Gemini
│
├── metadata/
│ └── spotify_metadata.json  # Table + column descriptions
│
├── utils/
│  ├── bigquery_client.py    # BigQuery setup + query function
│  ├── gemini_client.py      # Gemini API wrapper
│  └── memory.py             # Memory for past Q/A




---

## 🔧 Setup Instructions

### 1. Clone + Install

```bash
git clone https://github.com/yourusername/nl2sql_spotify_project.git
cd nl2sql_spotify_project
python -m venv venv
source venv/bin/activate  # Or venv\Scripts\activate on Windows
pip install -r requirements.txt
Add your environment variables
   Create a .env file:
   GOOGLE_API_KEY=your_gemini_api_key_here
   GOOGLE_APPLICATION_CREDENTIALS=SERVICE-ACCOUNT.json
Download your Google Cloud service account JSON key and place it in the root directory as `SERVICE-ACCOUNT.json`.

Run the app
python main.py


Type questions like:
"top 5 most streamed songs"
"tracks by taylor swift released in 2023"


Run with Docker
Build the image:
   docker build -t nl2sql-spotify .
Run the container:
   docker run -it \
      -e GOOGLE_API_KEY=your_gemini_api_key_here \
      -e GOOGLE_APPLICATION_CREDENTIALS=/app/api-project-456117-xxxx.json \
      -v "$(pwd)/api-project-456117-xxxx.json:/app/api-project-456117-xxxx.json" \
      nl2sql-spotify



### 💡 Features
- Converts user questions into SQL using Gemini 1.5 Pro
- Executes SQL on BigQuery
- Returns natural language answers
- Maintains short-term memory (last 3 Q/A)
- Case-insensitive LIKE filtering for text fields

### 🔍 Example

**Input:**
> Show me the most streamed song by Taylor Swift

**SQL Generated:**
SELECT track_name, streams
FROM spotify_dataset.spotify_2023
WHERE LOWER(artists_name) LIKE '%taylor swift%'
ORDER BY streams DESC
LIMIT 1

**Answer:**
The most streamed song by Taylor Swift is "Anti-Hero" with 1.2B streams.



🧠 Credits
Google Cloud BigQuery
Gemini API
LangChain (Optional)
Built by Shriya
