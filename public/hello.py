from urlparse import parse_qsl

def app(environ, start_response):
    data = b""
    
    if environ['REQUEST_METHOD'] == 'GET':
        if environ['QUERY_STRING'] != '':
            d = parse_qsl(environ['QUERY_STRING'])
            for ch in d:
                data += ' = '.join(ch) + '\n'
    
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
