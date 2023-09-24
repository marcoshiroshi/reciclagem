# 🌱 Sistema Gerenciador de Serviços de Reciclagem

## 🌍🔄 Descrição do Projeto

Este é um projeto de conclusão de curso, desenvolvido por Marcos Hiroshi Souza Mori e Gabriel Dias, estudantes do Centro Universitário do Distrito Federal, sob a orientação da Professora Kadidja Valéria. O projeto consiste em um sistema de gerenciamento de serviços de reciclagem que envolve três atores principais: moradores, catadores, e centros de coleta. O sistema é projetado para facilitar a coleta eficiente de materiais recicláveis.

### 🎯 Objetivos do Projeto
- Promover a educação e o conhecimento
- Gerar empregos
- Ajudar na limpeza das cidades
- Reciclar materiais que seriam descartados de forma incorreta


## 🚀 Funcionalidades Principais

### 🏡 Para Moradores:
- Os moradores podem separar materiais recicláveis em suas residências.
- Com o auxílio do aplicativo, os moradores recem textos, avisos e intruções de como separar os materiais reciláveis da forma correta.
- Quando tiverem uma quantidade significativa de materiais recicláveis, podem utilizar o aplicativo para solicitar a coleta pelos catadores.

### ♻️ Para Catadores:
- Os catadores recebem solicitações de coleta de materiais recicláveis através do aplicativo.
- Eles podem visualizar as solicitações, aceitá-las e organizar suas rotas de coleta.
- O sistema calcula automaticamente as rotas e distâncias a serem percorridas pelos catadores.

### 🏭 Para Centros de Coleta:
- Os centros de coleta recebem os materiais recicláveis coletados pelos catadores.
- O sistema registra e monitora os materiais recebidos, garantindo uma destinação adequada para a reciclagem.


## Tecnologias Utilizadas

- 🐍 Linguagem de Programação: Python
- 🌐 Framework Backend: Django
- 🌐 Framework Frontend: Bootstrap
- 📦 Banco de Dados: SQLite
- 🗺️ Tecnologia de Rota e Distância: JavaScript com a biblioteca Leaflet

## Etapas Concluídas

- 🚀 Configuração do ambiente de desenvolvimento.
- ⚙️ Configuração do projeto.
- 📚 Configuração de frameworks e bibliotecas.
- 🔑 Desenvolvimento do módulo de login.
- 🏠 Criação da página inicial (home page).
- 👤 Perfis de atores: Moradores, Catadores, Centros de Coleta.
- 📝 Cadastro de atores.
- 📦 Cadastro de pedido pelo morador.
- 🚛 Recebimento de pedidos pelo catador.
- 📋 Controle de pedidos pelo catador.
- 🗺️ Sistema de cálculo de rota.

## Próximas Etapas

- 📦 Módulo de pedidos do centro de coleta.
- 📊 Módulo gerenciador de pedidos do centro de coleta.
- 📦 Controle de estoque no centro de coleta.
- 🌟 Sistema de ranqueamento e pontuação.
- 📢 Implementação de banners de notificações.
- 📢📚 Avisos, dicas e instruções para os usuários.

## Etapas a Fazer

- consertar localizacao do mapa iterativo no pedido de catador


## Como Executar o Projeto

1. Clone o repositório para o seu ambiente local: ```git clone https://github.com/marcoshiroshi/reciclagem.git```

2. Crie um ambiente virtual Python e instale as dependências: ```pip install -r "requirements.txt"```

3. Execute as migrações do banco de dados e inicie o servidor: 
```python manage.py migrate```
```python manage.py runserver```

4. Acesse o aplicativo em seu navegador: `http://127.0.0.1:8000`

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---