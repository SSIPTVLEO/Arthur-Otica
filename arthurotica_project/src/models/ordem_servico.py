from src.models.user import db

class OrdemServico(db.Model):
    __tablename__ = 'ordem_servico'
    
    id = db.Column(db.Integer, primary_key=True)
    numero_os = db.Column(db.String(50), nullable=False, unique=True)
    data_pedido = db.Column(db.Date, nullable=False)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    
    def to_dict(self):
        return {
            'ID_NUMERO_OS': f'{self.id} - {self.numero_os}',
            'data_pedido': self.data_pedido.strftime('%Y-%m-%d') if self.data_pedido else None,
            'ID_Cliente': self.id_cliente
        }

