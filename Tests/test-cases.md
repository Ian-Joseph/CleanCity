## 🧪 Test Cases for CleanCity - Waste Pickup Scheduler Web App

# 📄 Introduction

This document outlines the comprehensive set of test cases designed to validate the functionality, performance, and reliability of the application under test. Each test case has been developed based on the system’s requirements and user expectations to ensure that all features behave as intended across various scenarios. 

The test cases cover both **functional** and **non-functional** aspects of the system, enabling consistent quality assurance and traceability throughout the testing lifecycle.

---

### 🔐 Registration Test Cases

#### ✅ TC-R-01: Verifying user registration with Valid Inputs
- **Preconditions:** User is on the Register page
- **Test Steps:**
  1. Enter full name: "New Test User"
  2. Enter email: "newuser@test.com"
  3. Enter password: "NewPass123"
  4. Confirm password: "NewPass123"
  5. Click "Register" button
- **Expected Result:** Account is successfully created; user redirected to login with a success message

#### ❌ TC-R-02: Verifying user registration with missing name field
- **Test Steps:**
  1. Leave the name field blank
  2. Enter email: "newuser@test.com"
  3. Enter password: "NewPass123"
  4. Confirm password: "NewPass123"
  5. Click "Register" button
- **Expected Result:** Error displayed: "Full Name is required"

#### ❌ TC-R-03: Verifying user registration with an already existing email
**Test Steps:**
  1.Enter full name: "New Test User"
  2. Use an existing email: "user1@cleancity.com"
  3.Enter password: "NewPass123".
  4.Confirm password: "TestPass123"
  4. Click "Register" button
  
**Expected Result:** Error displayed: "Email already exists"

#### ❌ TC-R-04: Verifying user registration with password mismatch
**Test Steps:**
  1. Enter full name: "New Test User"
  2. Enter email: "newuser@test.com"
  3. Enter password: "TestPass123"
  4. Confirm password: "123abc"
  5. Click "Register" button
**Expected Result:** Error displayed: "Passwords do not match"

#### ❌ TC-R-05: Verify user registration with password too short
**Test Steps:**
  1. Enter full name: "New Test User"
  2. Enter email: "newuser@test.com"
  3. Enter password: "TestPass"
  4. Confirm password: "TestPass"
  5. Click "Register" button
     
- **Expected Result:** Error: "Password must be at least 8 characters"

#### ❌ TC-R-06: Verifying user registration with nvalid email format
- **Test Steps:**
  1. Enter full name: "New Test User"
  2. Enter email: "newuser@test"
  4. Enter password: "NewPass123"
  5. Confirm password: "NewPass123"
  6. Click "Register" button
     
- **Expected Result:** Error: "Invalid email address"

---

### 🔐 Login Test Cases

#### ✅ TC-L-01: Verifying valid user login
- **Test Steps:**
  1. Go to login page
  2. Enter: Email: "user1@cleancity.com"
  3. Enter Password: "TestPass123"
  4. Click "Login" button
- **Expected Result:** Redirect to Dashboard; user-specific links shown

#### ✅ TC-L-02: Verifying valid Admin login
- **Test Steps:**
  1. Enter: Email: "admin@cleancity.com"
  2. Password: "admin123"
  3. Click "Login" button
- **Expected Result:** Redirect to Dashboard; admin panel link is visible

#### ❌ TC-L-03: verifying user login with invalid password
- **Test Steps:**
  1. Enter valid registered user email e.g user1@test.com
  2. Enter incorrect password e.g "Test"
  3. Click "Login" button
- **Expected Result:** Error: "Invalid email or password"

#### ❌ TC-L-04: Verifying user login with non-existent email
- **Test Steps:**
  1. Enter unused email e.g "user@test"
  2. Enter any password
  3. Click "Login" button
     
- **Expected Result:** Error: "Invalid email or password"

#### ❌ TC-L-05: verifying user login with empty Email
- **Test Steps:**
  1. Leave email blank
  2. Enter valid password e.g "TestPass123"
  3. Click "Login" button
