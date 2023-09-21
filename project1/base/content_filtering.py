import pickle
import asyncio

def isValid(instance):
    valid = True
    flag = None
    with open('spam_detection_model.pkl', 'rb') as model_file:
        spam_model = pickle.load(model_file)
    if spam_model.predict([instance])[0] == 1:
        valid = False
        flag = "spam"
    return valid,flag
    
async def validate_message(message):
    str = message.body
    valid,flag = isValid(str)
    if not valid:
        await asyncio.sleep(5)
        message.delete()
        print('message deleted')
        return flag
    else:
        print('valid message')
        return None