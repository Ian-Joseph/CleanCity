# Linked GitHub Issues

## Access Control

- [Regular user can access Admin panel URL #1](https://github.com/Ian-Joseph/CleanCity/issues/1)
- [Scheduling Pickup of Waste with a Past Date #7](https://github.com/Ian-Joseph/CleanCity/issues/7)

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

---
