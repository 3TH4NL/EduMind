import pandas as pd
import numpy as np
import faiss
import google.generativeai as genai
from sentence_transformers import SentenceTransformer

genai.configure(api_key="AIzaSyAGf6gXG3CoyFLYcQjGYMX5K8_hTTeq8eI")

kb_path = "kb.csv"
kb_data = pd.read_csv(kb_path)

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

kb_contents = kb_data['Content'].tolist()
kb_embeddings = embedding_model.encode(kb_contents)

dimension = kb_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(kb_embeddings))

def retrieve_relevant_chunks(query, top_k=5, threshold=0.8):
    query_emb = embedding_model.encode([query])
    distances, indices = index.search(np.array(query_emb), top_k)

    results = []
    for dist, idx in zip(distances[0], indices[0]):
        if dist < threshold:
            results.append(kb_contents[idx])
    return results

def generate_prompt(task_type, keyword, context):
    if task_type == "Generate Class Notes":
        return f"Based on the following mental health materials, write clear and concise class notes about '{keyword}':\n\n{context}\n\nNotes:"
    elif task_type == "Generate 5 Practice Questions":
        return f"Based on the following mental health materials, create 5 practice questions related to '{keyword}'. Each question should be simple and clear.\n\n{context}\n\nPractice Questions:"
    elif task_type == "Generate Mini Lecture":
        return f"Based on the following mental health materials, write a short educational lecture (~150 words) about '{keyword}' suitable for students.\n\n{context}\n\nLecture:"
    else:
        return f"Explain '{keyword}' based on the following materials:\n\n{context}"


def ask_llm(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash-8b")
    response = model.generate_content(prompt)
    return response.text.strip()

def generate_content(keyword, task_type):
    chunks = retrieve_relevant_chunks(keyword)

    if chunks:
        context = "\n".join(chunks)
    else:
        context = "No relevant educational material found. Please generate based on general mental health knowledge."

    prompt = generate_prompt(task_type, keyword, context)
    answer = ask_llm(prompt)
    return answer