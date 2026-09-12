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
