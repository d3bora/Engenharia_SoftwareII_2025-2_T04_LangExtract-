# 🧠 Engenharia de Software II – 2025.2 – T04  
### Projeto: **LangExtract – Análise de Padrões de Arquitetura**

Este é o repositório oficial da **Atividade 1** da disciplina **Engenharia de Software II (Turma T04)**.  
O objetivo é aplicar técnicas de **Processamento de Linguagem Natural (PLN)** para identificar **Padrões de Arquitetura de Software** em um projeto de código aberto.

O trabalho é dividido em três **frentes de análise**, baseadas no material da disciplina (conforme o [PDF de sugestão](https://www.google.com/search?q=Sugest%25C3%25A3o_Atividade1.pdf)):

1. 🗒️ **Frente 1 – Documentação (READMEs)**  
2. 🧩 **Frente 2 – Código-Fonte (scripts `.py`)**  
3. 🗂️ **Frente 3 – Estrutura do Projeto (pastas, dependências)**  

---

## 🎯 Projeto Alvo da Análise

- **Repositório:** [`google/langextract`](https://github.com/google/langextract)  
- **Descrição:** Biblioteca Python desenvolvida pelo Google que utiliza **Modelos de Linguagem (LLMs)** para extrair informações estruturadas (como dados médicos) a partir de textos não estruturados.  
- **Hipótese Inicial:**  
  A leitura do `README.md` sugere o uso de uma **Arquitetura em Camadas** (separando extração, I/O e visualização) e uma **Arquitetura de Plugins** (para permitir múltiplos provedores de LLMs, como Gemini, OpenAI e Ollama).

---

## ⚙️ Como Reproduzir a Análise

Este repositório contém todo o código necessário para replicar as análises realizadas nas três frentes.

### 1. Configuração do Ambiente

> Recomendamos o uso de um ambiente virtual (`venv`) para isolar as dependências.

```bash
# 1. Clone o repositório
git clone https://github.com/[SEU_USUARIO]/Engenharia_SoftwareII_2025-2_T04_langextract.git
cd Engenharia_SoftwareII_2025-2_T04_langextract

# 2. Crie e ative o ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # No Windows: .\venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt
```

### 2. Executando as Análises

Os scripts de cada frente estão localizados na pasta `/scripts`.

```bash
# Frente 1 – Documentação
python scripts/analise_frente_documentacao.py

# Frente 2 – Código-Fonte (a ser implementado)
# python scripts/analise_frente_2.py

# Frente 3 – Estrutura do Projeto (a ser implementado)
# python scripts/analise_frente_3.py

```

## 🌿 Fluxo de Trabalho (Git Branches)

| Branch | Função |
|--------|--------|
| **main** | Branch principal, representa a versão final e estável. Nenhum commit direto é feito nela. |
| **frente-x-nome** | Branches individuais para cada frente ou tarefa (ex: `frente-1-documentacao`). |

---

## ⚙️ Padrão de Commits

Os commits devem seguir o formato:

```bash
tipo: descrição breve
```
Exemplo:
```bash
feat: adiciona análise da frente 1 de documentação
fix: corrige erro de importação no script de análise
docs: atualiza instruções de execução no README
```


---

## 🧩 Estrutura de Pastas

```bash
.
├── data/                 # Dados brutos e processados
├── outputs/              # Resultados gerados pelas análises
├── scripts/              # Scripts de execução de cada frente
│   ├── analise_frente_documentacao.py
│   ├── analise_frente_2.py
│   └── analise_frente_3.py
├── reports/              # Relatórios finais em formato .md e .pdf
└── README.md             # Documento principal com instruções do projeto
```

## 🧠 Observações Finais

- Sempre execute os scripts a partir da raiz do projeto.
- Use **ambiente virtual** para manter as dependências isoladas.
- Mantenha o padrão de branch e commit para facilitar o versionamento.
- Antes de abrir um **pull request**, execute os scripts e valide os resultados localmente.

---

