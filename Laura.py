# https://www.atlantis-press.com/journals/ijcis/125945415/view
# https://simpful.readthedocs.io/en/latest/index.html
# https://pypi.org/project/simpful/
# https://github.com/aresio/simpful/tree/master/examples

##############################################################################################################
#
# BackLog de Melhorias Fuzzy:
# 1. variar comida com a dieta prescrita
# 2. variar glicose com a prescrição da faixa
# 3. variar Insulina com a dose prescrita
# 4. incluir analise de tendência da glicose
# 5. criar modos Iniciante, Normal, Avançado
#
# BackLog para o App
# 1. correção dos valores informados
# 2. Alarmes de Insulina, Refeição e Medição
#
##############################################################################################################
##############################################################################################################

import simpful as sf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import csv

# ##############################################################################################################
# # Criando a entidade FS do Sistema Fuzzy
# FS = sf.FuzzySystem(show_banner=False)

# # ##############################################################################################################
# # Criando Fuzzy Set GLUCOSE da Medida de Glicose ( variar com a faixa alvo )
# lowest_glucose = 40 # definição do mínimo absoluto
# highest_glucose = 300 # definição do máximo absoluto

# low_range_glucose = 80 # ENTRADA: valor baixo da faixa alvo de glicose
# high_range_glucose = 160 # ENTRADA: valor alto da faixa alvo de glicose

# low_glucose = (lowest_glucose + low_range_glucose)/2 # ponto central da faixa baixa de glicose
# normal_glucose = (low_range_glucose + high_range_glucose)/2 # ponto central da faixa alvo de glicose
# high_glucose = (high_range_glucose + highest_glucose)/2 # ponto central da faixa baixa de glicose

# sigma_lowest = (low_glucose - lowest_glucose)/6
# sigma_low = (low_range_glucose - low_glucose)/3
# sigma_high = (high_glucose - high_range_glucose)/3

# # print(" lowest_glucose: ", lowest_glucose)
# # print(" low_glucose: ", low_glucose)
# # print(" low_range_glucose: ", low_range_glucose)
# # print(" normal_glucose: ", normal_glucose)
# # print(" high_range_glucose: ", high_range_glucose)
# # print(" high_glucose: ", high_glucose)
# # print(" highest_glucose: ", highest_glucose)
# # print(" --- ")
# # print(" sigma_lowest: ", sigma_lowest)
# # print(" sigma_low: ", sigma_low)
# # print(" sigma_high: ", sigma_high)

# GLCS_SET_HIPO = sf.DoubleGaussianFuzzySet(mu1=0, sigma1=sigma_lowest, mu2=lowest_glucose, sigma2=sigma_lowest, term="Hipo")
# GLCS_SET_LOW = sf.GaussianFuzzySet(mu=low_glucose, sigma=4, term="Low")
# GLCS_SET_NORMAL = sf.DoubleGaussianFuzzySet(mu1=low_range_glucose, sigma1=sigma_low, mu2=high_range_glucose, sigma2=sigma_high, term="Normal")
# GLCS_SET_HYPER = sf.DoubleGaussianFuzzySet(mu1=high_range_glucose+3*sigma_high, sigma1=sigma_high, mu2=highest_glucose, sigma2=sigma_high, term="Hyper")
# FS.add_linguistic_variable("GLUCOSE", sf.LinguisticVariable( [GLCS_SET_HIPO, GLCS_SET_LOW, GLCS_SET_NORMAL, GLCS_SET_HYPER], universe_of_discourse=[lowest_glucose, highest_glucose]))

# sf.LinguisticVariable( [GLCS_SET_HIPO, GLCS_SET_LOW, GLCS_SET_NORMAL, GLCS_SET_HYPER], universe_of_discourse=[lowest_glucose, highest_glucose]).plot()

# ##############################################################################################################
# # Criando a entidade FS do Sistema Fuzzy
FS = sf.FuzzySystem(show_banner=False)

# ##############################################################################################################
# Criando Fuzzy Set GLUCOSE da Medida de Glicose ( variar com a faixa alvo )
lowest_glucose = 40 # definição do mínimo absoluto
highest_glucose = 300 # definição do máximo absoluto

low_range_glucose = 80 # ENTRADA: valor baixo da faixa alvo de glicose
high_range_glucose = 160 # ENTRADA: valor alto da faixa alvo de glicose

low_glucose = (lowest_glucose + low_range_glucose)/2 # ponto central da faixa baixa de glicose
normal_glucose = (low_range_glucose + high_range_glucose)/2 # ponto central da faixa alvo de glicose
high_glucose = (high_range_glucose + highest_glucose)/2 # ponto central da faixa baixa de glicose

