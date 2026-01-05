import sys
import torch
import cudf
import cuml
import pandas as pd
import polars as pl
import sklearn
import cv2
import crewai
import ollama

print("--- 🛠️ SYSTEM CORE ---")
print(f"Python: {sys.version.split()[0]}")
print(f"PyTorch: {torch.__version__} | CUDA: {torch.cuda.is_available()}")

print("\n--- 🏎️ ACCELERATED DATA (RAPIDS/POLARS) ---")
print(f"cuDF (GPU Pandas): {cudf.__version__}")
print(f"cuML (GPU ML): {cuml.__version__}")
print(f"Polars (Rust-speed): {pl.__version__}")

print("\n--- 🤖 AGENTIC & GEN-AI ---")
print(f"CrewAI: {crewai.__version__}")
print(f"OpenCV: {cv2.__version__}")

print("\n--- 💾 HARDWARE ---")
if torch.cuda.is_available():
    print(f"GPU Name: {torch.cuda.get_device_name(0)}")
    vram = torch.cuda.get_device_properties(0).total_memory / 1e9
    print(f"VRAM: {vram:.2f} GB")