import transformers
from transformers import pipeline

# Initialize the text-generation pipeline with GPT-2


def main():
    generator = pipeline('text-generation', model='gpt2')
    history = []
    print("Enter 'quit' to exit")
    while True:
        user_input = input('User: ')
        if user_input.lower() == 'quit':
            break
        history.append(user_input)
        prompt = "\n".join(history)
        response = generator(prompt, max_length=len(prompt.split()) + 50, num_return_sequences=1)[0]['generated_text']
        reply = response[len(prompt):].strip()
        print('Bot:', reply)
        history.append(reply)


if __name__ == '__main__':
    main()
