
import pandas as pd
from langchain_community.vectorstores import FAISS
from langchain_community.llms import HuggingFacePipeline
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document
from model import load_local_llm

def preprocess_row(row):
    return (
        f"Commune : {row['libelle_commune_insee']}, "
        f"Département : {row['code_departement_insee']}, "
        f"Surface : {row['s_geom_groupe']} m², "
        f"Classe énergétique : {row['rpls_classe_ener_principale']}, "
        f"Année : {row['rpls_l_annee_construction']}, "
        f"Type : {row['rpls_type_construction']}"
    )

def build_rag_qa(csv_path="bdnb_capvm_500k.csv"):
    df = pd.read_csv(csv_path, low_memory=False)
    df = df[[
        "libelle_commune_insee", "code_departement_insee", "s_geom_groupe",
        "rpls_classe_ener_principale", "rpls_l_annee_construction", "rpls_type_construction"
    ]].dropna().astype(str)

    documents = [Document(page_content=preprocess_row(row)) for _, row in df.iterrows()]
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(documents, embedding_model)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    llm_pipeline = load_local_llm()
    llm = HuggingFacePipeline(pipeline=llm_pipeline)

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)
    return qa_chain
