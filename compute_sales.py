"""
    Compute Sales.
    The program compute the total cost for all sales from the input JSON.
    The results will be print on a file named SalesResults.txt.
"""

import json
import sys
import time


def load_json(file_path):
    """Load JSON data from a file with error handling."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")
    return None


def compute_total_sales(price_catalogue, sales_record):
    """Compute the total sales cost based on the price catalogue."""
    total_sales = 0.0
    errors = []

    for sale in sales_record:
        try:
            product = sale.get("product")
            quantity = sale.get("quantity")

            err_missing = "Missing product name/quantity in sales record."
            err_not_found = f"Product '{product}' not found."

            if product is None or quantity is None:
                raise ValueError(err_missing)

            if product not in price_catalogue:
                raise KeyError(err_not_found)

            price = price_catalogue[product]
            total_sales += price * quantity

        except (ValueError, KeyError) as e:
            errors.append(str(e))

    return total_sales, errors


def save_results(total_sales, errors, elapsed_time):
    """Save results to a file."""
    result_lines = [
        "==== Sales Report ====",
        f"Total Sales Cost: ${total_sales:,.2f}",
        f"Processing Time: {elapsed_time:.4f} seconds",
        "\nErrors Encountered:"
    ]

    if errors:
        result_lines.extend(errors)
    else:
        result_lines.append("No errors found.")

    result_text = "\n".join(result_lines)

    # Print to console
    print(result_text)

    # Write to file
    with open("SalesResults.txt", "w", encoding="utf-8") as result_file:
        result_file.write(result_text)


def main():
    """Main function to execute the program."""
    script_name = "compute_sales.py"
    input_json1 = "priceCatalogue.json"
    input_json2 = "salesRecord.json"
    if len(sys.argv) != 3:
        err_usage = f"Usage: python {script_name} {input_json1} {input_json2}"
        print(err_usage)
        sys.exit(1)

    price_file, sales_file = sys.argv[1], sys.argv[2]

    # Load json
    price_catalogue = load_json(price_file)
    sales_record = load_json(sales_file)

    if not price_catalogue or not sales_record:
        print("Error: Could not process files due to previous errors.")
        sys.exit(1)

    start_time = time.time()

    # Compute total sales
    total_sales, errors = compute_total_sales(price_catalogue, sales_record)

    # Record execution time
    elapsed_time = time.time() - start_time

    # Save results
    save_results(total_sales, errors, elapsed_time)


if __name__ == "__main__":
    main()
