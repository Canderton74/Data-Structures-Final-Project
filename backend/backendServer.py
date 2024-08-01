from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import csv
from RedBlackTree import RedBlackTree
from ProbabilityCalculator import *


class RequestHandler(BaseHTTPRequestHandler):



    #collecting the input cities and tree choice from the front end in the POST function
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        #take in the data from the frontend and create the tree
        try:
            # parse the data to store the inputs
            #this is where the
            data = json.loads(post_data)
            city1 = data.get('city1', 'Not provided')
            city2 = data.get('city2', 'Not provided')
            tree_choice = data.get('treeChoice', 'Not provided')

            # create tree based on type that is chosen
            if tree_choice == 'Red Black Tree':
                tree = RedBlackTree()
            #else statement for the B+ Tree

            count = 0
            #insert each accident from the dataset
            with open('US_Accidents_2023.csv', 'r') as f:
                allData = csv.reader(f)
                headers = next(allData)
                for row in allData:
                    count += 1
                    city = row[12]
                    tree.insert(city)
            print(f'Number of Accidents in 2023: {count}')
            #search for each city value and store the count
            city1_count = tree.search(city1)
            city2_count = tree.search(city2)

            #this is where we call to the probability function to calculate the value that will be returned in the response below
            probability, distance = calculate_probability(city1, city2, city1_count, city2_count);

            probability = f"{probability:.2f}"
            distance = int(distance)

            # create a response to be sent back to the front end
            response = {
                "city1": city1,
                "city2": city2,
                "treeChoice": tree_choice,
                "message": f"Traveling from {city1} to {city2} with a {tree_choice}: Over your {distance} mile long journey, with {city1} having {city1_count} accidents and {city2} having {city2_count} accidents in 2023, the probability that you will run into traffic from some form of accident on your journey is {probability}%"
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



    #handling the CORS
    def do_OPTIONS(self):
        # CORS for between hosts
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

#frontend server
def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting HTTP server on port {port}...')
    httpd.serve_forever()


if __name__ == "__main__":
    run()
