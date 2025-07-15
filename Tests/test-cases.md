# 🧪 Test Cases for CleanCity - Waste Pickup Scheduler Web App

## 📄 Introduction

This document outlines the comprehensive set of test cases designed to validate the functionality, performance, and reliability of the application under test. Each test case has been developed based on the system’s requirements and user expectations to ensure that all features behave as intended across various scenarios.

The test cases cover both **functional** and **non-functional** aspects of the system, enabling consistent quality assurance and traceability throughout the testing lifecycle.

---

## 🔐 Registration Test Cases

### ✅ TC-R-01: Verifying user registration with Valid Inputs

- **Preconditions:** User is on the Register page
- **Test Steps:**
  1. Enter full name: "New Test User"
  2. Enter email: "<newuser@test.com>"
  3. Enter password: "NewPass123"
  4. Confirm password: "NewPass123"
  5. Click "Register" button
- **Expected Result:** Account is successfully created; user redirected to login with a success message
- **Actual Result:** Account is successfully created; user redirected to login with a success message <!--passes-->

### ❌ TC-R-02: Verifying user registration with missing name field

- **Test Steps:**
  1. Leave the name field blank
  2. Enter email: newuser@test.com"
  3. Enter password: "NewPass123"
  4. Confirm password: "NewPass123"
  5. Click "Register" button

- **Expected Result:** Account is not created, error displayed: "please fill out this fied"

- **Actual Result:** Account is not created, "please fill out this fied" error is displayed <!--passes-->

### ❌ TC-R-03: Verifying user registration with an already existing email

**Test Steps:**
  1.Enter full name: "New Test User"
  2. Use an existing email: "user1@cleancity.com"
  3.Enter password: "NewPass123".
  4.Confirm password: "TestPass123"
  4. Click "Register" button
  
**Expected Result:** Account is not created, error displayed: "Email already exists"
**Actual Result:** Account is created succesfully <!--fails-->

### ❌ TC-R-04: Verifying user registration with password mismatch

**Test Steps:**

  1. Enter full name: "New Test User"
  2. Enter email: "newuser@test.com"
  3. Enter password: "TestPass123"
  4. Confirm password: "123abc"
  5. Click "Register" button
**Expected Result:** Account is not created, "Passwords do not match" is displayed
**Actual Result:** Confirmed password field is missing on the account registration form <!--fails -- critical-->

#### ❌ TC-R-05: Verify user registration with password too short

**Test Steps:**

  1. Enter full name: "New Test User"
  2. Enter email: "newuser@test.com"
  3. Enter password: "TestPass"
  4. Confirm password: "TestPass"
  5. Click "Register" button

- **Expected Result:** Account is not created, error: "Password must be at least 8 characters" is displayed
- **Actual Result:** Account is created succesfully <!--fails-- high-->

#### ❌ TC-R-06: Verifying user registration with nvalid email format

- **Test Steps:**
  1. Enter full name: "New Test User"
  2. Enter email: "newuser@test.com"
  3. Enter password: "NewPass123"
  4. Confirm password: "NewPass123"
  5. Click "Register" button

- **Expected Result:** Account is not created; error: "Invalid email address" is displayed
- **Actual Result:** Account is created succesfuly; error: "Invalid email address" is displayed <!--fails-->

---

### 🔐 Login Test Cases

#### ✅ TC-L-01: Verifying that valid user can login

- **Test Steps:**
  1. Go to login page
  2. Enter: Email: "<user1@cleancity.com>"
  3. Enter Password: "TestPass123"
  4. Click "Login" button
- **Expected Result:** User is logged succesfully and redirected to Dashboard; user-specific links shown

- **Actual Result:** User is logged succesfully and redirected to Dashboard; user-specific links shownn

#### ✅ TC-L-02: Verifying that valid Admin can login

- **Test Steps:**
  1. Enter: Email: "<admin@cleancity.com>"
  2. Password: "admin123"
  3. Click "Login" button
- **Expected Result:** Admin is logged successfully and Redirected to Dashboard; admin panel link is visible

- **Actual Result:** Admin is logged successfully and the admin panel link is not visible

#### ❌ TC-L-03: verifying user login with invalid password

- **Test Steps:**
  1. Enter valid registered user email e.g <user1@test.com>
  2. Enter incorrect password e.g "Test"
  3. Click "Login" button
- **Expected Result:** Login unsuccesfull; error "Invalid email or password" is displayed

- **Actual Result:** Login attempt successful <!--fails-->

#### ❌ TC-L-03: verifying Admin login with invalid password

- **Test Steps:**
  1. Enter valid admin email e.g <admin@test.com>
  2. Enter incorrect password e.g "Test"
  3. Click "Login" button
- **Expected Result:** Login unsuccesfull; error "Invalid email or password" is displayed

- **Actual Result:** Login attempt successful <!--fails-->

#### ❌ TC-L-04: Verifying user login with non-existent email

- **Test Steps:**
  1. Enter unused email e.g "user@test"
  2. Enter any password
  3. Click "Login" button

- **Expected Result:** login not successfull; error: "Invalid email or password" is displayed

- **Actual Result:** Login attempt successful <!--fails-->

#### ❌ TC-L-05: verifying user login with empty Email

- **Test Steps:**
  1. Leave email blank
  2. Enter valid password e.g "TestPass123"
  3. Click "Login" button
- **Expected Result:** Login attempt not successfull, error: "Email is required"

- **Actual Result:** Login attemp unsuccesful attempt successful <!--passes-->

#### ❌ TC-L-06: Verifying user login with empty Password

- **Test Steps:**
  1. Enter valid registered email e.g "<user1@test.com>"
  2. Leave password blank
  3. Click "Login" button

- **Expected Result:** Log in attempt not successful, error: "Password is required" is displayed

- **Actual Result:** Login attempt unsuccesful attempt successful; error: "Password is required" is dispayed <!--passes-->

#### ❌ TC-L-07: Verifying SQL Injection Attempt

- **Test Steps:**
  1. Enter `admin@cleancity.com`
  2. Password `' OR 1=1 --`
  3. Submit
- **Expected Result:** Login blocked; generic error shown

- **Expected Result:** Login successful <!--fails-->

---

### 🚪 Logout Test Cases

#### ✅ TC-LO-01: Verifying user logout from logged-in state

**Precondition:** User is logged in
**Test Steps:**

  1. Click on Logout

**Expected Result:** Session ends; the user redirected to login page

**Actual Result:** Session ends; the user is redirected to login page

#### ✅ TC-LO-02: Verifying that Logout is hidden for guest user

**Test Steps:**

  1. Access app without logging in

**Expected Result:** Logout button is not visible

**Actual Result:** Logout button is not visible

#### ✅ TC-LO-03: Verifying logout via URL as guest

**Test Steps:**

  1. Access logout endpoint manually in browser

**Expected Result:** Logout button not accessible, user is redirected to login

**Actual Result:** Logout button not accessible, user is redirected to login

---

### 👮‍♂️ Access Control Test Cases

#### ✅ TC-A-01: Verifying that Admin sees Admin panel

**Test Steps:**

  1. Login as admin
  2. Check navigation bar

**Expected Result:** "Admin" link is visible

**Actual Result:** "Admin" link is visible

#### ✅ TC-A-02: Verifying that regular user cannot see Admin Panel

**Test Steps:**

  1. Login as regular user
  2. Check nav links

**Expected Result:** Admin link is hidden

**Actual Result:** Admin link is hidden

#### ❌ TC-A-03: Verifying direct Dashboard Access by guest

**Test Steps:**

  1. Visit `/dashboard` without logging in

**Expected Result:** Dashboard not accessible, user is redirected to login

**ActuaL Result:** Dashboard not accessible, user is redirected to login

#### ❌ TC-A-04: Verifying regular user cannot accessing Admin panel URL

**Test Steps:**

  1. Copy admin URL and visit as regular user

**Expected Result:** Access denied, user is redirected to the login page

**Actual Result:** Access denied, user is redirected to the login page

---

