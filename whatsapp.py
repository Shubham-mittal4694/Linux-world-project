from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the main index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the WhatsApp scheduling page
@app.route('/schedule-whatsapp', methods=['GET', 'POST'])
def whatsapp():
    if request.method == 'POST':
        # Process the form submission
        phone_number = request.form['phone_number']
        message = request.form['message']
        hour = request.form['hour']
        minute = request.form['minute']

        # Here you would add your logic to schedule the WhatsApp message
        # For demonstration purposes, let's print the details
        print(f"Scheduling WhatsApp message to {phone_number} at {hour}:{minute} - {message}")

        # Redirect to the index page after scheduling
        return redirect(url_for('index'))

    # If it's a GET request, render the WhatsApp scheduling form
    return render_template('whatsapp.html')

if __name__ == '__main__':
    app.run(debug=True)
