print("Hello world")

import pandas
import seaborn
from sklearn.linear_model import LinearRegression

myynti = pandas.read_excel("./linreg1.xlsx")

print(myynti)

#seaborn.jointplot(data=myynti, x="Mainoskulut 1000 €", y="Myynti 1000 €")


x = myynti["Mainoskulut 1000 €"].to_frame()
y = myynti["Myynti 1000 €"]

model = LinearRegression().fit(x,y)

# Kysytään mallilta paljonko myyntiä tulisi 560€ markkinoinnilla

myyntiennuste = model.predict(pandas.DataFrame([0.56]))

print(myyntiennuste * 1000)