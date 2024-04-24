import openai

def get_car_ai_bio(model, brand , year):
    prompt = ''''
    me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas expecificas sobre o modelo do carro
'''
    openai.api_key = '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'
    response = openai.Completion.create(
        model = 'text-davinci-003',
        prompt='',
        max_tokens=1000,
    )
    return response['choices'][0]['text']