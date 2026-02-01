from langchain_community.document_loaders import PyMuPDFLoader
from pathlib import Path

data_dir = "../data"
output_dir = "../results"

def main():
    
    
    path = Path(data_dir)
    if path.is_dir():
        files = [item.name for item in path.iterdir() if item.is_file()]
        print(files)
    else:
        print("The directory does not exists.")
        
       
    for file in files:
        loader = PyMuPDFLoader(f"{data_dir}/{file}", mode="page")
        doc = loader.load()
        print(f"Page count of{file}:{len(doc)}")
        
        with open(f"{output_dir}/{file[:-2]}.txt", "w", encoding="utf8", ) as file_1:
            with open(f"{output_dir}/{file[:-2]}_metadata.txt", "w", encoding="utf8") as file_2:
                for i in range(len(doc)):
                    file_1.write(doc[i].page_content[:1000]+"\n")
                    
                    file_2.write(str(doc[i].metadata)+"\n")
                    
            

if __name__ == "__main__":
    main()

