from livereload import Server

server = Server()
server.watch('example_max.html')
server.watch('example_min.html')
server.serve(port='8000')
