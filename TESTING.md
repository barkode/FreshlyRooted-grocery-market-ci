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

Additionally, I used
the [Google Chrome Mobile Simulator extension](https://chromewebstore.google.com/detail/mobile-simulator-responsi/ckejmhbmlajgoklhgbapkiccekfoccmk)
to evaluate responsiveness on more specialized
devices. I examined device samples for navigation, element alignment, content layout, and functionality issues across
different breakpoints.

Test Results:

| Size | Device Example     | Navigation         | Element Alignments | Content Placement  | Functionality      | Notes |
|------|--------------------|--------------------|--------------------|--------------------|--------------------|-------|
| sm   | Samsung Galaxy S20 | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |       |
| sm   | iPhone 11 PRO      | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |       |
| sm   | iPhone 13 PRO MAX  | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |       |
| md   | iPad MINI          | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |       |
| md   | Galaxy Tab S7      | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |       |
| md   | iPad Air           | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |       |
| lg   | iPad Pro           | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |       |
| xl   | Mackbook Air       | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |       |
| xl   | HP Stream Laptop   | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |       |
| xxl  | Dell Lattitude     | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |       |
| xxl  | Desktop            | :white_check_mark: | :white_check_mark: | :white_check_mark: | :white_check_mark: |       |

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

| File Name                   | Pass               | Notes | View Result                                                    |
|-----------------------------|--------------------|-------|----------------------------------------------------------------|
| home page desktop           | :white_check_mark: |       | [Result](docs/test-img/home-page-desktop-html.png)             |
| home page mobile            | :x:                |       | [Result](docs/test-img/home-page-mobile-html.png)              |
| products page desktop       | :white_check_mark: |       | ![Result](/docs/test-img/product-page-desktop-html.png)        |
| products page mobile        | :white_check_mark: |       | ![Result](/docs/test-img/product-page-mobile-html.png)         |       
| blog page desktop           | :white_check_mark: |       | ![Result](/docs/test-img/blog-page-desktop-html.png)           |       
| blog page mobile            | :white_check_mark: |       | ![Result](/docs/test-img/blog-page-desktop-html.png)           |       
| contact page desktop        | :white_check_mark: |       | ![Result](/docs/test-img/contact-page-desktop-html.png)        |       
| contact page mobile         | :white_check_mark: |       | ![Result](/docs/test-img/contact-page-desktop-html.png)        |       
| privacy policy page desktop | :white_check_mark: |       | ![Result](/docs/test-img/privacy-policy-page-desktop-html.png) |       
| privacy policy page mobile  | :white_check_mark: |       | ![Result](/docs/test-img/privacy-policy-page-mobile-html.png)  |       
| return policy page desktop  | :white_check_mark: |       | ![Result](/docs/test-img/return-policy-page-desktop-html.png)  |
| return policy page mobile   | :white_check_mark: |       | ![Result](/docs/test-img/return-policy-page-mobile-html.png)   |       
| cart page desktop           | :white_check_mark: |       | ![Result](/docs/test-img/cart-page-desktop-html.png)           |       
| cart page mobile            | :white_check_mark: |       | ![Result](/docs/test-img/cart-page-mobile-html.png)            |       
| change-password.html        | :white_check_mark: |       | ![Result](/docs/test-img/change-password-htmlchecker.png)      |       
| profile.html                | :white_check_mark: |       | ![Result](/docs/test-img/profile-htmlchecker.png)              |       
| delete-modal.html           | :white_check_mark: |       | ![Result](/docs/test-img/profile-delete-htmlchecker.png)       |       
| product-detail.html         | :white_check_mark: |       | ![Result](/docs/test-img/product-details-htmlchecker.png)      |       |
| about.html                  | :white_check_mark: |       | ![Result](/docs/test-img/about-htmlchecker.png)                |       
| special-offers.html         | :white_check_mark: |       | ![Result](/docs/test-img/offers-htmlchecker.png)               |       
| signup.html                 | :white_check_mark: |       | ![Result](/docs/test-img/sign-up-htmlchecker.png)              |       
| login.html                  | :white_check_mark: |       | ![Result](/docs/test-img/login-htmlchecker.png)                |       
| logout.html                 | :white_check_mark: |       | ![Result](/docs/test-img/logout-htmlchecker.png)               |       
| cart.html                   | :white_check_mark: |       | ![Result](/docs/test-img/cart-htmlchecker.png)                 |       
| checkout-success.html       | :white_check_mark: |       | ![Result](/docs/test-img/success-htmlchecker.png)              |      
| checkout.html               | :white_check_mark: |       | ![Result](/docs/test-img/checkout-htmlchecker.png)             |       
| shipping-returns.html       | :white_check_mark: |       | ![Result](/docs/test-img/shipping-returns-htmlchecker.png)     |       
| privacy-policy.html         | :white_check_mark: |       | ![Result](/docs/test-img/privacy-policy-htmlchecker.png)       |       
| terms-of-service.html       | :white_check_mark: |       | ![Result](/docs/test-img/terms-htmlchecker.png)                |       

</details>

[Back to top](#contents) :top:

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

| App Name  | File Name          | Pass               | Notes                                                      | View Result                                                                                               |
|-----------|--------------------|--------------------|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| about     | views.py           | :white_check_mark: | The string is longer than 79 characters. Unable to reduce. | <details><summary>Screenshot</summary>![Result](/docs/test-img/about-views-py.png)</details>              |
| about     | urls.py            | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/about-urls-py.png)</details>               |
| about     | models.py          | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/about-models-py.png)</details>             |
| about     | forms.py           | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/about-forms-py.png)</details>              |
| about     | admin.py           | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/about-admin-py.png)</details>              |
| about     | test_views.py      | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/about-test-viewers-py.png)</details>       |
| about     | test_forms.py      | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/about-test-forms-py.png)</details>         |
| app       | settings.py        | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/settings-py.png)</details>                 |
| app       | urls.py            | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/testing-urls-py-main-app.png)</details>    |
| app       | views.py           | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/views-py-main-app.png)</details>           |
| blog      | views.py           | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/blog-views-py.png)</details>               |
| blog      | urls.py            | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/blog-urls-py.png)</details>                |
| blog      | models.py          | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/blog-models-py.png)</details>              |
| blog      | forms.py           | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/blog-forms-py.png)</details>               |
| blog      | admin.py           | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/blog-admin-py.png)</details>               |
| blog      | test_views.py      | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/blog-test-views-py.png)</details>          |
| blog      | test_models.py     | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/blog-test-models-py.png)</details>         |
| cart      | views.py           | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/cart-views-py.png)</details>               |
| cart      | urls.py            | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/cart-urls-py.png)</details>                |
| cart      | contexts.py        | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/cart-context-py.png)</details>             |
| cart      | test_context.py    | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/cart-test-contest-py.png)</details>        |
| checkout  | webhooks.py        | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkout-webhooks-py.png)</details>        |
| checkout  | webhook_handler.py | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkout-webhook-handler-py.png)</details> |
| checkout  | views.py           | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkaout-views.png)</details>             |
| checkout  | urls.py            | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkout-urls-py.png)</details>            |
| checkout  | signals.py         | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkout-signals-py.png)</details>         |
| checkout  | models.py          | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkout-models-py.png)</details>          |
| checkout  | forms.py           | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkout-forms-py.png)</details>           |
| checkout  | admin.py           | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkout-admin-py.png)</details>           |
| checkout  | test_models.py     | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkout-test-models-py.png)</details>     |
| checkout  | test_forms.py      | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/checkout-test-forms-py.png)</details>      |
| favorites | views.py           | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/favorites-views-py.png)</details>          |
| favorites | urls.py            | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/favorites-urls-py.png)</details>           |
| favorites | models.py          | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/favorites-models-py.png)</details>         |
| favorites | admin.py           | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/favorites-admin-py.png)</details>          |
| favorites | test_models.py     | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/favorites-test-models-py.png)</details>    |
| home      | views.py           | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/home-views-py.png)</details>               |
| home      | urls.py            | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/home-urls-py.png)</details>                |
| products  | widgets.py         | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/products-widgets-py.png)</details>         |
| products  | views.py           | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/products-views-py.png)</details>           |
| products  | urls.py            | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/products-urls-py.png)</details>            |
| products  | models.py          | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/products-models-py.png)</details>          |
| products  | forms.py           | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/products-forms-py.png)</details>           |
| products  | admin.py           | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/products-admin-py.png)</details>           |
| products  | test_views.py      | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/products-test-views-py.png)</details>      |
| products  | test_models.py     | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/productstest-models-py.png)</details>      |
| products  | test_forms.py      | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/products-test-forms-py.png)</details>      |
| profiles  | views.py           | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/profiles-views-py.png)</details>           |
| profiles  | urls.py            | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/profiles-urls-py.png)</details>            |
| profiles  | models.py          | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/profiles-models-py.png)</details>          |
| profiles  | forms.py           | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/profiles-forms-py.png)</details>           |
| profiles  | test_forms.py      | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/profiles-test-forms.png)</details>         |
| main      | custom_storages.py | :white_check_mark: |                                                            | <details><summary>Screenshot</summary>![Result](/docs/test-img/main-custom-storages.png)</details>        |

