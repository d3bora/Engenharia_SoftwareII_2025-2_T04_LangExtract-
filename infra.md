# 📄 INFRA.md — Infraestrutura Utilizada no Projeto

Este documento descreve detalhadamente toda a infraestrutura utilizada pela equipe para executar as análises das Frentes do projeto. 

## 💻 Ambiente da Frente 2 – Análise de Código Fonte

A frente 2 (Busca Semântica no Código com CodeBERT) foi executada localmente, usando a IDE **VSCode** no sistema operacional Linux.

As especificações do hardware utilizado são:

### 🔹 Processamento
- **CPU:** AMD Ryzen 5 5500u
- **GPU:** AMD Radeon Graphics (Integrada)

### 🔹 Memória e Armazenamento
- **RAM Total:** 12.0 GB
- **Armazenamento Disponível:** ~256 GB (SSD)

### 🔹 Sistema Operacional
- **Pop!_OS 22.04 LTS**

### 🔹 Versão do Python
- **Python 3.12.x** (Executado em ambiente virtual `venv`)

### 🔹 Bibliotecas Principais Utilizadas
- `transformers` (Carregamento do modelo CodeBERT)
- `torch` (Processamento tensorial/Deep Learning)
- `gitpython` (Clonagem automatizada do repositório)
- `pathlib` (Manipulação de caminhos de arquivos)

## 📌 Observações Sobre a Execução Local (Frente 2)

- **Uso de CPU/GPU:** Como o hardware não possui placa NVIDIA com CUDA, o PyTorch utilizou a **CPU** para os cálculos de inferência. Apesar disso, o desempenho foi satisfatório.
- **Consumo de Memória:** O modelo `microsoft/codebert-base` ocupou aproximadamente 500MB de RAM, o que foi facilmente suportado pelos 12GB disponíveis.
- **Armazenamento:** O repositório `langextract` foi clonado localmente e processado sem impactar significativamente o espaço em disco.

## ✔️ Conclusão (Frente 2)

A infraestrutura local foi totalmente adequada para a atividade. O hardware suportou a execução do modelo de linguagem e o cálculo de similaridade de cosseno para todos os arquivos `.py` do projeto sem gargalos de performance impeditivos.



## 🖥️ Ambiente da Frente 3 – Análise de Estrutura do Projeto

A Frente 3 (Estrutura de Pastas usando *Feature Extraction*) foi executada no ambiente **Google Colab Free**, utilizando recursos computacionais fornecidos pela plataforma.



## ☁️ Especificações da Nuvem (Google Colab – Free Tier)

Durante a execução da análise, o Google Colab Free disponibilizou os seguintes recursos:

### 🔹 GPU
- Modelo: **NVIDIA Tesla T4**
- VRAM: **15 GB**

### 🔹 CPU
- Tipo: **Intel Xeon**
- Núcleos disponíveis: **2**
- Clock aproximado: **2.20 GHz**

### 🔹 Memória RAM
- RAM total disponível: **12.6 GB**

### 🔹 Armazenamento Temporário
- Cerca de **78 GB** disponíveis no diretório `/content/`

### 🔹 Sistema Operacional
- **Ubuntu 22.04 LTS** (imagem base do Colab)

### 🔹 Versão do Python
- **Python 3.12.x**

### 🔹 Bibliotecas Principais Utilizadas
- `transformers`
- `torch`
- `sklearn`
- `matplotlib`
- `pandas`
- `numpy`
- `gitpython`



## 📌 Observações Importantes Sobre o Ambiente

- A GPU **não é garantida** no Colab Free — depende de disponibilidade.  
- As sessões possuem tempo limitado (entre 2h e 12h), podendo desconectar sem aviso.  
- O ambiente é temporário: sem salvar no Google Drive, **todos os arquivos são apagados** ao final da sessão.  
- Caso a GPU não estivesse disponível, o script rodava automaticamente em **CPU**, com desempenho mais lento.  



## ✔️ Conclusão

O Google Colab Free forneceu recursos suficientes para:

- Executar modelos **BERT** para *feature extraction*  
- Gerar embeddings das pastas do projeto **LangExtract**  
- Aplicar **t-SNE** para redução de dimensionalidade  
- Criar visualizações da estrutura arquitetural do repositório  

A infraestrutura foi adequada para cumprir todas as etapas da análise da **Frente 3**.
