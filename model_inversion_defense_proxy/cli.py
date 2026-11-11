"""CLI for model-inversion-defense-proxy."""
import sys
import argparse
from .proxy import ModelInversionProxy

def main():
    parser = argparse.ArgumentParser(description="Model Inversion Defense Proxy CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate distribution masking")
    args = parser.parse_args()

    if args.demo:
        proxy = ModelInversionProxy(epsilon=1.5, top_k=3)
        tokens = ["apple", "banana", "cherry", "date"]
        probs = [0.85, 0.10, 0.03, 0.02]
        res = proxy.protect_distribution("client_1", tokens, probs)
        print(f"Original top: {res.original_top_prob} -> Masked top: {res.masked_top_prob}")
        print(f"Masked distribution: {dict(zip(res.tokens, res.masked_probs))}")
    else:
        parser.print_help()
    sys.exit(0)

if __name__ == "__main__":
    main()
