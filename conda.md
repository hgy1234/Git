## 基础密钥

### closeai
base_url = "https://api.openai-proxy.org/v1"
api_key = "sk-2px7Nzng8D0OOWC1VGAo209S05XrOGmoswZZYhphdEaOvjMk"

### deepseek
base_url="https://api.deepseek.com"
api_key="sk-b1bde7da97e4446698760ce4fc71a4a4"
## 基础环境-BASE
除了基本的conda环境之外，包含了和 GIT 和 HUGGINGFACE 相关的一些包：
1. 从 huggingface 上下载模型、从 Github 上拉取仓库。

之后安装
1. openai - api接口调用
2. transformers - 模型调用

openai 、 transformers 已安装，能实现基本功能
之后安装 torch ， 问题是 之前下载的时候空间不够. torch 已安装，能够正常使用

ipynb 配置、加快调试
已安装

### Git操作
推送
git add "~"
git commit
git push -u git master


## 模型与数据路径

### ReTS - Mistral 路径
model_pth = "/home/data/hhj/Model/Mistral"
data_pth = "/home/data/hhj/Data"