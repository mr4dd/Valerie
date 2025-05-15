from sentence_transformers import SentenceTransformer

def check_single_similarity(categories, text):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    category_embeddings = model.encode(categories)
    text_embedding = model.encode(text)

    similarities = model.similarities(category_embeddings, text_embedding)
    
    return similarities

def check_batch_similarity(categories, text_array)
    model = SentenceTransformer("all-MiniLM-L6-v2")
    category_embeddings = model.encode(categories)
    text_embedding = model.encode(text_array)

    similarities = model.similarities(category_embeddings, text_embedding)
    
    return similarities
