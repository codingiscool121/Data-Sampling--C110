import statistics as st
import plotly.figure_factory as pf
import pandas as pd
import plotly.graph_objects as go
import random as rand
data=pd.read_csv("averages.csv")
average = data["average"].tolist()
graph = pf.create_distplot([average],["Averages"])
mean=st.mean(average)
sd=st.stdev(average)
graph.add_trace(go.Scatter(x=[mean,mean], y=[0,1.6], mode="lines", name="Mean"))
print("Actual:", mean)
print("Actual", sd)
print("LOADING....")
# graph.show()
list=[]
def sampling():
    for i in range(0,100):
        r= rand.randint(1,len(average)-1)
        list.append(average[r])
    listmean = st.mean(list)
    listsd = st.stdev(list)
    return(listmean)

meanlist=[]
for i in range(0,1000):
    meanlist.append(sampling())
# print(len(meanlist))
print("loaded")
meanofsamplingdistrubution= st.mean(meanlist)
sdofsamplingdistrubution = st.stdev(meanlist)
print("New Mean:", meanofsamplingdistrubution)
print("New standard deviation", sdofsamplingdistrubution)
meangraph = pf.create_distplot([meanlist], ["More accurate mean"])
meangraph.show()