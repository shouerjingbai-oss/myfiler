# Personal AI Knowledge Assistant

> 基于 LangChain + ChromaDB + DeepSeek + Streamlit 构建的个人知识库智能问答系统。

---

## 项目简介

Personal AI Knowledge Assistant 是一个基于 Retrieval-Augmented Generation（RAG）架构的个人文档智能问答系统。

用户上传 PDF 文档后，系统自动完成：

- 文档解析
- 文本切块
- 向量化
- 建立知识库
- 智能问答
- 引用来源展示

整个系统采用 LangChain Agent 调度工具，实现真正意义上的 AI Native 工作流。

---

## 项目特点

✅ 支持 PDF 文档上传

✅ 自动构建知识库

✅ 基于 bge-small-zh-v1.5 中文Embedding

✅ ChromaDB 本地向量数据库

✅ LangChain Agent Tool Calling

✅ DeepSeek API 智能问答

✅ Streamlit 可视化聊天界面

✅ 回答引用原始文档来源

---

## 技术栈

| 模块 | 技术 |
|------|------|
| Language | Python 3.11 |
| LLM | DeepSeek API |
| Framework | LangChain |
| Embedding | BAAI/bge-small-zh-v1.5 |
| Vector DB | ChromaDB |
| PDF Parser | PyMuPDF |
| Frontend | Streamlit |

---

## 系统架构

```
PDF
    │
    ▼
PyMuPDF
    │
    ▼
Text Splitter
    │
    ▼
Embedding
    │
    ▼
ChromaDB
    │
    ▼
Retriever
    │
    ▼
LangChain Agent
    │
    ▼
DeepSeek
    │
    ▼
Answer + Citation
```

---

## 项目结构

```
personal-ai-knowledge-assistant/
│
├── app.py
├── config.py
├── rag/
├── agent/
├── llm/
├── ui/
├── evaluation/
├── utils/
└── data/
```

---

## 快速开始

### 克隆项目

```bash
git clone https://github.com/yourname/personal-ai-knowledge-assistant.git

cd personal-ai-knowledge-assistant
```

### 创建环境

```bash
conda create -n rag python=3.11

conda activate rag
```

### 安装依赖

```bash
pip install -r requirements.txt
```

### 配置 API Key

复制：

```
.env
```

修改：

```
DEEPSEEK_API_KEY=你的Key
```

### 运行

```bash
streamlit run app.py
```

浏览器访问：

```
http://localhost:8501
```

---

## 功能展示

上传 PDF

↓

自动建立知识库

↓

用户提问

↓

LangChain Agent

↓

向量检索

↓

DeepSeek 回答

↓

返回引用来源

---

## 后续规划

- 支持 Markdown
- 支持 DOCX
- Hybrid Search（BM25 + Dense Retrieval）
- Reranker
- LangGraph Agent
- 多文档管理
- Docker 一键部署

---


