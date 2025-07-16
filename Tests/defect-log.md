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

**Expected Result:** Error – modification not allowed
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

---