- **Expected Result:** Error: "Email is required"

#### ❌ TC-L-06: Verifying user login with empty Password
- **Test Steps:**
  1. Enter valid registered email e.g "user1@test.com"
  2. Leave password blank
  3. Click "Login" button
     
- **Expected Result:** Error: "Password is required"

#### ❌ TC-L-07: Verifying SQL Injection Attempt
- **Test Steps:**
  1. Enter `admin@cleancity.com`
  2. Password `' OR 1=1 --`
  3. Submit
- **Expected Result:** Login blocked; generic error shown

---

### 🚪 Logout Test Cases

#### ✅ TC-LO-01: Verifying user logout from logged-in state
**Precondition:** User is logged in
**Test Steps:**
  1. Click on Logout
**Expected Result:** Session ends; redirected to login page

#### ✅ TC-LO-02: Verifying that Logout is hidden for guest user
**Test Steps:**
  1. Access app without logging in
**Expected Result:** Logout button is not visible

#### ✅ TC-LO-03: Verifying logout via URL as guest
**Test Steps:**
  1. Access logout endpoint manually in browser
**Expected Result:** Redirected to login/homepage; no error

---

### 👮‍♂️ Access Control Test Cases

#### ✅ TC-A-01: Verifying Admin sees Admin panel
**Test Steps:**
  1. Login as admin
  2. Check navigation bar
**Expected Result:** "Admin" link is visible

#### ✅ TC-A-02: Verifying that regular user cannot see Admin Panel
**Test Steps:**
  1. Login as regular user
  2. Check nav links
**Expected Result:** Admin link is hidden

#### ❌ TC-A-03: Verifying direct Dashboard Access by guest
**Test Steps:**
  1. Visit `/dashboard` without logging in
**Expected Result:** Redirect to login

#### ❌ TC-A-04: Verifying regular user cannot accessing Admin panel URL
**Test Steps:**
  1. Copy admin URL and visit as regular user
**Expected Result:** Access denied or redirected

---

### 🧪 UI & Usability Test Cases

#### ✅ TC-UI-01: Verifying that placeholder texts exist
**Test Steps:**
  1. Check email and password fields
**Expected Result:** Placeholder like "Enter your email" visible

#### ✅ TC-UI-02: Verifying that required fields have indicator
**Test Steps:**
  1. Check label next to required fields
**Expected Result:** Asterisk (*) shown

#### ✅ TC-UI-03: Verifying field tab Navigation
**Test Steps:**
  1. Use Tab key to move between fields
**Expected Result:** Order flows logically

#### ✅ TC-UI-04: Verifying password masking
**Test Steps:**
  1. Type password
**Expected Result:** Dots shown instead of visible text

#### ✅ TC-UI-05: Verifying that UI is responsive
**Test Steps:**
  1. Load form on mobile browser
**Expected Result:** All inputs and buttons are usable

---

# 🧪 Test Cases for Waste Management System

## 4.1 Pickup Scheduling

### ✅ TC-001: Verifying scheduling Pickup with valid inputs
1. Navigate to scheduling page
2. Enter a registered full name  e.g "John Doe"
3. Enter valid registered email e.g "user1@test.com"
4. Select a pick up location e.g "Nairobi"
7. Select waste type (e.g., Recyclable)
8. Choose quantity (e.g medium)
9. Choose future pick date  e.g "12/07/2025"
10. Enter any additional description (max 200 characters)
11. Click "Submit request" button
      
**Expected Result:** Pickup is scheduled successfully

### ❌ TC-002: Verifying scheduling Pickup with a past date
1. Navigate to scheduling page
2. Enter a registered full name  e.g "John Doe"
3. Enter valid registered email e.g "user1@test.com"
4. Select a pick up location e.g "Nairobi"
5. Select waste type (e.g., Recyclable)
6. Choose quantity (e.g medium)
7. Enter a past date e.g "1/07/2025"
8. Enter any additional description  
9. Click "Submit request" button

**Expected Result:** Error message displayed – date must be in the future

