import os
import hashlib
import numpy as np
import torch
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference.models import SystemMessage, UserMessage

# Define a very simple custom encoder that doesn't rely on transformers
class CustomEmbedder:
    """
    A simplified embedding generator that uses word counting and basic statistics
    as a temporary fallback until the transformers issue is resolved.
    """
    def __init__(self, embedding_size=384):
        self.vocab = {}
        self.vector_size = embedding_size
        self.next_id = 0
        print("Using CustomEmbedder as fallback solution")
    
    def _get_word_id(self, word):
        """Get a consistent numerical ID for each word"""
        if word not in self.vocab:
            self.vocab[word] = self.next_id
            self.next_id += 1
        return self.vocab[word]
    
    def _hash_to_vector(self, word, vector_size):
        """Convert a word to a pseudo-random vector using hash function"""
        # Create a hash of the word
        word_hash = hashlib.md5(word.encode()).hexdigest()
        
        # Convert hash to a list of floats
        hash_values = []
        for i in range(0, min(len(word_hash), vector_size * 2), 2):
            if i+1 < len(word_hash):
                # Convert each pair of hex digits to a float between -1 and 1
                value = int(word_hash[i:i+2], 16) / 255.0 * 2 - 1
                hash_values.append(value)
        
        # Pad or truncate to desired vector size
        while len(hash_values) < vector_size:
            hash_values.append(0.0)
        return hash_values[:vector_size]
    
    def encode(self, text, convert_to_tensor=True):
        """
        Convert text to a vector representation
        """
        if isinstance(text, list):
            # Handle list of texts
            embeddings = [self.encode(t, convert_to_tensor=False) for t in text]
            if convert_to_tensor:
                return torch.tensor(embeddings)
            return embeddings
        
        # Normalize text
        text = text.lower()
        words = ''.join(c if c.isalnum() else ' ' for c in text).split()
        
        # Generate vector
        embedding = np.zeros(self.vector_size)
        
        # Add word vectors
        word_count = 0
        for word in words:
            if len(word) > 1:  # Skip single character words
                word_vector = self._hash_to_vector(word, self.vector_size)
                embedding += np.array(word_vector)
                word_count += 1
        
        # Normalize
        if word_count > 0:
            embedding = embedding / max(1, word_count)
        
        # Convert to tensor if requested
        if convert_to_tensor:
            return torch.tensor([embedding], dtype=torch.float32)
        return embedding.tolist()

# Initialize our custom embedder
model = CustomEmbedder()

def get_component_and_style(prompt: str) -> str:
    """
    Get structured component and styling breakdown using DeepSeek via Azure.
    """
    try:
        token = os.getenv("GITHUB_TOKEN")
        if not token:
            raise ValueError("GITHUB_TOKEN environment variable not set")
            
        endpoint = "https://models.inference.ai.azure.com"
        model_name = "DeepSeek-V3"

        client = ChatCompletionsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(token),
        )

        messages = [
            SystemMessage("You are a web design expert. Given a user prompt, identify required website components and styling preferences in a structured bullet list. Format response with two sections: 'Components:' and 'Styling:'."),
            UserMessage(f"Prompt: {prompt}")
        ]

        response = client.complete(
            messages=messages,
            model=model_name,
        )

        if not response.choices or not response.choices[0].message or not response.choices[0].message.content:
            raise Exception("Azure AI API returned an empty response.")

        structured_text = response.choices[0].message.content.strip()
        return structured_text

    except Exception as e:
        print(f"Error in DeepSeek LLM call: {str(e)}")
        # Provide a fallback if the API call fails
        return f"Components:\n- Basic layout for: {prompt}\n\nStyling:\n- Default styling"

    finally:
        if 'client' in locals():
            client.close()

def embed_prompt(prompt: str):
    """
    Convert processed prompt string into embedding vector.
    """
    try:
        return model.encode(prompt, convert_to_tensor=True)
    except Exception as e:
        print(f"Error encoding prompt: {e}")
        # Return a zero vector of appropriate size as fallback
        return torch.zeros(384)

def process_prompt_to_embedding(prompt: str):
    """
    Full pipeline: Prompt -> DeepSeek (structured output) -> Embedding
    """
    structured = get_component_and_style(prompt)
    embedding = embed_prompt(structured)
    return embedding, structured