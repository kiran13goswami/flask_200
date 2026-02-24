from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary Database (List)
accounts = []

# ================= HOME =================
@app.route("/")
def home():
    return render_template("home.html")


# ================= CREATE (Register) =================
@app.route("/register-now", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        account = {
            "id": len(accounts) + 1,
            "ac_no": request.form.get("account_number"),
            "name": request.form.get("name"),
            "mobile": request.form.get("mobile"),
            "address": request.form.get("address")
        }

        accounts.append(account)
        return redirect(url_for("all_accounts"))

    return render_template("register.html")


# ================= READ (Show All Accounts) =================
@app.route("/all-accounts")
def all_accounts():
    return render_template("all_account.html", accounts=accounts)


# ================= DELETE =================
@app.route("/delete/<int:id>")
def delete(id):
    global accounts
    accounts = [acc for acc in accounts if acc["id"] != id]
    return redirect(url_for("all_accounts"))


# ================= UPDATE =================
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    account = next((acc for acc in accounts if acc["id"] == id), None)

    if request.method == "POST":
        account["ac_no"] = request.form.get("account_number")
        account["name"] = request.form.get("name")
        account["mobile"] = request.form.get("mobile")
        account["address"] = request.form.get("address")

        return redirect(url_for("all_accounts"))

    return render_template("register.html", account=account)


# ================= RUN SERVER =================
if __name__ == "__main__":
    app.run(debug=True)


    