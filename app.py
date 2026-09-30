from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Pencheff DAST Lab</title>
        </head>
        <body>
            <h1>Pencheff DAST Security Lab</h1>

            <p>This application is created for authorized security testing.</p>

            <h2>Lab Endpoints</h2>

            <ul>
                <li><a href="/search?q=hello">Search</a></li>
                <li><a href="/api/users">Users API</a></li>
                <li><a href="/login">Login</a></li>
            </ul>
        </body>
    </html>
    """


@app.route("/search")
def search():
    query = request.args.get("q", "")

    return f"""
    <h1>Search Results</h1>
    <p>You searched for: {query}</p>
    <a href="/">Back</a>
    """


@app.route("/api/users")
def users():
    return {
        "users": [
            {"id": 1, "name": "Karthik"},
            {"id": 2, "name": "DevOps User"}
        ]
    }


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        return f"""
        <h1>Login Result</h1>
        <p>Username: {username}</p>
        <p>Login attempted.</p>
        <a href="/login">Back</a>
        """

    return """
    <h1>Login</h1>

    <form method="POST">

        <label>Username:</label>
        <input type="text" name="username">

        <br><br>

        <label>Password:</label>
        <input type="password" name="password">

        <br><br>

        <button type="submit">Login</button>

    </form>

    <br>
    <a href="/">Back</a>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
