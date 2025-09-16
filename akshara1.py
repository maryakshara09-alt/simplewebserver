from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>
            akshara's page
        </title>
    </head>
    <body>
        <h1><b>
            Device Specification(AKSHARA)
         </b>
     </h1>
     <table border="5" bgcolor="pink" cellspacing="50" cellpadding="10git clone">
     <tr>
        <th>S.NO</th>
        <th>DEVICE NAME</th>
        <th>DEVICE ID</th>
        <th>PRODUCT ID</th>
        <th>SYSTEM TYPE</th>
     </tr>
     <tr>
        <td>1</td>
        <td>TMP215-75-G2</td>
        <td>2AF0CDD3-C3F2-4002-8B7E-901D1BOC91B0</td>
        <td>00342-42784-66113-AAOEM</td>
        <td>64-bit operating system,x64-based processor</td>
     </tr>
     </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()