#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def simple_app(environ, start_response):
    from wsgiref.util import setup_testing_defaults
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    ret = [("%s: %s\n" % (key, value)).encode("utf-8")
           for key, value in environ.items()]
    return ret

def main():
    from wsgiref.simple_server import make_server
    with make_server('', 8000, simple_app) as httpd:
        print("Serving on port 8000...")
        httpd.serve_forever()


if __name__ == '__main__':
    main()


