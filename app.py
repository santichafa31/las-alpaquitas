from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        hotdog_price = max(float(request.form.get("hotdog_price", 0) or 0), 0)
        hotdog_qty = max(int(request.form.get("hotdog_qty", 0) or 0), 0)
        shake_price = max(float(request.form.get("shake_price", 0) or 0), 0)
        shake_qty = max(int(request.form.get("shake_qty", 0) or 0), 0)

        hotdog_discount = request.form.get("hotdog_discount") == "on"
        shake_discount = request.form.get("shake_discount") == "on"

        hotdog_subtotal = hotdog_price * hotdog_qty
        shake_subtotal = shake_price * shake_qty

        hotdog_discount_amount = hotdog_subtotal * 0.10 if hotdog_discount else 0
        shake_discount_amount = shake_subtotal * 0.10 if shake_discount else 0

        subtotal = hotdog_subtotal + shake_subtotal
        discount = hotdog_discount_amount + shake_discount_amount
        total = subtotal - discount

        result = {
            "hotdog_subtotal": hotdog_subtotal,
            "shake_subtotal": shake_subtotal,
            "subtotal": subtotal,
            "discount": discount,
            "total": total,
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
