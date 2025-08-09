from flask import Flask, jsonify, request

app = Flask(__name__)

# 示例路由
@app.route('/')
def home():
    return "Hello, World!"

# 示例 API 路由
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')  # 取得URL參數
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run(debug=True)
    pass
