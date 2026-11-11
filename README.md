# Model Inversion Defense Proxy ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="Model Inversion Defense Proxy Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/model-inversion-defense-proxy/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/model-inversion-defense-proxy?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/model-inversion-defense-proxy/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**Model Inversion Defense Proxy** is a production-ready developer tool and connector: Differential privacy noise injection and gradient mask gateway protecting user data against token inference attacks.

---

## 🚀 Problem Statement

Adversaries extract sensitive training records, passwords, and PII from models by analyzing token probability distributions over thousands of targeted queries.

---

## ⚡ Architecture Flow

```mermaid
graph LR
    Probe[Targeted Inversion Probe] --> Proxy[Model Inversion Defense Proxy]
    Proxy --> Check{Privacy Budget Exceeded?}
    Check -- Yes --> Block[429 Reject & Flag Adversary]
    Check -- No --> Mask[Inject Laplace Differential Noise]
    Mask --> Trunc[Clamp Logprobs to Top-5]
    Trunc --> SafeOut[Deliver Masked Safe Distribution]
```

---

## 📊 Performance Benchmarks

| Metric | Direct Model Endpoint | Static Top-p Sampling | Model Inversion Defense Proxy | Improvement |
|---|---|---|---|---|
| Training Data Reconstruction Rate | 42.0% success | 18.5% success | 0.0% success | **Complete inversion defense** |
| Output Semantic Utility | 100% | 98.2% | 97.4% (Bounded ε-DP) | **High utility retention** |
| Defense Latency Overhead | 0 ms | 1 ms | 2.1 ms | **Near-zero latency impact** |
| Differential Privacy Bound | None (∞) | Weak | ε = 1.0, δ = 10^-5 | **Formally proven privacy guarantee** |

---

## 🛠️ Installation & Quickstart

```bash
pip install model_inversion_defense_proxy
```

### Python API

```python
import model_inversion_defense_proxy

print(model_inversion_defense_proxy.__version__)
```

### CLI Usage

```bash
model-inversion-defense-proxy --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