sigma_lowest = (low_glucose - lowest_glucose)/6
sigma_low = (low_range_glucose - low_glucose)/3
sigma_high = (high_glucose - high_range_glucose)/3

# print(" lowest_glucose: ", lowest_glucose)
# print(" low_glucose: ", low_glucose)
# print(" low_range_glucose: ", low_range_glucose)
# print(" normal_glucose: ", normal_glucose)
# print(" high_range_glucose: ", high_range_glucose)
# print(" high_glucose: ", high_glucose)
# print(" highest_glucose: ", highest_glucose)
# print(" --- ")
# print(" sigma_lowest: ", sigma_lowest)
# print(" sigma_low: ", sigma_low)
# print(" sigma_high: ", sigma_high)

GLCS_SET_HIPO = sf.DoubleGaussianFuzzySet(mu1=0, sigma1=sigma_lowest, mu2=lowest_glucose, sigma2=sigma_lowest, term="Hipo")
GLCS_SET_LOW = sf.GaussianFuzzySet(mu=low_glucose, sigma=4, term="Low")
GLCS_SET_NORMAL = sf.DoubleGaussianFuzzySet(mu1=low_range_glucose, sigma1=sigma_low, mu2=high_range_glucose, sigma2=sigma_high, term="Normal")
GLCS_SET_HYPER = sf.DoubleGaussianFuzzySet(mu1=high_range_glucose+3*sigma_high, sigma1=sigma_high, mu2=highest_glucose, sigma2=sigma_high, term="Hyper")
FS.add_linguistic_variable("GLUCOSE", sf.LinguisticVariable( [GLCS_SET_HIPO, GLCS_SET_LOW, GLCS_SET_NORMAL, GLCS_SET_HYPER], universe_of_discourse=[lowest_glucose, highest_glucose]))

sf.LinguisticVariable( [GLCS_SET_HIPO, GLCS_SET_LOW, GLCS_SET_NORMAL, GLCS_SET_HYPER], universe_of_discourse=[lowest_glucose, highest_glucose]).plot()

# ##############################################################################################################
# Criando Fuzzy Set FOOD da Comida ( varia com a dieta diária prescrita )
daily_feed = 50 # ENTRADA: valor de uma refeição padrão
full_feed = 2 * daily_feed
max_feed = 4 * daily_feed

plateau_feed = daily_feed/5
sigma_feed = daily_feed/6

# print(" daily_feed: ", daily_feed)
# print(" full_feed: ", full_feed)
# print(" max_feed: ", max_feed)
# print(" --- ")
# print(" plateau_feed: ", plateau_feed)
# print(" sigma_feed: ", sigma_feed)

FOOD_SET_LOW = sf.DoubleGaussianFuzzySet(mu1=(0)-plateau_feed, sigma1=sigma_feed, mu2=(0)+plateau_feed, sigma2=sigma_feed, term="Low")
FOOD_SET_NORMAL = sf.DoubleGaussianFuzzySet(mu1=(1*daily_feed)-plateau_feed, sigma1=sigma_feed, mu2=(1*daily_feed)+plateau_feed, sigma2=sigma_feed, term="Normal")
FOOD_SET_HIGH = sf.DoubleGaussianFuzzySet(mu1=(2*daily_feed)-plateau_feed, sigma1=sigma_feed, mu2=(2*daily_feed)+plateau_feed, sigma2=sigma_feed, term="High")
# FOOD_SET_HYPER = sf.DoubleGaussianFuzzySet(mu1=(3*daily_feed)-plateau_feed, sigma1=sigma_feed, mu2=(3*daily_feed)+plateau_feed, sigma2=sigma_feed, term="Hyper")
FOOD_SET_HYPER = sf.DoubleGaussianFuzzySet(mu1=(3*daily_feed)-plateau_feed, sigma1=sigma_feed, mu2=max_feed, sigma2=sigma_feed, term="Hyper")
FS.add_linguistic_variable("FOOD", sf.LinguisticVariable( [FOOD_SET_LOW, FOOD_SET_NORMAL, FOOD_SET_HIGH, FOOD_SET_HYPER], universe_of_discourse=[0, max_feed]))

sf.LinguisticVariable( [FOOD_SET_LOW, FOOD_SET_NORMAL, FOOD_SET_HIGH, FOOD_SET_HYPER], universe_of_discourse=[0, max_feed]).plot()

