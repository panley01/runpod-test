# Runpod deployment notes

This repository is a Runpod-compatible serverless worker for the black-forest-labs/FLUX.1-dev model.

## Quick deploy
- Use the Runpod GitHub integration (fork this repository, connect your Github account to Runpod and deploy) to instantly create the serverless worker.

## Required secret(s)
- Add a secret named `HF_TOKEN` in the Runpod Serverless dashboard.
- `HF_TOKEN` must be a Hugging Face token authorized to read on behalf of the user (i.e., has read access to the license-gated model) so the model can be downloaded at runtime.

## Resource recommendations
- Docker disk size: increase to at least 35 GB to accommodate the model files.
- GPU: use a GPU with >= 36 GB VRAM to ensure sufficient memory for the model.

## Notes
- Deployment will fail or the model will not download without a valid `HF_TOKEN`.
- Adjust resources upward if you encounter out-of-disk or out-of-memory errors.