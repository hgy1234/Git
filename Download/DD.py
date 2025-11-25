from datasets import load_dataset

# ReSt 中 用于训练 价值模型 的数据
data_name = "zd21/ReST-MCTS-PRM-0th"
D_dir = "/home/data/hhj/Data"

# 下载数据文件
# ds = load_dataset(data_name, cache_dir=D_dir)
# print(ds['train'][:10])

# 读取数据文件
ds = load_dataset('arrow',data_files = "/home/data/hhj/Data/zd21___re_st-mcts-prm-0th/default/0.0.0/4318a214504f641641e5e35bb0471a8ff0544295/re_st-mcts-prm-0th-test.arrow")
print(ds)