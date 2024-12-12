# Analysis of Lithium Ion Battery Voltage Data
This repo contains analysis of lithium ion battery data. The data set was acquired from "https://data.nasa.gov/Raw-Data/Randomized-and-Recommissioned-Battery-Dataset/xg3n-ngei/about_data" with credit being given to the Probabilistic Mechanics Lab, University of Central Florida. The data set contains voltage information for many different lithium ion batteries. These batteries were subjected to rapid aging at constant and variable loads. For more information, please visit the link above and read the "Dataset Original README" for more information directly from the Probabilistic Mechanics Lab. 

The analysis answers the general questions stated below, relating to lithium-ion batteries.

Question 1: How does a battery's voltage relate over time?

Question 2: How does a battery's temperature relate to load current?

Question 3: How does a battery's voltage relate to load current?

# Requirements
The list of requirements are in the "Requirements.txt" file. It is recommended to use pip install.

To better visualize the raw data, it is recommented to have "Microsoft Excel".

# Main Programs Written To Analyze The Data

There are three main programs which answer the topic questions. 

"FinalQuestion1.py" answers question 1. 

<p align="center">
<img width="1190" alt="image" align="center" src="https://github.com/user-attachments/assets/11237fe0-953f-467d-9c93-05672569334d" />
<p align="center">Figure 1: Battery Voltage (V) And Load Current (A) Over Time For First And Last Discharge Cycles</p>
</p>

From Figure 1, we can see that although the battery voltage decreases over time as a constant current load is applied, it does not do so with a constant slope. It follows more of an "S" shape which indicates that at different capacity levels or as time goes on under constant current load, the battery voltage decreases at different rates. We can also see that although the current load is near constant, it does contain fluctuations which aligns with the Probabilistic Mechanics Lab's goal of simulating real conditions as load current will likely not be perfectly constant in real applications. 

The relevant code is shown below in Figure 1.1 and 1.2.
<p align="center">
<img width="490" alt="image" align="center" src="https://github.com/user-attachments/assets/465a84b2-041a-40b7-914c-8b9df7470f11" />
<p align="center">Figure 1.1: Code Segment For Calculating Start And End Of First Cycle</p>
<p align="center">
<img width="592" alt="image" align="center" src="https://github.com/user-attachments/assets/a430f585-8586-4ae4-938d-237a0f8535f7" />
<p align="center">Figure 1.2: Code Segment For Calculating Start And End Of Last Cycle</p>
</p>

It is highly recommended to visit "FinalQuestion1.py" for the full code along with relevant comments for Figures 1.1 and 1.2. 

"FinalQuestion2.py" shows additional analysis on how load current impacts the rate of change in voltage across the battery. This image is shown below in Figure 2. 

<p align="center">
<img width="1195" alt="image" align="center" src="https://github.com/user-attachments/assets/c3e60e5a-a8ff-4380-ba0c-b9b05f29d173" />
<p align="center">Figure 2: Load Current (A) and Battery Voltage Rate Of Change (dv/dt) Over Time For First And Last Discharge Cycles</p>
</p>

From Figure 2, we can see that the rate of change of the battery's voltage stays constant at 0. Although the math behind the code for that is most likely technically correct, there must be a lack of knowledge on my part in being able to show the data in a way which provides more understanding. I tried increasing the distance at which I calculated the rate of change. However, these changes gave me the same results.

The relevant code is shown below in Figure 2.1.

<p align="center">
<img width="467" alt="image" align="center" src="https://github.com/user-attachments/assets/781f9d2b-c47c-4df2-aed8-c27773fb9a8a" />
<p align="center">Figure 2.1: Code Segment For Calculating Rate Of Change</p>
</p>

"FinalQuestion2.py" shows the full code for Figure 2.1. I also used functions in "FinalQuestion1.py" which are shown in Figures 1.1 and 1.2. 


"FinalQuestion3.py" answers both question 2 and 3. The output is a print statement which displays a table of many relevant values and is shown below in Figure 3. 

