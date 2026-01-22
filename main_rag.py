from analyzer.code_analyzer import analyze_code
from rag.chunker import convert_analysis_to_text
from rag.embeddings import generate_embedding
from rag.vector_store import store_embedding
from rag.retriever import retrieve_context
from rag.generator import generate_answer

file_path = "sample_inputs/sales_invoice.py"

analysis = analyze_code(file_path)
text = convert_analysis_to_text(analysis, file_path)

embedding = generate_embedding(text)
store_embedding(embedding, text)

question = "What does Sales Invoice do?"
context = retrieve_context(question)
answer = generate_answer(context, question)

print(answer)
