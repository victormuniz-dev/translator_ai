# 🌐 Translator AI - Serviço de Tradução com LangChain & LangServe

Este repositório contém uma aplicação completa de tradução de idiomas utilizando a API do Google Gemini, orquestrada com **LangChain** e disponibilizada como uma API web RESTful através do **LangServe** e **FastAPI**.

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**: Linguagem de programação principal.
* **LangChain**: Framework para desenvolvimento de aplicações baseadas em modelos de linguagem.
  * `ChatGoogleGenerativeAI`: Integração com os modelos Gemini da Google.
  * `ChatPromptTemplate`: Criação de prompts dinâmicos e reutilizáveis.
  * `StrOutputParser`: Tratamento e formatação de saídas dos modelos.
* **LangServe**: Biblioteca para implantar cadeias e executáveis do LangChain como APIs REST via FastAPI.
* **FastAPI**: Framework web moderno e rápido para construção das rotas do serviço.
* **Uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.
* **python-dotenv**: Gerenciamento de variáveis de ambiente e chaves de API.
