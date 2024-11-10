# Testing

Return back to the [README.md](README.md) file.

![Main Image](docs/images/main.png)

# Contents

<!-- TOC -->

* [Testing](#testing)
* [Contents](#contents)
    * [Responsiveness Tests](#responsiveness-tests)
    * [Code Validation](#code-validation)
        * [HTML](#html)
        * [CSS](#css)
        * [JavaScript](#javascript)
        * [Python](#python)
    * [Manual Testing](#manual-testing)
    * [**PRODUCT CATALOG**](#product-catalog)
    * [**MEAL PLANS**](#meal-plans)
    * [**SHOPPING CART**](#shopping-cart)
    * [**CHECKOUT**](#checkout)
    * [**USER PROFILE**](#user-profile)
    * [**ADMIN DASHBOARD**](#admin-dashboard)
    * [**SPECIAL FEATURES**](#special-features)
    * [Role-based Restrictions](#role-based-restrictions)
    * [Bugs](#bugs)
    * [Browser Compatibility](#browser-compatibility)
    * [User Story Testing](#user-story-testing)
    * [Dev Role User Stories](#dev-role-user-stories)
    * [Visitor User Stories](#visitor-user-stories)
    * [Customer User Stories](#customer-user-stories)
    * [Admin User Stories](#admin-user-stories)
    * [Epic: Product Management](#epic-product-management)
    * [Epic: Order Management](#epic-order-management)
    * [Epic: Customer Service](#epic-customer-service)
        * [Product Management](#product-management)
        * [Customer Features](#customer-features)
        * [Admin Dashboard](#admin-dashboard-1)
    * [Lighthouse Testing](#lighthouse-testing)
    * [Accessibility Testing](#accessibility-testing)

<!-- TOC -->

## Responsiveness Tests

I adopted a mobile-first strategy and verified all modifications using the DevTools in Google Chrome and Microsoft Edge.

Additionally, I used
the [Google Chrome Mobile Simulator extension](https://chromewebstore.google.com/detail/mobile-simulator-responsi/ckejmhbmlajgoklhgbapkiccekfoccmk)
to evaluate responsiveness on more specialized
devices. I examined device samples for navigation, element alignment, content layout, and functionality issues across
different breakpoints.

Test Results:

| Size | Device Example     | Navigation | Element Alignments | Content Placement | Functionality | Notes |
|------|--------------------|------------|--------------------|-------------------|---------------|-------|
| sm   | Samsung Galaxy S20 | ☑️         | ☑️                 | ☑️                | ☑️            |       |
| sm   | iPhone 11 PRO      | ☑️         | ☑️                 | ☑️                | ☑️            |       |
| sm   | iPhone 13 PRO MAX  | ☑️         | ☑️                 | ☑️                | ☑️            |       |
| md   | iPad MINI          | ☑️         | ☑️                 | ☑️                | ☑️            |       |
| md   | Galaxy Tab S7      | ☑️         | ☑️                 | ☑️                | ☑️            |       |
| md   | iPad Air           | ☑️         | ☑️                 | ☑️                | ☑️            |       |
| lg   | iPad Pro           | ☑️         | ☑️                 | ☑️                | ☑️            |       |
| xl   | Mackbook Air       | ☑️         | ☑️                 | ☑️                | ☑️            |       |
| xl   | HP Stream Laptop   | ☑️         | ☑️                 | ☑️                | ☑️            |       |
| xxl  | Dell Lattitude     | ☑️         | ☑️                 | ☑️                | ☑️            |       |
| xxl  | Desktop            | ☑️         | ☑️                 | ☑️                | ☑️            |       |

[Back to top](#contents) :top:

## Code Validation

### HTML

The recommended [HTML W3C Validator](https://validator.w3.org) to validate all the project's HTML files.

This is the process which was followed of validating an HTML file by direct input:

1. **Access the Validator**: Visit the [W3C Markup Validation Service](https://validator.w3.org/).
2. **Choose Direct Input**: Select the "Validate by Direct Input" tab.
3. **Paste Your HTML Code**: Copy HTML code and paste it into the text box.
4. **Validate**: Click the "Check" button to validate HTML.

<details>

<summary>HTML Validation Results</summary>

| File Name                   | Pass | Notes             | View Result                                                    |
|-----------------------------|------|-------------------|----------------------------------------------------------------|
| home page desktop           | ☑️   |                   | ![Result](docs/test-img/home-page-desktop-html.png)            |
| home page mobile            | ☑️   |                   | ![Result](docs/test-img/home-page-mobile-html.png)             |
| products page desktop       | ☑️   |                   | ![Result](/docs/test-img/product-page-desktop-html.png)        |
| products page mobile        | ☑️   |                   | ![Result](/docs/test-img/product-page-mobile-html.png)         |       
| blog page desktop           | ☑️   |                   | ![Result](/docs/test-img/blog-page-desktop-html.png)           |       
| blog page mobile            | ☑️   |                   | ![Result](/docs/test-img/blog-page-mobile-html.png)            |       
| blog post page desktop      | ☑️   |                   | ![Result](/docs/test-img/blog-post-page-desktop-html.png)      |       
| blog post page mobile       | ☑️   |                   | ![Result](/docs/test-img/blog-post-page-mobile-html.png)       |       
| contact page desktop        | ☑️   |                   | ![Result](/docs/test-img/contact-page-desktop-html.png)        |       
| contact page mobile         | ☑️   |                   | ![Result](/docs/test-img/contact-page-mobile-html.png)         |       
| privacy policy page desktop | ☑️   |                   | ![Result](/docs/test-img/privacy-policy-page-desktop-html.png) |       
| privacy policy page mobile  | ☑️   |                   | ![Result](/docs/test-img/privacy-policy-page-mobile-html.png)  |       
| return policy page desktop  | ☑️   |                   | ![Result](/docs/test-img/return-policy-page-desktop-html.png)  |
| return policy page mobile   | ☑️   |                   | ![Result](/docs/test-img/return-policy-page-mobile-html.png)   |       
| cart page desktop           | ☑️   |                   | ![Result](/docs/test-img/cart-page-desktop-html.png)           |       
| cart page mobile            | ☑️   |                   | ![Result](/docs/test-img/cart-page-mobile-html.png)            |       
| profile page desktop        | ☑️   | From crispy forms | ![Result](/docs/test-img/profile-page-desktop-html.png)        |       
| profile page mobile         | ☑️   | From crispy forms | ![Result](/docs/test-img/profile-page-mobile-html.png)         |       
| favorites page desktop      | ☑️   |                   | ![Result](/docs/test-img/favorites-page-desktop-html.png)      |       
| favorites page mobile       | ☑️   |                   | ![Result](/docs/test-img/favorites-page-mobile-html.png)       |       |
| logout page desktop         | ☑️   |                   | ![Result](/docs/test-img/logout-page-desktop-html.png)         |       
| logout page mobile          | ☑️   |                   | ![Result](/docs/test-img/logout-page-mobile-html.png)          |       
| register page desktop       | ☑️   |                   | ![Result](/docs/test-img/register-page-desktop-html.png)       |       
| register page mobile        | ☑️   |                   | ![Result](/docs/test-img/register-page-desktop-html.png)       |       
| login page desktop          | ☑️   |                   | ![Result](/docs/test-img/login-page-desktop-html.png)          |       
| login page mobile           | ☑️   |                   | ![Result](/docs/test-img/login-page-mobile-html.png)           |       

</details>

[Back to top](#contents) :top:

### CSS

The [W3C Jigsaw](https://jigsaw.w3.org/css-validator/) tool, provided by the W3C, enables to validate and verify the
correctness of CSS code. It ensures that your web pages adhere to W3C standards, promoting interoperability and
accessibility.

<details>

<summary>CSS Validation Results</summary>

| File Name     | Pass | View Result                                                |
|---------------|------|------------------------------------------------------------|
| base.css      | ☑️   | ![Result](docs/test-img/base-file-validation-css.png)      |
| favorites.css | ☑️   | ![Result](/docs/test-img/favorites-file-validaton-css.png) |
| checkout.css  | ☑️   | ![Result](/docs/test-img/checkout-file-validation-css.png) |

</details>

### JavaScript

No major errors were found when validating JavaScript through [Jshint](https://jshint.com/).


<details>

<summary>JavaScript Validation Results</summary>

| File Name    | Pass | View Result                                                  |
|--------------|------|--------------------------------------------------------------|
| countryfield | ☑️   | ![Result](docs/test-img/countryfield-file-validation-js.png) |
| blog         | ☑️   | ![Result](/docs/test-img/blog-file-validaton-js.png)         |

</details>

### Python

The python files have all been passed through [PEP8 CI Online](https://pep8ci.herokuapp.com/)

<details><summary><b>PEP8 Test Results</b></summary>

| App Name  | File Name          | Pass | Notes | View Result                                                                                               |
|-----------|--------------------|------|-------|-----------------------------------------------------------------------------------------------------------|
| about     | views.py           | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/about-views-py.png)</details>              |
| about     | urls.py            | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/about-urls-py.png)</details>               |
| about     | models.py          | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/about-models-py.png)</details>             |
| about     | forms.py           | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/about-forms-py.png)</details>              |
| about     | admin.py           | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/about-admin-py.png)</details>              |
| about     | test_views.py      | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/about-test-viewers-py.png)</details>       |
| about     | test_forms.py      | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/about-test-forms-py.png)</details>         |
| app       | settings.py        | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/settings-py.png)</details>                 |
| app       | urls.py            | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/testing-urls-py-main-app.png)</details>    |
| app       | views.py           | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/views-py-main-app.png)</details>           |
| blog      | views.py           | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/blog-views-py.png)</details>               |
| blog      | urls.py            | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/blog-urls-py.png)</details>                |
| blog      | models.py          | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/blog-models-py.png)</details>              |
| blog      | forms.py           | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/blog-forms-py.png)</details>               |
| blog      | admin.py           | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/blog-admin-py.png)</details>               |
| blog      | test_views.py      | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/blog-test-views-py.png)</details>          |
| blog      | test_models.py     | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/blog-test-models-py.png)</details>         |
| cart      | views.py           | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/cart-views-py.png)</details>               |
| cart      | urls.py            | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/cart-urls-py.png)</details>                |
| cart      | contexts.py        | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/cart-context-py.png)</details>             |
| cart      | test_context.py    | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/cart-test-contest-py.png)</details>        |
| checkout  | webhooks.py        | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkout-webhooks-py.png)</details>        |
| checkout  | webhook_handler.py | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkout-webhook-handler-py.png)</details> |
| checkout  | views.py           | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkaout-views.png)</details>             |
| checkout  | urls.py            | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkout-urls-py.png)</details>            |
| checkout  | signals.py         | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkout-signals-py.png)</details>         |
| checkout  | models.py          | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkout-models-py.png)</details>          |
| checkout  | forms.py           | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkout-forms-py.png)</details>           |
| checkout  | admin.py           | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkout-admin-py.png)</details>           |
| checkout  | test_models.py     | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkout-test-models-py.png)</details>     |
| checkout  | test_forms.py      | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkout-test-forms-py.png)</details>      |
| favorites | views.py           | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/favorites-views-py.png)</details>          |
| favorites | urls.py            | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/favorites-urls-py.png)</details>           |
| favorites | models.py          | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/favorites-models-py.png)</details>         |
| favorites | admin.py           | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/favorites-admin-py.png)</details>          |
| favorites | test_models.py     | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/favorites-test-models-py.png)</details>    |
| home      | views.py           | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/home-views-py.png)</details>               |
| home      | urls.py            | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/home-urls-py.png)</details>                |
| products  | widgets.py         | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/products-widgets-py.png)</details>         |
| products  | views.py           | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/products-views-py.png)</details>           |
| products  | urls.py            | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/products-urls-py.png)</details>            |
| products  | models.py          | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/products-models-py.png)</details>          |
| products  | forms.py           | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/products-forms-py.png)</details>           |
| products  | admin.py           | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/products-admin-py.png)</details>           |
| products  | test_views.py      | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/products-test-views-py.png)</details>      |
| products  | test_models.py     | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/productstest-models-py.png)</details>      |
| products  | test_forms.py      | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/products-test-forms-py.png)</details>      |
| profiles  | views.py           | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/profiles-views-py.png)</details>           |
| profiles  | urls.py            | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/profiles-urls-py.png)</details>            |
| profiles  | models.py          | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/profiles-models-py.png)</details>          |
| profiles  | forms.py           | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/profiles-forms-py.png)</details>           |
| profiles  | test_forms.py      | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/profiles-test-forms.png)</details>         |
| main      | custom_storages.py | ☑️   |       | <details><summary>Screenshot</summary>![Result](/docs/test-img/main-custom-storages.png)</details>        |