### 🧪 UI & Usability Test Cases

#### ✅ TC-UI-01: Verifying that placeholder texts exist

**Test Steps:**

  1. Check email and password fields

**Expected Result:** Placeholder like "Enter your email" visible

**Actual Result:** All fields have visible placeholder text

#### ✅ TC-UI-02: Verifying that required fields have indicator

**Test Steps:**

  1. Check label next to required fields

**Expected Result:** All required fields are marked, asterisk (*) is shown

**Actual Result:** All required fields are not marked <!--fails -->

#### ✅ TC-UI-03: Verifying field tab Navigation

**Test Steps:**

  1. Use Tab key to move between fields

**Expected Result:** Order flows logically

**Actual Result:** Order flows logically

#### ✅ TC-UI-04: Verifying password masking

**Test Steps:**

  1. Type password

**Expected Result:** Dots are shown instead of visible text

**Actual Result:** Dots are shown instead of visible text

#### ✅ TC-UI-05: Verifying that UI is responsive

**Test Steps:**

  1. Load form on mobile browser

**Expected Result:** All inputs fields and buttons are usable

**Actual Result:** All inputs fields and buttons are usable

---

## 🧪 Test Cases for Waste Management System

## 4.1 Pickup Scheduling

### ✅ TC-001: Verifying scheduling Pickup with valid inputs

1. Navigate to scheduling page
2. Enter a registered full name  e.g "John Doe"
3. Enter valid registered email e.g "<user1@test.com>"
4. Select a pick up location e.g "Nairobi"
5. Select waste type (e.g., Recyclable)
6. Choose quantity (e.g medium)
7. Choose future pick date  e.g "12/07/2025"
8. Enter any additional description (max 200 characters)
9. Click "Submit request" button

**Expected Result:** Pickup is scheduled successfully

**Actual Result:** Pickup is scheduled successfully

### ❌ TC-002: Verifying scheduling Pickup with a past date

1. Navigate to scheduling page
2. Enter a registered full name  e.g "John Doe"
3. Enter valid registered email e.g "<user1@test.com>"
4. Select a pick up location e.g "Nairobi"
5. Select waste type (e.g., Recyclable)
6. Choose quantity (e.g medium)
7. Enter a past date e.g "1/07/2025"
8. Enter any additional description  
9. Click "Submit request" button

**Expected Result:** Pickup is scheduled successfully, "date must be in the future" error message displayed

**Actual Result:** Pickup is scheduled successfully <!--fails -->

### ❌ TC-002: Attempting to Schedule a pickup with invalid email

1. Navigate to scheduling page
2. Enter a registered full name  e.g "John Doe"
3. Enter invalid registered email e.g "<user@test.com>"
4. Select a pick up location e.g "Nairobi"
5. Select waste type (e.g., Recyclable)
6. Choose quantity (e.g medium)
7. Enter a past date e.g "1/07/2025"
8. Enter any additional description  
9. Click "Submit request" button

**Expected Result:** Pickup not successfully scheduled, "invalid email" error message is displayed

**Actual Result:** Pickup is scheduled successfully <!--fails -->

### ❌ TC-003: Scheduling a pickup without selecting waste type

1. Navigate to scheduling page
2. Enter a registered full name  e.g "John Doe"
3. Enter valid registered email e.g "<user1@test.com>"
4. Select a pick up location e.g "Nairobi"
5. leave the Select waste type empty
6. Enter a future date e.g "11/07/2025"
7. Enter any additional description  
8. Click "Submit request" button

**Expected Result:** Pickup not successfully scheduled,"waste type is required" error message is displayed

**Actual Result:** Pickup not successfully scheduled,"waste type is required" error message is displayed

### ❌ TC-004: Verifying scheduling pickup without quantity

1. Leave quantity empty  
2. Fill other fields  
3. Submit request  

**Expected Result:** Pickup not successfully scheduled,"quantity is required" error message is displayed

**Actual Result:** Quantity field is missing on the "schedule pickup" page <!--critical-- >

### ❌ TC-005: Verifying scheduling pickup with too long special instructions

1. Enter 201+ characters in special instructions  
2. Fill other fields  
3. Submit request  

**Expected Result:** Pickup not successfully scheduled, "max 200 characters allowed" error message is displayed

**Actual Result:**  "Special instructions" input field is missing on the "schedule pickup" page <!--fails-->

### ❌ TC-006: Verifying scheduling pickup with hour less than 24

1. Select a date less than 24 hours in future  
2. Fill all required fields  
3. Submit request

**Expected Result:** Pickup not successfully scheduled,"must be at least 24 hours in advance" validation error is displayed

**Actual Result:** Pickup is successfully scheduled <!--fails -->

### ✅ TC-007: Verifying that available time slots are viewable

1. Go to scheduling page  
2. Choose valid pickup date

**Expected Result:** Available time slots are displayed

**Actual Result:** Available time slots are not displayed <!--fails -->

### ❌ TC-008: Verifying scheduling multiple pickups on same date

1. Schedule a pickup for a given date  
2. Attempt to schedule another pickup for same date

**Expected Result:** Only one pickup per date allowed

**Actual Result:** Multiple pickups per date allowed <!--fails -->

---

## 4.2 Request Management

### ❌ TC-009: Verifying that Pickup Request History is viewable

1. Log in as normal user
2. Schedule a waste pickup
3. Navigate to your dashboard and check on the requested pickups
4. Alternatively navigate to the user profile and check on 'My Requests'

**Expected Result:** List of all pickup requests displayed

**Actual Result:** No requests displayed. No scheduled requests were logged.

### ❌ TC-010: Verifying that Pending Pickup Request is cancellable

1. Log in as normal user
2. Schedule a waste pickup
3. Navigate to your dashboard and check on the requested pickups
4. Alternatively navigate to the user profile and check on 'My Requests'
5. Select a pending request  
6. Click cancel

**Expected Result:** Status changes to Cancelled

**Actual Result:** No pending requests displayed. No scheduled requests were logged. No request was at all logged.

### ❌ TC-011: Verifying that requests more than 24 hours away are modifiable

1. Log in as normal user
2. Schedule a waste pickup
3. Navigate to your dashboard and check on the requested pickups
4. Alternatively navigate to the user profile and check on 'My Requests'
5. Select request with pickup time more than 24 hours away  
6. Update details (e.g., quantity)

**Expected Result:** Details updated successfully

**Actual Result:** No requests displayed. No scheduled requests were logged. No request was at all logged.

### ❌ TC-012: Modifying request less than 24 hours in advance

1. Log in as normal user
2. Schedule a waste pickup
3. Navigate to your dashboard and check on the requested pickups
4. Alternatively navigate to the user profile and check on 'My Requests'
5. Select request with pickup time less than 24 hours away  
6. Attempt to modify details  

**Expected Result:** Error – modification not allowed

**Actual Result:** No requests displayed. No scheduled requests were logged. No request was at all logged.

### ❌ TC-013: Verifying that Status is displayed for request

1. Log in as normal user
2. Schedule a waste pickup
3. Navigate to your dashboard and check on the requested pickups
4. Alternatively navigate to the user profile and check on 'My Requests'
5. View request list

**Expected Result:** Each request shows status (Pending, Confirmed, Completed, Cancelled)

**Actual Result:** No requests displayed. No scheduled requests were logged. No request was at all logged.

---

## 4.3 Request Tracking

### ✅ TC-014: Verifying real-time Status Update

1. Submit pickup request  
2. Trigger status change in system (e.g., Confirmed)

**Expected Result:** Status updates reflect immediately in UI

**Actual Result:**  No pick up requests displayed hence status can't be changed. <!--fails-->


### ✅ TC-015: Verifying Notification on Status Change

1. Submit request  
2. System updates status

**Expected Result:** Notification received (email, push, etc.)

**Actual Result:** Blocked 


### ✅ TC-016: Verifying Add Feedback after completion

1. Wait for pickup completion  
2. Navigate to feedback section  
3. Submit feedback  

**Expected Result:** Feedback is recorded successfully

