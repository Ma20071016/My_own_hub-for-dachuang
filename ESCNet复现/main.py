import sys
import torch
import transformers

print("Python:", sys.executable)
print("PyTorch:", torch.__version__)
print("Transformers:", transformers.__version__)
print("CUDA 可用:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("显卡:", torch.cuda.get_device_name(0))