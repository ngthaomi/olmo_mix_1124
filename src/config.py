BRANDS = ["barclays", "lloyds", "natwest", "hsbc", "monzo", "revolut", "tsb", "santander", "starling", "nationwide"]

BANKING_CONTEXT = [
    "finance", "financial", "bank", "banking", "account", "savings", "current", "mortgage", "loan", "credit", "debit", "card",
    "app", "mobile", "online", "branch", "atm", "transfer", "fees", "overdraft", "service", "support"
]

NEGATIVE_CONTEXT = {
    "nationwide": ["global", "worldwide", "across the nation", "nationwide coverage"],
    "revolut": ["revolution", "revolutionary", "national revolution"],
    "barclays": ["barclays center", "barclays arena"],
    "lloyds": ["lloyds of london"],
    "natwest": [],
    "hsbc": [],
    "monzo": [],
    "tsb": [],
    "santander": [],
    "starling": ["starling bird", "starlings"],
    "nationwide": ["nationwide insurance"]
}