import matplotlib.pyplot as plt
from sales_data import item_sale

def bar_graph_creator(data_name , itemCode , year):

  months_array = ["January" , "February" , "March" , "April" , "May" , "June" , "July" , "August" , "September","October","November","December"]
  y_axis = []
  for month in months_array:
    # if month in data_name[itemCode][year]:
    #   y_axis.append(data_name[itemCode][year][month]["total_sale"])
    # else:
    #   y_axis.append(0)
    if month not in data_name[itemCode][year]:
      data_name[itemCode][year][month] = 0

    if year in data_name[itemCode]:
      if month in data_name[itemCode][year]:
        
        print(itemCode , year , month)
        y_axis.append(data_name[itemCode][year][month]["total_sale"])
      else:
        y_axis.append(0)
    else:
      data_name[itemCode][year] = {
        'January': 0,
        'February': 0,
        'March': 0,
        'April': 0,
        'May': 0,
        'June': 0,
        'July': 0,
        'August': 0,
        'September': 0,
        'October': 0,
        'November': 0,
        'December': 0
        }






  plt.bar(months_array , y_axis , width=0.5)
  plt.xticks(rotation=45)
  plt.xlabel("Months")
  plt.ylabel("Total Sale")
  plt.title(f"{item_sale[itemCode]['item_name']} sale for year {year}")
  plt.savefig("graph1.png" , dpi=300 , bbox_inches="tight")


bar_graph_creator(item_sale , "787" , "2020")