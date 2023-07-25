import timeit
import argparse
from cliftonai.chain import ChainFactory

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('question',
                        type=str,
                        help='Your question')
    args = parser.parse_args()

    start = timeit.default_timer()
    chain = ChainFactory.create()
    response = chain({'query': args.question})
    end = timeit.default_timer()

    print(f'\nQuestion: {args.question}')
    print(f'\nAnswer: {response["result"]}')
    print('='*50)

    # Process source documents
    source_docs = response['source_documents']
    for i, doc in enumerate(source_docs):
        print(f'\nSource Document {i+1}\n')
        print(f'Source Text: {doc.page_content}')
        print(f'Document Name: {doc.metadata["source"]}')
        print(f'Page Number: {doc.metadata["page"]}\n')
        print('='* 60)

    print(f"Time to retrieve response: {end - start}")
