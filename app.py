import streamlit as st
import google.generativeai as genai
import settings
import dict_cars # Importe o arquivo teste.py
from PIL import Image
import os

API_KEY = 'chave_api' 
# Substitua pela sua API KEY

genai.configure(api_key=API_KEY)

def generate_car_description(pilot, year, wins, titles):
    """Gera a descrição do carro usando IA."""

    generation_config = {
        "temperature": 0.7,
        "top_p": 1,
        "top_k": 0,
        "max_output_tokens": 256,
    }
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=settings.safety_settings)

    prompt = f"""
    Crie uma descrição envolvente e informativa sobre o carro de Fórmula 1 pilotado por {pilot} em {year}, destacando suas conquistas:

    Piloto: {pilot}
    Ano: {year}
    Vitórias: {wins}
    Títulos: {titles}
    """

    convo = model.start_chat()
    convo.send_message(prompt)
    description = convo.last.text
    
    return description

# Dicionário 'cars' importado de teste.py
cars = dict_cars.cars

# Caminho para o diretório das imagens 
image_dir = '/home/matheus/repos_github/projetos_matheus/DesafioAlura2024/images'

# def get_senna_info(year):
#   """
#   Retorna informações sobre Ayrton Senna e seu carro em um determinado ano.

#   Args:
#     year: O ano desejado (string).

#   Returns:
#     Uma string contendo a descrição do carro, títulos e vitórias de Senna naquele ano.
#   """

#   if year in cars:
#     car_info = cars[year]
#     model = car_info["model"]
#     description = car_info["description"]
#     titles = car_info["titles"]
#     wins = car_info["wins"]
#     return f"Em {year}, Ayrton Senna pilotou o {model}. {description} Ele conquistou {titles} título mundial e {wins} vitórias nesse ano."
#   else:
#     return "Informações sobre esse ano não estão disponíveis."

def main():
    st.set_page_config("Ayrton Senna: Uma Lenda", layout="wide")
    st.header("Ayrton Senna: Uma Lenda nas Pistas", divider=True)

    with st.sidebar:
        #st.image("images/carro.png") # Substitua pela imagem desejada
        st.markdown("""
        ## Bem vindo ao *Ayrton Senna: Uma Lenda*.
        ## Conheça a trajetória do piloto brasileiro e seus carros.
        ------------------------------------------
        ## Explore a carreira de Senna:
        * Selecione um ano para saber mais sobre o carro que ele pilotou, suas vitórias e conquistas.
        """)

   # if st.button("Gerar Descrição"):
   
        
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

    # Obtém informações sobre Senna
    #senna_info = get_senna_info(selected_year)

    # Exibe as informações 
    #st.write(senna_info)



if __name__ == "__main__":
    main()

