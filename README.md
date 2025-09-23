# EX01 Developing a Simple Webserver
## Date:08.09.2025

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
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
```

## OUTPUT:
![alt text](<Screenshot (15).png>)
![alt text](<Screenshot (14).png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
