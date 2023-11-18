import requests
import time
import csv
import random
import concurrent.futures
import os
import threading
from bs4 import BeautifulSoup

# Header padrão usado na request
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

MAX_THREADS = 10

# Bloqueio global para escrita no CSV
csv_lock = threading.Lock()

# Função para garantir nome único
def get_unique_filename(base_filename, directory):
    # Retornando um caminho de arquivo único no diretório especificado
    return os.path.join(directory, f"{base_filename}.csv")

def write_to_csv(output_file, data):
    # Escrevendo dados no arquivo CSV de forma segura usando um bloqueio
    with csv_lock:
        with open(output_file, mode='a', newline='', encoding='utf-8') as file:
            movie_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            movie_writer.writerow(data)

def extract_movie_details(movie_link, output_file):
    # Aguardando um tempo aleatório para simular comportamento humano e evitar bloqueios
    time.sleep(random.uniform(0, 0.2))
    response = requests.get(movie_link, headers=headers)
    movie_soup = BeautifulSoup(response.content, 'html.parser')
    title, date, position, rating, summary = '', '', '', '', ''

    movie_data = movie_soup.find('div', attrs={'class': 'sc-e226b0e3-3 dwkouE'})
    if movie_data:
        # Extraindo informações do filme
        title = movie_data.find('h1').find('span', attrs={'class': 'sc-7f1a92f5-1 benbRT'}).get_text()
        date = movie_data.find('a', attrs={'class': 'ipc-link ipc-link--baseAlt ipc-link--inherit-color'}).get_text().strip()
        position = movie_data.find('div', attrs={'class': 'sc-5f7fb5b4-1 fTREEx'}).get_text()
        rating = movie_data.find('span', attrs={'class': 'sc-bde20123-1 cMEQkK'}).get_text()
        summary = movie_soup.find('span', attrs={'class': 'sc-466bb6c-1 dWufeH'}).get_text().strip()

    # Verificando se todos os dados necessários estão disponíveis antes de gravar em CSV
    if all([position, title, date, rating, summary]):
        write_to_csv(output_file, [position, title, date, rating, summary])

def extract_movies(soup, output_directory):
    # Encontrando todos os elementos de filme na página
    movie_list = soup.findAll('div', class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-479faa3c-9 dkLVoC cli-title')
    
    # Criando links para os filmes
    movie_links = ['https://imdb.com' + movie.find('a')['href'] for movie in movie_list]

    # Definindo o arquivo de saída usando a função para garantir nome único
    output_file = get_unique_filename('movies', output_directory)

    # Iniciando a execução paralela para extrair detalhes dos filmes
    threads = min(MAX_THREADS, len(movie_links))
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(lambda link: extract_movie_details(link, output_file), movie_links)

def main():
    start_time = time.time()

    try:
        popular_movies_url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
        response = requests.get(popular_movies_url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
        else:
            print(f"Falha ao buscar dados. Código de status: {response.status_code}")
            return None

        output_directory = './output'
        os.makedirs(output_directory, exist_ok=True)

        extract_movies(soup, output_directory)

    except Exception as e:
        print(f"Um erro ocorreu: {e}")

    end_time = time.time()
    print(f'Tempo total gasto: {round(end_time - start_time)}')

if __name__ == '__main__':
    main()
