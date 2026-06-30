import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestPaginasPublicas:
    """Testa se todas as rotas GET retornam status 200."""

    @pytest.mark.parametrize("rota", [
        "/",
        "/instrucoes",
        "/fase/1",
        "/fase/x7k2m9q3p5r8t4v6wz",
        "/fase/p3n8w",
        "/fase/sombra",
        "/fase/nexus",
        "/fim",
        "/boas-vindas",
        "/fazer-parte",
        "/confidencial",
    ])
    def test_rota_retorna_200(self, client, rota):
        response = client.get(rota)
        assert response.status_code == 200


class TestConteudoPaginas:
    """Testa se o conteúdo esperado está presente nas páginas."""

    def test_home_tem_titulo(self, client):
        response = client.get("/")
        assert b"3301" in response.data

    def test_fase1_tem_binario(self, client):
        response = client.get("/fase/1")
        assert b"01" in response.data

    def test_fase5_tem_link_oculto(self, client):
        response = client.get("/fase/nexus")
        html = response.data.decode()
        assert '<p hidden>' in html
        assert 'pedroaruana.pythonanywhere.com/fim' in html

    def test_fim_tem_parabens(self, client):
        response = client.get("/fim")
        html = response.data.decode()
        assert "rab" in html and "ns." in html

    def test_boas_vindas_tem_imagens(self, client):
        response = client.get("/boas-vindas")
        html = response.data.decode()
        assert "sidney.png" in html
        assert "florida.png" in html
        assert "paris.png" in html
        assert "poland.png" in html

    def test_fazer_parte_tem_formulario(self, client):
        response = client.get("/fazer-parte")
        html = response.data.decode()
        assert '<form' in html
        assert 'name="nome"' in html
        assert 'name="pais"' in html
        assert 'name="estado"' in html
        assert 'name="cidade"' in html

    def test_confidencial_tem_ip(self, client):
        response = client.get("/confidencial")
        assert b"127.0.0.1" in response.data


class TestCertificado:
    """Testa a geração do certificado via POST."""

    def test_post_certificado_retorna_200(self, client):
        response = client.post("/certificado", data={
            "nome": "Alan Turing",
            "pais": "Inglaterra",
            "estado": "Londres",
            "cidade": "Maida Vale",
        })
        assert response.status_code == 200

    def test_certificado_exibe_nome(self, client):
        response = client.post("/certificado", data={
            "nome": "Alan Turing",
            "pais": "Inglaterra",
            "estado": "Londres",
            "cidade": "Maida Vale",
        })
        assert b"Alan Turing" in response.data

    def test_certificado_exibe_localizacao(self, client):
        response = client.post("/certificado", data={
            "nome": "Ada Lovelace",
            "pais": "Brasil",
            "estado": "Bahia",
            "cidade": "Salvador",
        })
        html = response.data.decode()
        assert "Salvador" in html
        assert "Bahia" in html
        assert "Brasil" in html

    def test_certificado_get_nao_permitido(self, client):
        response = client.get("/certificado")
        assert response.status_code == 405


class TestRotasInvalidas:
    """Testa que rotas inexistentes retornam 404."""

    def test_rota_inexistente(self, client):
        response = client.get("/pagina-que-nao-existe")
        assert response.status_code == 404

    def test_fase_inexistente(self, client):
        response = client.get("/fase/999")
        assert response.status_code == 404
