import http.server, socketserver
 

class Server(http.server.BaseHTTPRequestHandler):
    pwd =  '/' + '/'.join(tuple(i for i in __file__.split('/') if i != '')[:-1]) + '/' 
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', len(open(self.pwd + 'skrip/chat.html','rb').read()))
            self.end_headers()
            self.wfile.write(open(self.pwd + 'skrip/chat.html','rb').read())

        elif self.path == '/chat.js':
              self.send_response(200)
              self.send_header('Content-Type', 'javascript/js; charset=utf-8')
              self.send_header('Content-Length',len(open(self.pwd + 'skrip/chat.js','rb').read()))
              self.end_headers()
              self.wfile.write(open(self.pwd + 'skrip/chat.js','rb').read())
        
        elif self.path == '/chat.css':
              self.send_response(200)
              self.send_header('Content-Type', 'text/css; charset=utf-8')
              self.send_header('Content-Length',len(open(self.pwd + 'skrip/chat.css','rb').read()))
              self.end_headers()
              self.wfile.write(open(self.pwd + 'skrip/chat.css','rb').read())

        else:
              self.send_response(302)
              self.send_header('Location', '/')
              self.end_headers()



class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    pass


if __name__ == '__main__':
    ThreadingHTTPServer(('', 17957), Server).serve_forever()
