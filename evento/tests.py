from django.test import TestCase
from .models  import Evento
from users.models import Usuario
from django.contrib.auth.models import User
from datetime import datetime, date
import unittest
from evento.funcoes import distancia

class TesteEvento(TestCase):
    def testa_evento(self):
        User.objects.create_user(
                username="lucas",
                first_name="Lucao",
                last_name="lulu",
                password="123"
                )
        usuario = Usuario.objects.filter(user__username="lucas")[0]
        usuario.save()

        evento = Evento.objects.create(

                nome = "dia da pizza",
                id_doador = usuario,
                data_inicio = datetime.now(),
                data_final = datetime.now(),
                local = "samambaia",
                desc = "lalala"
        )

        self.assertEqual(str(evento), "dia da pizza {}".format(usuario.id))


    def teste_calcula_distancia(self):
        print("\nCalcula distancia")
        valor =  distancia(5,2,2,5)
        esperado = 3.0
        self.assertEqual(esperado,valor)



'''
class EventoTest(unittest.TestCase):
    def setUp(self):
        # o id do doador nao ta funcionando corretamente, o restante esta
        doador = Usuario.objects.create(user="Fulano", cnpj="12345678901234")
        id_doador = doador.id

        self.evento = Evento.objects.create(
            nome="Teste",
            id_doador= id_doador,
            data_inicio=datetime.now(),
            data_final=datetime.now(),
            desc="Apenas um teste"
            )

    def test_criacao_evento(self):
        print("Testando criacao de evento")
        self.assertEqual(self.evento.getID(), "Teste")
        print("Criacao de evento testado")


class TestEvento(TestCase):
    def testa_str_do_objeto(self):
        id_doador = Usuario.objects.create(
            username="doador",
            first_name="Nome",
            last_name="Sobrenome",
            password="123",
        )
        self.assertEqual(str(doador), "doador Nome Sobrenome")

        return doador


    cria_evento = Evento.models.create(
        nome="Teste",
        id_doador_id = 1,
        data_inicio="2019-09-09",
        data_final="2019-09-10",
        desc="Apenas um teste"

    )

'''
