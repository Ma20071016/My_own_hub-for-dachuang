from dataclasses import dataclass


@dataclass
class ESCNetConfig:
    bert_path: str = "/home/egene-deng/ESCNet/pretrained/bert-base-uncased"  #BERT模型所在位置
    text_hidden_size: int = 768
    num_classes: int = 2
