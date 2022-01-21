import http.server
import json

'''
This is a Base Service Class, which has all the necessary functions like "request_data" which
extracts POST request data, "success_response" which is used to send response in case of success
and "error_response" in case of failure. This Class provides basic functionality for our service.
And can also be used to develop new services.
'''
class BaseServiceClass(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
        self.post()

    def request_data(self):
        try:
            content_length = 0
            if self.headers['Content-Length']:
                content_length = int(self.headers['Content-Length'])
            
            if content_length:
                data_json = self.rfile.read(content_length)
                data = json.loads(data_json)
            else:
                data = None

            return data

        except:
            raise ValueError("Invalid JSON.")


    def success_response(self, status, reason=None):
        output_data = {}
        output_data['status'] = status

        if reason:
            output_data['reason'] = reason
        
        output_json = json.dumps(output_data)
        self.response(status_code=200, output=output_json)


    def error_response(self, status, reason=None, message=None):
        output_data = {}
        output_data['status'] = status

        if reason:
            output_data['reason'] = reason

        if message:
            output_data['message'] = message
     
        output_json = json.dumps(output_data)
        self.response(status_code=400, output=output_json)

    def response(self, status_code, output):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        self.wfile.write(output.encode('utf-8'))
