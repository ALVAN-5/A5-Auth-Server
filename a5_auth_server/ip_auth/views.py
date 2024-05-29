from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
import json
from .validators.validate_ip_address import validateIPAddress
from .validators.validate_token import validateToken
from .validators.validate_session_key import validateSessionKey
from .validators.validate_home_group import validateHomeGroup
from .controllers.createIPUserController import createIPUserController
from .controllers.createSessionController import createSessionController
from .controllers.validateSessionController import validateSessionController
from .controllers.resetIPTokenController import resetIPTokenController
from .controllers.removeIPUserController import removeIPUserController


def createSession(request):
    '''
    Check clientIP parameter from request body in IPs table
        if IP found create session in Sessions table
            session holder IP
            session session_key
            session expiration timestamp (1 week)
        else
            is clientToken a token for any IPUser?
                create session
                    session clientToken's respective IP
                    session session_key
                    session expiration (3 day)
            else
                reject
    '''
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    try:
        params = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return HttpResponseBadRequest()

    try:
        ip = params['clientIP']
    except KeyError:
        return HttpResponseBadRequest()

    try:
        if not validateIPAddress(ip):
            return HttpResponseBadRequest()
    except KeyError:
        return HttpResponseBadRequest()

    return createSessionController(ip=ip)


def createSessionFromToken(request):
    '''
    Check clientIP parameter from request body in IPs table
        if IP found create session in Sessions table
            session holder IP
            session session_key
            session expiration timestamp (1 week)
        else
            is clientToken a token for any IPUser?
                create session
                    session clientToken's respective IP
                    session session_key
                    session expiration (3 day)
            else
                reject
    '''

    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    try:
        params = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return HttpResponseBadRequest()

    try:
        token = params['token']
    except KeyError:
        return HttpResponseBadRequest()

    try:
        if not validateToken(token):
            return HttpResponseBadRequest()
    except KeyError:
        return HttpResponseBadRequest()

    return createSessionController(token=token)


def validateSession(request, session_key):
    '''
    If session_key is in IPSessions
        return 200 {clientIP: <clientIP associated with clientIPProxyKey>}
    Else
        return 301 redirect to create session
    '''
    if validateSessionKey(session_key):
        return validateSessionController(session_key)

    return HttpResponseBadRequest()


def createIPUser(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    try:
        params = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        try:
            paramsString = request.body.decode('ascii')
            params = {}
            for paramSet in paramsString.split('&'):
                if '=' not in paramSet:
                    continue
                pKey = paramSet.split('=')[0]
                pVal = paramSet.split('=')[1]
                params[pKey] = pVal
        except json.decoder.JSONDecodeError:
            return HttpResponseBadRequest()

    try:
        ip = params['clientIP']
        home_group = params['home_group']
    except KeyError:
        return HttpResponseBadRequest()

    try:
        if not validateIPAddress(ip):
            return HttpResponseBadRequest()
        elif not validateHomeGroup(home_group):
            return HttpResponseBadRequest()
    except KeyError:
        return HttpResponseBadRequest()

    return createIPUserController(ip, home_group)


def resetIPToken(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    try:
        params = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return HttpResponseBadRequest()

    try:
        ip = params['clientIP']
        home_group = params['home_group']
    except KeyError:
        return HttpResponseBadRequest()

    try:
        if not validateIPAddress(ip):
            return HttpResponseBadRequest()
        elif not validateHomeGroup(home_group):
            return HttpResponseBadRequest()
    except KeyError:
        return HttpResponseBadRequest()
    
    return resetIPTokenController(ip, home_group)


def removeIPUser(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    try:
        params = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return HttpResponseBadRequest()

    try:
        ip = params['clientIP']
    except KeyError:
        return HttpResponseBadRequest()

    try:
        if not validateIPAddress(ip):
            return HttpResponseBadRequest()
    except KeyError:
        return HttpResponseBadRequest()
    
    return removeIPUserController(ip)
