import wolframalpha
import wikipedia
import re

def search_wiki(keyword=''):
    searchResults = wikipedia.search(keyword)
    if not searchResults:
        message = "Sorry, No result from Wikipedia. Try again"
        response(message)
        return
    try:
        page = wikipedia.page(searchResults[0])
    except Exception as err:
        page = wikipedia.page(err.options[0])
    wikiTitle = str(page.title.encode('utf-8'))
    wikiSummary = str(page.summary.encode('utf-8'))
    return str(wikiSummary)[2:]

def search(text=''):
    res = client.query(text)
    if res['@success'] == 'false':
        response(search_wiki(text))
    else:
        result = ''
        pod0 = res['pod'][0]
        pod1 = res['pod'][1]
        if (('definition' in pod1['@title'].lower()) or ('result' in pod1['@title'].lower()) or
        (pod1.get('@primary','false') == 'true')):
            result = resolveListOrDict(pod1['subpod'])
            return result
        else:
            question = resolveListOrDict(pod0['subpod'])
            question = question.split('(')[0]
            search_wiki(question)

def resolveListOrDict(variable):
    if isinstance(variable, list):
        return variable[0]['plaintext']
    else:
        return variable['plaintext']

def activity(data):
    if re.search("who are you", data) or re.search("what is your name", data):
        listening = True
        intro = "I'm Wiki-Bandaara. I have access to Wolfram | Alpha and Wikipedia."
        response(intro)
    elif re.search("help", data) or re.search("what do you do", data):
        listening = True
        message = 'I have access to Wolfram|Alpha and Wikipedia.Ask anything.To get results from wikipedia, say so.To quit say bye or stop'
        response(message)
    elif re.search("in wikipedia", data) or re.search("from wikipedia", data):
        listening = True
        result = search_wiki(data)
        if result != None:
            response(result)
    elif re.search("stop", data) or re.search("bye",data) or re.search("quit", data):
        listening = False
        print('Bot: Bye')
        print('Listening stopped')
        return listening
    else:
        listening = True
        result = search(data)
        if result is not None:
            response(result)
        else:
            message = "Please try again."
            response(message)
    return listening

def response(data):
    print('Bot:', data)

appId = 'J6E5UP-37TTV3XWA2'
# Wolfram Instance
client = wolframalpha.Client(appId)
greet = "Hi there, what can I do for you?"
response(greet)
# loop till listening is False
listening = True
while listening == True:
    data = str(input('User: ')).lower()
    if data != '':
        listening = activity(data)
    else:
        message = "Please try again."
        response(message)