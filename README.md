# Ollama Web Search API

This project integrates **Ollama (Dolphin-Mistral)** with **LangChain** and **SerpAPI** to provide real-time web search capabilities. It runs as a **FastAPI server**, allowing Open WebUI or other clients to fetch live data.

## 🚀 Features
- Uses **Dolphin-Mistral** model in Ollama.
- Fetches real-time information using **SerpAPI**.
- Provides a **FastAPI endpoint (`/realtime-search`)** for integration with Open WebUI.
- Supports **interactive CLI mode**.

---

## 🛠️ Installation

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/ollama-web-search.git
cd ollama-web-search
```

### 2️⃣ **Install Dependencies**
Ensure you have **Python 3.11+** installed, then run:
```bash
pip install -r requirements.txt
```
If you don’t have a `requirements.txt` file, install manually:
```bash
pip install langchain langchain-community langchain-ollama google-search-results fastapi uvicorn colorama
```

### 3️⃣ **Set Up Your SerpAPI Key**
Before running, you must **set your SerpAPI key**:
```bash
export SERPAPI_API_KEY="your_serpapi_key"   # For Linux/macOS
set SERPAPI_API_KEY=your_serpapi_key        # For Windows (PowerShell)
```

---

## 🏃 Running the API Server
Once everything is set up, start the **FastAPI server**:
```bash
python ollama_web_search.py
```
If successful, you should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 🔗 **Testing the API**
After starting the server, you can test it:
```bash
curl "http://127.0.0.1:8000/realtime-search?query=What is the current time?"
```
Or open in a browser:
```
http://127.0.0.1:8000/realtime-search?query=Who won the latest election?
```

---

## 🖥️ **Using Open WebUI Integration**
1. **Open WebUI** (`http://localhost:3000`).
2. Go to **Settings > Custom API Endpoints**.
3. Click **"Add New Endpoint"** and enter:
   - **Name**: `Real-Time Search`
   - **URL**: `http://127.0.0.1:8000/realtime-search?query={query}`
   - **Method**: `GET`
4. **Save and enable it.**
5. **Now you can ask Open WebUI real-time questions!** 🎉

---

## 📌 **Interactive CLI Mode**
If you prefer using the command line, simply run:
```bash
python ollama_web_search.py
```
Then, type any question:
```
Ask me anything: What is the current time and date?
```
To exit, type `exit`.

---

## 🤝 Contributing
Pull requests and issues are welcome! Feel free to fork this project and submit improvements.

---

## 📜 License
This project is licensed under the **MIT License**.

