def lambda_handler(event, context):
    texto = event.get('text',0)
    n = event.get('n',0)
    if texto!=0 and n!=0:
        for i in range(n):
            print(texto)
            
        return {
            'statusCode': 200,
            'body': texto
        }
    return {
        'statusCode': 400,
        'body': 'parametros incorrecotos'
    }
