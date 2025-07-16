# Linked GitHub Issues

- [Regular user can access Admin panel URL #1](https://github.com/Ian-Joseph/CleanCity/issues/1)
- [Scheduling Pickup of Waste with a Past Date #7](https://github.com/Ian-Joseph/CleanCity/issues/7)
- [Pickup Request History is Not Available #9](https://github.com/Ian-Joseph/CleanCity/issues/9)
- [Pending Pickup Request is not cancellable #10](https://github.com/Ian-Joseph/CleanCity/issues/10)
- [Requests more than 24 hours away are not modifiable #11](https://github.com/Ian-Joseph/CleanCity/issues/11)
- [Request less than 24 hours are not modifiable #12](https://github.com/Ian-Joseph/CleanCity/issues/12)
- [Status for the requests are not displayed #13](https://github.com/Ian-Joseph/CleanCity/issues/13)
- [System allows account registration with existing email #2](https://github.com/Ian-Joseph/CleanCity/issues/2)
- [Registration Form Missing Confirm Password Field, Password Mismatch Validation Not Possible #3](https://github.com/Ian-Joseph/CleanCity/issues/3)
- [Account created with too short password #4](https://github.com/Ian-Joseph/CleanCity/issues/4)
- [Account is created with invalid email format #5](https://github.com/Ian-Joseph/CleanCity/issues/5)
- [Login Successful with Incorrect Passwordl #6](https://github.com/Ian-Joseph/CleanCity/issues/6)
- [Real-time validation not triggering #14](https://github.com/Ian-Joseph/CleanCity/issues/14)
- [User-generated content not sanitized #15](https://github.com/Ian-Joseph/CleanCity/issues/15)
- [SQL Injection and XSS not prevented #16](https://github.com/Ian-Joseph/CleanCity/issues/16)
- [The system fails to meet WCAG 2.1 AA compliance due to low color contrast between foreground text and background elements in multiple UI components. #17](https://github.com/Ian-Joseph/CleanCity/issues/17)
- [Admin moderation panel missing  #18]()
- [Pickup requests not displayed #19](https://github.com/Ian-Joseph/CleanCity/issues/19)



## Access Control

## Bug Report 1

**Title**: Regular user can access Admin panel URL

**Steps to Reproduce**:

1. Log in as an admin user
2. Copy admin URL and visit as regular user

**Expected**: Access denied or redirected

**Actual**: Site replicates with no authentication needed and user can access anything the admin has rights to. 

**Severity**: Critical

## Bug Report 2

**Title**: Scheduling pickup of waste with a past date

**Steps to Reproduce**:

1. Navigate to scheduling page
2. Enter a registered full name  e.g. "John Doe"
3. Enter valid registered email e.g. `user1@test.com`
4. Select a pick up location e.g. "Nairobi"
5. Select waste type (e.g., Recyclable)
6. Enter a past date e.g. "1/07/2025"
7. Enter any additional description  
8. Click "Submit request" button

- **Expected**: Error message displayed – date must be in the future
- **Actual**: "Your waste pickup request has been submitted!" message is displayed
- **Severity**: Medium

## 4.2 Request Management

## Bug Report 3

**Title**: Pickup Request History is not available

**Steps to Reproduce**:

1. Log in as normal user
2. Schedule a waste pickup
3. Navigate to your dashboard and check on the requested pickups
4. Alternatively navigate to the user profile and check on 'My Requests'

**Expected Result:** List of all pickup requests displayed

**Actual Result:** No requests displayed. No scheduled requests were logged.

**Severity**: Critical

## Bug Report 4

**Title**: Pending Pickup Request is not cancellable

**Steps to Reproduce**:

1. Log in as normal user
2. Schedule a waste pickup
3. Navigate to your dashboard and check on the requested pickups
4. Alternatively navigate to the user profile and check on 'My Requests'
5. Select a pending request  
6. Click cancel

**Expected Result:** Status changes to Cancelled

**Actual Result:** No pending requests displayed. No scheduled requests were logged. No request was at all logged.

**Severity**: Critical

## Bug Report 5

**Title**: Requests more than 24 hours away are not modifiable

**Steps to Reproduce**:

1. Log in as normal user
2. Schedule a waste pickup
3. Navigate to your dashboard and check on the requested pickups
4. Alternatively navigate to the user profile and check on 'My Requests'
5. Select request with pickup time more than 24 hours away  
6. Update details (e.g., quantity)

**Expected Result:** Details updated successfully

**Actual Result:** No requests displayed. No scheduled requests were logged. No request was at all logged.

**Severity**: Critical

## Bug Report 6

**Title**: Request less than 24 hours are not modifiable

**Steps to Reproduce**:

1. Log in as normal user
2. Schedule a waste pickup
3. Navigate to your dashboard and check on the requested pickups
4. Alternatively navigate to the user profile and check on 'My Requests'
5. Select request with pickup time less than 24 hours away  
6. Attempt to modify details  

**Expected Result:** Error – modification not allowed.

**Actual Result:** No requests displayed. No scheduled requests were logged. No request was at all logged.

**Severity**: Critical

## Bug Report 7

**Title**: Status for the requests are not displayed

**Steps to Reproduce**:

1. Log in as normal user
2. Schedule a waste pickup
3. Navigate to your dashboard and check on the requested pickups
4. Alternatively navigate to the user profile and check on 'My Requests'
5. View request list

**Expected Result:** Each request shows status (Pending, Confirmed, Completed, Cancelled)

**Actual Result:** No requests displayed. No scheduled requests were logged. No request was at all logged.  

**Severity**: Critical

## Bug Report 8

**Title**: System allows account registration with existing email

**Steps to Reproduce**:

1. Navigate to the registration page  
2. Enter full name: `New Test User`  
3. Enter an already registered email: `user1@cleancity.com`  
4. Enter password: `NewPass123`  
5. Click the **Register** button

**Expected Result:** Account registration is blocked, `"Email already exists"` error message is displayed.

**Actual Result:** Account is created successfully despite duplicate email

**Severity**: High

**Priority:** Critical  

## Bug Report 9

**Title**: Registration form missing confirm password field, password mismatch validation not possible

**Steps to Reproduce**:

1. Navigate to the registration page  
2. Enter full name: `New Test User`  
3. Enter email: `newuser@test.com`  
4. Enter password: `TestPass123`  
5. Attempt to confirm password (Field missing) 

**Expected Result:** A **"Confirm Password"** field is present 

**Actual Result:** **"Confirm Password"** field is missing from the form 

**Severity**: Critical

**Priority:** High 


## Bug Report 10

**Title**: Account created with too short password

**Steps to Reproduce**:

1. Navigate to the registration page  
2. Enter full name: `New Test User`  
3. Enter email: `newuser@test.com`  
4. Enter password: `TestPass`    
5. Click the **Register** button   

**Expected Result:** Password is validated for minimum length (e.g., at least 8 characters),`"Password must be at least 8 characters" error message is displayed.

**Actual Result:** Account is created successfully with a short password. 

**Severity**: High

**Priority:** High 


## Bug Report 11

**Title**: Account is created with invalid email format

**Steps to Reproduce**:

1. Navigate to the registration page  
2. Enter full name: `New Test User`  
3. Enter email: `newuser@test`  
4. Enter password: `NewPass123`   
5. Click the **Register** button   

**Expected Result:** The system should reject the registration and display an error message indicating the email format is invalid.

**Actual Result:** The system accepts the email `newuser@test` and creates the account successfully without validation. 

**Severity**: Moderate 

**Priority:** Medium   


## Bug Report 12

**Title**: Login Successful with Incorrect Password

**Steps to Reproduce**:

1. Navigate to the login page  
2. Enter registered email: `user1@test.com`  
3. Enter incorrect password: `Test`  
4. Click the **Login** button   

**Expected Result:**  Login is blocked; `"Invalid email or password"` error message is displayed.

**Actual Result:** Login attempt is successful

**Severity**: Critical 

**Priority:** Critical   


## Bug Report 13

**Title**: Real-time validation not triggering

**Steps to Reproduce**:

1. Navigate to the registration form.  
2. Enter an invalid email (e.g., `john@`) into the email input field.  
3. Move focus to another field or wait for validation.  
4. Observe system behavior.  

**Expected Result:**  The system should immediately display a validation message .

**Actual Result:** The system does not provide instant feedback.

**Severity**: medium   

**Priority:** low


## Bug Report 14

**Title**: SQL Injection and XSS not prevented

**Steps to Reproduce**:

1. Navigate to a user input form (e.g., login, comment box).  
2. Enter the following as input:  
   - SQL Injection: `' OR '1'='1`  
   - XSS Script: `<script>alert('x')</script>`  
3. Submit the form.  
4. Observe whether the input is executed, stored, or displayed unsanitized. 

**Expected Result:**  The system should either reject the malicious input with an error message or sanitize it so that it is rendered harmless.

**Actual Result:** The system accepts and stores the input. Script tags are rendered in output, and no error or sanitization is applied. SQL injection input is not blocked, potentially exposing the backend to query tampering.

**Severity**: Critical

**Priority:** High 


## Bug Report 15

**Title**: The system fails to meet WCAG 2.1 AA compliance due to low color contrast between foreground text and background elements in multiple UI components.

**Steps to Reproduce**:

1. Open the application in the browser.  
2. Launch an accessibility testing tool ANDI.  
3. Run a full-page audit.  
4. Review contrast ratio test results 

**Expected Result:**  All UI elements (buttons, text, links, etc.) should meet or exceed the minimum contrast ratio defined in WCAG 2.1 AA (4.5:1 for normal text, 3:1 for large text).

**Actual Result:**  Several elements (e.g., "Recent Posts"  on light gray background) fail the contrast ratio test, scoring below 4.5:1. These failures are flagged as critical accessibility issues by ANDI

**Severity**: High 

**Priority:** High 



## Bug Report 16

**Title**: Admin moderation panel missing

**Steps to Reproduce**:

1. Log in as an admin.  
2. Navigate to the admin dashboard.  
3. Open the community moderation panel.  
4. Attempt to take an action (e.g., edit, hide, flag) on a post or comment. 

**Expected Result:**   Admin should be able to manage posts and comments by using moderation tools (edit, delete, hide, flag, etc.)

**Actual Result:**  The community moderation panel is missing, and moderation actions are not visible or accessible.

**Severity**: High 

**Priority:** High


## Bug Report 17

**Title**: Pickup requests not displayed

**Steps to Reproduce**:

1. Login as an admin user.  
2. Navigate to the **Admin Dashboard**.  
3. Click on the **Pickup Requests** section

**Expected Result:**   All pickup requests should be displayed in a structured table view.

**Actual Result:**  No pickup requests are displayed.

**Severity**: moderate

**Priority:** Low


## Bug Report 18

**Title**: User-generated content not sanitized

**Steps to Reproduce**:

1. Go to the community feed post  
2. Enter the following into the text area:  
   ```html
   <script>alert('XSS')</script>

3. Submit the content.
4. View the submitted content on the frontend.

**Expected Result:**  The system should sanitize user input so that HTML and script tags are removed or rendered harmless.
**Actual Result:**  The script is not sanitized

**Severity**: Critical 

**Priority:** High  



---
