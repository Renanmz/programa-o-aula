from config import *
from datetime import date

class Pessoa(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))

    def __str__(self):
        return self.nome + "[id="+str(self.id)+ "], " +\
            self.email + ", " + self.telefone

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone
        }

class Exame(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254)) 
    vr = db.Column(db.String(254))

    def __str__(self):
        return f"{self.nome} [{self.id}], ({self.vr})"

    def json(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "vr":self.vr
        }  


class ExameRealizado(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date) 
    resultado = db.Column(db.String(254)) 
    
    pessoa_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False)
    pessoa = db.relationship("Pessoa")
    exame_id =  db.Column(db.Integer, db.ForeignKey(Exame.id), nullable=False)
    exame = db.relationship("Exame")


    def __str__(self): # expressão da classe em forma de texto
        return f"{self.data}, {self.resultado}, " + \
            f"{self.pessoa}, {self.exame}"


    def json(self):
        return {
            "id":self.id,
            "data":self.data,
            "resultado":self.resultado,
            "pessoa_id":self.pessoa_id,
            "pessoa":self.pessoa.json(),
            "exame_id":self.exame_id,
            "exame":self.exame.json()
        }


class Respirador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(254)) 
    data_aquisicao = db.Column(db.Date)
    data_emprestimo = db.Column(db.Date)

    pessoa_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id))
    pessoa = db.relationship("Pessoa")

    def __str__(self): 
        s = f"Respirador {self.codigo} adquirido em {self.data_aquisicao}"
        if self.pessoa != None:
            s += f", emprestado para {self.pessoa} desde {self.data_aquisicao}"
        return s

    def json(self):
        if self.pessoa is None: 
            pessoa_id = ""
            pessoa = ""
            data_emprestimo = ""
        else: 
            pessoa_id = self.pessoa_id
            pessoa = self.pessoa.json()
            data_emprestimo = self.data_emprestimo 

        return {
            "id": self.id,
            "codigo": self.codigo,
            "data_aquisicao": self.data_aquisicao,
            "pessoa_id": pessoa_id,
            "pessoa": pessoa,
            "data_emprestimo": data_emprestimo
        }

if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    db.create_all() 

    p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", 
        telefone = "47 99012 3232")
    db.session.add(p1)
    db.session.commit()
    print(p1)
    
    # criar exame
    b12 = Exame(nome="B12", vr="239 a 931")
    colesterol = Exame(nome="Colesterol total", vr="menor que 150")
    db.session.add(b12)
    db.session.add(colesterol)
    db.session.commit()
    print(b12)

    # criar resultado de exame
    e1 = ExameRealizado(data=date(2020, 2, 2), exame=b12, 
        resultado="219,0 pg/mL", pessoa=p1)
    db.session.add(e1)
    db.session.commit()
    print(f"Exame realizado: {e1}")
    print(f"Exame realizado em json: {e1.json()}")