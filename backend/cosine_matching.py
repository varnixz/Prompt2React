import torch
import numpy as np
from templates import design_templates

# Import our custom embedder from prompt_preprocess to maintain consistency
from prompt_preprocess import CustomEmbedder, model

def cos_sim(a, b):
    """
    Compute cosine similarity between two vectors
    """
    if isinstance(a, torch.Tensor):
        a = a.numpy().flatten()
    if isinstance(b, torch.Tensor):
        b = b.numpy().flatten()
    
    # Convert lists to numpy arrays if needed
    if isinstance(a, list):
        a = np.array(a)
    if isinstance(b, list):
        b = np.array(b)
    
    # Flatten if multidimensional
    a = a.flatten()
    b = b.flatten()
    
    # Calculate cosine similarity
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    
    if norm_a == 0 or norm_b == 0:
        return 0
    
    return np.dot(a, b) / (norm_a * norm_b)

def match_best_template(llm_embedding):
    """
    Compares the embedding of the LLM-extracted description with all template descriptions
    and returns the index (0-9) of the most similar template.
    """
    # Extract descriptions from all templates
    template_descriptions = [template["description"] for template in design_templates]

    # Get embeddings of template descriptions
    template_embeddings = model.encode(template_descriptions, convert_to_tensor=True)
    
    # Convert to numpy for easier handling
    if isinstance(llm_embedding, torch.Tensor):
        llm_embedding = llm_embedding.numpy()
    
    # Compute cosine similarities
    similarities = []
    for i, template_emb in enumerate(template_embeddings):
        if isinstance(template_emb, torch.Tensor):
            template_emb = template_emb.numpy()
        sim = cos_sim(llm_embedding, template_emb)
        similarities.append(sim)
    
    # Get the index of the highest similarity
    best_match_index = np.argmax(similarities)
    
    return int(best_match_index)