# ----------------------------------------------------
# Análise da Frente 1: Documentação (README.md)
# Modelo: Zero-Shot Classification
# ----------------------------------------------------

from transformers import pipeline
import textwrap

def analisar_documentacao():
    print("Iniciando Análise da Frente 1: Documentação...")
    print("-" * 40)

    # texto do README.md que será analisado (seções "Why LangExtract?" e "Adding Custom Model Providers")

    texto_para_analisar = """
    Why LangExtract?
    1.  Precise Source Grounding: Maps every extraction to its exact location in the source text...
    2.  Reliable Structured Outputs: Enforces a consistent output schema...
    3.  Optimized for Long Documents: Overcomes the "needle-in-a-haystack" challenge... by using an optimized strategy of text chunking, parallel processing, and multiple passes for higher recall.
    4.  Interactive Visualization: Instantly generates a self-contained, interactive HTML file...
    5.  Flexible LLM Support: Supports your preferred models...
    6.  Adaptable to Any Domain: Define extraction tasks for any domain...
    7.  Leverages LLM World Knowledge: Utilize precise prompt wording...

    Adding Custom Model Providers
    LangExtract supports custom LLM providers via a lightweight plugin system. You can add support for new models without changing core code.
    - Add new model support independently of the core library
    - Distribute your provider as a separate Python package
    - Keep custom dependencies isolated
    - Override or extend built-in providers via priority-based resolution
    """

    rotulos_candidatos = [
        "pipe-and-filter architecture",
        "plugin architecture",
        "layered architecture",
        "component-based system",
        "MVC architecture"
    ]

    print("Carregando modelo 'facebook/bart-large-mnli'")

    classificador = pipeline("zero-shot-classification",
                             model="facebook/bart-large-mnli")


    resultado = classificador(textwrap.dedent(texto_para_analisar),
                              candidate_labels=rotulos_candidatos)

    print("\n--- RESULTADO DA ANÁLISE (FRENTE 1) ---")
    print(f"Texto Analisado: '{resultado['sequence'][:50]}...'")
    print("-" * 40)

    for rotulo, pontuacao in zip(resultado['labels'], resultado['scores']):
        percentual = pontuacao * 100
        print(f"  {rotulo:<30} | {percentual:05.2f}%")


if __name__ == "__main__":
    analisar_documentacao()