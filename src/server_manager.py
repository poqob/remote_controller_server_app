from server import UDPServer
import configparser


class ServerManager:
    # constructor
    def __init__(self, config_file_path) -> None:
        # Create a configparser object
        self.config = configparser.ConfigParser()
        # Read the configuration file
        self.config.read(config_file_path)
        # Define the server parameters
        self.server_address = self.config.get("Server", "address")
        self.server_port = self.config.getint("Server", "port")
        self.buffer_size = self.config.getint("Server", "buffer_size")
        # Create an instance of the UDPServer
        self.server = UDPServer(self.server_address, self.server_port, self.buffer_size)

    def start(self) -> None:
        self.server.start_server()

    def stop(self) -> None:
        self.server.kill_server()
