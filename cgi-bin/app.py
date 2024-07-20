from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('template.html')

@app.route('/command/<command>', methods=['POST'])
def command(command):
    if command == 'low':
        # Code to set fan to low
        print("Fan set to low")
    elif command == 'medium':
        # Code to set fan to medium
        print("Fan set to medium")
    elif command == 'high':
        # Code to set fan to high
        print("Fan set to high")
    elif command == 'stop':
        # Code to stop the fan
        print("Fan stopped")
    else:
        return "Invalid command", 400

    return f"Command {command} executed", 200

if __name__ == '__main__':
    app.run(debug=True)