### ❌ TC-002: Attempting to Schedule a pickup with invalid email
1. Navigate to scheduling page
2. Enter a registered full name  e.g "John Doe"
3. Enter invalid registered email e.g "user@test.com"
4. Select a pick up location e.g "Nairobi"
5. Select waste type (e.g., Recyclable)
6. Choose quantity (e.g medium)
7. Enter a past date e.g "1/07/2025"
8. Enter any additional description  
9. Click "Submit request" button

**Expected Result:** Error message displayed – invalid email


### ❌ TC-003: Scheduling a pickup without selecting waste type
1. Navigate to scheduling page
2. Enter a registered full name  e.g "John Doe"
3. Enter valid registered email e.g "user1@test.com"
4. Select a pick up location e.g "Nairobi"
5. leave the Select waste type empty
6. Enter a future date e.g "11/07/2025"
7. Enter any additional description  
8. Click "Submit request" button
**Expected Result:** Error message – waste type is required

### ❌ TC-004: Verifying scheduling pickup without quantity
1. Leave quantity empty  
2. Fill other fields  
3. Submit request  
**Expected Result:** Error message – quantity is required

### ❌ TC-005: Verifying scheduling pickup with too long special instructions
1. Enter 201+ characters in special instructions  
2. Fill other fields  
3. Submit request  
**Expected Result:** Error message – max 200 characters allowed

### ❌ TC-006: Verifying scheduling pickup with hour less than 24 
1. Select a date less than 24 hours in future  
2. Fill all required fields  
3. Submit request  
**Expected Result:** Validation error – must be at least 24 hours in advance

### ✅ TC-007: Verifying that available time slots are viewable
1. Go to scheduling page  
2. Choose valid pickup date  
**Expected Result:** Available time slots are displayed

### ❌ TC-008: Verifying scheduling multiple pickups on same date
1. Schedule a pickup for a given date  
2. Attempt to schedule another pickup for same date  
**Expected Result:** Error – only one pickup per date allowed

---

## 4.2 Request Management

### ✅ TC-009: Verifying that Pickup Request History is viewable
1. Log in  
2. Go to request history 
 
**Expected Result:** List of all past pickup requests displayed

### ✅ TC-010: Verifying that Pending Pickup Request is cancellable
1. Select a pending request  
2. Click cancel

**Expected Result:** Status changes to Cancelled

### ✅ TC-011: Verifying that requests more than 24 hours away are modifiable
1. Select request with pickup time more than 24 hours away  
2. Update details (e.g., quantity)

**Expected Result:** Details updated successfully

### ❌ TC-012: Modifying request less than 24 hours in advance
1. Select request with pickup time less than 24 hours away  
2. Attempt to modify details  
**Expected Result:** Error – modification not allowed

### ✅ TC-013: Verifying that Status is displayed for request
1. View request list 

**Expected Result:** Each request shows status (Pending, Confirmed, Completed, Cancelled)

---

## 4.3 Request Tracking

### ✅ TC-014: Verifying real-time Status Update
1. Submit pickup request  
2. Trigger status change in system (e.g., Confirmed)

**Expected Result:** Status updates reflect immediately in UI

### ✅ TC-015: Verifying Notification on Status Change
1. Submit request  
2. System updates status  
**Expected Result:** Notification received (email, push, etc.)

### ✅ TC-016: Verifying Add Feedback after completion
1. Wait for pickup completion  
2. Navigate to feedback section  
3. Submit feedback  

**Expected Result:** Feedback is recorded successfully


# 🧪 Dashboard & Analytics Test Cases 

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
   **Expected:** Personalized dashboard is shown

2. **Verifying that recent pickup requests appear correctly when present**
    **Precondition:** User has made at least one pickup request
    **Steps**
     1. Login to the system
     2. Navigate to the dashboard
     3. Locate the 'Recent pickups' section
  **Expected:** List of recent requests is visible

