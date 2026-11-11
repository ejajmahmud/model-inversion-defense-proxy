"""Core Model Inversion Defense Proxy implementation."""
import math
import random
from dataclasses import dataclass
from typing import Dict, List, Tuple

@dataclass
class ProtectedDistribution:
    original_top_prob: float
    masked_top_prob: float
    tokens: List[str]
    masked_probs: List[float]
    epsilon_spent: float

class ModelInversionProxy:
    """Injects calibrated Laplace noise into token probabilities to protect training data from inversion."""
    
    def __init__(self, epsilon: float = 1.0, top_k: int = 5):
        self.epsilon = epsilon
        self.top_k = top_k
        self.client_spend_ledger: Dict[str, float] = {}

    def sample_laplace(self, scale: float) -> float:
        u = random.random() - 0.5
        return -scale * math.copysign(1.0, u) * math.log(1.0 - 2.0 * abs(u))

    def protect_distribution(self, client_id: str, tokens: List[str], raw_probs: List[float]) -> ProtectedDistribution:
        # 1. Truncate to top-k
        pairs = sorted(zip(tokens, raw_probs), key=lambda x: x[1], reverse=True)[:self.top_k]
        sub_tokens = [p[0] for p in pairs]
        sub_probs = [p[1] for p in pairs]

        # 2. Add Laplace noise
        scale = 1.0 / max(0.1, self.epsilon)
        noisy = [max(0.001, p + self.sample_laplace(scale * 0.05)) for p in sub_probs]
        
        # 3. Re-normalize to sum to 1.0
        tot = sum(noisy)
        norm_probs = [round(n / tot, 4) for n in noisy]

        # Record epsilon budget
        self.client_spend_ledger[client_id] = self.client_spend_ledger.get(client_id, 0.0) + 0.1

        return ProtectedDistribution(
            original_top_prob=raw_probs[0] if raw_probs else 0.0,
            masked_top_prob=norm_probs[0] if norm_probs else 0.0,
            tokens=sub_tokens,
            masked_probs=norm_probs,
            epsilon_spent=0.1
        )
