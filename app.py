import streamlit as st
import google.generativeai as genai
import settings
import dict_cars  # Importe o arquivo dict_cars.py
from PIL import Image
import os

GEMINI_API_KEY = 'CHAVE_API'
# Substitua pela sua API KEY

genai.configure(api_key=GEMINI_API_KEY)


def generate_random_phrase(language_and_accent: str):
    generation_config = {
        "temperature": 1,
        "top_p": 1,
        "top_k": 0,
        "max_output_tokens": 2048,
    }
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=settings.safety_settings)

    language_treated = language_and_accent.split(
        "-")[0]  # pegando somente a lingua

    convo = model.start_chat(history=[])
    convo.send_message(
        f"""Gere uma frase curta aleatória em {language_treated}. Me envie SOMENTE a frase.""")
    response = convo.last.text

    return response


def generate_car_description(pilot, year, wins, titles, text_to_check: str, language_and_accent: str):
    """Gera a descrição do carro e da vida do Ayrton Senna usando IA."""

    generation_config = {
        "temperature": 1,
        "top_p": 1,
        "top_k": 0,
        "max_output_tokens": 1024,
    }
    system_instruction = "Voce é uma ferramenta focada em conversar sobre a história do Ayrton Senna."
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                  generation_config=generation_config,
                                  system_instruction=system_instruction,
                                  safety_settings=settings.safety_settings)

    language_treated = language_and_accent.split(
        "-")[0]  # pegando somente a lingua
    convo = model.start_chat(history=[
        {
            "role": "user",
            "parts": ["""Voce é uma ferramenta focada em contar a história do Ayrton Senna, sua principal função é falar sobre um pouco da história desse grande piloto nos {year} que correu. Descreva as {wins}, {titles} desse grande {pilot}.\n
                       texto: Senna juntou-se à McLaren em 1988, formando uma dupla imbatível com Alain Prost. A bordo do MP4-4, considerado um dos carros mais dominantes da história da F1, Senna conquistou seu primeiro título mundial com oito vitórias e treze poles positions em dezesseis corridas. A rivalidade com Prost marcou a temporada."""]
        },
        {
            "role": "model",
            "parts": [f"""
                      Crie uma descrição envolvente e informativa sobre o carro de Fórmula 1 pilotado por {pilot} em {year}, destacando suas conquistas:
                      Piloto: {pilot},
                      Ano: {year},
                      Vitórias: {wins},
                      Títulos: {titles}"""]
        },
    ]
    )
    convo.send_message(f"""Voce é uma ferramenta focada em narrar a história do Ayrton Senna do Brasil, sua principal função é resumir e contar momentos marcantes da vida do Ayrton Senna na carreira automobilística.\n
                       texto: {text_to_check}""")
    response = convo.last.text
    # print(response)

    return response


# Dicionário 'cars' importado de teste.py
cars = dict_cars.cars

# Caminho para o diretório das imagens
image_dir = '/home/matheus/repos_github/projetos_matheus/DesafioAlura2024/images'


def main():
    st.set_page_config("Ayrton Senna: Uma Lenda", layout="wide")
    st.header("Ayrton Senna: Uma Lenda nas Pistas", divider=True)

    with st.sidebar:
        # st.image("images/carro.png") # Substitua pela imagem desejada
        st.markdown("""
        ## Bem vindo ao *Ayrton Senna: Uma Lenda*.
        ## Conheça a trajetória do piloto brasileiro e seus carros.
        ------------------------------------------
        ## Explore a carreira de Senna:
        * Selecione um ano para saber mais sobre o carro que ele pilotou, suas vitórias e conquistas.
        """)

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

    tab_escrita = st.tabs(["Resumo", "Escrita"])
    with tab_escrita[0]:
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

    with tab_escrita[1]:
        st.subheader(
            "Vamos ver se você conhece a história do Ayrton Senna.")
        text_to_check = st.text_area("Escreva aqui seu texto/frase")
        if text_to_check:
            response = generate_car_description(
                pilot="Ayrton Senna", year=selected_year, wins=wins, titles=titles, text_to_check=text_to_check, language_and_accent="pt-BR"
            )
            st.divider()
            st.write(response)


if __name__ == "__main__":
    main()
