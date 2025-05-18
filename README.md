# Bot de Cuidados com Pets no Telegram

Um bot do Telegram que fornece orientações e responde dúvidas sobre os primeiros cuidados ao adotar um novo pet.

## Instruções de Configuração

1. Clone este repositório
2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
3. Crie um arquivo `.env` no diretório raiz e adicione seu Token do Bot do Telegram:
   ```
   TELEGRAM_BOT_TOKEN=seu_token_aqui
   ```
4. Execute o bot:
   ```bash
   python bot.py
   ```

## Funcionalidades

- Responde dúvidas sobre adoção e primeiros cuidados
- Fornece orientações para diferentes tipos de pets (cachorros, gatos, etc.)
- Formato interativo de perguntas e respostas
- Interface fácil de usar

## Como Obter um Token do Bot do Telegram

1. Abra o Telegram e procure por "@BotFather"
2. Inicie uma conversa com o BotFather
3. Envie o comando `/newbot`
4. Siga as instruções para criar seu bot
5. Copie o token da API fornecido pelo BotFather
6. Cole o token no seu arquivo `.env`

## Exemplos de Perguntas

Você pode fazer perguntas como:
- "O que fazer no primeiro dia do meu cachorro?"
- "Com que frequência devo alimentar meu gato?"
- "Quais são os cuidados básicos de saúde para cães?"
- "Como adaptar minha casa para pets?"
- "Quais são algumas dicas de treinamento?" 