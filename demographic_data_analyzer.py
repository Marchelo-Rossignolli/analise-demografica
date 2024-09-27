import pandas as pd

def calculate_demographic_data(print_data=True):
    # Ler os dados do arquivo
    df = pd.read_csv('adult.data.csv')

    # Quantos de cada raça estão representados neste conjunto de dados? Isso deve ser uma série do Pandas com os nomes das raças como rótulos de índice.
    race_count = df.race.value_counts()

    # Qual é a idade média dos homens?
    average_age_men = df[df.sex == 'Male'].age.mean().round(1)

    # Qual é a porcentagem de pessoas que têm um diploma de bacharel?
    percentage_bachelors = ((df.education == 'Bachelors').sum() / len(df) * 100).round(1)

    # Qual porcentagem de pessoas com educação avançada (Bacharelado, Mestrado ou Doutorado) ganha mais de 50K?
    # Qual porcentagem de pessoas sem educação avançada ganha mais de 50K?

    # Com e sem Bacharelado, Mestrado ou Doutorado
    # Filtrar o DataFrame para níveis de educação superior e inferior
    mascara = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education = df[mascara]
    lower_education = df[~mascara]

    # Calcular a porcentagem de pessoas com salário >50K para cada nível de educação
    higher_education_rich = (higher_education[higher_education['salary'] == ">50K"].shape[0] / higher_education.shape[0]) * 100, round(1)
    lower_education_rich = (lower_education[lower_education['salary'] == ">50K"].shape[0] / lower_education.shape[0]) * 100, round(1)

    # Qual é o número mínimo de horas que uma pessoa trabalha por semana (característica horas-por-semana)?
    min_work_hours = df["hours-per-week"].min()

    # Qual porcentagem das pessoas que trabalham o número mínimo de horas por semana têm um salário >50K?
    min_hour_workers = df.loc[df['hours-per-week'] == min_work_hours]
    num_min_workers = min_hour_workers.shape[0]

    rich_percentage = round((min_hour_workers[min_hour_workers['salary'] == ">50K"].shape[0] / num_min_workers) * 100, 1)

    # Qual país tem a maior porcentagem de pessoas que ganham >50K?
    country_rich = df[df['salary'] == '>50K'].groupby('native-country').size()
    total_country = df.groupby('native-country').size()
    country_percentage = (country_rich / total_country) * 100
    highest_earning_country = country_percentage.sort_values(ascending=False).idxmax()
    highest_earning_country_percentage = round(country_percentage[highest_earning_country], 1)

    # Identificar a ocupação mais popular para aqueles que ganham >50K na Índia.
    people_in_india = df.loc[df['native-country'] == 'India']
    rich_in_india = people_in_india.loc[people_in_india['salary'] == ">50K"]
    rich_occupations_india = rich_in_india.groupby('occupation').size()
    top_IN_occupation = rich_occupations_india.idxmax()

    # NÃO MODIFIQUE ABAIXO DESTA LINHA

    if print_data:
        print("Quantidade de cada raça:\n", race_count) 
        print("Idade média dos homens:", average_age_men)
        print(f"Porcentagem com diploma de bacharel: {percentage_bachelors}%")
        print(f"Porcentagem com educação avançada que ganham >50K: {higher_education_rich}%")
        print(f"Porcentagem sem educação avançada que ganham >50K: {lower_education_rich}%")
        print(f"Tempo mínimo de trabalho: {min_work_hours} horas/semana")
        print(f"Porcentagem de ricos entre aqueles que trabalham menos horas: {rich_percentage}%")
        print("País com maior porcentagem de ricos:", highest_earning_country)
        print(f"Maior porcentagem de pessoas ricas em um país: {highest_earning_country_percentage}%")
        print("Principais ocupações na Índia:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