# ##############################################################################################################
# Definindo Fuzzy Set de Saída INSULIN de quantidade de UI de Insulina Rápida  ( varia com a dose prescrita )
insuline_dose = 1 # ENTRADA: dose padrão de insulina
max_insuline_dose = 4 * insuline_dose
# sigma_dose = insuline_dose/3
sigma_dose = insuline_dose/6

INSL_SET_NO = sf.GaussianFuzzySet(mu=0, sigma=sigma_dose, term="No_Insulin")
INSL_SET_1UI = sf.GaussianFuzzySet(mu=insuline_dose, sigma=sigma_dose, term="1_Dose_Insulin")
INSL_SET_2UI = sf.GaussianFuzzySet(mu=2*insuline_dose, sigma=sigma_dose, term="2_Doses_Insulin")
INSL_SET_3UI = sf.GaussianFuzzySet(mu=3*insuline_dose, sigma=sigma_dose, term="Extra_Dose_Insulin")
FS.add_linguistic_variable("INSULIN", sf.LinguisticVariable( [INSL_SET_NO, INSL_SET_1UI, INSL_SET_2UI, INSL_SET_3UI], universe_of_discourse=[0, max_insuline_dose]))

sf.LinguisticVariable( [INSL_SET_NO, INSL_SET_1UI, INSL_SET_2UI, INSL_SET_3UI], universe_of_discourse=[0, (max_insuline_dose)]).plot()

##############################################################################################################
# Definindo Fuzzy Rules
FS.add_rules([
    # Glicose em Hipo
	"IF (GLUCOSE IS Hipo) THEN (INSULIN IS No_Insulin)",
    
    # Glicose Low
	"IF (GLUCOSE IS Low) AND ((FOOD IS Low) OR (FOOD IS Normal)) THEN (INSULIN IS No_Insulin)",
	"IF (GLUCOSE IS Low) AND ((FOOD IS High) OR (FOOD IS Hyper)) THEN (INSULIN IS 1_Dose_Insulin)",
    
    # Glicose Normal
	"IF (GLUCOSE IS Normal) AND (FOOD IS Low) THEN (INSULIN IS No_Insulin)",
	"IF (GLUCOSE IS Normal) AND ((FOOD IS Normal) OR (FOOD IS High)) THEN (INSULIN IS 1_Dose_Insulin)",
	"IF (GLUCOSE IS Normal) AND (FOOD IS Hyper) THEN (INSULIN IS 2_Doses_Insulin)",
    
    # Glicose Hyper
	"IF (GLUCOSE IS Hyper) AND (FOOD IS Low) THEN (INSULIN IS 1_Dose_Insulin)",
	"IF (GLUCOSE IS Hyper) AND ((FOOD IS Normal) OR (FOOD IS High)) THEN (INSULIN IS 2_Doses_Insulin)",
	"IF (GLUCOSE IS Hyper) AND (FOOD IS Hyper) THEN (INSULIN IS Extra_Dose_Insulin)"
	])

##############################################################################################################
# Testando Fuzzy Logic com refeição padrão e glicose normal
food_idx = daily_feed
glucose_idx = normal_glucose
food_idx = 43
glucose_idx = 282
FS.set_variable("FOOD", food_idx)
FS.set_variable("GLUCOSE", glucose_idx)

INSULIN = FS.inference()
result = round(INSULIN.get('INSULIN'), 2)
print(" ########## Teste básico: ########## ")
print("   GLUCOSE: ", glucose_idx, "; FOOD: ", food_idx, " == INSULIN: ", result)

##############################################################################################################
# # Testando Fuzzy Logic para verificar os pontos limites padrões
# print(" ########## Testes de Verificação ##########")

# print(" 1. GLUCOSE IS Hipo")
# glucose_idx = lowest_glucose
# FOOD_TST = [0, (0.25*daily_feed), (0.5*daily_feed), (0.75*daily_feed), (1*daily_feed), (1.25*daily_feed), (1.5*daily_feed), (1.75*daily_feed), (2*daily_feed), (2.5*daily_feed), (2.75*daily_feed), (3*daily_feed)]

# for food_idx in FOOD_TST:
    # FS.set_variable("GLUCOSE", glucose_idx)
    # FS.set_variable("FOOD", food_idx)
    # INSULIN = FS.inference()
    # # print (INSULIN)
    # result = round(INSULIN.get('INSULIN'), 1)
    # print( "   GLUCOSE: ", glucose_idx, "; FOOD: ", food_idx, " == INSULIN: ", result)
    # # Laura_writer.writerow([str(glucose_idx), str(food_idx), str(result)])

