vegetable = ["arugula", "kale", "red bell pepper", "baby leaf lettuce", "broccoli"]

vegetable_pricing = [3.49, 2.99, 3.79, 2.49, 3.99]

after_tax_amount = 0.00

zipped_complete_vegetable_list = zip(vegetable, vegetable_pricing)
complete_vegetable_list = list(zipped_complete_vegetable_list)

print(complete_vegetable_list)

for item in vegetable:
    if item == "arugula":
        print("\nArugula is a cruciferous vegetable.\n")
    elif item == "kale":
        print("Kale is a cruciferous vegetable.\n")
    elif item == "broccoli":
        print("Broccoli is a cruciferous vegetable.\n")
    else:
        print("This vegetable is not cruciferous.\n")

print("All of the cruciferous vegetables have been listed.\n")

print("The non-cruciferous vegetables are: " + vegetable[2].title() +  " and " + vegetable[3].title())
print("\nThe total quantity of all vegetables is: " + str(len(vegetable)))

print("\nThe subtotal for the list of vegetables is $" + str(sum(vegetable_pricing)))

sales_tax = .1025
total_sales_tax = sales_tax * sum(vegetable_pricing)
after_tax_amount += sum(vegetable_pricing) + total_sales_tax

print("The total amount of the vegetables' pricing after tax is: $" + str((after_tax_amount)))