</details><br/>

[Back to top](#contents) :top:

## Manual Testing

In addition to using `unittest`, extensive manual testing was performed on the application. Each feature was verified
against success criteria. Where applicable, negative testing was conducted by providing invalid or unexpected inputs to
assess the application's robustness in handling errors and exceptions.

<details>
<summary>Manual Testing Results</summary>:white_chec k_mark:
## **AUTHENTICATION**

| Test Case                       | Element                                    | Action                               | Expected Outcome                                        | Result |
|---------------------------------|--------------------------------------------|--------------------------------------|---------------------------------------------------------|--------|
| Register with Valid Credentials | Registration form fields (email, password) | Fill out form with valid credentials | User redirected to home page, welcome message displayed | ☑️     |
| Register with Existing Email    | Registration form                          | Use existing email address           | Error message "Email already exists" shown              | ☑️     |
| Login with Valid Credentials    | Login form                                 | Enter valid email/password           | Successfully logged in, redirected to home              | ☑️     |
| Login with Invalid Credentials  | Login form                                 | Enter incorrect password             | Error message shown, remains on login page              | ☑️     |
| Password Reset                  | Reset form                                 | Request password reset               | Reset email sent to user                                | ☑️     |
| Logout                          | Logout button                              | Click logout                         | User logged out, session ended                          | ☑️     |

## **PRODUCT CATALOG**

| Test Case            | Element          | Action                    | Expected Outcome                   | Result |
|----------------------|------------------|---------------------------|------------------------------------|--------|
| Filter by Category   | Category filters | Select "Organic Produce"  | Shows only organic produce items   | ☑️     |
| Filter by Diet Type  | Diet filters     | Select "Vegan"            | Shows only vegan products          | ☑️     |
| Sort by Price        | Sort dropdown    | Select "Price Low-High"   | Products sorted by ascending price | ☑️     |
| Search Products      | Search bar       | Search "organic juice"    | Relevant juice products displayed  | ☑️     |
| View Product Details | Product card     | Click product image       | Shows detailed product information | ☑️     |
| Check Stock Status   | Stock indicator  | View product availability | Shows in/out of stock status       | ☑️     |

## **MEAL PLANS**

| Test Case                | Element            | Action                     | Expected Outcome                     | Result |
|--------------------------|--------------------|----------------------------|--------------------------------------|--------|
| Browse Meal Plans        | Meal plan section  | View available plans       | Shows different meal plan options    | ☑️     |
| Customize Plan           | Plan customization | Select dietary preferences | Plan adjusted to preferences         | ☑️     |
| Select Delivery Schedule | Schedule selector  | Choose delivery frequency  | Schedule confirmed                   | ☑️     |
| View Meal Contents       | Meal details       | Click meal preview         | Shows ingredients and nutrition info | ☑️     |

## **SHOPPING CART**

| Test Case           | Element           | Action                   | Expected Outcome            | Result |
|---------------------|-------------------|--------------------------|-----------------------------|--------|
| Add to Cart         | Add button        | Click "Add to Cart"      | Product added, cart updated | ☑️     |
| Update Quantity     | Quantity selector | Change product quantity  | Quantity and total updated  | ☑️     |
| Remove Item         | Remove button     | Remove product from cart | Item removed, total updated | ☑️     |
| Apply Coupon        | Coupon field      | Enter valid code         | Discount applied to total   | ☑️     |
| Check Minimum Order | Cart total        | Add items below minimum  | Warning message shown       | ☑️     |

## **CHECKOUT**

| Test Case              | Element           | Action                 | Expected Outcome               | Result |
|------------------------|-------------------|------------------------|--------------------------------|--------|
| Enter Delivery Address | Address form      | Input delivery details | Address validated and saved    | ☑️     |
| Select Delivery Time   | Time slots        | Choose delivery window | Time slot reserved             | ☑️     |
| Payment Processing     | Payment form      | Enter payment details  | Payment processed successfully | ☑️     |
| Order Confirmation     | Confirmation page | Complete checkout      | Order confirmed, email sent    | ☑️     |

## **USER PROFILE**

| Test Case            | Element            | Action                        | Expected Outcome         | Result |
|----------------------|--------------------|-------------------------------|--------------------------|--------|
| View Order History   | Orders section     | Check past orders             | Shows order history      | ☑️     |
| Save Preferences     | Preferences form   | Update dietary preferences    | Preferences saved        | ☑️     |
| Manage Subscriptions | Subscription panel | Modify meal plan subscription | Changes saved            | ☑️     |
| Update Payment Info  | Payment settings   | Update payment method         | New payment method saved | ☑️     |

## **ADMIN DASHBOARD**

| Test Case        | Element          | Action                  | Expected Outcome            | Result |
|------------------|------------------|-------------------------|-----------------------------|--------|
| Manage Inventory | Inventory panel  | Update stock levels     | Stock counts updated        | ☑️     |
| Process Orders   | Order management | View and process orders | Orders properly fulfilled   | ☑️     |
| Update Products  | Product editor   | Edit product details    | Changes saved and displayed | ☑️     |
| Manage Users     | User management  | View user accounts      | Access to user information  | ☑️     |

## **SPECIAL FEATURES**

| Test Case            | Element            | Action                     | Expected Outcome           | Result |
|----------------------|--------------------|----------------------------|----------------------------|--------|
| Nutrition Calculator | Calculator tool    | Enter meal selections      | Shows nutritional totals   | ☑️     |
| Recipe Suggestions   | Recipe section     | View recommended recipes   | Relevant recipes shown     | ☑️     |
| Seasonal Products    | Seasonal filter    | View seasonal items        | Current season items shown | ☑️     |
| Subscription Savings | Savings calculator | View subscription benefits | Shows price comparisons    | ☑️     |

## Role-based Restrictions

| Admin Access              | Test Pass |
|---------------------------|-----------|
| Full inventory management | ☑️        |
| Order processing          | ☑️        |
| User management           | ☑️        |
| Content management        | ☑️        |

| Registered User Access  | Test Pass |
|-------------------------|-----------|
| Place orders            | ☑️        |
| Manage profile          | ☑️        |
| View order history      | ☑️        |
| Subscribe to meal plans | ☑️        |

| Guest Access     | Test Pass |
|------------------|-----------|
| Browse products  | ☑️        |
| View public info | ☑️        |
| Create account   | ☑️        |

This test documentation covers the core functionality of an organic food marketplace. You can expand or modify these
test cases based on your specific features and requirements.

</details>

[Back to top](#contents) :top:

## Bugs

| Bug                           | Status |
|-------------------------------|--------|
| Not correct rating view       | ☑️     |
| Category search does not work | ☑️     |
| Bad Request (400)             | ☑️     |
| Herroku Error 500             | ️️ ☑️  |
| immortal loader               | ☑️     |

[Back to top](#contents) :top:

## Browser Compatibility

The deployed project was tested on the most popular browsers for compatibility issues.
No major issues identified.

<table>
    <thead>    
        <tr> 
            <th rowspan="2">Page</th> 
            <th colspan="5">Mobile</th> 
            <th colspan="5">Tablet</th> 
            <th colspan="5">Desktop</th> 
            <th rowspan="2">Note</th> 
        </tr>
        <tr> 
            <th>Edge</th>
            <th>Firefox</th>
            <th>Chrome</th>
            <th>Opera</th>
            <th>Safari</th>
            <th>Edge</th>
            <th>Firefox</th>
            <th>Chrome</th>
            <th>Opera</th>
            <th>Safari</th>
            <th>Edge</th>
            <th>Firefox</th>
            <th>Chrome</th>
            <th>Opera</th>
            <th>Safari</th>
        </tr>
    </thead>
    <tbody>    
        <tr>
            <td>Home</td>
            <td>☑️</td> 
            <td>☑️</td> 
            <td>☑️</td> 
            <td>☑️</td> 
            <td>❌</td> 
            <td>☑️</td> 
            <td>☑️</td> 
            <td>☑️</td> 
            <td>☑️</td> 
            <td>❌</td>
            <td>☑️</td> 
            <td>☑️</td> 
            <td>☑️</td> 
            <td>☑️</td> 
            <td>❌</td> 
            <td>Test issue on Safari</td>
        </tr>
        <tr>
            <td>Contact</td >
            <td>☑️</td> 
            <td>☑️</td> 
            <td>☑️</td> 
            <td>❌</td> 
            <td>☑️</td> 
            <td>☑️</td> 
            <td>☑️</td> 
            <td>☑️</td> 
            <td>☑️</td> 
            <td>☑️</td>
            <td>☑️</td> 
            <td>☑️</td>
            <td>❌</td> 
             <td>☑️</td> 
            <td>☑️</td> 
            <td>Issue on Opera in Tablet</td>
        </tr>
    </tbody>
</table>

[Browser Testing Results]()

## User Story Testing

## Dev Role User Stories

| User Story               | Status | Notes                                  |
|--------------------------|--------|----------------------------------------|
| Adopt Agile Methodology  | ☑️     | Documented in README.md                |
| Design Database Schema   | ☑️     | ERD and schema documented in README.md |
| Create Wireframes        | ☑️     | Balsamiq wireframes in README.md       |
| Design Visuals           | ☑️     | Color scheme and typography documented |
| Create Django Project    | ☑️     | Git Commit #d469c28                    |
| AWS Integration          | ☑️     | Static/media files configuration       |
| Performance Optimization | ☑️     | Documented in TESTING.md               |
| Code Validation          | ☑️     | Python, JS, CSS validation results     |
| SEO Implementation       | ☑️     | Meta tags and sitemap.xml added        |
| Marketing Strategy       | ☑️     | Social media marketing plan documented |

## Visitor User Stories

| User Story              | Status | Implementation Details                       |
|-------------------------|--------|----------------------------------------------|
| Browse Organic Products | ☑️     | Product catalog with filters                 |
| View Meal Plans         | ☑️     | Meal plan comparison page                    |
| Newsletter Signup       | ☑️     | Footer signup form                           |
| Navigation Experience   | ☑️     | Intuitive menu structure                     |
| Product Search          | ☑️     | Search by name/category/dietary requirements |
| Nutritional Information | ☑️     | Detailed product information pages           |

## Customer User Stories

| User Story             | Status | Features                             |
|------------------------|--------|--------------------------------------|
| Account Management     | ☑️     | Registration, login, profile updates |
| Password Reset         | ☑️     | Email-based reset functionality      |
| Order History          | ☑️     | View past orders and status          |
| Meal Plan Subscription | ☑️     | Subscribe/modify meal plans          |
| Shopping Cart          | ☑️     | Add/remove items, update quantities  |
| Checkout Process       | ☑️     | Secure payment integration           |
| Save Preferences       | ☑️     | Dietary preferences storage          |
| Review Products        | ☑️     | Product rating and reviews           |
| Apply Discounts        | ☑️     | Coupon code functionality            |

## Admin User Stories

| User Story          | Status | Capabilities                    |
|---------------------|--------|---------------------------------|
| Product Management  | ☑️     | Add/edit/delete products        |
| Inventory Control   | ☑️     | Stock level management          |
| Order Processing    | ☑️     | View/update order status        |
| User Management     | ☑️     | Manage customer accounts        |
| Content Management  | ☑️     | Update site content/blogs       |
| Reports Access      | ☑️     | Sales and inventory reports     |
| Discount Management | ☑️     | Create/manage promotional codes |

## Epic: Product Management

| User Story        | Status | Details                  |
|-------------------|--------|--------------------------|
| Add New Products  | ☑️     | Product creation form    |
| Update Products   | ☑️     | Edit existing products   |
| Delete Products   | ☑️     | Remove with confirmation |
| Manage Categories | ☑️     | Category CRUD operations |
| Stock Updates     | ☑️     | Inventory management     |

## Epic: Order Management

| User Story          | Status | Features                  |
|---------------------|--------|---------------------------|
| View Orders         | ☑️     | Order listing and details |
| Process Orders      | ☑️     | Update order status       |
| Refund Management   | ☑️     | Process refund requests   |
| Delivery Scheduling | ☑️     | Manage delivery slots     |

## Epic: Customer Service

| User Story             | Status | Implementation            |
|------------------------|--------|---------------------------|
| Support Tickets        | ☑️     | Customer inquiry system   |
| FAQ Management         | ☑️     | Update help content       |
| Review Moderation      | ☑️     | Manage product reviews    |
| Customer Communication | ☑️     | Email notification system |

### Product Management

- ☑️ Admin can add new products with images
- ☑️ Product updates reflect immediately
- ☑️ Stock levels update automatically
- ☑️ Category management interface
- ☑️ Bulk product operations

### Customer Features

- ☑️ Easy account creation/login
- ☑️ Intuitive shopping cart
- ☑️ Secure checkout process
- ☑️ Order tracking capability
- ☑️ Profile customization

### Admin Dashboard

- ☑️ Real-time sales data
- ☑️ Inventory alerts
- ☑️ Order management interface
- ☑️ Customer data access
- ☑️ Report generation

## Lighthouse Testing

Freshly Rooted Online Market underwent comprehensive testing using Chrome Dev Tools and Microsoft Edge Dev Tools
Lighthouse Testing tool. Testing focused on critical metrics affecting user experience and conversion rates for an
e-commerce food platform.

<details>

<summary>Lighthouse Test Results</summary>

| File Name                   | Pass | Notes | View Result                                                  |
|-----------------------------|------|-------|--------------------------------------------------------------|
| home page desktop           | ☑️   |       | ![Result](docs/test-img/home-page-desktop-lh.png)            |
| home page mobile            | ☑️   |       | ![Result](docs/test-img/home-page-mobile-lh.png)             |
| products page desktop       | ☑️   |       | ![Result](/docs/test-img/product-page-desktop-lh.png)        |
| products page mobile        | ☑️   |       | ![Result](/docs/test-img/product-page-mobile-lh.png)         |       
| blog page desktop           | ☑️   |       | ![Result](/docs/test-img/blog-page-desktop-lh.png)           |       
| blog page mobile            | ☑️   |       | ![Result](/docs/test-img/blog-page-mobile-lh.png)            |       
| blog post page desktop      | ☑️   |       | ![Result](/docs/test-img/blog-post-page-desktop-lh.png)      |       
| blog post page mobile       | ☑️   |       | ![Result](/docs/test-img/blog-post-page-mobile-lh.png)       |       
| contact page desktop        | ☑️   |       | ![Result](/docs/test-img/contact-page-desktop-lh.png)        |       
| contact page mobile         | ☑️   |       | ![Result](/docs/test-img/contact-page-mobile-lh.png)         |       
| privacy policy page desktop | ☑️   |       | ![Result](/docs/test-img/privacy-policy-page-desktop-lh.png) |       
| privacy policy page mobile  | ☑️   |       | ![Result](/docs/test-img/privacy-policy-page-mobile-lh.png)  |       
| return policy page desktop  | ☑️   |       | ![Result](/docs/test-img/return-policy-page-desktop-lh.png)  |
| return policy page mobile   | ☑️   |       | ![Result](/docs/test-img/return-policy-page-mobile-lh.png)   |       
| cart page desktop           | ☑️   |       | ![Result](/docs/test-img/cart-page-desktop-lh.png)           |       
| cart page mobile            | ☑️   |       | ![Result](/docs/test-img/cart-page-mobile-lh.png)            |       
| profile page desktop        | ☑️   |       | ![Result](/docs/test-img/profile-page-desktop-lh.png)        |       
| profile page mobile         | ☑️   |       | ![Result](/docs/test-img/profile-page-mobile-lh.png)         |       
| favorites page desktop      | ☑️   |       | ![Result](/docs/test-img/favorites-page-desktop-lh.png)      |       
| favorites page mobile       | ☑️   |       | ![Result](/docs/test-img/favorites-page-mobile-lh.png)       |       |
| logout page desktop         | ☑️   |       | ![Result](/docs/test-img/logout-page-desktop-lh.png)         |       
| logout page mobile          | ☑️   |       | ![Result](/docs/test-img/logout-page-mobile-lh.png)          |       
| register page desktop       | ☑️   |       | ![Result](/docs/test-img/register-page-desktop-lh.png)       |       
| register page mobile        | ☑️   |       | ![Result](/docs/test-img/register-page-mobile-lh.png)        |       
| login page desktop          | ☑️   |       | ![Result](/docs/test-img/login-page-desktop-lh.png)          |       
| login page mobile           | ☑️   |       | ![Result](/docs/test-img/login-page-mobile-lh.png)           |       

</details>

[Back to top](#contents) :top:

## Accessibility Testing

Accessibility scores were high on Lighthouse, however I retested the page.
[WAVE](https://wave.webaim.org/) online tool was used to check terminal color contrast. All tests were passed.

While building the application, the general principles of accessibility were adhered to:

- Using clear instructions
- Validating inputs before moving on to the next step
- Testing the page to make sure it does not affect performance from user input
- Using ARIA labels

[Back to top](#contents) :top:
