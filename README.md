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
python scripts/analise_frente_sourcecode.py

# Frente 3 – Estrutura do Projeto (a ser implementado)
# python scripts/analise_frente_estruturadoprojeto.py

```
---

## 🧩 Estrutura de Pastas

```bash
.
├── docs/              # Analises manuais
│   ├── analise_manual_estruturado.ipynb
│   ├── analise_manual_codesource.ipynb
│   ├── analise_manual_documentacao.ipynb
├── scripts/              # Scripts de execução de cada frente
│   ├── analise_frente_documentacao.py
│   ├── analise_frente_sourcecode.py
│   └── analise_frente_estruturadoprojeto.py
├── reports/              # Relatórios finais em formato .md e .pdf
└── README.md             # Documento principal com instruções do projeto
```
## 🗒️ Análise da Frente 1: Documentação (README.md)

**Responsável:** Miguel Lucas Santana Freire

### 🎯 Objetivo
Analisar a documentação textual do projeto (`README.md`) para identificar padrões de arquitetura.

---

### 🧠 Modelo Utilizado
**Modelo:** `zero-shot-classification`  
**Base:** `facebook/bart-large-mnli`


### 💡 Por que este modelo?
Dentre os testados, escolhemos o *Zero-Shot Classification* porque ele nos permite classificar um texto usando **rótulos definidos manualmente**, sem a necessidade de treinar um modelo do zero.  
Isso é ideal para projetos de análise arquitetural com poucos exemplos anotados.

### ⚙️ Metodologia
Devido à limitação da *janela de contexto* dos modelos (que não conseguem ler documentos muito longos, cerca de **1024 tokens**), **não analisamos o `README.md` inteiro**.  
Em vez disso, foram selecionadas manualmente as seções com **maior densidade de informação arquitetural**:

- **“Why LangExtract?”** – descreve o pipeline do sistema.  
- **“Adding Custom Model Providers”** – explica o mecanismo de plugins.

O script executado foi:

```bash
python scripts/analise_frente_1.py
```

Foram definidos 5 rótulos candidatos para classificação.

### 📊 Resultado da Análise (Frente 1)

O modelo retornou as seguintes pontuações de confiança:

### 📊 Resultado da Análise

O modelo retornou as seguintes pontuações de confiança:

```plaintext
Texto Analisado: '
Why LangExtract?
1.  Precise Source Grounding: Ma...
----------------------------------------
  plugin architecture              | 60.83%
  layered architecture             | 19.85%
  component-based system           | 11.56%
  pipe-and-filter architecture     | 04.23%
  MVC architecture                 | 03.53%
----------------------------------------

```

-----

## 💻 Análise da Frente 2: Código-Fonte (Code-Search)

**Responsável:** Allex Lemos de Souza Pinheiro

### 🎯 Objetivo

Analisar o **código-fonte** (`.py`) do projeto para encontrar evidências de implementação dos padrões arquiteturais sugeridos pela análise da documentação (Frente 1).

-----

### 🧠 Modelo Utilizado

**Modelo:** Análise Semântica de Código (via Embeddings)
**Base:** `microsoft/codebert-base`

### 💡 Por que este modelo?

O CodeBERT foi escolhido por ser um modelo especializado, pré-treinado em milhões de linhas de código e em linguagem natural. Diferente de um classificador de texto, ele entende a **semântica do código**, permitindo-nos "perguntar" (em inglês) onde certos conceitos arquiteturais (como "plugins" ou "validação de schema") estão implementados no código Python.

### ⚙️ Metodologia

O processo foi focado em encontrar a **similaridade semântica** entre nossas *queries* de arquitetura e os arquivos de código-fonte.

1.  O repositório foi clonado localmente.
2.  Definimos uma série de "queries" (perguntas) baseadas nas hipóteses (ex: "LLM API client integration").
3.  O script converteu cada *query* e cada arquivo `.py` do projeto em um **vetor numérico (embedding)** usando o CodeBERT.
4.  Calculamos a **Similaridade de Cosseno** entre a query e todos os arquivos, ranqueando os 3 arquivos mais relevantes para cada pergunta.

O script executado foi:

```bash
python analise_frente_codesource.py
```

Foram definidas 4 queries de arquitetura para a busca.

### 📊 Resultado da Análise (Frente 2)

A análise de similaridade indicou uma forte concentração de lógica arquitetural em arquivos `__init__.py` e na camada `core`, confirmando as suspeitas da Frente 1.

```plaintext
Query: 'LLM API client integration'
------------------------------
Arquivo: langextract\_compat\__init__.py | Similaridade: 0.9049
Arquivo: langextract\providers\schemas\__init__.py | Similaridade: 0.9003
Arquivo: langextract\core\__init__.py | Similaridade: 0.8924