</details><br/>

[Back to top](#contents) :top:

### Python (Unit Testing)

Python's `unittest` framework offers a robust and flexible testing solution.
Ideally, every part of the project should be put through the robust automated testing. Due to time constraints I have
conentrated automated tests concentrated on CRUD related functionality views, models and forms.

The automated tests highlighted a redundant view and html file naming issue. Although these issues did not affect the
functionality of the application, the quality and maintainability of the code are equally important.

![Unittest]()

[Back to top](#contents) :top:

## Manual Testing

In addition to using `unittest`, extensive manual testing was performed on the application. Each feature was verified
against success criteria. Where applicable, negative testing was conducted by providing invalid or unexpected inputs to
assess the application's robustness in handling errors and exceptions.

<details>
<summary>Manual Testing Results</summary>

</details>

[Back to top](#contents) :top:

## Role-based Restrictions

[Back to top](#contents) :top:

## Bugs

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
            <td>:white_chec k_mark:</td> 
            <td>:white_chec k_mark:</td> 
            <td>:white_check_mark:</td> 
            <td>:white_check_mark:</td> 
            <td>:✗:</td> 
            <td>:white_chec k_mark:</td> 
            <td>:white_chec k_mark:</td> 
            <td>:white_check_mark:</td> 
            <td>:white_check_mark:</td> 
            <td>:✗:</td>
            <td>:white_chec k_mark:</td> 
            <td>:white_chec k_mark:</td> 
            <td>:white_check_mark:</td> 
            <td>:white_check_mark:</td> 
            <td>:✗:</td> 
            <td>Test issue on Safari</td>
        </tr>
        <tr>
            <td>Contact</td >
            <td>:white_check_mark:</td> 
            <td>:white_check_mark:</td> 
            <td>:white_check_mark:</td> 
            <td>:✗:</td> 
            <td>:white_chec k_mark:</td> 
            <td>:white_chec k_mark:</td> 
            <td>:white_chec k_mark:</td> 
            <td>:white_chec k_mark:</td> 
            <td>:white_chec k_mark:</td> 
            <td>:white_chec k_mark:</td>
            <td> :white_check_mark:</td> 
            <td>:white_check_mark:</td> 
            <td>:✗:</td> 
             <td>:white_chec k_mark:</td> 
            <td>:white_check_mark:</td> 
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
