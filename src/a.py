import re

import numpy as np
import torch
import torch.nn as nn
from transformers import BertModel, BertTokenizer

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
VEC_LEN = 768


class v2g_Model(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.bert = BertModel.from_pretrained("bert-base-uncased")
        self.w_mu = nn.Linear(VEC_LEN, VEC_LEN)
        self.w_var = nn.Linear(VEC_LEN, VEC_LEN)

    def __call__(self, *args, **kwds):
        return super().__call__(*args, **kwds)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids, attention_mask)
        emb = outputs.last_hidden_state[:, 0]
        var = self.w_var(emb).exp()
        mu = self.w_mu(emb)
        return mu, var


train_f = open("./data/wikisub.txt")
train_S = train_f.readlines()
train_S = train_S[:5]
train_S_d = []
for i in train_S:
    train_S_d.append(i)
    train_S_d.append(i)

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
inputs = tokenizer(train_S_d, padding=True, truncation=True)
input_ids = torch.from_numpy(np.array(inputs.input_ids).astype(np.float32)).clone()
input_ids = input_ids.to(torch.long)
attention_mask = torch.from_numpy(np.array(inputs.attention_mask).astype(np.float32)).clone()
attention_mask = attention_mask.to(torch.long)
v2g = v2g_Model()
v2g.eval()
mu, var = v2g(input_ids, attention_mask)

print(mu)
print(var)
