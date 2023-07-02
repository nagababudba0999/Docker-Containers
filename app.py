from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return ''' <html> 
               <head>
                  <style>
                    body {
                       background-color: pink;
                    }
                  </style>
               </head>
                 <body>
                   <h1> Congratulations!!!!!! </h1> 
                   <h2> Hello , You have flask app launched your container </h2>
                 </body>
               </html>
    '''

if __name__ == '__main__':
    app.run()


