from app.analys.parse import Test, TestOfCode


data: Test = TestOfCode()
text = "Что выдаст код, если пользователь введёт <code>data</code>"
data.set_text(text, num=2, path_code='code.py')
data.export()
