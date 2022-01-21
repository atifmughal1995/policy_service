import socketserver

'''
This is a function is used to run a server and provides us a endpoint that can be used
to send request to our service(s).
'''
def run_server(service_handler, ip='127.0.0.1', port='8000'):
    try:
        with socketserver.TCPServer(("", port), service_handler) as httpd:
            print(f"Server Started: http://{ip}:{port}")
            httpd.serve_forever()

    except KeyboardInterrupt:
        print("Server Stopped by Ctrl+C")
        httpd.server_close() 