# print(" 2. GLUCOSE IS Low")
# glucose_idx = low_glucose
# FOOD_TST = [0, (0.25*daily_feed), (0.5*daily_feed), (0.75*daily_feed), (1*daily_feed), (1.25*daily_feed), (1.5*daily_feed), (1.75*daily_feed), (2*daily_feed), (2.5*daily_feed), (2.75*daily_feed), (3*daily_feed)]

# for food_idx in FOOD_TST:
    # FS.set_variable("GLUCOSE", glucose_idx)
    # FS.set_variable("FOOD", food_idx)
    # INSULIN = FS.inference()
    # # print (INSULIN)
    # result = round(INSULIN.get('INSULIN'), 1)
    # print( "   GLUCOSE: ", glucose_idx, "; FOOD: ", food_idx, " == INSULIN: ", result)
    # # Laura_writer.writerow([str(glucose_idx), str(food_idx), str(result)])
        
# print(" 2. GLUCOSE IS Normal")
# glucose_idx = normal_glucose
# FOOD_TST = [0, (0.25*daily_feed), (0.5*daily_feed), (0.75*daily_feed), (1*daily_feed), (1.25*daily_feed), (1.5*daily_feed), (1.75*daily_feed), (2*daily_feed), (2.5*daily_feed), (2.75*daily_feed), (3*daily_feed)]

# for food_idx in FOOD_TST:
    # FS.set_variable("GLUCOSE", glucose_idx)
    # FS.set_variable("FOOD", food_idx)
    # INSULIN = FS.inference()
    # # print (INSULIN)
    # result = round(INSULIN.get('INSULIN'), 1)
    # print( "   GLUCOSE: ", glucose_idx, "; FOOD: ", food_idx, " == INSULIN: ", result)
    # # Laura_writer.writerow([str(glucose_idx), str(food_idx), str(result)])
        
# print(" 2. GLUCOSE IS Hyper")
# glucose_idx = highest_glucose
# FOOD_TST = [0, (0.25*daily_feed), (0.5*daily_feed), (0.75*daily_feed), (1*daily_feed), (1.25*daily_feed), (1.5*daily_feed), (1.75*daily_feed), (2*daily_feed), (2.5*daily_feed), (2.75*daily_feed), (3*daily_feed)]

# for food_idx in FOOD_TST:
    # FS.set_variable("GLUCOSE", glucose_idx)
    # FS.set_variable("FOOD", food_idx)
    # INSULIN = FS.inference()
    # # print (INSULIN)
    # result = round(INSULIN.get('INSULIN'), 1)
    # print( "   GLUCOSE: ", glucose_idx, "; FOOD: ", food_idx, " == INSULIN: ", result)
    # # Laura_writer.writerow([str(glucose_idx), str(food_idx), str(result)])


##############################################################################################################
# Gráfico Fuzzy Logic 
print(" ########## Gráfico Fuzzy Logic  ##########")

# Eixo X
FOOD_TST = np.arange(0, max_feed + daily_feed/10, daily_feed/10)
# print(" FOOD_TST:", FOOD_TST)
# print(" tamanho FOOD_TST:", len(FOOD_TST))

# Eixo Y
GLUCOSE_TST = np.arange(lowest_glucose, highest_glucose + 5, 5)
# print(" GLUCOSE_TST:", GLUCOSE_TST)
# print(" tamanho GLUCOSE_TST:", len(GLUCOSE_TST))

# Eixo Z
Z = []
# print(" Z:", Z)

for glucose_idx in GLUCOSE_TST:
    for food_idx in FOOD_TST:
        FS.set_variable("FOOD", food_idx)
        FS.set_variable("GLUCOSE", glucose_idx)
        INSULIN = FS.inference()
        result = round(INSULIN.get('INSULIN'), 2)
        # print( "   GLUCOSE: ", glucose_idx, "; FOOD: ", food_idx, " == INSULIN: ", result)
        Z = np.append(Z, result)

Z = np.reshape(Z,(len(GLUCOSE_TST),len(FOOD_TST)))
# print(" Z:", Z)

# Crinado gráfico 3d
ax = plt.figure().add_subplot(projection='3d')

# Criando Grid (X,Y)
FOOD_TST, GLUCOSE_TST = np.meshgrid(FOOD_TST, GLUCOSE_TST)

# Plot the surface with face colors taken from the array we made.
surf = ax.plot_surface(FOOD_TST, GLUCOSE_TST, Z, cmap=cm.viridis)
plt.title("Insulin Dose")
plt.xlabel('Food value')
plt.ylabel('Glucose value')

# Rotacionando gráfico
ax.view_init(elev=20, azim=-135)
plt.savefig('3D_Fuzzy_Insulin.jpg')
plt.show()

