import torch
import time

# Matrix size (10,000 x 10,000 is about 100 million operations)
N = 10000 

print(f"🏁 Starting Speed Test with Matrix Size: {N}x{N}\n")

# --- 1. CPU BENCHMARK ---
# We use standard PyTorch on the CPU
x_cpu = torch.randn(N, N)
y_cpu = torch.randn(N, N)

start_cpu = time.time()
result_cpu = torch.matmul(x_cpu, y_cpu)
end_cpu = time.time()

cpu_time = end_cpu - start_cpu
print(f"🐌 CPU Time: {cpu_time:.4f} seconds")

# --- 2. GPU BENCHMARK (RTX 3060) ---
if torch.cuda.is_available():
    device = torch.device("cuda")
    
    # Move tensors to the GPU
    x_gpu = torch.randn(N, N).to(device)
    y_gpu = torch.randn(N, N).to(device)

    # 🔥 WARM-UP: The first GPU call is always slow due to overhead
    _ = torch.matmul(x_gpu, y_gpu)
    torch.cuda.synchronize() # Wait for GPU to finish warm-up

    # ACTUAL TEST
    start_gpu = time.time()
    result_gpu = torch.matmul(x_gpu, y_gpu)
    
    # IMPORTANT: CUDA is asynchronous. We must synchronize to get true timing.
    torch.cuda.synchronize() 
    end_gpu = time.time()

    gpu_time = end_gpu - start_gpu
    print(f"🚀 GPU Time: {gpu_time:.4f} seconds")
    print(f"\n💎 SPEEDUP: {cpu_time / gpu_time:.2f}x FASTER")
else:
    print("❌ GPU not detected. Check your WSL2 CUDA drivers.")