3. **Verifying that the system handles no recent pickup requests gracefully**
   **Precondition:** User has no history
   **Steps**
     1. Login to the system
     2. Open the dashboard
   **Expected:** Message like "No recent pickups"

4. **Verifying that upcoming scheduled pickups are showing**
   **Precondition:** Scheduled pickups exist
   **Steps**
     1. Login to the system
     2. Open the dashboard
     3. Scroll to the 'Upcoming pickups' section
   **Expected:** Upcoming pickups are listed

5. **Verifying how the system handles case with no scheduled pickups**
   **Precondition:** None scheduled
   **Steps**
     1. Login to the system
     2. Open the dashboard
   **Expected:** "No upcoming pickups" message shown

6. **Verifying that environmental statistics is displayrd properly**
   **Precondition:** User has pickup history
   **Steps**
     1. Login to the system
     2. Open the dashboard
     3. Locate the 'Environmental Impact' section
   **Expected:** Total waste, CO2 saved, and trees saved are shown

7. **Verifying that achievement badges are displayed if earned**
   **Precondition:** User has earned badges
   **Steps**
     1. Login to the system
     2. Navigate to the dashboard
     3. Locate the 'Achievement Badges' section
   **Expected:** Badges are visible with correct labels

8. **Verifying that absence of badges is handled with friendly message**
   **Precondition:** New user
   **Steps**
     1. Login to the system
     2. Open the dashboard
   **Expected:** Message encouraging action appears

9. **Verifying that Quick action buttons are visible and clickable**
   **Precondition:** User logged in
   **Steps:**
     1. Login to the system
     2. Navigate to the dashboard
     3. Locate the quick action buttons
   **Expected:** Buttons are functional

10. **Verifying that Quick action buttons redirect to correct screens**
    **Precondition:** Buttons enabled
    **Steps**
      1. Login to the system
      2. Navigate to the dashboard
      3. Click on "Request Pickup" button
    **Expected:** Redirects to pickup form

---

## ❌ Negative Test Cases 

1. **Verifying Access dashboard without login**
   **Steps**
     1. Open browser
     2. Enter dashboard URL directly
   **Expected:** Redirect to login

2. **Verifying that Network error is displayed on dashboard**
   **Steps**
     1. Disconnect internet
     2. Open dashboard
   **Expected:** Show network error

3. **Verifying Pickup data fetch failure**
   **Precondition:** API down
   **Steps**
     1. Login to the system
     2. Navigate to dashboard
   **Expected:** Error message shown

4. **Verifying corrupted pickup record**
   **Precondition:** Incomplete data exists
   **Steps**
     1. Login to the system
     2. View dashboard
   **Expected:** “Date unavailable” or similar fallback

5. **Verifying that Quick action buttons are unresponsive**
   **Steps**
     1. Login to the system
     2. Disable JavaScript
     3. Click any quick action button
   **Expected:** Error handled gracefully

6. **Verifying Session hijack**
   **Steps**
     1. Acquire another user’s session ID
     2. Try to access dashboard with it
   **Expected:** Access denied or logout

---

## ⚠️ Edge Cases 


1. **Verifying Pickup with future date**
   **Steps**
     1. Schedule pickup for a future date
     2. Open dashboard
   **Expected:** Date handled gracefully


2. **Verifying that single badge displayed**
   **Precondition:** One badge earned
   **Steps**
     1. Login to the system
     2. View dashboard
   **Expected:** Layout doesn’t break

---

## 🎨 UI/UX Test Cases 

1. **Verifying responsive layout on mobile/tablet**
   **Steps**
     1. Open dashboard on mobile emulator
     2. Resize and interact with elements
   **Expected:** UI adapts smoothly

2. **Verifying loading state during data fetch**
   **Steps**
     1. Throttle network
     2. Load dashboard
   **Expected:** Loading indicator or skeleton appears


# 🧪 Gamification Test Cases

---

## ✅ Positive Test Cases

---

