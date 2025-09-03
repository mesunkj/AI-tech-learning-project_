這是一個使用 **Flask** 框架建立的簡單 Python Web 應用程式。這個應用程式有兩個主要路由：

  * `/`：返回 "Hello, World\!" 的文字。
  * `/api/greet`：可以接受一個名為 `name` 的 URL 參數，並返回一個 JSON 格式的問候訊息，例如 `{"message": "Hello, [你的名字]!"}`。如果沒有提供 `name` 參數，則預設返回 `{"message": "Hello, Guest!"}`。

以下是一個為此專案設計的 **Markdown** 格式 **README.md** 檔案。您可以在 GitHub 上直接使用它。

-----

# 簡單的 Flask Web 應用程式

這是一個基於 Python Flask 框架的簡單範例 Web 應用程式。它展示了如何建立基本的路由、處理 URL 參數以及回傳 JSON 格式的回應。

## 功能

  * **首頁 (/)**: 顯示一個簡單的 "Hello, World\!" 訊息。
  * **問候 API (/api/greet)**:
      * 這是一個 **GET** 請求的 API 端點。
      * 可以透過 URL 參數 `name` 來客製化問候語。
      * 如果提供了 `name` 參數，例如：`  /api/greet?name=Gemini `，它將回傳 `{"message": "Hello, Gemini!"}`。
      * 如果沒有提供 `name` 參數，它將回傳 `{"message": "Hello, Guest!"}`。

## 安裝與執行

### 先決條件

請確保您的系統已安裝 Python 3.6 或更高版本。

### 步驟

1.  **克隆此儲存庫 (如果需要)**：

    ```bash
    git clone [您的儲存庫 URL]
    cd [您的專案目錄]
    ```

2.  **安裝 Flask**：
    您可以使用 `pip` 來安裝 Flask 函式庫。

    ```bash
    pip install Flask
    ```

3.  **執行應用程式**：
    從專案根目錄執行以下命令。

    ```bash
    python app.py
    ```

    應用程式啟動後，您將會在終端機看到類似以下的輸出，表示伺服器正在執行：

    ```
    * Serving Flask app 'app'
    * Running on http://127.0.0.1:5000
    ```

## 使用範例

### 1\. 訪問首頁

在您的瀏覽器中輸入以下 URL：

```
http://127.0.0.1:5000/
```

您將會看到 `Hello, World!` 的文字。

### 2\. 訪問問候 API

  * **不帶參數**：
    在您的瀏覽器中輸入以下 URL：

    ```
    http://127.0.0.1:5000/api/greet
    ```

    將會回傳：

    ```json
    {
      "message": "Hello, Guest!"
    }
    ```

  * **帶有 `name` 參數**：
    在您的瀏覽器中輸入以下 URL：

    ```
    http://127.0.0.1:5000/api/greet?name=User
    ```

    將會回傳：

    ```json
    {
      "message": "Hello, User!"
    }
    ```

## 貢獻

如果您想為這個專案做出貢獻，請隨時提交 Pull Request。

## 許可

這個專案使用 MIT 許可證。

-----