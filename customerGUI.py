
#TASK 3 :--- Customer Segmentation Analysis using Clustering


from tkinter import *
from tkinter import messagebox
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

root = Tk()
root.title("Customer Segementation By Raj")
root.geometry("500x400+50+50")
root.configure(bg="lightpink")
f = ("Tw cen MT", 20, "bold")

lab_header = Label(root, text="Customer Segmentation Analysis", font=f,bg="lightpink")
lab_header.pack(pady=30)

lab_Annual_Income = Label(root,text=" Annual Income", font=f,bg="lightpink")
ent_Annual_Income = Entry(root, font=f)
lab_Annual_Income.pack(pady=5)
ent_Annual_Income.pack(pady=5)

lab_Spending_Score = Label(root,text=" Spending Score", font=f,bg="lightpink")
ent_Spending_Score = Entry(root, font=f)
lab_Spending_Score.pack(pady=5)
ent_Spending_Score.pack(pady=5)

def find():
	data = pd.read_csv("C:/demo/ML/internship/customer_segmetation/customers_oct23.csv")
	features = data[["Annual_Income", "Spending_Score"]]

	mms = MinMaxScaler()
	nfeatures = mms.fit_transform(features)

	model = KMeans(n_clusters=5)
	res = model.fit_predict(nfeatures)
	#data["clusters"] = res
	print(data)

	Annual_Income = (ent_Annual_Income.get())
	Spending_Score = (ent_Spending_Score.get())

	#d = [[income, spending]]
	#nd = mms.transform(d)
	#ans = model.predict(nd)

	if not Annual_Income:
		messagebox.showerror("Error", "Income cannot be empty")
		#ent_TV.focus()
		return

	if not Spending_Score:
		messagebox.showerror("Error", "Spending score cannot be empty")
		return

	if Annual_Income.strip() == "":
		messagebox.showerror("Error", "Annual_Income cannot be spaces")
		return

	if Spending_Score.strip() == "":
		messagebox.showerror("Error", "Spending_Score cannot be spaces")
		return

	if Annual_Income.isalpha():
		messagebox.showerror("Error", "Annual_Income cannot be text")
		return

	if Spending_Score.isalpha():
		messagebox.showerror("Error", "Spending_Score cannot be text")
		return

	if not Annual_Income.replace('.', '', 1).isdigit():
		messagebox.showerror(f"Error", "Annual_Income cannot be Special Characters")

	if not Spending_Score.replace('.', '', 1).isdigit():
		messagebox.showerror(f"Error", "Spending_Score cannot be Special Characters")



	try:
		Annual_Income = int(Annual_Income)
		Spending_Score = int(Spending_Score)
		

	except ValueError as e:
		print("Error", "Something Went Wrong!")
		return

	if (Annual_Income < 0)  :
		messagebox.showerror("Error", " Annual_Income values cannot be Negative")
		return

	if (Spending_Score < 0)  :
		messagebox.showerror("Error", " Spending_Score values cannot be Negative")
		return

	if (Annual_Income < 1)  :
		messagebox.showerror("Error", " MIN. value should be 1.")
		return

	if (Spending_Score < 1)  :
		messagebox.showerror("Error", " MIN. value should be 1.")
		return

	
	ent_Annual_Income.delete(0 ,'end')
	ent_Spending_Score.delete(0, 'end')
	ent_Annual_Income.focus()

	analysis = model.predict([[Annual_Income, Spending_Score]])
	#msg = "Prediction :" + str(round(analysis[0],2))
	#lab_ans.configure(text=msg)


	if analysis == 0:
		messagebox.showinfo("Analysis",f"High income,low spending(Cluster 0)")
	elif analysis == 1:
		messagebox.showinfo("Analysis",f"mid income, mid spending(Cluster 1)")
	elif analysis == 2:
		messagebox.showinfo("Analysis",f"High income,high spending(Cluster 2)")
	elif analysis == 3:
		messagebox.showinfo("Analysis",f"low income, high spending(Cluster 3)")
	elif analysis == 4:
		messagebox.showinfo("Analysis",f"low income, low spending(Cluster 4)")

	else:
        	messagebox.showerror('Analysis', 'something went wrong!')

btn_predict = Button(root, text="Predict ", font=f,command=find)
lab_ans = Label(root, font=f,bg="lightpink")
btn_predict.pack(pady=8)
lab_ans.pack(pady=5)
root.mainloop()