#### 1. Verifying that badge for first pickup scheduled is awarded

 **Precondition:** The user has no previous pickups.

 **Steps:**
  1. Login to the application using valid credentials.
  2. Navigate to the **Pickup** section.
  3. Schedule a new pickup with valid details.
  4. Submit the pickup request.
  5. Navigate to the **Badges** section.

 **Expected Result:**  A badge labeled **"First Pickup Scheduled"** is awarded and visible.

---

#### 2. Verifying that badge is awarded after 10 pickups completed

 **Precondition:** The user has already completed 9 pickups.

 **Steps:**
  1. Login to the application.
  2. Schedule and complete one more pickup.
  3. Return to the dashboard or profile.
  4. Navigate to **Badges** section.

 **Expected Result:**  **"10 Pickups Completed"** badge appears in the user's badge list.

---

#### 3. Verifying Award badge for perfect recycling score

 **Precondition:** Recycling score logic is implemented.

 **Steps:**
  1. Login to the application.
  2. Schedule a pickup with correctly sorted recyclables.
  3. Submit the pickup.
  4. Check recycling score on the dashboard.
  5. Open **Badges** section.

 **Expected Result:**  Badge for **"Perfect Recycling Score"** is displayed.

---

#### 4. Verifying award badge for community contributor

 **Precondition:** User participates in community activities (e.g., referrals).

 **Steps:**
  1. Login to the application.
  2. Refer a new user or join a community cleanup event.
  3. Complete the qualifying community action.
  4. Visit the **Badges** section.

 **Expected Result:**  **"Community Contributor"** badge is awarded.

---

#### 5. Verifying award points for completed pickup

**Precondition:** Point awarding logic is enabled.

 **Steps:**
  1. Login to the application.
  2. Schedule and complete a pickup.
  3. Navigate to the user profile or dashboard.

 **Expected Result:** Points are added to the user's total.

---

#### 6. Verifying that level increases after reaching point threshold

 **Precondition:** User is close to leveling up (e.g., 95/100 points).

 **Steps:**
  1. Complete an activity that awards sufficient points.
  2. Refresh the dashboard or profile page.

 **Expected Result:**  User’s level increases and reflects the new level.

---

#### 7. Verifying View current level and points in profile

 **Precondition:** User has accumulated some points.

 **Steps:**
  1. Login to the application.
  2. Navigate to the user profile.
  3. Locate the points and level section.

**Expected Result:** Current point total and level are displayed.

---

## ❌ Negative Test Cases

---

#### 8. Verifying that badge is awarded multiple times for the same event

 **Precondition:** User has already earned the **"First Pickup Scheduled"** badge.

 **Steps:**
  1. Schedule another pickup.
  2. Refresh the badge section.

 **Expected Result:**  **"First Pickup Scheduled"** badge is not duplicated.

---

#### 9. Verifying that user receives points without valid activity

 **Precondition:** API or frontend vulnerability.

 **Steps:**
  1. Attempt to manipulate point API via console or external tool.

 **Expected Result:** System rejects the manipulation; points remain unchanged.

---

#### 10. Verifying that level does not update correctly after rollback

**Precondition:** Points rollback due to admin correction.

 **Steps:**
  1. Admin reduces user points below threshold.
  2. User logs in and checks level.

 **Expected Result:** Level reflects reduced points accurately.

---

#### 11. Verifying that badge is not awarded without completing valid community action

 **Steps:**
  1. Attempt to claim community badge without doing referral.
  2. Reload badge list.

 **Expected Result:** Community badge is not awarded.

---

## 🎨 UI/UX Test Cases

---

#### 12. Verifying that badge icons are unique and well labeled

 **Steps:**
  1. Navigate to **Badges** section.

 **Expected Result:** Each badge has unique icons and labels.

---

#### 13. Verifying that points and levels use consistent styles and colors

 **Steps:**
  1. View dashboard and profile.

 **Expected Result:**  Progress bar and colors match level progression.

---

#### 14. Verifying responsive badge and level display on mobile devices

 **Steps:**
  1. Open app on mobile or resize browser.
  2. View badges and level display.

**Expected Result:**  All elements adjust without overflow or distortion.

