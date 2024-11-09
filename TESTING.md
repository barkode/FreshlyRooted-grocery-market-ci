# Testing

Return back to the [README.md](README.md) file.

![Main Image]()

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
        * [Python (Unit Testing)](#python-unit-testing)
    * [Manual Testing](#manual-testing)
    * [Role-based Restrictions](#role-based-restrictions)
    * [Bugs](#bugs)
    * [Browser Compatibility](#browser-compatibility)
    * [User Story Testing](#user-story-testing)
    * [Lighthouse Testing](#lighthouse-testing)
    * [Accessibility Testing](#accessibility-testing)

<!-- TOC -->

## Responsiveness Tests

I adopted a mobile-first strategy and verified all modifications using the DevTools in Google Chrome and Microsoft Edge.
For testing the deployed versions, I utilized external websites
like [Responsive Design Checker](https://responsivedesignchecker.com/)
and [Am I Responsive](https://ui.dev/amiresponsive) to obtain a unified view across various device breakpoints.

Additionally, I used
the [Google Chrome Mobile Simulator extension](https://chromewebstore.google.com/detail/mobile-simulator-responsi/ckejmhbmlajgoklhgbapkiccekfoccmk)
to evaluate responsiveness on more specialized
devices. I examined device samples for navigation, element alignment, content layout, and functionality issues across
different breakpoints.

Test Results:

| Size | Device Example     | Navigation | Element Alignments | Content Placement | Functionality | Notes |
|------|--------------------|------------|--------------------|-------------------|---------------|-------|
| sm   | Samsung Galaxy S20 | &check;    | &check;            | &check;           | &check;       |       |
| sm   | iPhone 11 PRO      | &check;    | &check;            | &check;           | &check;       |       |
| sm   | iPhone 13 PRO MAX  | &check;    | &check;            | &check;           | &check;       |       |
| md   | iPad MINI          | &check;    | &check;            | &check;           | &check;       |       |
| md   | Galaxy Tab S7      | &check;    | &check;            | &check;           | &check;       |       |
| md   | iPad Air           | &check;    | &check;            | &check;           | &check;       |       |
| lg   | iPad Pro           | &check;    | &check;            | &check;           | &check;       |       |
| xl   | Mackbook Air       | &check;    | &check;            | &check;           | &check;       |       |
| xl   | HP Stream Laptop   | &check;    | &check;            | &check;           | &check;       |       |
| xxl  | Dell Lattitude     | &check;    | &check;            | &check;           | &check;       |       |
| xxl  | Desktop            | &check;    | &check;            | &check;           | &check;       |       |

[Back to top](#contents)

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

| File Name             | Pass | View Result                                                | Notes                                                                                                                                                                                             |
|-----------------------|------|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| index.html            | ⛔    | [Result](docs/test-img/header-1.png)                       |                                                                                                                                                                                                   |
| product-list.html     | ⛔    | [Result](docs/test-img/all-prod.png)                       |                                                                                                                                                                                                   |
| search-results.html   | ✅    | ![Result](/docs/test-img/search-results-htmlchecker.png)   |                                                                                                                                                                                                   |
| edit-product.html     |      | ![Result](/docs/test-img/edit-product-htmlchecker.png)     |                                                                                                                                                                                                   |
| add-product.html      | ✅    | ![Result](/docs/test-img/add-product-htmlchecker.png)      |                                                                                                                                                                                                   |
| admin-summary.html    | ✅    | ![Result](/docs/test-img/admin-summary-htmlchecker.png)    |                                                                                                                                                                                                   |
| manage-author.html    | ✅    | ![Result](/docs/test-img/manage-author-htmlchecker.png)    |                                                                                                                                                                                                   |
| manage-genre.html     | ✅    | ![Result](/docs/test-img/manage-genre-htmlchecker.png)     |                                                                                                                                                                                                   |
| manage-coupon.html    |      | ![Result](/docs/test-img/manage-coupon-htmlchecker.png)    | It intermittently throws an error for dropdown selection for percentage option. Based on online research there seems to be an ongoing html issue. All html code is updated to meet the standards. |
| manage-category.html  | ✅    | ![Result](/docs/test-img/manage-category-htmlchecker.png)  |                                                                                                                                                                                                   |
| manage-orders.html    | ✅    | ![Result](/docs/test-img/manage-orders-htmlchecker.png)    |                                                                                                                                                                                                   |
| dashboard.html        | ✅    | ![Result](/docs/test-img/dashboard-htmlchecker.png)        |                                                                                                                                                                                                   |
| profile.html          | ✅    | ![Result](/docs/test-img/profile-htmlchecker.png)          |                                                                                                                                                                                                   |
| my-orders.html        | ✅    | ![Result](/docs/test-img/user-orders-htmlchecker.png)      |                                                                                                                                                                                                   |
| wishlist.html         | ✅    | ![Result](/docs/test-img/user-favourites-htmlchecker.png)  |                                                                                                                                                                                                   |
| change-password.html  | ✅    | ![Result](/docs/test-img/change-password-htmlchecker.png)  |                                                                                                                                                                                                   |
| delete-modal.html     | ✅    | ![Result](/docs/test-img/profile-delete-htmlchecker.png)   |                                                                                                                                                                                                   |
| product-detail.html   | ✅    | ![Result](/docs/test-img/product-details-htmlchecker.png)  |                                                                                                                                                                                                   |
| about.html            | ✅    | ![Result](/docs/test-img/about-htmlchecker.png)            |                                                                                                                                                                                                   |
| special-offers.html   | ✅    | ![Result](/docs/test-img/offers-htmlchecker.png)           |                                                                                                                                                                                                   |
| signup.html           | ✅    | ![Result](/docs/test-img/sign-up-htmlchecker.png)          |                                                                                                                                                                                                   |
| login.html            | ✅    | ![Result](/docs/test-img/login-htmlchecker.png)            |                                                                                                                                                                                                   |
| logout.html           | ✅    | ![Result](/docs/test-img/logout-htmlchecker.png)           |                                                                                                                                                                                                   |
| cart.html             | ✅    | ![Result](/docs/test-img/cart-htmlchecker.png)             |                                                                                                                                                                                                   |
| checkout-success.html | ✅    | ![Result](/docs/test-img/success-htmlchecker.png)          |                                                                                                                                                                                                   |
| checkout.html         | ✅    | ![Result](/docs/test-img/checkout-htmlchecker.png)         |                                                                                                                                                                                                   |
| shipping-returns.html | ✅    | ![Result](/docs/test-img/shipping-returns-htmlchecker.png) |                                                                                                                                                                                                   |
| privacy-policy.html   | ✅    | ![Result](/docs/test-img/privacy-policy-htmlchecker.png)   |                                                                                                                                                                                                   |
| terms-of-service.html | ✅    | ![Result](/docs/test-img/terms-htmlchecker.png)            |                                                                                                                                                                                                   |

</details>

[Back to top](#contents)

### CSS

The [W3C Jigsaw](https://jigsaw.w3.org/css-validator/) tool, provided by the W3C, enables to validate and verify the
correctness of CSS code. It ensures that your web pages adhere to W3C standards, promoting interoperability and
accessibility.

<details>

<summary>CSS Validation Results</summary>

</details>

### JavaScript

No major errors were found when validating JavaScript through [Jshint](https://jshint.com/).


<details>

<summary>JavaScript Validation Results</summary>

</details>

### Python

The python files have all been passed through [PEP8 CI Online](https://pep8ci.herokuapp.com/)

<details><summary><b>PEP8 Test Results</b></summary>

| App Name  | File Name          | Pass | View Result                                                                                            |
|-----------|--------------------|------|--------------------------------------------------------------------------------------------------------|
| app       | settings.py        | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/settings-py.png)</details>              |
| app       | urls.py            | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/testing-urls-py-main-app.png)</details> |
| app       | views.py           | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/views-py-main-app.png)</details>        |
| blog      | views.py           | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/bag-tools-py.png)</details>             |
| blog      | urls.py            | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/test-views-cart-py.png)</details>       |
| blog      | models.py          | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/apps-cart-py.png)</details>             |
| blog      | forms.py           | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/contexts-cart-py.png)</details>         |
| blog      | admin.py           | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/test-views-cart-py.png)</details>       |
| blog      | test_views.py      | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/apps-cart-py.png)</details>             |
| blog      | test_models.py     | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/contexts-cart-py.png)</details>         |
| blog      | test_forms.py      | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/contexts-cart-py.png)</details>         |
| cart      | views.py           | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/urls-cart-py.png)</details>             |
| cart      | urls.py            | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/views-cart-py.png)</details>            || cart     | bag_tools.py       | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/bag-tools-py.png)</details>             |
| cart      | models.py          | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/test-views-cart-py.png)</details>       |
| cart      | contexts.py        | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/apps-cart-py.png)</details>             |
| cart      | test_context.py    | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/contexts-cart-py.png)</details>         |
| cart      | context.py         | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/urls-cart-py.png)</details>             |
| checkout  | webhooks.py        | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/test-forms-checkout-py.png)</details>   |
| checkout  | webhook_handler.py | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/test-models-checkout-py.png)</details>  |
| checkout  | views.py           | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/admin-checkout-py.png)</details>        |
| checkout  | urls.py            | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/apps-checkout-py.png)</details>         |
| checkout  | signals.py         | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/forms-checkout-py.png)</details>        |
| checkout  | models.py          | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/models-checkout-py.png)</details>       |
| checkout  | forms.py           | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/signals-checkout-py.png)</details>      |
| checkout  | admin.py           | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/urls-checkout-py.png)</details>         |
| checkout  | test_models.py     | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/views-checkout-py.png)</details>        |
| checkout  | test_forms.py      | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/handler-checkout-py.png)</details>      |
| favorites | views.py           | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/apps-core-py.png)</details>             |
| favorites | urls.py            | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/urls-core-py.png)</details>             |
| favorites | models.py          | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/views-core-py.png)</details>            |
| favorites | admin.py           | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/views-core-py.png)</details>            |
| favorites | test_models.py     | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/views-core-py.png)</details>            |
| home      | views.py           | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/views-core-py.png)</details>            |
| home      | urls.py            | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/views-core-py.png)</details>            |
| home      | models.py          | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/views-core-py.png)</details>            |
| products  | widgets.py         | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/query-products-py.png)</details>        |
| products  | views.py           | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/test-models-products-py.png)</details>  |
| products  | urls.py            | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/test-views-products-py.png)</details>   |
| products  | models.py          | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/admin-products-py.png)</details>        |
| products  | admin.py           | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/apps-products-py.png)</details>         |
| products  | test_views.py      | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/filters-products-py.png)</details>      |
| products  | test_models.py     | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/forms-products-py.png)</details>        |
| products  | test_forms.py      | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/mixins-products-py.png)</details>       |
| profiles  | views.py           | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/models-products-py.png)</details>       |
| profiles  | urls.py            | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/urls-products-py.png)</details>         |
| profiles  | models.py          | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/views-products-py.png)</details>        |
| profiles  | forms.py           | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/admin-prof-py.png)</details>            |
| profiles  | test_forms.py      | ✅    | <details><summary>Screenshot</summary>![Result](/docs/test-img/apps-prof-py.png)</details>             |

