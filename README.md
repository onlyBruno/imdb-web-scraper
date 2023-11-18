# IMDb Web Scraper

Este script Python coleta dados do site da IMDb para coletar informações sobre filmes populares. Ele extrai detalhes como título, data de lançamento, posição, classificação e resumo de cada filme no gráfico "Movie Meter".

## Table of Contents / Índice

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

O IMDb Web Scraper é um script Python que usa técnicas de web scraping para recuperar detalhes do filme do site da IMDb. Ele aproveita a biblioteca BeautifulSoup para análise de HTML e faz solicitações assíncronas para coletar com eficiência informações de várias páginas de filmes simultaneamente.

## Features

- Extrai informações sobre filmes populares da IMDb.
- Extrai detalhes como título, data de lançamento, posição, classificação e resumo.
- Utiliza programação simultânea com threading para melhorar o desempenho.

## Requirements

- Python 3.x
- Requests library
- BeautifulSoup library

## Installation

1. Clonar o repositório:

```bash
git clone https://github.com/onlyBruno/imdb-web-scraper.git
cd imdb-web-scraper
```
2. Crie e ative um ambiente virtual:

#### No Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```
#### No macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Instale dependências:

```bash
pip install -r requirements.txt
```

## Usage

Execute o script para coletar informações sobre filmes populares na IMDb:
```bash
python scraper.py
```
O script criará um arquivo CSV no diretório de saída (output/) com os detalhes do filmes extraídos.

## Contributing

Contribuições são bem-vindas! Se você quiser contribuir com o projeto, siga as orientações do arquivo CONTRIBUTING.md.

## License

This project is licensed under the MIT License.