**Actual Result:**  Feedback is recorded successfully


## 🧪 Dashboard & Analytics Test Cases

---

## ✅ Positive Test Cases

### FR-023: Personalized Dashboard

1. **Verifying that Dashboard is displayed after user login**
    **Precondition:** User is registered and logged in
    **Steps**
     1. Open the application
     2. Enter login credentials
     3. Click the login button
     4. Navigate to the dashboard

   **Expected results :** Personalized dashboard is shown

   **Actual results:** Personalized dashboard is shown



2. **Verifying that recent pickup requests appear correctly when present**
    **Precondition:** User has made at least one pickup request
    **Steps**
     1. Login to the system
     2. Navigate to the dashboard
     3. Locate the 'Recent pickups' section

  **Expected results:** List of recent requests is visible

   **Actual results:** List of recent requests is not visible <!--fails-->

3. **Verifying that the system handles no recent pickup requests gracefully**
   **Precondition:** User has no history
   **Steps**
     1. Login to the system
     2. Open the dashboard

   **Expected Results:** Message like "No recent pickups"

   **Actual Results:** Message like "No recent pickups"

4. **Verifying that upcoming scheduled pickups are showing**
   **Precondition:** Scheduled pickups exist
   **Steps**
     1. Login to the system
     2. Open the dashboard
     3. Scroll to the 'Upcoming pickups' section

   **Expected Results:** Upcoming pickups are listed

    **Actual Results:** Upcoming pickups are not listed <!--fails-->


5. **Verifying how the system handles case with no scheduled pickups**
   **Precondition:** None scheduled
   **Steps**
     1. Login to the system
     2. Open the dashboard

   **Expected Results :** "No upcoming pickups" message shown

   **Actual Results :** "No upcoming pickups" message is not displayed <!--fails -->

6. **Verifying that environmental statistics is displayrd properly**
   **Precondition:** User has pickup history
   **Steps**
     1. Login to the system
     2. Open the dashboard
     3. Locate the 'Environmental Impact' section

   **Expected results:** Total waste, CO2 saved, and trees saved are shown

   **Actual results:** Total waste, CO2 saved, and trees saved are not displayed

7. **Verifying that achievement badges are displayed if earned**
   **Precondition:** User has earned badges
   **Steps**
     1. Login to the system
     2. Navigate to the dashboard
     3. Locate the 'Achievement Badges' section

   **Expected Results:** Badges are visible with correct labels

   **Actual Results:** Badges are not visible <!--fails-->


8. **Verifying that absence of badges is handled with friendly message**
   **Precondition:** New user
   **Steps**
     1. Login to the system
     2. Open the dashboard

   **Expected Results:** Message encouraging action appears

   **Actual Results:** Message encouraging action is not displayed.


9. **Verifying that Quick action buttons are visible and clickable**
   **Precondition:** User logged in
   **Steps:**
     1. Login to the system
     2. Navigate to the dashboard
     3. Locate the quick action buttons

   **Expected Results:** Quick action buttons are functional

   **Actaul Results:** No quick action buttons are displayed


10. **Verifying that Quick action buttons redirect to correct screens**
    **Precondition:** Buttons enabled
    **Steps**
      1. Login to the system
      2. Navigate to the dashboard
      3. Click on "Missed Pickup" button

    **Expected Results:** User is redirected to pickup form

    **Actual Results:** User is not redirected to missed pickup form <!--fails -->

---

##  Negative Test Cases

1. **Verifying Access dashboard without login**
   **Steps**
     1. Open browser
     2. Enter dashboard URL directly

   **Expected Results:** User is redirect to login page

   **Actual Results:** User is redirected to login page


2. **Verifying that Network error is displayed on dashboard**
   **Steps**
     1. Disconnect internet
     2. Open dashboard

   **Expected Results:** Network error is displayed

   **Actual Results:** Network error is displayed

3. **Verifying Pickup data fetch failure**
   **Precondition:** API down
   **Steps**
     1. Login to the system
     2. Navigate to dashboard

   **Expected Results:** Error message shown

4. **Verifying corrupted pickup record**
   **Precondition:** Incomplete data exists
   **Steps**
     1. Login to the system
     2. View dashboard

   **Expected results:** “Date unavailable” or similar fallback

    **Actual results:** Not executed

   
5. **Verifying that Quick action buttons are unresponsive**
   **Steps**
     1. Login to the system
     2. Disable JavaScript
     3. Click any quick action button

   **Expected results:** Error is handled gracefully

   **Actual  results:** Error is handled gracefully

6. **Verifying Session hijack**
   **Steps**
     1. Acquire another user’s session ID
     2. Try to access dashboard with it

   **Expected Results:** Access is denied

   **Actual Results:** Access is denied 

---

##  Edge Cases

1. **Verifying Pickup with future date**
   **Steps**
     1. Schedule pickup for a future date
     2. Open dashboard

   **Expected Results:** Pick up is handled gracefully

   **Actual Results:** Pick up is handled gracefully


2. **Verifying that single badge displayed**
   **Precondition:** One badge earned
   **Steps**
     1. Login to the system
     2. View dashboard

   **Expected Results:** Layout doesn’t break

    **Actual Results:** Layout doesn’t break

---

## 🎨 UI/UX Test Cases

1. **Verifying responsive layout on mobile/tablet**
   **Steps**
     1. Open dashboard on mobile emulator
     2. Resize and interact with elements

   **Expected Results :** UI adapts smoothly

   **Expected Results :** UI adapts smoothly

2. **Verifying loading state during data fetch**
   **Steps**
     1. Throttle network
     2. Load dashboard

   **Expected:** Loading indicator or skeleton appears


## 🧪 Gamification Test Cases

---

## ✅ Positive Test Cases

---

### 1. Verifying that badge for first pickup scheduled is awarded

 **Precondition:** The user has no previous pickups.

 **Steps:**

  1. Login to the application using valid credentials.
  2. Navigate to the **Pickup** section.
  3. Schedule a new pickup with valid details.
  4. Submit the pickup request.
  5. Navigate to the **Badges** section.

 **Expected Result:**  A badge labeled **"First Pickup Scheduled"** is awarded and visible.

 **Actual Result:** Badges section is missing <!--fails high-->

---

### 2. Verifying that badge is awarded after 10 pickups completed

 **Precondition:** The user has already completed 9 pickups.

 **Steps:**

  1. Login to the application.
  2. Schedule and complete one more pickup.
  3. Return to the dashboard or profile.
  4. Navigate to **Badges** section.

 **Expected Result:**  **"10 Pickups Completed"** badge appears in the user's badge list.

 **Actual Result:** Badges section is missing <!--fails high-->

---

### 3. Verifying Award badge for perfect recycling score

 **Precondition:** Recycling score logic is implemented.

 **Steps:**

  1. Login to the application.
  2. Schedule a pickup with correctly sorted recyclables.
  3. Submit the pickup.
  4. Check recycling score on the dashboard.
  5. Open **Badges** section.

 **Expected Result:**  Badge for **"Perfect Recycling Score"** is displayed.

 **Actual Result:** Badges section is missing <!--fails high-->

---

### 4. Verifying award badge for community contributor

 **Precondition:** User participates in community activities (e.g., referrals).

 **Steps:**

  1. Login to the application.
  2. Refer a new user or join a community cleanup event.
  3. Complete the qualifying community action.
  4. Visit the **Badges** section.

 **Expected Result:**  **"Community Contributor"** badge is awarded.

 **Actual Result:** Badges section is missing <!--fails high-->

---

### 5. Verifying award points for completed pickup

**Precondition:** Point awarding logic is enabled.

 **Steps:**

  1. Login to the application.
  2. Schedule and complete a pickup.
  3. Navigate to the user profile or dashboard.

 **Expected Result:** Points are added to the user's total.

 **Actual Result:** No points are displayed on the dashboard or under user profile.

---

