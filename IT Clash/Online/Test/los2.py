import random

bill_names = {
    "M-": [
        "Chicken Meat Bulk", "Cooking Oil", "Flour Bags", "Napkins", "Disposable Gloves",
        "Packaging Boxes", "Sauce Bottles", "Cleaning Detergent", "Paper Towels", "Plastic Utensils",
        "Rice Sacks", "Frozen Wings", "Burger Buns", "Pickles", "Salt and Pepper",
        "Gravy Mix", "Coleslaw Mix", "Cup Lids", "Soup Containers", "Seasoning Packets"
    ],
    "W-": [
        "Monthly Water Bill", "Kitchen Sink Usage", "Toilet Maintenance", "Ice Machine Supply", "Steam Cleaning Water",
        "Water Dispenser Refills", "Drinking Water Gallons", "Dishwasher Water", "Mop Refill Water", "Cleaning Tap",
        "Sanitizer Mix Water", "Bathroom Cleaning Water", "Cooler Water Supply", "External Pipe Repair", "Leakage Fix",
        "Water Heater Service", "Wet Area Maintenance", "Basement Drain", "Garden Hose Use", "Tank Top Up"
    ],
    "E-": [
        "Monthly Electricity Bill", "Freezer Maintenance", "Light Bulb Replacement", "Air Conditioner Usage", "Electric Fryer Power",
        "POS Machine Power", "Refrigerator Power", "Exhaust Fan Power", "Oven Electricity", "Hot Plate Usage",
        "Heater Replacement", "Electric Kettle", "Food Warmer", "Outlet Repair", "Walk-in Cooler",
        "CCTV Electricity", "Electric Signboard", "Kitchen Hood", "Voltage Stabilizer", "Back-up Generator"
    ],
    "S-": [
        "Cashier Salary", "Cook Salary", "Manager Salary", "Waiter Salary", "Delivery Staff Pay",
        "Cleaner Pay", "Part-Time Helper", "Accountant Fee", "Shift Leader Bonus", "Chef Salary",
        "Night Shift Allowance", "Overtime Pay", "Staff Incentive", "Kitchen Porter Pay", "Assistant Chef Salary",
        "Trainee Allowance", "Maintenance Staff Pay", "Supervisor Salary", "Receptionist Bonus", "Driver Pay"
    ],
    "T-": [
        "Monthly VAT", "Sales Tax", "Service Tax", "Property Tax", "Import Tax",
        "Income Tax", "Municipal Tax", "State Tax", "Central Tax", "Tax Penalty",
        "Restaurant Levy", "Tax Adjustment", "Withholding Tax", "Corporate Tax", "Digital Tax",
        "Packaging Tax", "Luxury Tax", "Turnover Tax", "Environmental Tax", "Stamp Duty"
    ],
    "I/O-": [
        "Chicken Combo Sale", "Beverage Sales", "Delivery Order Income", "Walk-in Customer", "Franchise Royalty",
        "Online Order", "Special Menu Sale", "Bulk Order", "Weekend Promotion", "Membership Income",
        "Event Catering", "Birthday Package", "Dine-in Income", "Food App Income", "Lunch Rush Sale",
        "Late Night Order", "Family Pack Sale", "Loyalty Program", "New Year Boost", "Catering Service Payment"
    ]
}

def random_date():
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    year = random.randint(2020, 2025)
    return f"{day:02d}/{month:02d}/{year}"

def generate_test():
    bill_type = random.choice(list(bill_names.keys()))
    name = random.choice(bill_names[bill_type])
    date = random_date()
    price = round(random.uniform(10.00, 1000000.00), 2)
    mark = "-+"
    sign = mark[random.randint(0, 1)]
    label_map = {
    "M-": "M-Material",
    "W-": "W-Water",
    "E-": "E-Electricity",
    "S-": "S-Salary",
    "T-": "T-Tax",
    "I/O-": "I/O-Income/Outcome"
    }
    return f"{label_map[bill_type]}: {name} {date} {sign}{price}"

def generate_full_testcase(num_cases=5):
    all_cases = []
    for _ in range(num_cases):
        num_bills = random.randint(1, 100)
        bills = [str(num_bills)]
        for _ in range(num_bills):
            bills.append(generate_test())
        all_cases.append(bills)
    return all_cases

generated_cases = generate_full_testcase(50)

for i in range(len(generated_cases)):
    print("Testcase number:", i + 1)
    for j in generated_cases[i]:
        print(j)
    print("\n")
