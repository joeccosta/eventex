# Eventex

Sistema de Eventos encomendado pela Morena

[![Build Status](https://travis-ci.org/joeccosta/eventex.svg?branch=master)](https://travis-ci.org/joeccosta/eventex)

[![Maintainability](https://api.codeclimate.com/v1/badges/6718a626f4a8b5ed5101/maintainability)](https://codeclimate.com/github/joeccosta/eventex/maintainability)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:joeccosta/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRETY_KEY segura para a instância.
4. Defina DEBUG=False.
5. Configure o serviço de E-mail.
6. Envie o código para o heroku.

``` console
heroku create minhainstancia
heroku config:push
heroku config:set SECRETY_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#configuro o e-mail
git push heroku master --force
```