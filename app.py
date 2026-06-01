import gradio as gr
import fitz
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)


def extract_pdf_text(pdf_file):
    if pdf_file is None:
        return "请先上传 PDF 文件。", ""

    doc = fitz.open(pdf_file.name)
    text = ""

    for page_index, page in enumerate(doc):
        page_text = page.get_text()
        text += f"\n\n===== 第 {page_index + 1} 页 =====\n"
        text += page_text

    if not text.strip():
        return "没有提取到文字，可能是扫描版 PDF。", ""

    preview = text[:2000]
    return preview, text


def summarize_pdf(pdf_text):
    if not pdf_text:
        return "请先上传 PDF 并解析。"

    prompt = f"""
请帮我总结下面 PDF 的内容。

要求：
1. 用中文回答
2. 提取核心内容
3. 总结重点知识
4. 给出学习建议

PDF内容：
{pdf_text[:12000]}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "你是一个大学课程学习助手。"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


def ask_pdf(question, pdf_text):
    if not pdf_text:
        return "请先上传 PDF 并解析。"

    if not question.strip():
        return "请先输入问题。"

    prompt = f"""
你是一个 PDF 学习助手。请根据 PDF 内容回答用户问题。

要求：
1. 必须根据 PDF 内容回答
2. 如果 PDF 里没有明确提到，请说“PDF 中没有明确提到”
3. 用中文回答
4. 回答要清晰，适合学生理解

用户问题：
{question}

PDF内容：
{pdf_text[:12000]}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "你是一个严谨的大学课程学习助手。"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


with gr.Blocks(title="AI PDF 学习助手") as demo:
    gr.Markdown("# AI PDF 学习助手")
    gr.Markdown("上传 PDF 后，可以进行内容预览、AI 总结和 PDF 问答。")

    pdf_text_state = gr.State("")

    pdf_file = gr.File(
        label="上传 PDF 文件",
        file_types=[".pdf"]
    )

    parse_button = gr.Button("解析 PDF")

    preview_output = gr.Textbox(
        label="PDF 文字预览",
        lines=12
    )

    parse_button.click(
        fn=extract_pdf_text,
        inputs=pdf_file,
        outputs=[preview_output, pdf_text_state]
    )

    gr.Markdown("## AI 总结")

    summary_button = gr.Button("总结 PDF")

    summary_output = gr.Textbox(
        label="AI 总结结果",
        lines=12
    )

    summary_button.click(
        fn=summarize_pdf,
        inputs=pdf_text_state,
        outputs=summary_output
    )

    gr.Markdown("## 根据 PDF 提问")

    question_input = gr.Textbox(
        label="输入你的问题",
        placeholder="例如：这篇 PDF 主要讲了什么？mini-batch 的作用是什么？"
    )

    ask_button = gr.Button("向 PDF 提问")

    answer_output = gr.Textbox(
        label="AI 回答",
        lines=12
    )

    ask_button.click(
        fn=ask_pdf,
        inputs=[question_input, pdf_text_state],
        outputs=answer_output
    )


demo.launch()