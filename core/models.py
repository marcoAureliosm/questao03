from django.db import models
# Create your models here.
class despesas(models.Model):
    data = models.DateField()
    despesas = (
        ('Remedio', 'Remedio'),
        ('Roupas', 'Roupas'),
        ('Alimentação', 'Alimentação'),
        ('Educação', 'Educação'),
        ('Transporte', 'Transporte'),
        ('Outros', 'Outros'),
    )
    formas_pagamento = models.CharField(
        max_length=14,
        choices=despesas,
        default='Outros',
    )

    def is_upperclass(self):
        return self.dispesas in (self.Remedio, self.Roupas, self.Alimentação,self.Educacao,self.Trasporte)


    formas_pagamento = (
        ('Boleto', 'Boleto'),
        ('Credito', 'Credito'),
        ('Debito', 'Debito'),
    )
    formas_pagamento = models.CharField(
        max_length=14,
        choices=formas_pagamento,
        default='Boleto',
    )

    def is_upperclass(self):
        return self.formas_pagamento in (self.Boleto, self.Credito, self.Debito)
    vencimento = models.DateField()
    quitado = models.BooleanField()




