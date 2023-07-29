import argparse
from cliftonai.chatbot import Chatbot

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('question',
                        type=str,
                        help='Your question')
    args = parser.parse_args()

    chatbot = Chatbot()
    response = chatbot.ask(args.question)

    print(f'\nQuestion: {response.question}')
    print(f'\nAnswer: {response.answer}')
    print('='*50)

    for i, doc in enumerate(response.source_documents):
        print(f'\nSource Document {i+1}\n')
        print(f'Source Text: {doc.page_content}')
        print(f'Document Name: {doc.metadata["source"]}')
        print(f'Page Number: {doc.metadata["page"]}\n')
        print('='* 60)

    print(f"Time to retrieve response: {response.response_time}")
