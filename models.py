from main import db,relationship

class Ogrenci(db.Model):
    __tablename__ = 'ogrenci'
    ogrenci_no = db.Column(db.Integer, primary_key=True, )
    ad = db.Column(db.String(80), nullable=False)
    soyad = db.Column(db.String(80),nullable=False)
    adres = db.Column(db.String(80), nullable=False)
    dogum_tarihi =db.Column(db.String(80))
    bolum_id =db.Column(db.Integer,db.ForeignKey('bolum.bolum_id', name = 'bolum_adi'))
    bolumAdi = db.relationship('Bolum', backref='ogrenci', foreign_keys= bolum_id)
    def __init__(self, ad, soyad, adres, dogum_tarihi,bolum_id):
        self.ad = ad
        self.soyad = soyad
        self.adres = adres
        self.dogum_tarihi = dogum_tarihi
        self.bolum_id = bolum_id

class Bolum(db.Model):
    __tablename__ = 'bolum'
    bolum_id = db.Column(db.Integer, primary_key=True )
    bolum_adi = db.Column(db.String(80), nullable=False)


class OgretimUyesi(db.Model):
    __tablename__ = 'ogretim_uyesi'
    ogretmen_id = db.Column(db.Integer, primary_key=True, )
    ad = db.Column(db.String(80), nullable=False)
    soyad = db.Column(db.String(80),nullable=False )
    unvan = db.Column(db.String(80), nullable=False)
    bolum_id = db.Column(db.Integer, db.ForeignKey('bolum.bolum_id',name='bolum_adi'))
    bolumAdi = db.relationship('Bolum', backref='ogretim_uyesi', foreign_keys=bolum_id)

    def __init__(self, ad, soyad, unvan, bolum_id):
        self.ad = ad
        self.soyad = soyad
        self.unvan = soyad
        self.bolum_id = bolum_id

class Ders(db.Model):
    __tablename__ = 'ders'
    ders_id = db.Column(db.Integer, primary_key=True, )
    ders_adi = db.Column(db.String(80), nullable=False)
    ogretmen_id = db.Column(db.Integer,db.ForeignKey('ogretim_uyesi.ogretmen_id', name='ad'))
    ogretmenAdi = db.relationship('OgretimUyesi', backref='ders', foreign_keys=ogretmen_id)
    bolum_id = db.Column(db.Integer,db.ForeignKey('bolum.bolum_id', name='bolum_adi'))
    bolumAdi = db.relationship('Bolum', backref='ders', foreign_keys=bolum_id)

    def __init__(self, ders_adi,ogretmen_id, bolum_id):
        self.ders_adi = ders_adi
        self.ogretmen_id = ogretmen_id
        self.bolum_id = bolum_id

class OgrenciBasari(db.Model):
    __tablename__ = 'ogrenci_basari'
    id = db.Column(db.Integer, primary_key=True,)
    ders_id = db.Column(db.Integer,db.ForeignKey('ders.ders_id',name='ders_adi'))
    dersAdi = db.relationship('Ders', backref='ogrenci_basari', foreign_keys=ders_id)
    ogrenci_no = db.Column(db.Integer, db.ForeignKey('ogrenci.ogrenci_no', name='ad'))
    ogrenciAdi = db.relationship('Ogrenci', backref='ogrenci_basari', foreign_keys=ogrenci_no)
    vize = db.Column(db.Integer, nullable=False)
    final = db.Column(db.Integer, nullable=False)
    butunleme = db.Column(db.Integer, nullable=False)

    def __init__(self, ders_id, ogrenci_no, vize, final, butunleme):
        self.ders_id = ders_id
        self.ogrenci_no = ogrenci_no
        self.vize = vize
        self.final = final
        self.butunleme = butunleme


class OgrenciDers(db.Model):
    __tablename__ = 'ogrenci_ders'
    id = db.Column(db.Integer, primary_key=True,)
    ders_id = db.Column(db.Integer,db.ForeignKey('ders.ders_id',name='ders_adi'))
    dersAdi = db.relationship('Ders', backref='ogrenci_ders', foreign_keys=ders_id)
    ogrenci_no = db.Column(db.Integer, db.ForeignKey('ogrenci.ogrenci_no', name='ad'))
    ogrenciAdi = db.relationship('Ogrenci', backref='ogrenci_ders', foreign_keys=ogrenci_no)
    donemi = db.Column(db.Integer, nullable=False)


    def __init__(self, ders_id, ogrenci_no, donemi):
        self.ders_id = ders_id
        self.ogrenci_no = ogrenci_no
        self.donemi = donemi

#sanırım bitti. Çalıştır bakalım olmamış yine olmamış





