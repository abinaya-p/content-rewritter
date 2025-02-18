import asyncio
import ollama
import faiss
import numpy as np
import gradio as gr
from crawl4ai import AsyncWebCrawler
from sentence_transformers import SentenceTransformer

# Load embedding model once (fast retrieval)
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize FAISS index
dimension = 384  # Model output dimension
faiss_index = faiss.IndexFlatL2(dimension)
stored_content = None  # Store only the latest crawled content

async def crawl_and_store(url):
    """Crawls a webpage, extracts content, embeds it, and stores it."""
    global stored_content  # Store only the latest crawled content
   
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
        content = result.markdown.strip()

    if content:
        embedding = embed_model.encode([content], convert_to_numpy=True)
        faiss_index.add(embedding)  # Store in FAISS
        stored_content = content  # Keep track of content
        return content
    return None

def retrieve_website_knowledge(query):
    """Retrieves the most relevant content from FAISS based on the query."""
    query_embedding = embed_model.encode([query], convert_to_numpy=True)
   
    if query_embedding is None or query_embedding.size == 0:
        return ""

    _, indices = faiss_index.search(query_embedding, 1)
   
    if indices[0][0] == -1 or stored_content is None:
        return ""
   
    return stored_content

def generate_prompt(original_content, keyword):
    """Generates a structured prompt with strict output format."""
    return f"""
    Use the following website knowledge to rewrite the content with SEO improvements:
    - Optimize keyword placement for '{keyword}'.
    - Improve readability while maintaining factual accuracy.

    Website Knowledge:
    {stored_content}

    Strictly format the output as follows:
    Before: {original_content}
    After (LLM-generated): <Optimized Content>
    """

async def rewrite_content(url, input_text):
    """Crawls, stores content, and rewrites user input using website knowledge."""
    await crawl_and_store(url)  # Crawl and store content
   
    website_knowledge = retrieve_website_knowledge(input_text)
   
    if not website_knowledge:
        return "No relevant website knowledge found."

    prompt = generate_prompt(input_text, input_text)
    response = await asyncio.to_thread(ollama.chat, model="deepseek-r1", messages=[{"role": "user", "content": prompt}])

    optimized_content = response["message"]["content"].strip()

    # Extract only optimized content by removing <think> sections
    if "<think>" in optimized_content:
        optimized_content = optimized_content.split("</think>")[-1].strip()

    # Limit to 2-line summary
    optimized_lines = optimized_content.split("\n")
    optimized_summary = " ".join(optimized_lines[:2])

    return optimized_summary if optimized_summary else "Failed to generate optimized content."


def gradio_interface(url, input_text):
    """Wrapper function to run async code in Gradio."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(rewrite_content(url, input_text))


# Gradio UI
iface = gr.Interface(
    fn=gradio_interface,
    inputs=[gr.Textbox(label="Enter the URL to extract knowledge from"),
            gr.Textbox(label="Enter the content to rewrite")],
    outputs=gr.Textbox(label="Rewritten Content"),
    title="AI-Powered SEO Content Rewriter"
)

if __name__ == "__main__":
    iface.launch()
