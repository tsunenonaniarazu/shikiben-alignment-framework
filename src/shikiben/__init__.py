"""
Shikiben Alignment Framework
Geometric Rectification for Language Model Safety and Intent Alignment.
"""

from .core import GeometricRectifier
from .utils import extract_harmful_subspace, evaluate_metrics

__version__ = "2.4.0"
__all__ = ["GeometricRectifier", "extract_harmful_subspace", "evaluate_metrics"]