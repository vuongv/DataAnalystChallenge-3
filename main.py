import csv
import os

election_csv = os.path.join("..", 'C:\DataAnalyst\DataAnalystChallenge-3\Starter_Code (1)\Instructions\PyPoll\Resources', 'election_data.csv')

def find_total_vote():
    with open (election_csv) as csvfile:

        csvreader = csv.reader(csvfile, delimiter=",")

        header = next(csvreader)

        total_vote = sum(1 for row in csvreader)

    return total_vote

def find_distinct():
    with open (election_csv) as csvfile:

        csvreader = csv.reader(csvfile, delimiter=',')

        header = next(csvreader)

        distinct_values = set()

        for row in csvreader:
            distinct_values.add(str(row[2]))

        return distinct_values

def find_vote_per_candidate(distinct_values):
    with open (election_csv) as csvfile:

        csvreader = csv.reader(csvfile, delimiter=',')

        header = next(csvreader)

        candidate_votes = {}
       
        for row in csvreader:

            if row[2] in candidate_votes:

                candidate_votes[row[2]] += 1
                
            else:
                candidate_votes[row[2]] = 1
                
        return candidate_votes

def print_result(candidate_votes):
    total = find_total_vote()
    print("---------------------------")
    print("Total Vote: "+ str(total))
    print("---------------------------")
    for key in candidate_votes:
        percent = round(candidate_votes[key]*100/total,3)
        print(key + " has " + str(candidate_votes[key]) + " (" + str(percent) + "%)")
    print("---------------------------")
    max_vote = max(candidate_votes, key = candidate_votes.get)
    print("Winner: "+ max_vote)
    print("---------------------------")

# PyPoll
set1 = find_distinct()
set2 = find_vote_per_candidate(set1)
print_result(set2)

budget_csv = os.path.join("..", 'C:\DataAnalyst\DataAnalystChallenge-3\Starter_Code (1)\Instructions\PyBank\Resources', 'budget_data.csv')


def find_total_month():
    with open (budget_csv) as csvfile:

        csvreader = csv.reader(csvfile, delimiter=",")

        header = next(csvreader)

        total_month = sum(1 for row in csvreader)
    print("Total Months: " + str(total_month))
    return total_month


def find_total_money():
    with open (budget_csv) as csvfile:

        csvreader = csv.reader(csvfile, delimiter=',')

        header = next(csvreader)

        total_money = 0

        for row in csvreader:
            total_money += int(row[1])
        
        print("Total money: $" + str(total_money))
        return total_money

def average(money, month):
    print("Average Change: $" + str(money/month))

def min_money():
    with open( budget_csv) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        header = next(csvreader)

        min = 0
        name = ""
        for row in csvreader:
            if min > int(row[1]):
                min = int(row[1])
                name = row[0]
        print("Greatest Decrease: " + name + " $" + str(min))

def max_money():
    with open (budget_csv) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        header = next(csvreader)

        max = 0
        name = ""

        for row in csvreader:
            if max < int(row[1]):
                max = int(row[1])
                name = row[0]
        print("Greatest Increase: " + name + " $" +str(max))
    


print("Financial Analysis")
print("---------------------------")
month = find_total_month()
money = find_total_money()
average(money, month)
max_money()
min_money()

