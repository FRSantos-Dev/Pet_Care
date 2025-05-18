PET_CARE_INFO = {
    "general": {
        "welcome": "Bem-vindo ao Assistente de Cuidados com Pets! Posso ajudar você com dúvidas sobre adoção e cuidados com seu novo pet. O que você gostaria de saber?",
        "help": "Você pode me perguntar sobre:\n- Primeiros passos após a adoção\n- Requisitos básicos de cuidados\n- Orientações sobre alimentação\n- Check-ups de saúde\n- Dicas de treinamento\n- Como adaptar sua casa para pets\n\nBasta digitar sua pergunta ou usar /start para começar!",
    },
    "dogs": {
        "first_day": """Aqui está o que você precisa fazer no primeiro dia do seu cachorro:
1. Criar um espaço seguro com cama e brinquedos
2. Mostrar onde estão os potes de comida e água
3. Levá-lo para um passeio curto para explorar o bairro
4. Dar tempo para ele se adaptar ao novo ambiente
5. Começar a estabelecer uma rotina de alimentação e passeios""",
        "feeding": """Orientações de alimentação para cães:
- Filhotes (2-6 meses): 3-4 refeições por dia
- Cães adultos: 2 refeições por dia
- Use ração de alta qualidade apropriada para a idade e tamanho
- Sempre forneça água fresca
- Evite comida humana, especialmente chocolate, uvas e cebolas""",
        "health": """Cuidados essenciais de saúde para cães:
1. Check-ups veterinários regulares (anualmente)
2. Vacinações
3. Prevenção contra pulgas e carrapatos
4. Prevenção contra vermes do coração
5. Higiene regular
6. Cuidados dentários""",
    },
    "cats": {
        "first_day": """Aqui está o que você precisa fazer no primeiro dia do seu gato:
1. Prepare um quarto tranquilo com caixa de areia, comida, água e cama
2. Deixe-o explorar no seu próprio ritmo
3. Mostre onde está a caixa de areia
4. Forneça lugares para se esconder
5. Dê espaço para ele se adaptar""",
        "feeding": """Orientações de alimentação para gatos:
- Filhotes (2-6 meses): 3-4 refeições por dia
- Gatos adultos: 2 refeições por dia
- Use ração de alta qualidade apropriada para a idade
- Sempre forneça água fresca
- Considere opções de ração úmida e seca""",
        "health": """Cuidados essenciais de saúde para gatos:
1. Check-ups veterinários regulares (anualmente)
2. Vacinações
3. Prevenção contra pulgas
4. Higiene regular
5. Cuidados dentários
6. Castração/esterilização""",
    },
    "common_questions": {
        "pet_proofing": """Para adaptar sua casa para pets:
1. Remova plantas tóxicas
2. Proteja fios elétricos
3. Guarde produtos químicos e medicamentos com segurança
4. Instale portões de segurança se necessário
5. Remova objetos pequenos que possam ser engolidos
6. Proteja as lixeiras
7. Verifique possíveis rotas de fuga""",
        "training": """Dicas básicas de treinamento:
1. Use reforço positivo
2. Seja consistente com os comandos
3. Comece o treinamento cedo
4. Mantenha as sessões curtas e divertidas
5. Recompense o bom comportamento
6. Seja paciente e persistente""",
    }
}

def get_response(query):
    """
    Process the user's query and return an appropriate response.
    """
    query = query.lower()
    
    # Check for general queries
    if any(word in query for word in ["olá", "oi", "oi", "start"]):
        return PET_CARE_INFO["general"]["welcome"]
    elif "ajuda" in query:
        return PET_CARE_INFO["general"]["help"]
    
    # Check for dog-related queries
    if any(word in query for word in ["cachorro", "cão", "cachorrinho"]):
        if any(word in query for word in ["primeiro", "dia", "adotar"]):
            return PET_CARE_INFO["dogs"]["first_day"]
        elif any(word in query for word in ["alimentar", "comida", "ração"]):
            return PET_CARE_INFO["dogs"]["feeding"]
        elif any(word in query for word in ["saúde", "saudavel", "veterinário"]):
            return PET_CARE_INFO["dogs"]["health"]
    
    # Check for cat-related queries
    if any(word in query for word in ["gato", "gata", "gatinho"]):
        if any(word in query for word in ["primeiro", "dia", "adotar"]):
            return PET_CARE_INFO["cats"]["first_day"]
        elif any(word in query for word in ["alimentar", "comida", "ração"]):
            return PET_CARE_INFO["cats"]["feeding"]
        elif any(word in query for word in ["saúde", "saudavel", "veterinário"]):
            return PET_CARE_INFO["cats"]["health"]
    
    # Check for common questions
    if any(word in query for word in ["adaptar casa", "seguro", "proteger"]):
        return PET_CARE_INFO["common_questions"]["pet_proofing"]
    elif any(word in query for word in ["treinar", "treinamento", "educar"]):
        return PET_CARE_INFO["common_questions"]["training"]
    
    # Default response for unrecognized queries
    return "Desculpe, não tenho certeza sobre isso. Por favor, tente perguntar sobre:\n- Cuidados do primeiro dia\n- Orientações de alimentação\n- Cuidados com a saúde\n- Dicas de treinamento\n- Como adaptar sua casa para pets" 