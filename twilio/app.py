from flask import Flask

@app.route('/')
def hello():
    return "Hello Flask"

if __name__ == '__main__':
    app.run(debug=True)


