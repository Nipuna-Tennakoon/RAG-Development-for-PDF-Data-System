from langchain_community.document_loaders import PyMuPDFLoader


data_dir = "../data"
output_dir = "../results"

def main():
    extracted_texts = open(f"{output_dir}/extracted_texts.txt", "wb")
    loader = PyMuPDFLoader(f"{data_dir}/RAG development.pdf", mode = "page")
    docs = loader.load()
    page_count = len(docs)

    for i in range(10):
        texts = docs[i].page_content.encode("utf-8")
        extracted_texts.write(texts)
        extracted_texts.write(bytes((12,)))
        
    extracted_texts.close()

if __name__ == "__main__":
    main()

