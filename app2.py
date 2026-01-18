from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# 初始化資料庫：建立資料表並新增幾筆課程
def init_db():
    conn = sqlite3.connect('teaching.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY, name TEXT, code TEXT)')
    # 先清空測試資料再新增
    cursor.execute('DELETE FROM courses')
    cursor.execute('INSERT INTO courses (name, code) VALUES ("ASP.NET 轉型 Python", "PY101")')
    cursor.execute('INSERT INTO courses (name, code) VALUES ("HTML5 與 前端開發", "FE202")')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    # 讀取資料庫
    conn = sqlite3.connect('teaching.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM courses')
    data = cursor.fetchall()
    conn.close()
    
    # 這裡演示 Jinja2 模板（就像您的 Razor 語法）
    html_template = """
    <h1>我的教學課程清單</h1>
    <table border="1">
        <tr>ID</tr> <tr>課程名稱</tr> <tr>代號</tr>
        {% for row in data %}
        <tr>
            <td>{{ row[0] }}</td>
            <td>{{ row[1] }}</td>
            <td>{{ row[2] }}</td>
        </tr>
        {% endfor %}
    </table>
    """
    from flask import render_template_string
    return render_template_string(html_template, data=data)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)