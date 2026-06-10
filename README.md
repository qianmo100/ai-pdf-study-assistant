# AI PDF Study Assistant

基于 Gradio 和 OpenAI API 开发的 AI PDF 学习助手。

## 项目简介

AI PDF Study Assistant 是一个面向学习场景的 PDF 智能助手。用户可以上传 PDF 文件，系统会自动提取 PDF 文本内容，并调用大语言模型完成内容总结和基于 PDF 的问答。

## 功能特点

* 支持上传 PDF 文件
* 自动提取 PDF 文本内容
* 支持 AI 总结 PDF 核心内容
* 支持根据 PDF 内容进行提问
* 使用 Gradio 构建本地网页界面
* 使用 `.env` 管理 API Key，避免密钥泄露

## 技术栈

* Python
* Gradio
* PyMuPDF
* OpenAI API
* python-dotenv
* Git / GitHub

## 项目结构

```text
ai-pdf-study-assistant
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

说明：

* `app.py`：项目主程序
* `requirements.txt`：项目依赖
* `README.md`：项目说明文档
* `.gitignore`：Git 忽略文件配置
* `.env`：本地环境变量文件，不上传 GitHub

## 安装依赖

```bash
pip install -r requirements.txt
```

## 配置环境变量

在项目根目录创建 `.env` 文件：

```env
API_KEY=你的OpenAI API Key
BASE_URL=https://api.openai.com/v1
MODEL_NAME=gpt-4o-mini
```

注意：`.env` 文件包含 API Key，不要上传到 GitHub。

## 运行项目

```bash
python app.py
```

运行后，在浏览器中打开：

```text
http://127.0.0.1:7860
```

## 当前版本

V2 版本已实现：

* PDF 上传
* PDF 文本解析
* AI 自动总结
* 基于 PDF 的问答

## 后续计划

* 支持长 PDF 分块处理
* 增加更稳定的长文本总结能力
* 增加 RAG 检索问答功能
* 优化页面布局
* 增加学习题目生成功能

## License

MIT License