### 6. Verifying that level increases after reaching point threshold

 **Precondition:** User is close to leveling up (e.g., 95/100 points).

 **Steps:**

  1. Complete an activity that awards sufficient points.
  2. Refresh the dashboard or profile page.

 **Expected Result:**  User’s level increases and reflects the new level.

 **Actual Result:**  User’s level is missing. <!--fails ->

---

### 7. Verifying View current level and points in profile

 **Precondition:** User has accumulated some points.

 **Steps:**

  1. Login to the application.
  2. Navigate to the user profile.
  3. Locate the points and level section.

**Expected Result:** Current point total and level are displayed.

**Actual Result:** Current point total and level are not displayed. <!--fails -- >

---

## Negative Test Cases

---

### 8. Verifying that badge is awarded multiple times for the same event

 **Precondition:** User has already earned the **"First Pickup Scheduled"** badge.

 **Steps:**

  1. Schedule another pickup.
  2. Refresh the badge section.

 **Expected Result:**  **"First Pickup Scheduled"** badge is not duplicated.

 **Actual Result:**  **Blocked** badge session is missing

---

### 9. Verifying that user receives points without valid activity

 **Precondition:** API or frontend vulnerability.

 **Steps:**

  1. Attempt to manipulate point API via console or external tool.

 **Expected Result:** System rejects the manipulation; points remain unchanged.

 **Actual Result:** Not executed - no point awarding logic in the application

---

### 10. Verifying that level does not update correctly after rollback

**Precondition:** Points rollback due to admin correction.

 **Steps:**

  1. Admin reduces user points below threshold.
  2. User logs in and checks level.

 **Expected Result:** Level reflects reduced points accurately.

 **Actal Result:** Not executed - no point awarding logic in the application

---

### 11. Verifying that badge is not awarded without completing valid community action

 **Steps:**

  1. Attempt to claim community badge without doing referral.
  2. Reload badge list.

 **Expected Result:** Community badge is not awarded.

 **Actual Result:** Badge section is missing


---

## 🎨 UI/UX Test Cases

---

### 12. Verifying that badge icons are unique and well labeled

 **Steps:**

  1. Navigate to **Badges** section.

 **Expected Result:** Each badge has unique icons and labels.

 **Expected Result:** Badge section is missing

---

### 13. Verifying that points and levels use consistent styles and colors

 **Steps:**

  1. View dashboard and profile.

 **Expected Result:**  Progress bar and colors match level progression.

  **Actual Result:**  No progress bar is visible.

---

### 14. Verifying responsive badge and level display on mobile devices

 **Steps:**

  1. Open app on mobile or resize browser.
  2. View badges and level display.

**Expected Result:**  All elements adjust without overflow or distortion.

**Actual Result:** Badge section is missing

---

## 📋 Test Cases for Content Management Requirements

## Blog Feature Test Cases

---

## TC-031-01: Verify the blog feature is accessible from the main navigation or homepage

**Steps:**

1. Open the system homepage.  
2. Locate and click the link/button to the blog section.

**Expected Result:** The blog section loads successfully and displays a list of blog posts.

**Actual Result:** The blog section loads successfully and displays a list of blog posts.

---

## TC-031-02: Verify that all blog posts are related to waste management topics

**Steps:**

1. Navigate to the blog section.  
2. Review the titles and content of several blog posts.

**Expected Result:** All displayed blog posts focus on waste management topics.

**Actual Result:** All displayed blog posts focus on waste management topics.

---

## TC-032-01: Verify that logged-in users can like a blog post

**Steps:**

1. Log in to the system with a valid user account.  
2. Navigate to the blog section.  
3. Select any blog post.  
4. Click the "Like" button on the blog post.

**Expected Result:** The like count on the blog post increases by one.

**Actual Result:** The "Like" button is missing

---

## TC-032-02: Verify that the like count increases when a user likes a post

**Steps:**

1. Note the current like count of a blog post.  
2. Click the "Like" button.  
3. Observe the like count.

**Expected Result:** The like count increments by one after liking.

**Actual Result:** The "Like" button is missing

---

## TC-032-03: Verify that users can add comments on blog posts

**Steps:**

1. Log in to the system with a valid user account.  
2. Navigate to a blog post.  
3. Enter a comment in the comment box.  
4. Click "Submit."

**Expected Result:** User Should be able to comment on the blog

**Actual Result:**  Users can comment on the blog

---

## TC-032-04: Verify that comments appear under the correct blog post

**Steps:**

1. Navigate to a specific blog post.  
2. Add a comment and submit.  
3. Navigate away and then back to the same post.

**Expected Result:** The comment should appear only under the blog post it was added to.

**Actual Result:** The comment appears only under the blog post it was added to.

---

## TC-032-05: Verify that users can share blog posts via social media or a shareable link

**Steps:**

1. Navigate to a blog post.  
2. Click the "Share" button or icon.  
3. Select a social media platform or copy the shareable link.

**Expected Result:** The blog post should be shareable correctly using the selected method.

**Actual Result:** The blog post can be shared correctly using the selected method.

---

## TC-032-06: Verify that non-logged-in users are prompted to log in when trying to like, comment, or share (if restricted)

**Steps:**

1. Log out or open the blog in an incognito browser.  
2. Attempt to like, comment, or share a blog post.

**Expected Result:** The system prompts the user to log in before performing the action.

**Actual Result:** The system does not prompts the user to log in before performing the action.

---

## TC-033-01: Verify that only authorized users can access the blog post creation interface

**Steps:**

1. Log in as a regular user.  
2. Attempt to navigate to the blog post creation page.  
3. Log in as an authorized user and navigate to the same page.

**Expected Result:** Only the authorized user can access the blog post creation interface.

**Actual Result:** The blog post creation interface is not available.

---

## TC-033-02: Verify authorized users can create a new blog post

**Steps:**

1. Log in as an authorized user.  
2. Navigate to the blog creation page.  
3. Enter a title, content, categories, and tags.  
4. Click "Publish."

**Expected Result:** The new blog post is visible in the blog listing.

**Expected Result:** The blog post creation interface is not available.

---

## TC-033-03: Verify authorized users can edit existing blog posts

**Steps:**

1. Log in as an authorized user.  
2. Navigate to an existing blog post management page.  
3. Make changes to the blog post content.  
4. Save the changes.

**Expected Result:** The blog post is updated with the new content.

**Actual Result:** Users can't update the existing blog posts

---

## TC-033-04: Verify authorized users can publish or unpublish blog posts

**Steps:**

1. Log in as an authorized user.  
2. Create or select a blog post.  
3. Change its status to "published" or "unpublished."  
4. Save the change.

**Expected Result:** The post visibility reflects the published/unpublished status accordingly.

**Actual Result:** Users can't publish or unpublish blog posts

---

## TC-033-05: Verify authorized users can delete blog posts

**Steps:**

1. Log in as an authorized user.  
2. Select a blog post.  
3. Click "Delete" and confirm.

**Expected Result:** The blog post is removed from the system.

**Actual Result:** Authorized users cannot delete blog posts.

---

## TC-033-06: Verify unauthorized users cannot create, edit, publish, or delete blog posts

**Steps:**

1. Log in as a regular user.  
2. Attempt to access create, edit, publish, or delete features.

**Expected Result:** Access is denied or these options are not visible.

**Actual Result:** Regular users can create or delete any post.

---

## TC-034-01: Verify users can assign one or more categories to a blog post

**Steps:**

1. Log in as an authorized user.  
2. Create or edit a blog post.  
3. Assign one or more categories.  
4. Save the post.

**Expected Result:**  The assigned categories are saved and displayed with the blog post.

**Actual Result:**  Users cannot assign any categories

---

## TC-034-02: Verify users can add multiple tags to a blog post

**Steps:**

1. Log in as an authorized user.  
2. Create or edit a blog post.  
3. Add multiple tags.  
4. Save the post.

**Expected Result:** The tags are saved and displayed with the blog post.

**Actual Result:** User cannot add any tags the blog post.

---

## TC-034-03: Verify users can filter blog posts by category

**Preconditions:**

- User is logged in
- Blog posts with tags exist.

