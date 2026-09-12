# Time Series Anomaly Detection using HAI Dataset

## About this project
This project was built for the **Tic-Tech-Toe Hackathon**, organized by **DA-IICT Gandhinagar**, 
by a 3-member team. It focuses on anomaly detection in Industrial Control Systems (ICS) using 
the HAI security dataset. This repo contains my individual contribution to the team project.

## My contribution
- Feature engineering on the HAI multivariate sensor dataset
- Trained and tuned: Isolation Forest, LSTM Autoencoder, Transformer Autoencoder
- Built the ensemble scoring logic combining all three models
- Generated SHAP-based explainability outputs (feature importance, root-cause insights)
- Saved trained model artifacts (see `models/`)

## Team contributions
- Dashboard / frontend — Jinay Shah
- Backend / API — Flora

## Repo structure
- `notebooks/` — model training, feature engineering, and ensemble notebook
- `models/` — trained model weights and metadata
- `backend/` — API layer (built by teammate)
- `dashboard/` — dashboard UI (built by teammate)

## Dataset
Uses the [HAI Security Dataset](https://github.com/icsdataset/hai) — auto-downloaded via 
`kagglehub` in the training notebook, no manual download needed.

## Tech stack
Python, PyTorch, scikit-learn, SHAP, pandas

## Approach

### Feature Engineering
- Engineered 221 features from raw HAI sensor telemetry, including:
  - Setpoint-vs-process-variable error features for each control loop (pressure, level, flow, temperature, speed)
  - Rate-of-change (first derivative) features to capture sudden sensor jumps
  - Rolling statistics (mean, std, max) over 10s / 30s / 60s windows for key sensors
- Built 60-second sliding-window sequences for the deep learning models

### Ensemble Model
Combined three models into a single anomaly score:
- **Isolation Forest** — tree-based statistical outlier detection
- **LSTM Autoencoder** — reconstruction-error-based sequential anomaly detection
- **Transformer Autoencoder** — self-attention-based detection of long-range dependencies

ensemble_score = 0.50 × LSTM_AE + 0.30 × Transformer_AE + 0.20 × Isolation_Forest

Anomalies are flagged using an **adaptive rolling threshold** (95th percentile), which adjusts to local process dynamics rather than a fixed cutoff.

### Explainability
Used **SHAP** to identify which of the 221 features contributed most to each anomaly, enabling root-cause identification (e.g., pinpointing a manipulated setpoint or spoofed sensor reading behind a detected attack).

## How to run the notebook
1. Open `notebooks/model_training_and_ensemble.ipynb` in Google Colab or Jupyter
2. Install dependencies: pip install pandas numpy torch scikit-learn shap joblib kagglehub
3. Run all cells — the HAI dataset downloads automatically via `kagglehub`
4. Trained models and metrics will be saved to a `hai_models/` output folder

## Using the pre-trained models
The trained weights are already available in `models/` if you don't want to retrain:
- `iso_forest.pkl`, `scalers.pkl` — load with `joblib.load()`
- `lstm_ae_full.pt`, `transformer_ae_full.pt` — load with `torch.load()`
- `feature_cols.json`, `metadata.json` — feature list and training config
