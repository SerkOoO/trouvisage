# 🙂 TrouveVisage

TrouveVisage est un mini projet qui permet de détécter des visages dans des images.

## 🛠️ Technologies utilisées
- Python
- FastAPI
- OpenCV

## 🛠️ Installer le projet


```bash
git clone https://github.com/SerkOoO/trouvisage.git
cd trouvisage
pip install -r requirements.txt
fastapi dev main.py
```

(si il y a un problème faites)
```bash
pip install fastapi[standard]
fastapi dev main.py
```

Avec Docker 🐳
```bash
docker build -t trouvevisage .
docker run -p 5000:5000 trouvevisage
```

@SerkOoO
