"""
RAG 核心处理模块

学习路线（按 RAG 流水线顺序）：
1. document_loader.py  → 理解文档如何被解析为纯文本
2. text_splitter.py    → 理解长文本如何被切分为检索友好的片段
3. embeddings.py       → 理解文本如何被映射到向量空间
4. vector_store.py     → 理解 FAISS 如何存储和检索向量
5. bm25_index.py       → 理解稀疏检索如何与密集检索互补
6. retriever.py        → 理解混合检索策略的设计
7. reranker.py         → 理解两阶段检索（recall + rerank）
8. generator.py        → 理解 Prompt 构建和 LLM 调用
"""

"""
1. document_loader.py:

各种类型的文档，比如pdf、markdown、txt、excel，通过使用python或者pandas的各种库函数，将其读取出来，读出来的都是str类型字符串
其中，以excel举例，可能会将读出来的数据，做一些二次换行操作，如下：
    工作表: Sheet1
    姓名  年龄
    张三  25
    李四  30
    
    工作表: Sheet2
    产品  价格
    A     100
    B     200
二次换行本身代表的语义很强，表示是不同的Sheet。交给LLM可以更好的处理。

2. text_splitter.py

使用langchain_text_splitters库的RecursiveCharacterTextSplitter递归字符文本切分器
对提取出来的整段字符串，进行切分。

切分要素：
    - chunk_size：每个片段最大字符数
    - chunk_overlap：相邻片段重叠字符数（避免关键信息被切断）
    - separators：优先按照什么分隔符切分
    
3. embeddings.py

文档嵌入，将文本嵌入为embedding向量
（面试应该不会问，简单记录下，无论是sentence_transformers加载模型，还是langchain_huggingface加载模型，都把单文本和多文本分开了的，实际
全部使用多文本，也是一样的）

4. vector_store.py
5. bm25_index.py
"""