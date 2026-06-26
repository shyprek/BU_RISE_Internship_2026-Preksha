**Notes Format:**
The Hypothesis: "Changing the activation function from ReLU to GELU will reduce vanishing gradients in the deeper layers."

Data Split: Explicitly note your training/validation/testing split ratios and random seeds (e.g., random_state=42).

Hyperparameters: Learning rate, batch size, epochs, optimizer (e.g., AdamW), dropout rate.

Architecture: Number of layers, attention heads, or specific pre-trained weights used (e.g., resnet50).

Metrics: Validation loss, accuracy, F1-score, precision/recall curves, and training time.

### 📊 Run Log: [e.g., Run_v1.2_GELU_Adjustment]
* **Code Commit / Branch:** `origin/ml-baseline`
* **W&B or TensorBoard Link:** [Insert Link]

| Hyperparameter | Value |
| :--- | :--- |
| Optimizer | AdamW |
| Learning Rate | 1e-4 |
| Batch Size | 32 |
| Epochs | 50 |

#### Results & Convergence
* **Best Val Loss:** 0.234 (at Epoch 34)
* **Test Accuracy / F1:** 91.2% / 0.89
* *[Insert/Paste Loss Curve Graph Here]*

#### Key Takeaway / Interpretation
* The model converged faster with GELU, but started overfitting around epoch 35. Tomorrow, I need to implement early stopping or increase the dropout rate to 0.3.
