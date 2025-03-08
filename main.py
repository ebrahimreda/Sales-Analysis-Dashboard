import pandas as pd
import matplotlib.pyplot as plt

rd = pd.read_csv("pandas/main.csv")


Credit_Card_, Cash_, Online_, Mobile_ = [], [], [], []

def Credit_Card():
    for method in rd["PaymentMethod"]:
        if method == "Credit Card":
            Credit_Card_.append(method)

def Cash():
    for method in rd["PaymentMethod"]:
        if method == "Cash":
            Cash_.append(method)

def Online():
    for method in rd["PaymentMethod"]:
        if method == "Online":
            Online_.append(method)

def Mobile():
    for method in rd["PaymentMethod"]:
        if method == "Mobile Payment":
            Mobile_.append(method)

Credit_Card(), Cash(), Online(), Mobile()

target_1 = {
    "Credit Card": len(Credit_Card_),
    "Cash": len(Cash_),
    "Online": len(Online_),
    "Mobile Payment": len(Mobile_)
}
dp=pd.Series(target_1)
dp.to_csv("pandas/Top_Payment_Methods_Details.csv")


plt.plot(target_1.keys(), target_1.values(),marker='o') 
plt.title("Statistics of payment methods")
plt.xlabel("Payment Method")
plt.ylabel("Number of uses")
plt.savefig("pandas/Payment_Methods.png")  
plt.show()



def Egypt():
    egypt_sales = []
    for index, country in rd["Country"].items():
        if country == "Egypt":
            egypt_sales.append(rd["SaleAmount"][index])
    return sum(egypt_sales) / len(egypt_sales)  # استخدام قسمة عادية بدل //

def Saudi_Arabia():
    Saudi_Arabia_ = []
    for index, country in rd["Country"].items():
        if country == "Saudi Arabia":
            Saudi_Arabia_.append(rd["SaleAmount"][index])
    return sum(Saudi_Arabia_) / len(Saudi_Arabia_) 

def UAE():
    
    uae = []
    for index, country in rd["Country"].items():
        if country == "UAE":
            uae.append(rd["SaleAmount"][index])
    return sum(uae)//len(uae)

def USA():
    
    usa = []
    for index, country in rd["Country"].items():
        if country == "USA":
            usa.append(rd["SaleAmount"][index])
    return sum(usa)//len(usa)

def Germany():
    
    Germany = []
    for index, country in rd["Country"].items():
        if country == "Germany":
            Germany.append(rd["SaleAmount"][index])
    return sum(Germany)//len(Germany)

def France():
    
    France = []
    for index, country in rd["Country"].items():
        if country == "France":
            France.append(rd["SaleAmount"][index])
    return sum(France)//len(France)

target_2 = {
    "Egypt": Egypt(),
    "Saudi Arabia": Saudi_Arabia(),
    "UAE": UAE(),
    "USA": USA(),
    "Germany": Germany(),
    "France": France()
}
dp=pd.Series(target_2)
dp.to_csv("Geographical_Sales_Statistics.csv")


plt.plot(target_2.keys(), target_2.values(),marker='o')  
plt.title(f"Average sales across countries\ntotal SaleAmount: {round(sum(rd["SaleAmount"]))}")
plt.xlabel("Country")  
plt.ylabel("Sales")
plt.savefig("pandas/Geographical_Sales.png") 
plt.show()