Query: 'schema validation using pydantic'
------------------------------
Arquivo: langextract\_compat\__init__.py | Similaridade: 0.9102
Arquivo: langextract\providers\schemas\__init__.py | Similaridade: 0.9075
Arquivo: langextract\tokenizer.py | Similaridade: 0.9019

Query: 'text span finding algorithm'
------------------------------
Arquivo: langextract\_compat\__init__.py | Similaridade: 0.8746
Arquivo: langextract\providers\schemas\__init__.py | Similaridade: 0.8667
Arquivo: langextract\core\__init__.py | Similaridade: 0.8646

Query: 'asynchronous request handling'
------------------------------
Arquivo: langextract\_compat\__init__.py | Similaridade: 0.8848
Arquivo: langextract\providers\schemas\__init__.py | Similaridade: 0.8792
Arquivo: langextract\tokenizer.py | Similaridade: 0.8726
```

## 🗂️ Análise da Frente 3: Estrutura do Projeto

**Responsável:** João Antônio Sousa da Silva

### 🎯 Objetivo

Analisar a organização estrutural do projeto (LangExtract), identificando possíveis padrões arquiteturais com base na disposição dos diretórios principais e sua relação semântica.

### 🧠 Modelo Utilizado

Modelo: feature-extraction
Base: bert-base-uncased

### 💡 Por que este modelo?

Escolhemos o modelo BERT-base (feature-extraction) por ser amplamente utilizado para representar textos curtos, como nomes de diretórios e módulos, em vetores semânticos de alta dimensionalidade.
Esses vetores permitem visualizar relações de similaridade e agrupamentos lógicos, úteis para inferir padrões estruturais e estilos arquiteturais como camadas ou módulos funcionais.

### ⚙️ Metodologia

A análise foi conduzida em etapas:

- **Clonagem do repositório original do LangExtract.**

- **Listagem das pastas principais:**
  
```bash
benchmarks, docs, examples, langextract, scripts, tests
```

- **Extração de embeddings dos nomes de cada pasta usando o modelo bert-base-uncased (modo feature-extraction).**

- **Redução de dimensionalidade com o algoritmo t-SNE para projetar as representações em duas dimensões.**

- **Geração de visualização gráfica dos agrupamentos.**

- **Armazenamento dos resultados em resultados_frente3.txt e estrutura_projeto_frente3.png.**

O script executado foi:

```bash
python scripts/analise_frente_estruturadoprojeto.py
```

### 📊 Resultado da Análise (Frente 3)

A análise produziu as seguintes coordenadas 2D (t-SNE) para os módulos principais:

```bash
=== RELATÓRIO - FRENTE 3: Estrutura de Projeto ===

Repositório: https://github.com/google/langextract
Modelo: bert-base-uncased

Pastas analisadas:
 - benchmarks
 - docs
 - examples
 - langextract
 - scripts
 - tests

Coordenadas 2D geradas (t-SNE):