</details><br/>


[Back to top](#contents)

### Python (Unit Testing)

Python's `unittest` framework offers a robust and flexible testing solution.
Ideally, every part of the project should be put through the robust automated testing. Due to time constraints I have
conentrated automated tests concentrated on CRUD related functionality views, models and forms.

The automated tests highlighted a redundant view and html file naming issue. Although these issues did not affect the
functionality of the application, the quality and maintainability of the code are equally important.

![Unittest]()

[Back to top](#contents)

## Manual Testing

In addition to using `unittest`, extensive manual testing was performed on the application. Each feature was verified
against success criteria. Where applicable, negative testing was conducted by providing invalid or unexpected inputs to
assess the application's robustness in handling errors and exceptions.

<details>
<summary>Manual Testing Results</summary>

</details>

[Back to top](#contents)

## Role-based Restrictions

[Back to top](#contents)

## Bugs

[Back to top](#contents)

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
            <td>✓</td> 
            <td>✓</td> 
            <td>✓</td> 
            <td>✓</td> 
            <td>✗</td> 
            <td>✓</td> 
            <td>✓</td> 
            <td>✓</td> 
            <td>✓</td> 
            <td>✗</td>
            <td>✓</td> 
            <td>✓</td> 
            <td>✓</td> 
            <td>✓</td> 
            <td>✗</td> 
            <td>Test issue on Safari</td>
        </tr>
        <tr>
            <td>Contact</td>
            <td>✓</td> 
            <td>✓</td> 
            <td>✓</td> 
            <td>✗</td> 
            <td>✓</td> 
            <td>✓</td> 
            <td>✓</td> 
            <td>✓</td> 
            <td>✗</td> 
            <td>✓</td>
            <td>✓</td> 
            <td>✓</td> 
            <td>✗</td> 
            <td>✓</td> 
            <td>✓</td> 
            <td>Issue on Opera in Tablet</td>
        </tr>
    </tbody>
</table>

[Browser Testing Results]()

## User Story Testing

## Lighthouse Testing

<details>
<summary>Lighthouse Test Results</summary>

</details>

[Back to top](#contents)

## Accessibility Testing

Accessibility scores were high on Lighthouse, however I retested the page.
[WAVE](https://wave.webaim.org/) online tool was used to check terminal color contrast. All tests were passed.

While building the application, the general principles of accessibility were adhered to:

- Using clear instructions
- Validating inputs before moving on to the next step
- Testing the page to make sure it does not affect performance from user input
- Using ARIA labels

[Back to top](#contents)
