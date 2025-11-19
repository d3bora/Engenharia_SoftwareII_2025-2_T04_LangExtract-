# 📄 INFRA.md — Infraestrutura Utilizada no Projeto

Este documento descreve detalhadamente toda a infraestrutura utilizada pela equipe para executar as análises das Frentes do projeto. 

---

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
