import sys
import torch
import pandas as pd
import sklearn
import xgboost

print(f"✅ Python Version: {sys.version.split()[0]}")
print(f"✅ Pandas Version: {pd.__version__}")
print(f"✅ Scikit-Learn Version: {sklearn.__version__}")
print(f"✅ XGBoost Version: {xgboost.__version__}")

print("\n--- GPU CHECK ---")
if torch.cuda.is_available():
    print(f"✅ CUDA is available!")
    print(f"   GPU Name: {torch.cuda.get_device_name(0)}")
    print(f"   PyTorch Version: {torch.__version__}")
else:
    print("❌ CUDA is NOT available. PyTorch is running on CPU only.")
    
print("\n🎉 Environment is healthy and ready for Phase 1!")