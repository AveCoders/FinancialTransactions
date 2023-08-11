import argparse
from collections import defaultdict
from dataclasses import dataclass, fields
from csv import DictReader
from statistics import mean
from typing import Dict, List

@dataclass
class Transaction:
    transactionId: str
    accountId: str
    transactionDay: int
    category: str
    transactionAmount: float

def load_transactions(file_path: str) -> List[Transaction]:
    """
    Load transactions from a given file and return a list of Transaction objects.
    
    Args:
    - file_path (str): Path to the file containing transaction data.
    
    Returns:
    - List[Transaction]: List of Transaction objects.
    """
    with open(file_path) as csv_file:
        return [
            Transaction(**{
                field.name: field.type(row[field.name])
                for field in fields(Transaction)
            }) for row in DictReader(csv_file)
        ]

def question_one(transactions: List[Transaction]) -> None:
    """
    Calculate and print the total transaction value for all transactions performed each day.
    
    Args:
    - transactions (List[Transaction]): List of Transaction objects.
    """
    # Use a defaultdict to accumulate transaction amounts for each day.
    day_totals = defaultdict(float)
    
    # For each transaction, add the transaction amount to the day in the defaultdict.
    for xact in transactions:
        day_totals[xact.transactionDay] += xact.transactionAmount
    
    # Print the accumulated totals for each day.
    for day, total in day_totals.items():
        print(f'Day {day} brought {total:.2f} in total')


def question_two(transactions: List[Transaction]) -> None:
    """
    Calculate and print the average value of transactions per account for each type of transaction.
    
    Args:
    - transactions (List[Transaction]): List of Transaction objects.
    """
    # Use a defaultdict where each account ID maps to another defaultdict. 
    # The inner defaultdict maps categories to lists of transaction amounts.
    acct_cat_totals = defaultdict(lambda: defaultdict(list))
    
    # For each transaction, store the transaction amount for its account and category in the nested defaultdict.
    for xact in transactions:
        acct_cat_totals[xact.accountId][xact.category].append(xact.transactionAmount)
    
    # Calculate and print the average transaction amount for each account and category.
    for acct, cat_totals in acct_cat_totals.items():
        print(f'Account: {acct}\tAverage per category:')
        for cat, amounts in cat_totals.items():
            print(f'{cat}: {mean(amounts):.2f}\t', end='')
        print()


def question_three(transactions: List[Transaction], day: int, window_size: int = 5) -> None:
    """
    For a given day and window size, calculate and print statistics for each account for transactions over the previous days.
    The statistics include maximum transaction value, average transaction value, and total transaction value for specific types.
    
    Args:
    - transactions (List[Transaction]): List of Transaction objects.
    - day (int): Day for which statistics are to be calculated.
    - window_size (int): Number of previous days to consider for statistics.
    """
    # Filter transactions to only include those within the desired window of days.
    filtered_transactions = [
        xact for xact in transactions if day - window_size <= xact.transactionDay < day
    ]
    
    # Use a defaultdict to accumulate transaction amounts and totals for specified categories by account.
    acct_stats = defaultdict(lambda: {"amounts": [], "specified_types": 0})
    specified_categories = ["AA", "CC", "FF"]
    
    # For each transaction in the filtered list, accumulate amounts and totals for the specified categories.
    for xact in filtered_transactions:
        acct_stats[xact.accountId]["amounts"].append(xact.transactionAmount)
        if xact.category in specified_categories:
            acct_stats[xact.accountId]["specified_types"] += xact.transactionAmount
            
    # Compute and print the desired statistics for each account.
    for acct, stats in acct_stats.items():
        max_val = max(stats["amounts"]) if stats["amounts"] else 0
        avg_val = mean(stats["amounts"]) if stats["amounts"] else 0
        total_specified = stats["specified_types"]
        print(
            f'Account: {acct}\t'
            f'Max Value (Last {window_size} Days): {max_val:.2f}\t'
            f'Average Value (Last {window_size} Days): {avg_val:.2f}\t'
            f'Total for AA, CC, FF (Last {window_size} Days): {total_specified:.2f}'
        )


# Load the transactions from the provided file
transactions = load_transactions("./transactions.txt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process transaction data.')
    parser.add_argument('file_path', type=str, help='Path to the transaction data file.')
    parser.add_argument('--question', type=int, choices=[1, 2, 3], required=True, help='Which question to answer.')
    parser.add_argument('--day', type=int, help='The day for question 3.')
    parser.add_argument('--window_size', type=int, default=5, help='The window size for question 3.')
    args = parser.parse_args()

    transactions = load_transactions(args.file_path)

    if args.question == 1:
        question_one(transactions)
    elif args.question == 2:
        question_two(transactions)
    elif args.question == 3:
        if args.day is None:
            raise ValueError('The --day argument is required for question 3.')
        question_three(transactions, args.day, args.window_size)