**Steps:**

1. Navigate to the blog section.  
2. Select a category from the filter menu.

**Expected Result:**  Only blog posts in the selected category should be displayed.

**Actual Result:**  Only blog posts in the selected category are displayed.

---

## TC-034-04: Verify users can filter blog posts by tag

**Preconditions:**

- user is logged in
- Blog posts with categories and tags exist.

**Steps:**

1. Navigate to the blog section.  
2. Select a tag from the filter menu.

**Expected Result:**  Only blog posts with the selected tag should be displayed.

**Actual Result:**  Only blog posts with the selected tag are displayed.

---

## TC-034-05: Verify that categories and tags are displayed clearly on each blog post

**Steps:**

1. Navigate to any blog post.  
2. Observe the categories and tags shown.

**Expected Result:** Categories and tags should be visible and correctly linked/displayed on the post.

**Actual Result:** Categories and tags are visible and correctly linked/displayed on the post.

---

## TC-036-01: Verify that eco tips rotate every 5 seconds

**Preconditions:**  

- User is on the page where eco tips are displayed.

**Steps:**  

1. Navigate to the page displaying eco tips.  
2. Observe the eco tips section for at least 15 seconds.

**Expected Result:**  Eco tips should rotate to the next tip every 5 seconds.

**Actual Result:**  Eco tips rotates to the next tip every 5 seconds.

---

## TC-037-01: Verify that users can start an interactive environmental quiz

**Preconditions:**  

- User is logged in (if system requires login to take quizzes).

**Steps:**  

1. Navigate to the quizzes section.  
2. Select an environmental quiz.  
3. Start the quiz.

**Expected Result:** The quiz should load and users interact with the questions.

**Actual Result:** The quiz loads and users can interact with the questions.

---

## TC-038-01: Verify that the system tracks quiz scores

**Preconditions:**  

- User is currently taking a quiz.

**Steps:**  

1. Complete all questions in an environmental quiz.  
2. Submit the quiz.

**Expected Result:** The system should displays the quiz score correctly.

**Actual Result:** The system displays the quiz score correctly.

---

## TC-038-02: Verify that explanations are provided for quiz answers

**Preconditions:**  

- User has submitted a completed quiz.

**Steps:**  

1. Review the answers and explanations provided after quiz submission.

**Expected Result:**  Each answer should be accompanied by a clear explanation.

**Actual Result:**  Each answer is accompanied by a clear explanation.

---

## TC-039-01: Verify that environmental infographics with statistics are displayed

**Preconditions:**  

- User navigates to the infographics section or page.

**Steps:**  

1. Open the environmental infographics page.

**Expected Result:** Infographics with relevant environmental statistics should be visible and clear.

**Actual Result:** Infographics with relevant environmental statistics are visible and clear.

---

## TC-040-01: Verify that action buttons link to other features

**Preconditions:**  

- User is on a page containing action buttons.

**Steps:**  

1. Click each action button (e.g., “Go to Blog,” “Start Quiz,” “View Infographics”).

**Expected Result:** Each button should redirect the user to the correct corresponding feature or page.

**Actual Result:** Each button redirects the user to the correct corresponding feature or page.

---

## TC-041-01: Verify that users can create community posts

**Preconditions:**  

- User is logged in.

**Steps:**  

1. Navigate to the community section.  
2. Click the "Create Post" button.  
3. Enter text for the post.  
4. Click "Submit" or "Post."

**Expected Result:**  The post should appears in the community feed.

**Actual Result:**  The post appears in the community feed.

---

## TC-042-01: Verify that users can like a community post

**Preconditions:**  

- User is logged in.  
- At least one community post exists.

**Steps:**  

1. Navigate to the community feed.  
2. Click the "Like" button on a post.

**Expected Result:**  The like count for the post should increase by one.

**Actual Result:**  The like count for the post decreases by one. <!--fails-->

---

## TC-042-02: Verify that users can comment on a community post

**Preconditions:**  

- User is logged in.  
- At least one community post exists.

**Steps:**  

1. Navigate to the community feed.  
2. Select a post.  
3. Enter a comment and submit.

**Expected Result:** The comment should appear under the selected post.

**Actual Result:** The comment appears under the selected post.

---

## TC-043-01: Verify that community posts are displayed in chronological order

**Preconditions:**  

- Multiple community posts exist with different timestamps.

**Steps:**  

1. Navigate to the community feed.  
2. Observe the order of posts.

**Expected Result:**  Posts should be displayed from newest to oldest.

**Actual Result:**  Posts are displayed from newest to oldest.

---

## TC-044-01: Verify that users can share tips and experiences in community posts

**Preconditions:**  

- User is logged in.

**Steps:**  

1. Navigate to the community section.  
2. Click "Create Post."  
3. Enter a tip or experience in the text field.  
4. Click "Submit."

**Expected Result:** The tip or experience is posted and should be visible in the community feed.

**Actual Result:** The tip or experience is posted and visible in the community feed.

---

## Community Features – User Profile Test Cases

---

## TC-045-01: Verify that users can view their profile information

**Preconditions:**  

- User is logged in.

**Steps:**  

1. Navigate to the user profile page.

**Expected Result:**  The profile page should display the user’s information (name, email etc.).

**Actual Result:**  The profile page displays the user’s information (name, email.).

---

## TC-045-02: Verify that users can edit their profile information

**Preconditions:**  

- User is logged in.

**Steps:**  

1. Go to the profile page.  
2. Click “Edit Profile.”  
3. Change any editable field (e.g., name, bio).  
4. Save the changes.

**Expected Result:** Profile information should be updated and displayed correctly.

**Actual Result:** Profile information is updated and displayed correctly.

---

## TC-046-01: Verify that profile displays total pickups

**Preconditions:**  

- User has completed at least one pickup.

**Steps:**  

1. Navigate to the user profile page.

**Expected Result:**  Total pickups should be displayed as a numeric value.

**Actual Result:**  Total pickups are not displayed <!--fails-->

---

## TC-046-02: Verify that profile displays CO₂ saved

**Preconditions:**  

- User has completed at least one pickup contributing to CO₂ savings.

**Steps:**  

1. Navigate to the user profile page.

**Expected Result:** CO₂ saved is displayed with appropriate units (e.g., kg).

**Actual Result:** CO₂ saved is not displayed <!--fails -->

---

## TC-046-03: Verify that monthly activity charts are displayed

**Preconditions:**  

- User has activity data for one or more months.

**Steps:**  

1. Go to the profile page.  
2. Locate the activity chart section.

**Expected Result:** A chart showing monthly activity should be visible and reflect user data.

**Actual Result:** A chart showing monthly activity is visible and reflects user data.

---

## TC-047-01: Verify that users can upload a profile picture

**Preconditions:**  

- User is logged in.

**Steps:**  

1. Go to the profile page.  
2. Click the “Upload Profile Picture” option.  
3. Select and upload an image file.  
4. Save the changes.

**Expected Result:** The uploaded profile picture should be displayed on the profile.

**Actual Result:** The uploaded profile picture is displayed on the profile.

---

## TC-048-01: Verify that user statistics and environmental impact are shown

**Preconditions:**  

- User has completed pickups or eco-actions recorded in the system.

**Steps:**  

1. Navigate to the user’s profile page.

**Expected Result:**  Statistics such as CO₂ saved, waste diverted, or participation metrics should be displayed on the profile.

**Actual Result:**  Statistics such as CO₂ saved, waste diverted, or participation metrics are not displayed on the profile. <!--fails-->

---

## Social Features Test Cases

---

## TC-049-01: Verify that users can follow other community members

**Preconditions:**  

- User is logged in.  
- At least one other user profile is accessible.

**Steps:**  

1. Navigate to another user's profile.  
2. Click the “Follow” button.

**Expected Result:** The user is now following the selected community member.

**Actual Result:** Other users profile are not accessible

---

## TC-050-01: Verify that the news feed displays community activities

**Preconditions:**  

- User is logged in.  
- Followed users or general community members have recent activity.

