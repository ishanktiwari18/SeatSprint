from rest_framework.response import Response

def success_response(data=None, message=None, status_code=200):
    response = {'success': True}
    if data is not None:
        response['data'] = data
    if message:
        response['message'] = message
    return Response(response, status=status_code)

def error_response(message, status_code=400, errors=None):
    response = {'success': False, 'error': message}
    if errors:
        response['errors'] = errors
    return Response(response, status=status_code)
