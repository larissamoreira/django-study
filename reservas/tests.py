from django.test import TestCase # quando ta usando bd
from django.test import SimpleTestCase
from .models import Cliente
from django.utils import timezone  
# Create your tests here.

def test_index_page_status(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)

class ClienteModelTest(TestCase):
    
    def setUp(self):
        Cliente.objects.create(
            nome = 'teste',
            endereco = 'teste 1234 casa',
            telefone = '1111111',
            email = 'teste@gmail.com',
            registrado_em = timezone.now()
        )

    def test_client(self):
        cliente = Cliente.objects.get(id=1)
        self.assertEqual(f'{cliente.nome}', 'teste')