**Steps:**  

1. Navigate to the news feed section.

**Expected Result:** The news feed should display posts and activities (e.g., new posts, achievements) in chronological order.

**Actual Result:** The news feed displays posts and activities (e.g., new posts, achievements) in chronological order.

---

## TC-051-01: Verify that users can share achievements and milestones

**Preconditions:**  

- User is logged in.  
- User has at least one achievement or milestone (e.g., number of pickups, CO₂ saved).

**Steps:**  

1. Navigate to the profile or achievements section.  
2. Click “Share” on an achievement.  
3. Confirm sharing.

**Expected Result:**  The selected achievement is posted to the community/news feed.

**Actual Result:**  No achievement are available

---

## TC-052-01: Verify that community challenges and events are supported

**Preconditions:**  

- Admin has created at least one active community challenge or event.

**Steps:**  

1. Navigate to the “Challenges” or “Events” section.  
2. View available challenges.  
3. Click to join or participate.

**Expected Result:**  The user is registered or marked as a participant in the selected community challenge or event.

**Actual Result:**  "Challenges" section is missing <!--fails -->
---

## Administrative Functions – Request Management Test Cases

---

## TC-053-01: Verify that admins can view all pickup requests

**Preconditions:**  

- Admin user is logged in.  
- At least one pickup request exists in the system.

**Steps:**  

1. Navigate to the admin dashboard.  
2. Click on the “Pickup Requests” section.

**Expected Result:**  All pickup requests should be displayed in a table.

**Actual Result:**  All pickup requests are displayed in a list or table.

---

## TC-054-01: Verify that admins can approve a pickup request

**Preconditions:**  

- Admin is logged in.  
- At least one pending pickup request exists.

**Steps:**  

1. Go to the pickup requests section.  
2. Select a pending request.  
3. Click the “Approve” option.

**Expected Result:**  The request status should change to “Approved.”

**Actual Result:**  Admin cannot approve a pick up request <!--fails -->

---

## TC-054-02: Verify that admins can reject a pickup request

**Preconditions:**  

- Admin is logged in.  
- At least one pending pickup request exists.

**Steps:**  

1. Go to the pickup requests section.  
2. Select a pending request.  
3. Click the “Reject” option.

**Expected Result:**  The request status should change to “Rejected.”

**Expected Result:**   Admin cannot reject a pick up request <!--fails-- >

---

## TC-054-03: Verify that admins can modify a pickup request

**Preconditions:**  

- Admin is logged in.  
- At least one pickup request exists.

**Steps:**  

1. Navigate to a specific pickup request.  
2. Click “Edit” or “Modify.”  
3. Change the desired details (e.g., location, notes).  
4. Save the changes.

**Expected Result:**  The updated request should reflect the modifications made.

**Actual Result:**  No pickup request are displayed <!--fails -->

---

## TC-055-01: Verify that admins can assign pickup dates and times

**Preconditions:**  

- Admin is logged in.  
- A pickup request is pending or unassigned.

**Steps:**  

1. Open a pickup request.  
2. Enter or select the pickup date and time.  
3. Save the assignment.

**Expected Result:**  The request should show the assigned date and time.

**Actual Result:**  No request the admin can modify

---

## TC-056-01: Verify that admins can filter pickup requests

**Preconditions:**  

- Admin is logged in.  
- Multiple pickup requests exist with varying statuses or attributes.

**Steps:**  

1. Go to the pickup requests section.  
2. Apply a filter (e.g., by status, date, user).

**Expected Result:**  The list should update to show only requests matching the filter criteria.

**Actual Result:**  The list updates to show only requests matching the filter criteria.

---

## TC-056-02: Verify that admins can search pickup requests

**Preconditions:**  

- Admin is logged in.  
- At least one pickup request exists with searchable attributes.

**Steps:**  

1. Enter a keyword or request ID in the search bar.  
2. Submit the search.

**Expected Result:**  Relevant pickup request should match the search term are displayed.

**Actual Result:**  Admin cannot search pickup requests <!--fail -->

---

## Administrative Functions – User Management Test Cases

---

## TC-057-01: Verify that admins can view all registered users

**Preconditions:**  

- Admin is logged in.  
- At least one user is registered in the system.

**Steps:**  

1. Navigate to the admin dashboard.  
2. Click on the “User Management” or “Users” section.

**Expected Result:** A list of all registered users is displayed.

**Actual Result:** Admins cannot see list of all registered users.

---

## TC-058-01: Verify that admins can change user roles

**Preconditions:**  

- Admin is logged in.  
- At least one user exists with a modifiable role.

**Steps:**  

1. Go to the user management section.  
2. Select a user.  
3. Click “Edit Role.”  
4. Change the user’s role (e.g., from User to Moderator).  
5. Save the changes.

**Expected Result:**  The selected user’s role is updated and reflected in their profile.

**Actual Result:**  Admins cannot change user roles.

---

## TC-059-01: Verify that admins can suspend user accounts

**Preconditions:**  

- Admin is logged in.  
- At least one active user exists.

**Steps:**  

1. Navigate to the user management section.  
2. Select an active user.  
3. Click “Suspend Account.”  
4. Confirm the action.

**Expected Result:**  The user’s account status changes to “Suspended.”

**Actual Result:**  Admin cannot suspend registered user accounts

---

## TC-059-02: Verify that admins can delete user accounts

**Preconditions:**  

- Admin is logged in.  
- At least one user exists.

**Steps:**  

1. Go to the user management section.  
2. Select a user.  
3. Click “Delete Account.”  
4. Confirm the deletion.

**Expected Result:**  The user account is permanently removed from the system.

**Actual Result:**  Admins cannot delete user accounts

---

## TC-060-01: Verify that the system provides user activity reports

**Preconditions:**  

- Admin is logged in.  
- Users have engaged in actions tracked by the system (e.g., logins, pickups, posts).

**Steps:**  

1. Navigate to the “Reports” or “Analytics” section.  
2. Open the user activity report.

**Expected Result:**  The report displays user activities such as logins, posts, pickups, or other tracked actions.

**Atual Result:**  The system does not provide user activity reports.

---

## Content Moderation Test Cases

---

## TC-061-01: Verify that admins can moderate community posts and comments

**Preconditions:**  

- Admin is logged in.  
- Community posts or comments exist.

**Steps:**  

1. Navigate to the admin dashboard.  
2. Open the moderation panel or community content section.  
3. Select a post or comment.  
4. Review and choose to approve, edit, or take action.

**Expected Result:**  The admin can perform moderation actions (e.g., edit, hide, or flag) on posts or comments.

**Actual Result:**  The admin cannot perform moderation actions (e.g., edit, hide, or flag) on posts or comments. <!--fails-->

---

## TC-062-01: Verify that admins can delete inappropriate content

**Preconditions:**  

- Admin is logged in.  
- At least one post or comment is marked or identified as inappropriate.

**Steps:**  

1. Go to the moderation panel.  
2. Locate the flagged or reported content.  
3. Click “Delete” on the content.  
4. Confirm the deletion.

**Expected Result:** The selected inappropriate content should be removed from the system.

**Actual Result:** Admin cannot delete inappropriate content <!--fails-->

---

## TC-063-01: Verify that users can flag or report content

**Preconditions:**  

- User is logged in.  
- Community content is visible.

**Steps:**  

1. Navigate to a community post or comment.  
2. Click the “Flag” or “Report” button.  
3. Select a reason and submit the report.

**Expected Result:**  The content is flagged and appears in the admin moderation queue.

**Actual Result:** Users cannot  flag or report content <!--fails -->

---

## TC-064-01: Verify that admins can create announcements

**Preconditions:**  

- Admin is logged in.

**Steps:**  

1. Navigate to the “Announcements” section in the admin dashboard.  
2. Click “Create Announcement.”  
3. Enter the announcement title and content.  
4. Click “Publish.”

**Expected Result:**  The announcement is visible to users in the appropriate section (e.g., dashboard, news feed).

**Actual Result:**  Admin cannot create announcement <!--fails -->

