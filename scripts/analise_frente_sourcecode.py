import os
import glob
import torch
import git
from pathlib import Path
from transformers import AutoTokenizer, AutoModel
from torch.nn.functional import cosine_similarity

# CONFIGURAÇÕES
REPO_URL = "https://github.com/google/langextract.git"
REPO_PATH = "./langextract_repo"
MODEL_NAME = "microsoft/codebert-base"
OUTPUT_FILE = "resultados_frente2.txt"

# 1. SETUP DO MODELO
print(f"Verificando dispositivo...")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Usando: {device}\n")

print(f"Carregando modelo {MODEL_NAME}...")
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModel.from_pretrained(MODEL_NAME).to(device)
    print("Modelo carregado com sucesso!\n")
except Exception as e:
    print(f"Erro ao carregar modelo: {e}")
    exit()

# 2. PREPARAÇÃO DOS DADOS (CLONE & MAPEAMENTO)
REPO_PATH_ABS = Path(REPO_PATH).resolve()

if not REPO_PATH_ABS.exists():
    print(f"Clonando repositório {REPO_URL}...")
    try:
        git.Repo.clone_from(REPO_URL, str(REPO_PATH_ABS))
        print("Repositório clonado!\n")
    except Exception as e:
        print(f"Erro ao clonar: {e}")
else:
    print("Repositório já existe localmente.\n")

arquivos_python = [str(p) for p in REPO_PATH_ABS.rglob("*.py")]

print(f"Encontrados {len(arquivos_python)} arquivos Python para análise.\n")

if len(arquivos_python) == 0:
    print("ERRO CRÍTICO: Nenhum arquivo .py encontrado.")
    exit()

# 3. FUNÇÕES DE BUSCA
def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512).to(device)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)

def buscar_no_codigo(query, lista_arquivos, top_k=3):
    print(f"Executando busca por: '{query}'...")
    query_vec = get_embedding(query)
    
    resultados = []
    for i, arquivo_path in enumerate(lista_arquivos):
        if i % 10 == 0: print(f".", end="", flush=True)
        
        try:
            with open(arquivo_path, 'r', encoding='utf-8', errors='ignore') as f:
                conteudo = f.read()
            
            code_vec = get_embedding(conteudo)
            sim = cosine_similarity(query_vec, code_vec).item()
            
            nome_relativo = os.path.relpath(arquivo_path, REPO_PATH)
            resultados.append((nome_relativo, sim))
            
        except Exception as e:
            pass

    print(" Concluído!")
    resultados.sort(key=lambda x: x[1], reverse=True)
    return resultados[:top_k]

# 4. EXECUÇÃO DAS ANÁLISES
QUERIES = [
    "LLM API client integration",
    "schema validation using pydantic",
    "text span finding algorithm",
    "asynchronous request handling"
]

print("\nINICIANDO ANÁLISE DE CÓDIGO PYTHON COM CODEBERT...\n")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f_out:
    f_out.write(f"RELATÓRIO DE ANÁLISE - FRENTE 2 (CodeBERT) - PYTHON\n")
    f_out.write(f"=================================================\n\n")

    for query in QUERIES:
        top_resultados = buscar_no_codigo(query, arquivos_python)
        
        print(f"\nTop 3 resultados para '{query}':")
        f_out.write(f"Query: '{query}'\n")
        f_out.write("-" * 30 + "\n")
        
        for nome, score in top_resultados:
            print(f"    {nome} | Score: {score:.4f}")
            f_out.write(f"Arquivo: {nome} | Similaridade: {score:.4f}\n")
        
        print("-" * 40 + "\n")
        f_out.write("\n")

print(f"Análise finalizada! Resultados salvos em '{OUTPUT_FILE}'.")
