from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisismysecretkeydonotstealit'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1/ogrencidb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from models import Ogrenci, OgretimUyesi, Ders, Bolum, OgrenciBasari, OgrenciDers

@app.route("/")
def GirisForm():
    return render_template("giris.html")

@app.route('/giris', methods=['GET', 'POST'])
def Giris():
    error = None
    if request.method == 'POST':
        if request.form['mail'] != 'kullanici@gmail.com' or request.form['sifre'] != 'kullanici':
            error = 'LÜTFEN TEKRAR DENEYİN.'
        else:
            return redirect(url_for('MENU'))
    return render_template('giris.html', error=error)


@app.route("/anasayfa")
def MENU():
    return render_template("menu.html")


@app.route('/ogrenci')
def OgrenciList():
    veri = Ogrenci.query.all()
    return render_template('ogrenciList.html', veri=veri)


@app.route('/ogretmen')
def OgretmenList():
    veri = OgretimUyesi.query.all()
    return render_template('ogretimuyesi.html', veri=veri)


@app.route('/ders')
def DersList():
    veri = Ders.query.all()
    return render_template('dersList.html', veri=veri)


@app.route('/bolum')
def BolumList():
    veri = Bolum.query.all()
    return render_template('bolumList.html', veri=veri)

@app.route('/ogrenci_basari')
def OgrenciBasariList():
    veri = OgrenciBasari.query.all()
    return render_template('ogrenciBasariList.html', veri=veri)

@app.route('/ogrenci_ders')
def OgrenciDersList():
    veri = OgrenciDers.query.all()
    return render_template('ogrenciDersList.html', veri=veri)

@app.route("/form")
def Form():
    return render_template("form.html")


@app.route('/verial', methods=['GET', 'POST'])
def verial():
    if request.method == 'POST':
        student = Ogrenci(request.form['ad'], request.form['soyad'],
                      request.form['adres'], request.form['dogum_tarihi'], request.form['bolum_id'])
        db.session.add(student)
        db.session.commit()
        veri = Ogrenci.query.all()
        return render_template("ogrenciList.html", veri=veri)


@app.route("/guncelleform")
def GuncelleForm():
    return render_template("guncelle.html")


@app.route('/guncelle', methods=['GET', 'POST'])
def Guncelle():
    if request.method == 'POST':
         guncelveri= Ogrenci.query.get(request.form.get('ogrenci_no'))
         guncelveri.ad = request.form['ad']
         guncelveri.soyad = request.form['soyad']
         guncelveri.adres = request.form['adres']
         guncelveri.dogum_tarihi = request.form['dogum_tarihi']
         guncelveri.bolum_id = request.form['bolum_id']
         db.session.commit()
         return redirect(url_for('OgrenciList'))


@app.route('/sil/<ogrenci_no>', methods=['GET', 'POST'])
def Sil(ogrenci_no):
    silinecekveri = Ogrenci.query.get(ogrenci_no)
    db.session.delete(silinecekveri)
    db.session.commit()
    return redirect(url_for('OgrenciList'))

@app.route('/ders_sil/<ders_id>', methods=['GET', 'POST'])
def DersSil(ders_id):
    silinecekveri = Ders.query.get(ders_id)
    db.session.delete(silinecekveri)
    db.session.commit()
    return redirect(url_for('DersList'))


@app.route('/not_sil/<id>', methods=['GET', 'POST'])
def NotSil(id):
    silineceknot =OgrenciBasari.query.get(id)
    db.session.delete(silineceknot)
    db.session.commit()
    return redirect(url_for('OgrenciBasariList'))


@app.route("/dersguncelleform")
def DersGuncelleForm():
    return render_template("dersguncelle.html")

@app.route('/dersguncelle', methods=['GET', 'POST'])
def DersGuncelle():
    if request.method == 'POST':
         dersguncelveri= Ders.query.get(request.form.get('ders_id'))
         dersguncelveri.ders_adi = request.form['ders_adi']
         dersguncelveri.ogretmen_id = request.form['ogretmen_id']
         dersguncelveri.bolum_id = request.form['bolum_id']
         db.session.commit()
         return redirect(url_for('DersList'))

@app.route("/notguncelleform")
def NotGuncelleForm():
    return render_template("notguncelleform.html")

@app.route('/notguncelle', methods=['GET', 'POST'])
def NotGuncelle():
    if request.method == 'POST':
         notguncelveri= OgrenciBasari.query.get(request.form.get('id'))
         notguncelveri.ders_id = request.form['ders_id']
         notguncelveri.ogrenci_no = request.form['ogrenci_no']
         notguncelveri.vize = request.form['vize']
         notguncelveri.final = request.form['final']
         notguncelveri.butunleme = request.form['butunleme']
         db.session.commit()
         return redirect(url_for('OgrenciBasariList'))


@app.route("/ogrenci_isleri")
def Ogrenci_İsleri():
    return render_template("ogrenci_isleri.html")

@app.route("/akademik_islemler")
def Akademikİslemler():
    return render_template("akademik_islemler.html")

@app.route("/dersform")
def DersForm():
    return render_template("dersekleform.html")

@app.route('/dersekle', methods=['GET', 'POST'])
def DersEkle():
    if request.method == 'POST':
        ders = Ders(request.form['ders_adi'], request.form['ogretmen_id'],
                      request.form['bolum_id'])
        db.session.add(ders)
        db.session.commit()
        veri = Ders.query.all()
        return render_template("dersList.html", veri=veri)

@app.route("/notform")
def NotForm():
    return render_template("notform.html")

@app.route('/notekle', methods=['GET', 'POST'])
def NotEkle():
    if request.method == 'POST':
        puan= OgrenciBasari(request.form['ders_id'], request.form['ogrenci_no'],
                      request.form['vize'],request.form['final'],request.form['butunleme'])
        db.session.add(puan)
        db.session.commit()
        veri = OgrenciBasari.query.all()
        return render_template("ogrenciBasariList.html", veri=veri)


@app.route("/akademiktakvim")
def AkademikTakvim():
    return render_template("akademiktakvim.html")


if __name__ == '__main__':
    app.run(debug=True)


