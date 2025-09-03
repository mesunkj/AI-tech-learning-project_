# AI 技術學習專案

import os
from transformers import pipeline

def main():
    # 設定模型
    model_name = "meta-llama/Llama-3.2-1B"
    text_generator = pipeline("text-generation", model=model_name)

    # 輸入提示
    prompt = input("請輸入提示文本：")

    # 生成文本
    generated_text = text_generator(prompt, max_length=100, num_return_sequences=1)

    # 輸出生成的文本
    print("生成的文本：")
    print(generated_text[0]['generated_text'])

if __name__ == "__main__": # 確保此腳本是主程序
    main() 