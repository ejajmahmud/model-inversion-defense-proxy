"""Unit tests for model-inversion-defense-proxy."""
import unittest
from model_inversion_defense_proxy.proxy import ModelInversionProxy

class TestModelInversionProxy(unittest.TestCase):
    def setUp(self):
        self.proxy = ModelInversionProxy(epsilon=1.0, top_k=3)

    def test_distribution_sum_and_truncation(self):
        tokens = ["a", "b", "c", "d", "e"]
        probs = [0.6, 0.2, 0.1, 0.05, 0.05]
        res = self.proxy.protect_distribution("c1", tokens, probs)
        self.assertEqual(len(res.tokens), 3)
        self.assertAlmostEqual(sum(res.masked_probs), 1.0, places=2)
