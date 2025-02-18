# AI-Powered SEO Content Rewriter 🚀

This project provides an **AI-powered SEO content rewriting tool** that extracts knowledge from a given webpage and rewrites user-provided content by optimizing it for SEO, improving readability, and maintaining factual accuracy.

## Key Features 🌟
- **Web Crawling**: The tool crawls a webpage and extracts its content using `crawl4ai` 🌐.
- **SEO Content Rewriting**: The extracted website content is used to optimize and rewrite input content for SEO improvements, keyword placement, and readability ✍️.
- **Efficient Content Retrieval:** The tool utilizes FAISS for semantic content retrieval and SentenceTransformer for text embedding and encoding to ensure accurate and effective content processing ⚡.
- **Generative AI**: `Ollama (DeepSeek)` is used to generate SEO-optimized content based on the extracted website knowledge 🤖.

## Tech Stack 🛠️
- **Python**: Backend programming language 🐍
- **Gradio**: User interface for easy interaction 💻
- **Ollama (DeepSeek)**: LLM for content generation 🔮
- **FAISS**: Vector search library for efficient content retrieval 🔍
- **SentenceTransformers**: Embedding model for text-to-vector conversion 🔠
- **crawl4ai**: Web crawling tool to extract content from webpages 🌐
- **asyncio**: For asynchronous execution of web crawling and content rewriting tasks ⏳

## Installation 🔧

### 1. Clone the repository:

```bash
git clone https://github.com/Abarnarajj/SEO-content-Rewritter-neural-Coders.git
cd SEO-content-Rewritter-neural-Coders
```

### 2. Install dependencies:
First, create a virtual environment and activate it:
```bash
python3 -m venv venv
venv\Scripts\activate # For Windows
```
Then, install the required dependencies:
```bash
pip install -r requirements.txt
```
### 3. Installation of Ollama:
Ollama is used for the content rewriting functionality in this project, utilizing the DeepSeek model. To set up Ollama, please follow the steps below:

Visit the official [Ollama website](https://ollama.com/download) and follow the installation instructions specific to your operating system (Windows, macOS, or Linux).
```bash
ollama run deepseek-r1
```
### 4. Running the Web Interface:
To launch the web interface, run the following command:
```bash
python app.py
```

### Workflow: 🔄
**Enter a URL:** The system will crawl and extract content from the webpage.
**Provide Content:** Input the content you want to improve for SEO.
**Content Rewriting:** The system will process the extracted content with FAISS for retrieval and rewrite it with SEO optimizations using Ollama's DeepSeek model.

The tool will generate SEO-optimized content as shown below:

![image](https://github.com/user-attachments/assets/0a003b8f-6d92-473b-a1ad-f8a3ddd65de5)

## Contributing 🤝
Feel free to fork the repository, make improvements, and submit pull requests. We welcome contributions!
