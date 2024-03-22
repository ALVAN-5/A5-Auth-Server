from django.http import HttpResponseNotAllowed, HttpResponse
import json

def healthCheck(request):
    '''
        returns 200
    '''
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    return HttpResponse(json.dumps({'health': 'ok'}))
