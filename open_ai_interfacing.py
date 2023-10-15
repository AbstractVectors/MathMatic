import openai

openai.api_key = "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"


def chat_gpt(prompt_text: str, conversation: list, privilage: str = 'user', conversation_level_tracker: dict=None, level: int=0):
    conversation.append({'role': privilage, 'content': prompt_text})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    if conversation_level_tracker is not None:
        if level in conversation_level_tracker:
            conversation_level_tracker[level].append(len(conversation) - 1)
        else:
            conversation_level_tracker[level] = [len(conversation) - 1]
        if level >= 2:
            num_delete = 0
            for indices in sorted(conversation_level_tracker[level-2], reverse=True):
                conversation.pop(indices)
                num_delete += 1
            for key, value in conversation_level_tracker.items():
                for index in range(len(value)):
                    conversation_level_tracker[key][index] -= num_delete
    if privilage != 'system':
        reply = response['choices'][0]['message']['content']
        conversation.append({"role": "assistant", "content": reply})
        if conversation_level_tracker is not None:
            if level in conversation_level_tracker:
                conversation_level_tracker[level].append(len(conversation) - 1)
            else:
                conversation_level_tracker[level] = [len(conversation) - 1]
        return reply
    return None
