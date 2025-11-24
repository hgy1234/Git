from huggingface_hub import snapshot_download
import os

# 可选：开启高速传输（需 pip install hf_transfer）
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"

snapshot_download(
    repo_id="meta-math/MetaMath-Mistral-7B",
    local_dir="/home/data/hhj/Model/Mistral",
    local_dir_use_symlinks=False,   # 直接落盘，不建软链
    resume_download=True            # 支持断点续传
)