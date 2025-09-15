from flask import Flask, request, send_file, render_template
import qrcode
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")  # Serve your UI

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.form.get("data")
    fill_color = request.form.get("fill_color", "black")
    back_color = request.form.get("back_color", "white")

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        box_size=15,
        border=3
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Save QR to memory instead of file
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
