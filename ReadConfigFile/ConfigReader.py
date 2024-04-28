import configparser
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class ConfigurationHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Handles GET requests and sends response containing configuration data in JSON format.
        self.send_response(200)   # Send 200 OK response with content type set to JSON
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Read and extract configuration data then convert to JSON
        filename = 'sample_config.ini'
        config = self.read_configuration_file(filename)
        configuration_data = self.extract_configuration_data(config)
        json_data = json.dumps(configuration_data, indent=4)

        # Send JSON data as response body
        self.wfile.write(json_data.encode())

    def read_configuration_file(self, filename):
        config = configparser.ConfigParser()  # Reads a configuration file and returns a ConfigParser object.
        try:
            with open(filename) as f:
                config.read_file(f)
            return config
        except FileNotFoundError:
            print("Error: Configuration file '{}' not found.".format(filename))
            return None
        except Exception as e:
            print("Error reading configuration file:", e)
            return None

    def extract_configuration_data(self, config):
        if config is None:
            return None
        data = {}
        for section in config.sections():  # Iterate over each section in file and store key-value pairs to dictionary
            data[section] = {}
            for key, value in config.items(section):
                data[section][key] = value
        return data


def save_data_to_json(data):
    try:
        with open('output.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
            print("Data saved to output.json successfully.")
    except Exception as e:
        print("Error saving data to JSON file:", e)


def main():
    filename = 'sample_config.ini'
    config = ConfigurationHandler.read_configuration_file(None, filename)
    if config:
        configuration_data = ConfigurationHandler.extract_configuration_data(None, config)
        save_data_to_json(configuration_data)
    else:
        print("Exiting program due to error reading configuration file.")


def start_server():
    # Starts an HTTP server to handle GET requests.
    server_address = ('', 8000)  # Port 8000
    httpd = HTTPServer(server_address, ConfigurationHandler)
    print('Starting server...')
    httpd.serve_forever()


if __name__ == "__main__":
    main()
    start_server()
