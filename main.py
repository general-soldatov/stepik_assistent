from app.analys.parse import Test, TestOfCode


data: Test = TestOfCode()
text = "Что выдаст код?"
data.set_text(text, num=2, path_code='code.py')
data.export()
