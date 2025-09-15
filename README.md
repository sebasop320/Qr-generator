# Qr-generator
A simple QR code generator

# Usage


1. Clone git repo ```git clone https://github.com/sebasop320/Qr-generator``` and ```cd Qr-generator```
2. Ensure python 3.8+
3. Create virtual env ( highly recomended! ) 
```
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```
5. Ensure you have ```pip install flask "qrcode[pil]"``` installed
6. Install the requerements
7. Run with ``` python app.py ```
8. Go to you browser and open ```http://127.0.0.1:5000```

# File structure:
```
qr-generator/
│
├── app.py                # Flask backend
├── templates/
   └── index.html         # Frontend UI
```
# To do:
- Add icons

- Ui improvement

- Custom filename option

- Support more formats (svg, jpg)

# Contributing 
Create PR request with your improvment and wait for merger!

  