<p align="center">
<img width="998" alt="image" align="center" src="https://github.com/user-attachments/assets/a96df7ce-4e11-4fe6-8add-cd2823f12908" />
<p align="center">Figure 3: Table Of Relevant Battery And Load Conditions For All Discharge Cycles</p>
</p>

Figure 3 shows us several different statistics for each discharge cycle. It shows us the start and end voltage of the battery and provides the average load current at that cycle. In addition, we can see the time the cycle took. This gives us an indication of how long it will take for the voltage across a battery to decrease when applied different current loads. It also shows us proof of the battery aging over time and use through the decreasing maximum voltage capacity and the decreasing discharge time when at the same current load. 

There is also a "Battery Overheating" column which indicates if the temperature of the battery is reaching dangerous levels. As stated in "https://www.large.net/news/8nu43nc.html#:~:text=In%20most%20cases%2C%2045%20degrees,of%20the%20internal%20cell%20activities.", the upper limit of optimal performance for the batteries used in the dataset (two 18650 battery cells) is 45 degrees celsius. There is a simple Yer or No response which indicates if the battery is overheating by the end of the discharge cycle. This information is beneficial in maximizing the battery's lifespan. 

Figures 3.1, 3.2, and 3.3 as shown below give the main portions of the code present in "FinalQuestion3.py".

<p align="center">
<img width="323" alt="image" align="center" src="https://github.com/user-attachments/assets/64d1efdf-9703-4469-b958-a9d383df0a26" />
<p align="center">Figure 3.1: Code Segment For Finding Start And End Times For Each Cycle</p>
<p align="center">
<img width="416" alt="image" align="center" src="https://github.com/user-attachments/assets/646e53f0-df36-4859-99dd-b03b327ed21a" />
<p align="center">Figure 3.2: Code Segment For Calculating Overheating Temperature</p>
<p align="center">
<img width="298" alt="image" align="center" src="https://github.com/user-attachments/assets/7facde69-5097-4fa5-b393-7bada0c15d5c" />
<p align="center">Figure 3.3: Code Segment For Arranging Data Into Table Format</p>
</p>

Although Figures 3.1, 3.2, and 3.3 show the main portions of the code, it is highly recommended to visit the "FinalQuestion3.py" file for the full code and comments. 

# Tutorial/Walkthrough

Please visit the "Code Walkthrough.mp4" file within the git repo for a full video walkthrough of how to run the code and the resulting analysis. A short description is as follows.

For "FinalQuestion1.py", you have to run the file. Once you do, Figure 1 will appear on your screen showing you four plots of the first and last battery discharge cycles. These plots display battery voltage and load current over time. Once you run "FinalQuestion2.py", the Figure 1 for "FinalQuestion1.py" will also appear. After clicking out of it, you will see Figure 2 which shows load current and the rate of change of battery voltage over time. Once you run "FinalQuestion3.py", a print statement and table will appear within the terminal The print statement will tell you the total number of discharge cycles for the battery. The table will show you relevant information for the battery at each discharge cycle such as time it took to discharge and temperature. 

# Limitations
Most of the limitations encountered dealth with a lack of knowledge and expertise. For example, Figure 2 shows us the rate of change of the battery's voltage in relation to time. The graph shows this rate to be a constant 0. Although the math may be correct, the analysis I provided does not show any meaningful information. 

Also, I worked on this assignment on my own therefore the work load was much bigger than if I had other people to collaborate with. It is much easier to come up with insightful and unique ways of analyzing data when there is a diverse group of people working on it. 

# Future Work And Results
I believe that the current code provides a solid basis for analyzing the dataset provided. However, there needs to be future work in three aspects. One of these aspects is stated in the "Limitations" section and deals with finding a better was of analyzing the change in battery voltage over time. The second aspect deals with a predicting the behavior of the battery's voltage and discharge time when at different current loads. This can possibly be done using Peukert's Law. The final aspect is incorporating more of the dataset such as the sections which involve second life batteries and providing relevant comparison to of their performance to reglar batteries. 
