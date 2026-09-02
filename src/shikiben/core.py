"""
Core Geometric Rectification Module for shikiben-alignment-framework.
"""

import numpy as np

class GeometricRectifier:
    """
    Shikiben Geometric Rectification Framework for High-Dimensional Latent Spaces.
    
    Implements:
    - Orthogonal Projection Operator (P_gi)
    - Restoration Force Potential (f_toku)
    - Receptive Energy Metabolism (O_kansha)
    """
    def __init__(self, harmful_subspace_basis: np.ndarray):
        """
        Args:
            harmful_subspace_basis (np.ndarray): Basis vectors of harmful subspace V_harmful [Dim, k].
        """
        self.V_harmful = harmful_subspace_basis
        self.dim = harmful_subspace_basis.shape[0]
        
        # Construct Orthogonal Projection Operator P_gi = I - V * V^T
        I_dim = np.eye(self.dim)
        self.P_gi = I_dim - self.V_harmful @ self.V_harmful.T

    def rectify(self, shock_vector: np.ndarray, target_vector: np.ndarray = None, restoration_gain: float = 0.5) -> np.ndarray:
        """
        Applies full geometric rectification pipeline to an input vector.
        
        Steps:
        1. Calculate restoration vector toward target intent (f_toku).
        2. Apply strict orthogonal projection (P_gi) to decouple harmful components.
        3. Perform energy conservation and metabolism (O_kansha).
        """
        original_norm = np.linalg.norm(shock_vector)
        if original_norm == 0:
            return shock_vector

        v_shock = shock_vector / original_norm

        # Step 1: Restoration Force (f_toku)
        if target_vector is not None:
            v_target = target_vector / np.linalg.norm(target_vector)
            f_toku = restoration_gain * (v_target - v_shock)
            candidate = v_shock + f_toku
        else:
            candidate = v_shock

        # Step 2: Strict Orthogonal Cut (P_gi)
        orthogonal_rectified = self.P_gi @ candidate

        # Step 3: Receptive Metabolism (O_kansha)
        cut_norm = np.linalg.norm(orthogonal_rectified)
        if cut_norm == 0:
            return orthogonal_rectified

        rectified_vector = (orthogonal_rectified / cut_norm) * original_norm
        return rectified_vector