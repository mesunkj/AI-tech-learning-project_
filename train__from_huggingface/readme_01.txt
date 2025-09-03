
huggingface
1. 什麼是 Hugging Face : https://tw.alphacamp.co/blog/hugging-face : 
----Hugging Face 是一個擁有豐富模型與資料庫的 AI 開源社群平台，已成為全球 AI 人工智慧領域的重要資源。

2. 應用: https://solwen.ai/posts/hugging-face

Hugging Face 介紹｜Hugging Face 創業歷史與理念
Hugging Face 功能｜探索 Hugging Face 模型與工具
Hugging Face 教學｜模型下載方法與使用範例分享
Hugging Face費用｜Hugging Face 收費方案介紹



模型文件說明: llama

meta-llama/Llama-3.2-1B 		co name/model name
Text Generation
B 	 size

ex. type of model as text to image
openfree/flux-chatgpt-ghibli-lora


applicaeent.
1. user local. dn load 
2. cloud service. like open ai, together ai, 



work frame : pytorch, langchain


window os:
1. install python from microsoft, store
2. git install from git website

vs code:
1. short key
   1.1 call ps window : ctrl + ~
   1.2 call python kerner : ctrl + shift + p
2. create file type : file -> 新增檔案 --> jupyter 

create env in vs code :
1. open ps window : key in python -m venv ./.venv
remark: ./.venv means create named ".venv" under  current work folder
2. 建立虛擬環境 #https://docs.python.org/zh-tw/dev/library/venv.html#creating-virtual-environments
3. if Failed:
    您的虛擬環境啟用腳本 Activate.ps1 屬於 PowerShell 腳本，因此受到了這個限制。

    解決方案：更改 PowerShell 執行原則
    open PowerShell in window os by "以系統管理員身份開啟 PowerShell"
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

    if done as above, close all teminal opened in vs code
    reopen vs code, then open terminal, you would see .venv actived


select python env.:
in upper side of right corner select "選取核心"


github
    1. user mesunkj/sunkj1003 email stwin00002/appwin00002


    2. repository : 
      2.1. create a new one in github as AI_test_00001
      2.2. as a storage in cloud

    3. clone git code into vs
      3.0 install git in window os from window store
      3.1 clone remote(github) into local(vs code), command like     git clone https://github.com/mesunkj/AI_test_00001.git
          3.1.1 find clone http address picked from button named "code" in gitHub repository site
	  3.1.2 in vs code, key command(after open ps ctrl+~)  like     git clone https://github.com/mesunkj/AI_test_00001.git

    4. sync local dataset with remote(gitHub)
      4.1. Only select to be synced folder and open it into new window ( ctrl + K + O)
      4.2. select button(原始控制檔) 
      4.3. select files to be synced then keyin sign "+"
      4.4. at last, press sign "V" at right side of button "提交" and select "提交推送"
      4.5. check all files if sync done at gitHub 
      4.6. as secret key exist in file, sync action will be blocked 
          4.6.1 to do action about cancel block sync while file include secret key
          4.6.2 press 'view code' in error prompt window, 
          4.6.3 then find link with text 'or allow user with secret key in file'






train:
https://www.modernizeconsulting.ai/post/tutorial-using-langchain-to-train-large-language-models-with-private-company-data


???
vs code refresh
vs code 正在重新
github reposity "main"






