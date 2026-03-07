import re
import json

def parse_receipt(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    date_match = re.search(r'Date:\s*(.+)', text, re.IGNORECASE)
    date = date_match.group(1).strip() if date_match else None

    item_pattern = r'^([A-Za-z\s]+?)\s+(\d+\.\d{2})\s*$'
    items = re.findall(item_pattern, text, re.MULTILINE)
    items_list = [{'name': name.strip(), 'price': float(price)} for name, price in items]

    total_match = re.search(r'Total:\s*(\d+\.\d{2})', text, re.IGNORECASE)
    total = float(total_match.group(1)) if total_match else None

    payment_match = re.search(r'Payment:\s*(.+)', text, re.IGNORECASE)
    payment = payment_match.group(1).strip() if payment_match else None

    receipt_data = {
        'date': date,
        'items': items_list,
        'total': total,
        'payment': payment
    }

    return receipt_data

if __name__ == '__main__':
    data = parse_receipt('raw.txt')
    print(json.dumps(data, indent=2, ensure_ascii=False))