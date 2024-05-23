from transformers import BertTokenizer, BertForQuestionAnswering
import torch

# Carrega o tokenizer e o modelo pré-treinados BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForQuestionAnswering.from_pretrained('bert-base-uncased')

def get_bert_response(question, context):
    # Codifica a pergunta e o contexto
    inputs = tokenizer.encode_plus(question, context, return_tensors='pt')
    
    # Obtém as pontuações para o início e o fim da resposta
    answer_start_scores, answer_end_scores = model(**inputs)
    
    # Identifica as posições do início e do fim da resposta
    answer_start = torch.argmax(answer_start_scores)
    answer_end = torch.argmax(answer_end_scores) + 1
    
    # Converte os IDs dos tokens na resposta para texto
    answer = tokenizer.convert_tokens_to_ids(inputs['input_ids'][0][answer_start:answer_end])
    
    # Decodifica e retorna a resposta como texto
    return tokenizer.decode(answer)