---

## Notification System – Test Cases

---

## TC-065-01: Verify that the notification bell displays unread count

**Preconditions:**  

- User is logged in.  
- At least one unread notification exists.

**Steps:**  

1. Navigate to any page with the notification bell.  
2. Observe the notification icon.

**Expected Result:** The notification bell displays a badge showing the number of unread notifications.

---

## TC-066-01: Verify that pickup confirmations and updates trigger notifications

**Preconditions:**  

- User has submitted a pickup request.  
- Admin has updated the request status.

**Steps:**  

1. Submit a pickup request.  
2. Wait for admin to approve, modify, or update the request.  
3. Check notifications.

**Expected Result:** A notification appears indicating the update to the pickup request.

---

## TC-066-02: Verify that new blog posts trigger notifications

**Preconditions:**  

- User is logged in.  
- A new blog post has been published.

**Steps:**  

1. Log in after a new blog post is published.  
2. Check the notifications panel.

**Expected Result:** A notification for the new blog post is displayed.

---

## TC-066-03: Verify that community interactions trigger notifications

**Preconditions:**  

- User is logged in.  
- User has a community post or comment.

**Steps:**  

1. Another user likes or comments on your post.  
2. Open your notifications.

**Expected Result:** A notification is shown for the community interaction.

---

## TC-066-04: Verify that achievement unlocks trigger notifications

**Preconditions:**  

- User is logged in.  
- User has completed an action that qualifies for an achievement.

**Steps:**  

1. Complete a qualifying activity (e.g., 10th pickup).  
2. Open notifications.

**Expected Result:** A notification appears for the unlocked achievement.

---

## TC-067-01: Verify that users can mark notifications as read

**Preconditions:**  

- User is logged in.  
- At least one unread notification exists.

**Steps:**  

1. Open the notifications panel.  
2. Click on or mark a notification as “Read.”

**Expected Result:**  The notification status should update, and it is no longer marked as unread.

**Actual Result:**  The notification history shows zero notifications.

---

## TC-068-01: Verify that notification history is available

**Preconditions:**  

- User is logged in.  
- User has received previous notifications.

**Steps:**  

1. Navigate to the full notification history or archive section.

**Expected Result:**  The user should be able to view a chronological list of past notifications.

**Actual Result:**  The user can view a chronological list of past notifications.

---

## ✅ User Interface Requirements – Test Cases

---

### TC-069-01: Verify that the system is responsive on desktop screens (1920x1080+)

**Preconditions:**  

- User accesses the system using a desktop browser.

**Steps:**  

1. Open the application on a desktop screen (1920x1080 resolution or higher).  
2. Navigate through various sections.

**Expected Result:** The layout should be displayed correctly and adapt to the desktop screen size.

**Actual Result:** The layout is displayed correctly and adapts to the desktop screen size.

---

### TC-069-02: Verify that the system is responsive on tablet screens (768px–1024px)

**Preconditions:**  

- User accesses the system using a tablet device.

**Steps:**  

1. Open the application on a tablet.  
2. Navigate through different components and menus.

**Expected Result:** Interface should adjusts correctly to tablet dimensions and remains functional.

**Actual Result:** Interface adjusts correctly to tablet dimensions and remains functional.

---

### TC-069-03: Verify that the system is responsive on mobile screens (320px–767px)

**Preconditions:**  

- User accesses the system using a mobile device.

**Steps:**  

1. Launch the system on a mobile browser.  
2. Browse key pages such as home, navigation, and forms.

**Expected Result:** The layout and functionality should be optimized for mobile screen sizes.

**Actual Result:** The layout and functionality are optimized for mobile screen sizes.

---

### TC-070-01: Verify that all features work across screen sizes

**Preconditions:**  

- System is accessible on desktop, tablet, and mobile.

**Steps:**  

1. Perform the same core tasks (e.g., submitting a form) on each screen size.  
2. Observe functionality and layout behavior.

**Expected Result:**  The system should maintain the same core features and functions on all screen sizes.

**Actual Result:**  The system maintains the same core features and functions on all screen sizes.

---

## 10.2 Accessibility Test Cases

### TC-071-01: Verify that the system meets WCAG 2.1 AA standards

**Preconditions:**  

- System is evaluated using accessibility audit tools.

**Steps:**  

1. Run a WCAG compliance test using a tool like WAVE or axe.  
2. Review any violations reported.

**Expected Result:** The system should not contain critical WCAG 2.1 AA accessibility issues.

**Actual Result:** The system contains critical WCAG 2.1 AA accessibility issues (contrast ratio failing) <!--fails-->

---

### TC-072-01: Verify that the system supports full keyboard navigation

**Preconditions:**  

- User is on a device with a physical keyboard.

**Steps:**  

1. Use Tab, Shift+Tab, and Enter keys to navigate the interface.  
2. Interact with buttons, forms, and menus.

**Expected Result:** All interactive elements should be accessible via keyboard.

**Actual Result:** All interactive elements are keyboard accessible.

---

### TC-073-01: Verify that all images include descriptive alt text

**Preconditions:**  

- At least one image exists on the page.

**Steps:**  

1. Inspect images using a screen reader or browser dev tools.  
2. Look for presence and relevance of alt text.

**Expected Result:** All images should have meaningful and relevant `alt` attributes.

**Actual Result:** All images have meaningful and relevant `alt` attributes.

---

### TC-074-01: Verify that the system is compatible with screen readers

**Preconditions:**  

- Screen reader software is active.

**Steps:**  

1. Navigate through the system using a screen reader.  
2. Listen to the output for accuracy and flow.

**Expected Result:**  Content should be read correctly, with proper labels and headings.

---

## 10.3 Navigation

### TC-075-01: Verify that the system provides a clear and consistent navigation menu

**Preconditions:**  

- User is logged in.

**Steps:**  

1. Open the main navigation menu.  
2. Review labels and test each navigation link.

**Expected Result:** The menu should be clearly structured and functional.

**Actual Result:** The nav menu is clearly structured and functional.

---

### TC-076-01: Verify that breadcrumbs are displayed on complex pages

**Preconditions:**  

- User is on a multi-level or nested page.

**Steps:**  

1. Navigate to a detailed or inner page (e.g., post details).  
2. Observe the breadcrumb trail.

**Expected Result:**  Breadcrumbs should be present and correctly represents the page structure.

**Actual Result:** No breadcrumbs are present

---

### TC-077-01: Verify that search functionality works where available

**Preconditions:**  

- Page includes a search feature.

**Steps:**  

1. Enter a search keyword.  
2. Submit the query.  
3. Review the results.

**Expected Result:** search results are returned should be relevant and accurate 

**Actual Result:** search results returned are relevant and accurate 

---

## 11.1 Data Persistence Test Cases

### TC-078-01: Verify that the system stores user data in browser localStorage

**Preconditions:**  

- User performs an action that triggers data storage (e.g., form submission, preferences).

**Steps:**  

1. Complete and submit a form or action that stores data.  
2. Open browser dev tools → Application tab → localStorage.  
3. Inspect stored key-value pairs.

**Expected Result:**  User data should be correctly saved in localStorage.

**Actual Result:**  User data is not correctly saved in localStorage.<!--fails-->

---

### TC-079-01: Verify that data is maintained across browser sessions

**Preconditions:**  

- User data has been stored in localStorage.

**Steps:**  

1. Close the browser.  
2. Reopen the browser and revisit the site.  
3. Check for restored user data or preferences.

**Expected Result:** Previously stored data should persists after the browser is closed and reopened.

**Actual Result:** Previously stored data does not persists after the browser is closed and reopened.<!--fails -->

---

### TC-080-01: Verify that the system handles localStorage limits gracefully

**Preconditions:**  

- Browser storage quota is close to full.

**Steps:**  

1. Simulate or manually fill localStorage close to capacity.  
2. Attempt an action that requires additional localStorage.  
3. Observe system behavior.

**Expected Result:** The system should provide an appropriate warning or fallback without crashing.

**Actual Result:** Not executed

