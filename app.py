from flask import Flask, request, redirect
import os

app = Flask(__name__)
posts = []

@app.route('/')
def home():
    html_posts = ""
    for p in reversed(posts):
        html_posts += f"<div style='background:white;padding:15px;border-radius:12px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.1)'>👤 {p}</div>"
    return f"""
    <html><head><meta name='viewport' content='width=device-width, initial-scale=1'>
    <style>body{{font-family:sans-serif;background:#f0f2f5;margin:0;padding:10px}}.header{{background:#1877f2;color:white;padding:16px;text-align:center;font-size:22px;font-weight:bold}}.box{{background:white;padding:15px;border-radius:12px;margin:10px 0}}input,textarea{{width:94%;padding:12px;margin:6px;border:1px solid #ddd;border-radius:10px;font-size:16px}}button{{background:#1877f2;color:white;border:none;padding:14px;border-radius:10px;font-weight:bold;width:100%;font-size:16px}}</style></head>
    <body><div class='header'>BrayanBook 🚀</div><div class='box'><h3>Quoi de neuf ?</h3><form action='/post' method='post'><input name='nom' placeholder='Ton prenom' value='Brayan' required><textarea name='msg' placeholder='Ecris ton post...' required></textarea><button>Publier</button></form></div><h3 style='padding-left:10px'>Fil d'actu :</h3>{html_posts if html_posts else "<p style='text-align:center;color:gray'>Vide pour l'instant</p>"}</body></html>
    """

@app.route('/post', methods=['POST'])
def post():
    nom = request.form.get('nom')
    msg = request.form.get('msg')
    posts.append(f"{nom}: {msg}")
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
