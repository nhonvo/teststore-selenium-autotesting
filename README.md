# Automated Testing Project with Python and Selenium WebDriver

## Project Overview:

The goal of this project is to perform automated testing on the website [https://teststore.automationtesting.co.uk/

## Feature of website:

1. **User Authentication:**
   - Allows users to log in and log out.
   - Test cases verify the correctness of the login and logout processes.
2. **Product Search:**
   - Enables users to search for products using keywords in the search bar.
   - Testing ensures accurate search results with complete product information.
3. **Add to Cart:**
   - Allows users to add products to the shopping cart from the product details page.
   - Testing confirms that the quantity in the cart increases after adding a product and displays accurate product information.
4. **Sort and Filter Products:**
   - Permits users to sort the product list by criteria such as name, price, and filter products by category.
   - Testing ensures the correct sorting and filtering of the product list.
5. **Apply Promotional Code:**
   - Lets users apply promotional codes to receive discounts on their orders.
   - Testing validates that the price is correct after applying the promotional code.
6. **View Product Details and Add to Cart:**
   - Allows users to view detailed product information and add products to the cart from the product details page.
   - Testing confirms that product details and cart quantity are updated correctly after adding to the cart.

## All test case

1. **Login and Logout Functionality:**
   - Verify successful login and logout process.
2. **Product Search Functionality:**
   - Verify the ability to search for products.
3. **Filter Products by Increasing Price:**
   - Verify the functionality to filter products by ascending price.
4. **Search with No Results:**
   - Verify behavior when there are no search results.
5. **Filter Products Functionality:**
   - Verify the ability to filter products.
6. **Filter "Home Accessories" Product Type:**
   - Verify filtering products by the "Home Accessories" category.
7. **Filter and Sort "Home Accessories" Products:**
   - Verify filtering and sorting "Home Accessories" products.
8. **Filter Men's Products:**
   - Verify filtering products for Men's category.
9. **Filter Reset Functionality:**
   - Verify the functionality of resetting all filters.
10. **Quickview and Add to Cart for 1 Product:**
    - Verify quickview and adding one product to the cart.
11. **Quickview and Add to Cart with Random Quantity:**
    - Verify quickview and adding a product to the cart with a random quantity.
12. **Shopping Functionality with Quickview:**
    - Verify the shopping process with the use of quickview.
13. **Remove Product from Cart:**
    - Verify the functionality of removing a product from the cart.
14. **Discount Feature in the Cart:**
    - Verify the discount feature in the shopping cart.
15. **Accuracy of Discount Amount in Reduced Product:**
    - Verify the correct display of the discount amount in discounted products.
16. **Order Placement Process:**
    - Verify the order placement process.
17. **Saving Old Orders and Adding a Product:**
    - Verify saving old orders and adding a new product.
18. **User Information Modification Functionality:**
    - Verify the ability to change user information.
19. **User Address Modification Functionality:**
    - Verify the ability to change user address.
20. **User Address Creation Functionality:**
    - Verify the ability to create a new user address.
21. **Website Navigation Functionality:**
    - Verify the functionality of navigating the website.
22. **Display of Products on the Page:**
    - Verify the correct display of products on the page.
23. **Contact Functionality:**
    - Verify the contact functionality on the website.
24. **Shopping and Payment Functionality:**
    - Verify the shopping and payment process.
25. **Order Placement After Login, Product Selection, and Multiple Conditions:**
    - Verify order placement after login, selecting products, and applying multiple conditions.
26. **Order Placement with Discounted Product and Login:**
    - Verify order placement with a discounted product and after logging in.
27. **Search and Add Product to Cart Functionality:**
    - Verify the ability to search and add a product to the cart.
28. **Add Product to Cart and Place Order Functionality:**
    - Verify the ability to add a product to the cart and place an order.

## Installation Guide:

### Install pip:

- Ensure Python is installed (version 3.4 or above).
- Confirm pip installation:

```bash
pip --version
```

### Set Up Virtual Environment (Optional):

- Navigate to your project directory.
- Create a virtual environment base on `env.example`

### Install Dependencies:

- Install project dependencies:

```bash
pip install -r requirements.txt
```

### Run Test Cases:

- Execute your test cases:

```bash
python testcase_name.py
```