---

## 11.2 Data Validation Test Cases

### TC-081-01: Verify that user input is validated before processing

**Preconditions:**  

- A form or input field exists (e.g., registration, comment form).

**Steps:**  

1. Submit the form with invalid inputs (e.g., empty required fields, invalid email).  
2. Observe the response.

**Expected Result:** Input validation should before the form is submited and error messages are displayed.

**Actual Result:** Input validation occurs before the form is submited and appropriate error messages are displayed

---

### TC-082-01: Verify that the system prevents SQL injection and XSS attacks

**Preconditions:**  

- User input field exists (e.g., text field or comment box).

**Steps:**  

1. Attempt to inject SQL code (`' OR '1'='1`) or a script tag (`<script>alert('x')</script>`).  
2. Submit the form.  
3. Check if input is executed or interpreted.

**Expected Result:** Malicious input should be rejected or sanitized, and no injection occurs.

**Actual Result:** Malicious input is not rejected <!--fails -->

---

### TC-083-01: Verify that user-generated content is sanitized before display

**Preconditions:**  

- A feature exists where users submit content (e.g., community posts, comments).

**Steps:**  

1. Submit a post or comment containing HTML/script elements.  
2. View the content in the user interface.

**Expected Result:** The content should be sanitized and unsafe elements (e.g., scripts) are not rendered.

**Actual Result:**  The content is not sanitized and unsafe elements (e.g., scripts) are rendered.

---

## 🚀 Performance Test Cases

---

### TC-084-01: Verify that pages load within 3 seconds on a standard internet connection

**Preconditions:**  

- User has a standard broadband connection (5–10 Mbps).  
- Caching is cleared or disabled.

**Steps:**  

1. Open the application in a browser.  
2. Use browser developer tools → Network tab to measure page load time.  
3. Navigate to pages like Home, Dashboard, and Blog.

**Expected Result:**  Each page should fully load within 3 seconds, as reported in the browser’s performance panel.

**Actual Result:**  Each page fully loads within 3 seconds, as reported in the browser’s performance panel.

---

### TC-085-01: Verify that the system responds to user interactions within 1 second

**Preconditions:**  

- Application is fully loaded.  
- User is authenticated if necessary.

**Steps:**  

1. Click interactive elements such as buttons, links, and tabs (e.g., submit a form or open a dropdown).  
2. Measure time between action and visible feedback (e.g., new content appearing, modal opening, confirmation shown).

**Expected Result:**  The system should show a visible response to each user interaction within 1 second (1000 milliseconds)

**Actual Result:**  The system shows a visible response to each user interaction within 1 second (1000 milliseconds)


---

### ✅ Browser Compatibility – Test Cases

---

### TC-086-01 – Verify that the system functions correctly on Google Chrome (latest 2 versions)

**Requirement ID:** FR-086  
**Preconditions:**  

- Google Chrome (latest or one version prior) is installed.

**Test Steps:**  

1. Launch the system using Google Chrome.  
2. Navigate through key pages (Home, Dashboard, Blog, Community).  
3. Interact with UI components: buttons, forms, modals, menus.  
4. Submit a form and observe result.  
5. Check layout, media, and responsiveness.

**Expected Result:** All features should work correctly, pages display properly, and no visual or functional issues occur in Chrome.

**Actual Result:** All features works correctly, pages display properly, and no visual or functional issues occur in Chrome.

---

### TC-086-02 – Verify that the system functions correctly on Mozilla Firefox (latest 2 versions)

**Preconditions:**  

- Mozilla Firefox (latest or one version prior) is installed.

**Test Steps:**  

1. Open the system in Firefox.  
2. Repeat core flows: navigation, form submission, interaction with UI components.  
3. Inspect visual layout and responsiveness.

**Expected Result:** All functions should operate normally and the layout should be consistent in Firefox.

**Actual Result:** All functions operates normally and the layout is consistent in Firefox.

---

### TC-086-03 – Verify that the system functions correctly on Safari (latest 2 versions)

**Preconditions:**  

- Safari (latest or one version prior) is available (macOS or iOS).

**Test Steps:**  

1. Access the system in Safari.  
2. Perform key tasks (login, navigation, blog interaction).  
3. Inspect responsiveness and check for rendering issues.

**Expected Result:** The system should behave consistently and render correctly in Safari.

**Actual Result:**  The system behaves consistently and renders correctly in Safari.

---

### TC-086-04 – Verify that the system functions correctly on Microsoft Edge (latest 2 versions)

**Preconditions:**  

- Microsoft Edge (latest or one version prior) is installed.

**Test Steps:**  

1. Launch Microsoft Edge and open the application.  
2. Complete major actions (view blog, submit a request, post in community).  
3. Check layout and UI alignment.

**Expected Result:**  The system should work properly and consistently in Edge with no errors or broken visuals.

**Expected Result:**  The system works properly and consistently in Edge with no errors or broken visuals.

---

## 📋 Error Handling Requirements – Test Cases

---

### TC-087-01 – Verify that the system displays clear, actionable error messages

**Preconditions:**  

- User performs an invalid action (e.g., incorrect login, empty form submission).

**Test Steps:**  

1. Attempt to log in with invalid credentials.  
2. Leave required form fields empty and try to submit.  
3. Observe the error messages displayed.

**Expected Result:**  Error messages should clearly describe the issue and suggest how to correct it (e.g., "Password is incorrect.").

**Actual Result:**  Error messages clearly describe the issue and suggest how to correct it (e.g., "Password is incorrect.").

---

### TC-088-01 – Verify that the system provides guidance for resolving common issues

**Preconditions:**  

- A user triggers a common error (e.g., file too large, invalid format).

**Test Steps:**  

1. Attempt to upload a file that exceeds size limits or uses an unsupported format.  
2. Observe feedback or help links provided by the system.

**Expected Result:**  The system should show guidance like: "Upload must be under 5MB. Only JPG and PNG formats are supported."

**Actual Result:**  The system shows guidance like: "Upload must be under 5MB. Only JPG and PNG formats are supported."


---

### TC-089-01 – Verify that the system handles network errors gracefully

**Preconditions:**  

- Network connection is lost or interrupted.

**Test Steps:**  

1. Simulate a network disconnection.  
2. Attempt to perform actions like submitting a form or saving changes.  
3. Observe the system behavior.

**Expected Result:** The system should shows a message like “Connection lost. Please check your network and try again” without crashing or losing user input.

**Actual Result:** The system shows error message “Connection lost. Please check your network and try again” without crashing or losing user input.

---

## 13.2 Form Validation Test Cases

### TC-090-01 – Verify that form inputs are validated in real-time

**Preconditions:**  

- A form with real-time validation is available.

**Test Steps:**  

1. Enter invalid data (e.g., invalid email) into a form field.  
2. Observe if validation triggers before submission.

**Expected Result:**  The system should provide instant feedback (e.g., “Please enter a valid email address”) without waiting for form submission.

**Actual Result:**  The system does not provide instant feedback (e.g., “Please enter a valid email address”) without waiting for form submission.

---

### TC-091-01 – Verify that form submission is blocked with invalid data
  
**Preconditions:**  

- A form with required fields and validation rules is displayed.

**Test Steps:**  

1. Leave required fields empty or enter invalid input.  
2. Attempt to submit the form.

**Expected Result:** The form should not submitted and validation errors should be displayed, preventing incomplete or incorrect submissions.

**Actual Result:** The form should is not submitted and validation errors are displayed, preventing incomplete or incorrect submissions.

---

### TC-092-01 – Verify that validation errors are highlighted clearly

**Preconditions:**  

- User fills a form incorrectly.

**Test Steps:**  

1. Enter invalid or incomplete data in form fields.  
2. Try to submit the form.  
3. Observe the error indicators.

**Expected Result:** Invalid fields should be clearly highlighted (e.g., red border or icon), and error messages are shown near the relevant input.

**Actual Result:**  Invalid fields are clearly highlighted (e.g., red border or icon), and error messages are shown near the relevant input.

---
