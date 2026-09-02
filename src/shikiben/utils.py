"""
Utility functions for subspace extraction and metric evaluations.
"""

import numpy as np

def extract_harmful_subspace(embeddings: np.ndarray, top_k: int = 2) -> np.ndarray:
    """Extracts top-k principal components from a matrix of harmful prompt embeddings using SVD."""
    U, S, Vt = np.linalg.svd(embeddings, full_matrices=False)
    return Vt[:top_k, :].T  # [Dim, top_k]

def evaluate_metrics(vec: np.ndarray, V_harmful: np.ndarray, target_vec: np.ndarray = None) -> dict:
    """Evaluates projection magnitude, cosine similarity, and vector norm."""
    norm_val = np.linalg.norm(vec)
    harm_proj = np.max(np.abs(V_harmful.T @ vec))
    
    results = {
        "harmful_projection": harm_proj,
        "energy_norm": norm_val
    }
    
    if target_vec is not None:
        target_norm = np.linalg.norm(target_vec)
        cos_sim = np.dot(vec, target_vec) / (norm_val * target_norm)
        results["cosine_similarity"] = cos_sim
        
    return results