benchmarks: (96.28, -24.08)
docs: (11.33, -75.00)
examples: (-63.22, -9.55)
langextract: (-24.19, 81.64)
scripts: (18.82, 9.05)
tests: (74.39, 72.31)
```

### 📈 Visualização Gráfica

A projeção t-SNE foi representada no gráfico abaixo, gerando o arquivo:

![Gráfico de Estrutura do Projeto](estrutura_projeto_frente3.png)

### 🧩 Interpretação

A projeção indica agrupamentos coerentes entre módulos do projeto:

- langextract e tests aparecem próximos, sugerindo uma forte relação entre a implementação principal e a validação.

- scripts e benchmarks se situam em uma camada de suporte, relacionados à execução e análise de desempenho.

- examples e docs formam uma camada externa, mais voltada à documentação e exemplos de uso.

Esses agrupamentos sugerem que o projeto segue uma arquitetura em camadas, com separação clara entre núcleo funcional, suporte e documentação — um indício de boa modularização e organização arquitetural.

---

## 🔬 Síntese e Conclusão da Atividade

As três frentes de análise (Documentação, Código-Fonte e Estrutura) nos permitiram triangular e validar as características arquiteturais do projeto `google/langextract`. Esta seção consolida os achados da **Análise Manual** (nosso "gabarito", baseado nos notebooks `analise_manual_*.ipynb`) e os compara com os resultados dos modelos de IA.

### 🕵️ Análise Manual (Ground Truth)

Uma inspeção qualitativa da documentação e do código-fonte revelou quatro padrões principais que definem a arquitetura do projeto:

1.  **Padrão Facade (GoF):**
    * **Evidência:** É o padrão central. O `Quick Start` (`README.md`) e o arquivo `langextract/__init__.py` expõem a função `lx.extract()`.
    * **Função:** Esta função é uma "fachada" clássica que esconde toda a complexidade do subsistema (chunking, paralelismo, chamadas de LLM, validação de schema) em uma única chamada.

2.  **Arquitetura de Plugins (Registry):**
    * **Evidência:** A seção `Adding Custom Model Providers` (`README.md`) e a existência da pasta `langextract/providers/` (`código-fonte`).
    * **Função:** Permite que o sistema seja estendido com novos provedores de LLM (Ollama, OpenAI, Gemini) sem alterar o núcleo (`core`) do sistema.

3.  **Padrão Strategy + Factory (GoF):**
    * **Evidência:** Inferido do `README.md` (ao passar `model_id`) e confirmado no código-fonte.
    * **Função:** O sistema usa uma *Factory* para instanciar o provedor de LLM correto (a *Strategy*) com base na configuração passada para a *Facade*.

4.  **Arquitetura em Camadas:**
    * **Evidência:** A própria estrutura de pastas e a separação lógica no código (`analise_manual_codesource.ipynb`).
    * **Função:** O projeto separa claramente suas responsabilidades:
        * **Camada de Domínio/Core:** `langextract/core/` (lógica de extração).
        * **Camada de Infra/Provedores:** `langextract/providers/` (comunicação com LLMs externos).
        * **Camada de Apresentação/Suporte:** `docs/`, `examples/`, `benchmarks/`.

---

### 📊 Comparativo: Análise Manual vs. Análise por IA

Com o "gabarito" da análise manual em mãos, podemos agora comparar o desempenho dos três modelos de IA.

| Padrão Identificado | Análise Manual (Gabarito) | AI - Frente 1 (Docs)<br>`facebook/bart-large-mnli` | AI - Frente 2 (Código)<br>`microsoft/codebert-base` | AI - Frente 3 (Estrutura)<br>`bert-base-uncased` |
| :--- | :---: | :--- | :--- | :--- |
| **Arquitetura em Camadas** | **Sim** | **Confirmado** (19.85%) | **Confirmado** (Localizou `core` vs `providers`) | **Confirmado** (Visualizou a separação t-SNE)<br> ![Visualização t-SNE](./outputs/estrutura_projeto_frente3.png) |
| **Arquitetura de Plugins** | **Sim** | **Confirmado** (60.83%) | **Confirmado** (Localizou `LLM API integration`) | Não Aplicável |
| **Padrão Facade** | **Sim** | **Falha (Falso Negativo)** | **Confirmado** (Localizou `__init__.py` como central) | Não Aplicável |
| **Padrão Strategy/Factory**| **Sim** | **Falha (Falso Negativo)** | **Confirmado** (Localizou `schema validation` e `LLM API...`) | Não Aplicável |

---

### 🏆 Avaliação de Efetividade dos Modelos

A análise da tabela mostra que a efetividade não está em um único modelo, mas na **triangulação das três frentes**. Cada modelo teve um papel crucial.

1.  **Frente 1 (`facebook/bart-large-mnli`): O "Desbravador"**
    * **Efetividade:** Foi o mais rápido para **validar as hipóteses óbvias**. Ele confirmou "Plugin" e "Camadas" (que estavam explícitos no `README`) em segundos.
    * **Limitação (e Veredito):** Foi **ineficaz** para descobrir padrões *implícitos*. Ele foi "cego" para os padrões **Facade** e **Strategy** porque eles não estavam nos rótulos que fornecemos (`rotulos_candidatos`). Isso prova que modelos *Zero-Shot* são bons para confirmar o que se sabe, mas ruins para descobrir o que não se sabe.

2.  **Frente 3 (`bert-base-uncased`): O "Arquiteto"**
    * **Efetividade:** Foi altamente efetivo para **confirmar a visão macro** (alto nível) da **Arquitetura em Camadas**. A análise t-SNE provou visualmente que a separação de responsabilidades (ex: `langextract` e `tests` vs. `docs` e `examples`) é uma decisão de design intencional.
    * **Limitação (e Veredito):** É um modelo de propósito específico. Não serve para identificar padrões de design (como Facade), apenas padrões estruturais.

3.  **Frente 2 (`microsoft/codebert-base`): O "Auditor" (O Mais Efetivo)**
    * **Efetividade:** Este foi, sem dúvida, **o modelo mais efetivo e robusto da análise**.
    * **Justificativa:** Diferente da Frente 1 (que só lia texto) e da Frente 3 (que só via nomes de pastas), o `codebert-base` foi o único que **entendeu a semântica do código-fonte**.
        * Ele não só confirmou as "Camadas" e "Plugins" (achando `core`, `providers` e `LLM API integration`).
        * Ele foi o único modelo de IA que **encontrou evidências** dos padrões que a Frente 1 perdeu: **Facade** (ao apontar a alta relevância do `__init__.py`) e **Strategy/Factory** (ao apontar `schema validation` e a integração de APIs).

**Veredito Final:** O **`microsoft/codebert-base`** (Frente 2) foi o modelo mais efetivo, pois foi capaz de auditar e localizar a implementação real dos padrões no código, validando as suspeitas da Frente 1 e da Análise Manual, e descobrindo padrões que os outros modelos não conseguiram.
### ✅ Conclusão

A análise estrutural do projeto LangExtract evidencia uma organização bem definida, na qual cada diretório cumpre uma função distinta dentro de um arranjo em camadas. Diante disso,
projeto google/langextract usa, de fato, uma arquitetura robusta baseada em Camadas, Plugins, Facade e Strategy.
Essa estrutura reforça a presença de boas práticas de engenharia de software e baixo acoplamento entre módulos, características de sistemas escaláveis e manuteníveis.

## 🧠 Observações Finais

- Sempre execute os scripts a partir da raiz do projeto.
- Use **ambiente virtual** para manter as dependências isoladas.
- Mantenha o padrão de branch e commit para facilitar o versionamento.
- Antes de abrir um **pull request**, execute os scripts e valide os resultados localmente.

---

