import pandas as pd
import matplotlib.pyplot as plt
# Load Dataset
file_path = 'ipl_matches.csv'
df = pd.read_csv("ipl_matches.csv")

# Display all row and coloum Data Set
print('Display all rows of data Set')
print(df.head(30))

# Display of Coloum and data type of data set
print ('Display the info of data set')
print(df.info())

# Total matches
print('Total Matches:', len(df))
# Team wise wins

team_wins = df['Winner'].value_counts()
print('\nTeam Wins:\n', team_wins)
#display Most Team runs

team_runs = df.groupby('Team')['Team_Runs'].sum().sort_values(ascending=False)
print('\nTeam Wins:\n', team_runs)
# Display top bowlers & wicket Taker

bowler_stats=df.groupby('Best_Bowler')['Wickets_Taken'].sum().sort_values(ascending=False)
top_bowlers = bowler_stats.head()
print('Top Wikect taker :',top_bowlers)

# Display top Batters & most runs
Runs_stats =df.groupby('Top_Scorer')['Top_Score'].sum().sort_values(ascending=False)
top_baters = Runs_stats.head()
print('Most Runs :',top_baters)

# Check missing values in each column
missing_values = df.isnull().sum()
print(" Missing Values in each column:\n", missing_values)

# Example: Unique teams
unique_teams = df['Team'].unique()
print("\n Unique Teams:", unique_teams)

# Example: Unique venues
unique_venues = df['Venue'].unique()
print("\n Unique Venues:", unique_venues)
# Example: Unique top scorers
unique_scorers = df['Top_Scorer'].unique()
print("\n Unique Top Scorers:", unique_scorers)
# ------------------- 1 Most Wins by Team Pie chart ------------------
plt.figure(figsize=(6,6))
team_wins.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title("Most Wins by Teams")
plt.ylabel('')
plt.show()
 #------------------- 2 Most Wickets by Bowlers -------------------
plt.figure(figsize=(8,5))
plt.bar(bowler_stats.index,bowler_stats.values, color='skyblue')
plt.title("Most Wickets by Bowlers")
plt.xlabel("Bowlers")
plt.ylabel("Wickets Taken")
plt.xticks(rotation=45, ha='right')
# Show numbers on top of bars
for i, v in enumerate(bowler_stats.values):
 plt.text(i, v+0.1, str(v), ha='center')
plt.tight_layout()
plt.show()
# ------------------- 3 Most Runs by Players Bar Graph -------------------
plt.figure(figsize=(10,5))
plt.bar(Runs_stats.index,Runs_stats.values, color='purple')
plt.title("Most Runs by Players")
plt.xlabel("Players")
plt.ylabel("Total Runs")
plt.xticks(rotation=45, ha='right')
for i, v in enumerate(Runs_stats.values):
 plt.text(i, v+0.1, str(v), ha='center')
plt.tight_layout()
plt.show()