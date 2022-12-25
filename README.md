<h1 align="center">Huobi primebox</h1>

<p align="center">Collect cards in Huobi primebox</p>
<p align="center">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
</p>

## ⚡ Installation
+ Install [python](https://www.google.com/search?client=opera&q=how+install+python)
+ [Download](https://sites.northwestern.edu/researchcomputing/resources/downloading-from-github) and unzip repository
+ Install requirements:
```python
pip install -r requirements.txt
```

## 💻 Preparing
+ Login to Huobi account via browser
+ Open inspect (Ctrl+Shift+C), select "Network" and reload the page (Ctrl+R)
+ Looking for "info" or something like that and open

![image](https://user-images.githubusercontent.com/119711235/209450119-67ff25bb-5d25-4969-9250-afc00063c083.png)

+ Scroll down and copy ```hb-pro-token```

![image](https://user-images.githubusercontent.com/119711235/209450238-e17fe24e-d426-4374-8e06-2d306daf2b95.png)

+ Run the bot:
```python
python huobi_primebox.py
```

## ✔️ Usage
+ ```Claim(1) or Play(2)``` - if you select ```1```, bot collects all available points. If you select ```2```, bot collects 2 cards from the game ```red packet rain```
+ ```Date(y-m-d)``` - you must enter the current date
  + Example: ```2022-12-31```
+ ```Round number``` - current round number in primebox
+ ```Token``` - enter the ```hb-pro-token``` you copied earlier

## 📧 Contacts
+ Telegram - [@flamingoat](https://t.me/flamingoat)
