# Testing

Return back to the [README.md](README.md) file.

![Main Image]()

# Contents

- [Testing](#testing)
- [Contents](#contents)
    - [Responsiveness Tests](#responsiveness-tests)
    - [Code Validation](#code-validation)
        - [HTML](#html)
        - [CSS](#css)
        - [JavaScript](#javascript)
        - [Python](#python)
        - [Python (Unit Testing)](#python-unit-testing)
    - [Manual Testing](#manual-testing)
    - [Role-based Restrictions](#role-based-restrictions)
    - [Bugs](#bugs)
    - [Browser Compatibility](#browser-compatibility)
    - [User Story Testing](#user-story-testing)
    - [Lighthouse Testing](#lighthouse-testing)
    - [Accessibility Testing](#accessibility-testing)

## Responsiveness Tests

I adopted a mobile-first strategy and verified all modifications using the DevTools in Google Chrome and Microsoft Edge.
For testing the deployed versions, I utilized external websites
like [Responsive Design Checker](https://responsivedesignchecker.com/)
and [Am I Responsive](https://ui.dev/amiresponsive) to obtain a unified view across various device breakpoints.

Additionally, I used the [Google Chrome Mobile Simulator extension](https://chromewebstore.google.com/detail/mobile-simulator-responsi/ckejmhbmlajgoklhgbapkiccekfoccmk) to evaluate responsiveness on more specialized
devices. I examined device samples for navigation, element alignment, content layout, and functionality issues across
different breakpoints.

Test Results:

| Size | Device Example     | Navigation | Element Alignments | Content Placement | Functionality | Notes                             |
| ---- | ------------------ | ---------- | ------------------ | ----------------- | ------------- | --------------------------------- |
| sm   | Samsung Galaxy S20 | &check;    | &check;            | &check;           | &check;       |                                   |
| sm   | iPhone 11 PRO      | &check;    | &check;            | &check;           | &check;       |
| sm   | iPhone 13 PRO MAX  | &check;    | &check;            | &check;           | &check;       |
| md   | iPad MINI          | &check;    | &check;            | &check;           | &check;       |                                   |
| md   | Galaxy Tab S7      | &check;    | &check;            | &check;           | &check;       |                                   |
| md   | iPad Air           | &check;    | &check;            | &check;           | &check;       |                                   |
| lg   | iPad Pro           | &check;    | &check;            | &check;           | &check;       |  |
| xl   | Mackbook Air       | &check;    | &check;            | &check;           | &check;       |                                   |
| xl   | HP Stream Laptop   | &check;    | &check;            | &check;           | &check;       |                                   |
| xxl  | Dell Lattitude     | &check;    | &check;            | &check;           | &check;       |                                   |
| xxl  | Desktop            | &check;    | &check;            | &check;           | &check;       |                                   |


[Back to top](#contents)

## Code Validation

### HTML

The recommended [HTML W3C Validator](https://validator.w3.org) to validate all of the project's HTML files.

This is the process which was followed of validating an HTML file by direct input:

1. **Access the Validator**: Visit the [W3C Markup Validation Service](https://validator.w3.org/).
2. **Choose Direct Input**: Select the "Validate by Direct Input" tab.
3. **Paste Your HTML Code**: Copy HTML code and paste it into the text box.
4. **Validate**: Click the "Check" button to validate HTML.

<details>

<summary>HTML Validation Results</summary>

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

Jshint retruned one note that `bootstrap` variable is undefined. This can be ignored because `bootstrap.Modal` relies on
bootstrap being a globally defined object, which Bootstrap itself provides. STRIPE and Mailchimp scripts were obtained
directly from the origins so no errors were taken into consideration in order to avoid interference with intended
fuctionality.

<details>

<summary>JavaScript Validation Results</summary>

</details>

### Python

The python files have all been passed through [PEP8 CI Online](https://pep8ci.herokuapp.com/)

<details>
<summary>PEP8 Test Results</summary>

</details>

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
