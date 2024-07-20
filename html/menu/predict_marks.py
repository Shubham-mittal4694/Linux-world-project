#!/usr/bin/env python3
import cgi
import cgitb
from sklearn.linear_model import LinearRegression
import numpy as np
cgitb.enable()

print("Content-Type: text/html\n")
print("""
<html>
<body>
    <h2>Linear Regression Predict Marks</h2>
    <form method="post" action="/cgi-bin/lr_marks.py">
        <input type="text" name="hours" placeholder="Enter hours studied">
        <input type="submit" value="Predict">
    </form>
</body>
</html>
""")

form = cgi.FieldStorage()
hours = form.getvalue('hours')

if hours:
    hours = np.array(float(hours)).reshape(-1, 1)
    model = LinearRegression()
    X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
    y = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
    model.fit(X, y)
    prediction = model.predict(hours)
    print(f"<p>Predicted marks for {hours[0][0]} hours: {prediction[0]}</p>")