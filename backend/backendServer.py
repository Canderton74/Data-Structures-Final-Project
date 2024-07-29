from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class RequestHandler(BaseHTTPRequestHandler):

    #collecting the input cities and tree choice from the front end in the POST function
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)


        try:
            # parse the data to store the inputs
            #this is where the
            data = json.loads(post_data)
            city1 = data.get('city1', 'Not provided')
            city2 = data.get('city2', 'Not provided')
            tree_choice = data.get('treeChoice', 'Not provided')

            # create a response to be sent back to the front end
            response = {
                "city1": city1,
                "city2": city2,
                "treeChoice": tree_choice,
                "message": f"Traveling from {city1} to {city2}, with tree choice of {tree_choice}"
            }
            response_json = json.dumps(response)

            # send response back to the front end to be printed in the
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response_json.encode())
        except json.JSONDecodeError:
            # handling JSON errors
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Invalid JSON"}).encode())

    def do_OPTIONS(self):
        # CORS for between hosts
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting HTTP server on port {port}...')
    httpd.serve_forever()


if __name__ == "__main__":
    run()
