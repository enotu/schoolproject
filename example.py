from ollama import chat
mess = [{'role' : 'user', 'content' : 'пример'}]
print(chat('phi4-mini', messages = mess).message.content)