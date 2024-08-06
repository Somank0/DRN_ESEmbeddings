import torch
from torch.utils.data import Dataset, DataLoader
class MyDataset(Dataset):
    def __init__(self, xECAL, xES):
        self.xECAL = xECAL
        self.xES = xES
    
    def __len__(self):
        return len(self.xECAL)
    
    def __getitem__(self, idx):
        return self.xECAL[idx], self.xES[idx]
    def __reduce__(self):
        return (self.__class__, (self.xECAL, self.xES))

