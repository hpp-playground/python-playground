import torch

# a = torch.stack([torch.randperm(i + 1) for i in range(5)])
a = [torch.randperm(i + 1) for i in range(5)]
print(a)
