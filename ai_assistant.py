# =============================
# AI Assistant 
# =============================

import openai
openai.api_key = "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"

def ask_ai(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except openai.error.RateLimitError:
        return "API rate limit exceeded. Please try again later."
    except Exception as e:
        return f"Error: {e}"

def answer_question():
    question = input("Enter your question: ")
    prompts = [
        f"Answer this factually: {question}",
        f"Explain briefly: {question}",
        f"Give 3 key points about: {question}"
    ]
    for i, p in enumerate(prompts, 1):
        print(f"\nProcessing Response Option {i}...")
        response = ask_ai(p)
        print(f"\nResponse Option {i}:\n{response}")

def summarize_text():
    text = input("Paste the text to summarize: ")
    prompts = [
        f"Summarize the following text: {text}",
        f"What are the main points of this text: {text}?",
        f"Provide a short overview of this: {text}"
    ]
    for i, p in enumerate(prompts, 1):
        print(f"\nProcessing Response Option {i}...")
        response = ask_ai(p)
        print(f"\nResponse Option {i}:\n{response}")

def generate_creative_content():
    idea = input("Enter topic/idea: ")
    prompts = [
        f"Write a short story about: {idea}",
        f"Create a poem about: {idea}",
        f"Generate a creative essay on: {idea}"
    ]
    for i, p in enumerate(prompts, 1):
        print(f"\nProcessing Response Option {i}...")
        response = ask_ai(p)
        print(f"\nResponse Option {i}:\n{response}")

def main():
    while True:
        print("\n=== Welcome to Your AI Assistant ===")
        print("1. Answer Questions")
        print("2. Summarize Text")
        print("3. Generate Creative Content")
        print("4. Exit")
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == "1":
            answer_question()
        elif choice == "2":
            summarize_text()
        elif choice == "3":
            generate_creative_content()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")
            
if __name__ == "__main__":
    main()
