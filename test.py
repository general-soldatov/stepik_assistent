import json

def step_visual():
    with open('2055467_1_text.step', 'r', encoding='utf-8') as file:
        text = json.load(file)

    with open('text.step', 'w', encoding='utf-8') as file:
        data = json.dumps(text, ensure_ascii=False, indent=4)
        file.write(data)

step_visual()
