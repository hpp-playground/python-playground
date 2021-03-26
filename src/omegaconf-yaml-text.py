from omegaconf import OmegaConf
from pathlib import Path

dic = {"hoge": "hoge", "huga": "fuga", "foo": {"boo": "bee"}}
conf = OmegaConf.create(dic)

# Path("./test.yaml").write_text(conf)
Path("./test.yaml").write_text(OmegaConf.to_yaml(conf))
