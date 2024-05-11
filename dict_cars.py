import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# Defina sua API key do Google Generative AI aqui
genai.configure(api_key='chave_api')

# Dicionário dos carros e suas descrições por ano
cars = {
    "1983": {"model": "Toleman TG183B",
             "description": "Projetado por Rory Byrne para a temporada 1983, este foi o carro que marcou a estreia de Ayrton Senna na Fórmula 1, em 1984. Foram quatro provas com o modelo, que permitiu a Senna os primeiros pontos na categoria, com dois sextos lugares nos GPs da África do Sul e da Bélgica.",
             "titles": 0,
             "wins": 0},
    "1984": {"model": "Toleman TG184",
             "description": "Em sua temporada de estreia na F1, Senna pilotou o Toleman TG184, conquistando um surpreendente segundo lugar no GP de Mônaco, sob chuva torrencial. Apesar do carro não ser dos mais competitivos, Senna demonstrou seu talento com atuações memoráveis.",
             "titles": 0,
             "wins": 0},
    "1985": {"model": "Lotus 97T",
             "description": "No comando do Lotus 97T, Senna conquistou sua primeira vitória na F1, no GP de Portugal, também sob forte chuva. Obteve outras seis poles positions e terminou o campeonato em quarto lugar, consolidando-se como um dos grandes nomes da categoria.",
             "titles": 0,
             "wins": 1},
    "1986": {"model": "Lotus 98T",
             "description": "Com o 98T, também projetado por Gérard Ducarouge e Martin Ogilvie, Senna conquistou duas vitórias, oito poles e oito pódios, terminando o ano em quarto lugar no Mundial de Pilotos. Sua pilotagem agressiva e precisa o consagrou como o 'Rei de Mônaco' após uma vitória dominante no principado.",
             "titles": 0,
             "wins": 2},
    "1987": {"model": "Lotus 99T",
             "description": "Foi com a última Lotus que pilotou, a 99T, que Senna conquistou a primeira vitória no GP de Mônaco. Assim como os modelos anteriores, foi projetada por Gérard Ducarouge e Martin Ogilvie. Naquele ano, Senna terminou o campeonato em terceiro, com a vitória em Mônaco e outra em Detroit, além de uma pole, três voltas mais rápidas e oito pódios.",
             "titles": 0,
             "wins": 2},
    "1988": {"model": "McLaren MP4-4",
             "description": "Senna juntou-se à McLaren em 1988, formando uma dupla imbatível com Alain Prost. A bordo do MP4-4, considerado um dos carros mais dominantes da história da F1, Senna conquistou seu primeiro título mundial com oito vitórias e treze poles positions em dezesseis corridas. A rivalidade com Prost marcou a temporada.",
             "titles": 1,
             "wins": 8},
    "1989": {"model": "McLaren MP4-5",
             "description": "A rivalidade com Prost se intensificou em 1989. Pilotando o MP4-5, Senna venceu seis corridas e conquistou o vice-campeonato após uma polêmica colisão com Prost no GP do Japão. O título foi decidido em favor de Prost na última corrida.",
             "titles": 0,
             "wins": 6},
    "1990": {"model": "McLaren MP4-5B",
             "description": "Senna conquistou seu segundo título mundial em 1990, pilotando o MP4-5B, uma evolução do carro do ano anterior. Venceu seis corridas e protagonizou duelos emocionantes com Prost, que havia se transferido para a Ferrari. A colisão com Prost na primeira curva do GP do Japão selou o bicampeonato de Senna.",
             "titles": 1,
             "wins": 6},
    "1991": {"model": "McLaren MP4-6",
             "description": "Com o MP4-6, Senna conquistou seu terceiro e último título mundial. Dominou a temporada com sete vitórias e oito poles positions. A superioridade do carro e o talento de Senna o levaram a um tricampeonato incontestável.",
             "titles": 1,
             "wins": 7},
    "1992": {"model": "McLaren MP4-7A",
             "description": "A temporada de 1992 marcou o início do domínio da Williams na F1. Senna, com o MP4-7A, lutou bravamente contra o forte carro de Nigel Mansell, mas terminou o campeonato em quarto lugar com três vitórias e duas poles positions. Apesar das dificuldades, Senna demonstrou sua garra e habilidade em diversas corridas memoráveis.",
             "titles": 0,
             "wins": 3},
    "1993": {"model": "McLaren MP4-8",
             "description": "Senna permaneceu na McLaren em 1993, pilotando o MP4-8. A Williams continuava dominante, mas Senna conquistou cinco vitórias espetaculares, incluindo uma atuação memorável sob chuva torrencial em Donington Park. Terminou o campeonato em segundo lugar, atrás de Alain Prost, que havia retornado à F1 pela Williams.",
             "titles": 0,
             "wins": 5},
    "1994": {"model": "Williams FW16",
             "description": "Senna assinou com a Williams em 1994, buscando um novo desafio e a chance de lutar pelo título novamente. A temporada começou de forma difícil, com o FW16 se mostrando um carro instável e difícil de pilotar. Senna conquistou três poles positions, mas não venceu nenhuma corrida. Infelizmente, sua trajetória foi interrompida por um trágico acidente no GP de San Marino, em Ímola, que tirou sua vida.",
             "titles": 0,
             "wins": 0}
}

# Caminho para o diretório das imagens 
image_dir = '/home/matheus/repos_github/projetos_matheus/DesafioAlura2024/images'

def main():
    st.title('Ayrton Senna: Uma Lenda nas Pistas')

    # Lista os anos disponíveis
    available_years = list(cars.keys())
    available_years.sort()

    # Seleção do ano pelo usuário
    selected_year = st.selectbox('Selecione o ano:', available_years)

    # Obtém informações do carro do ano selecionado
    car_info = cars[selected_year]
    model = car_info["model"]
    description = car_info["description"]
    titles = car_info["titles"]
    wins = car_info["wins"]

    # Monta o nome do arquivo de imagem
    image_file = f"{selected_year}_{model}.jpg"
    image_path = os.path.join(image_dir, image_file)

    # Exibe a imagem
    if os.path.isfile(image_path):
        image = Image.open(image_path)
        st.image(image, caption=f"{selected_year} - {model}")
    else:
        st.write("Imagem não encontrada.")

    # Exibe as informações do carro
    st.write(f"**Descrição:** {description}")
    st.write(f"**Títulos nesse ano:** {titles}")
    st.write(f"**Vitórias nesse ano:** {wins}")



if __name__ == "__main__":
    main()