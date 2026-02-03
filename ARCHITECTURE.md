# Afterhours – System Architecture 🧩

The Afterhours system follows a simple client-server architecture designed to support a physical space with minimal complexity and high reliability.

## High-Level Overview

[ User Interface ]
        |
        v
[ Backend API ]
        |
        v
[ Database ]

An Admin Panel connects directly to the Backend API for management operations.

---

## Components

### 1. User Interface (Web)
- Used by visitors and members
- Accessible via browser (mobile & desktop)
- Functions:
  - User registration
  - View digital card
  - View active plan and benefits
  - View coupons and offers

### 2. Admin Panel (Web)
- Used by staff or owner
- Secure login
- Functions:
  - Create and manage membership plans
  - Assign benefits
  - Recharge digital cards
  - Create coupons
  - View user activity logs

### 3. Backend API
- Central logic layer
- Handles:
  - Authentication
  - Membership validation
  - Benefit usage tracking
  - Coupon redemption
- Exposes REST APIs for UI and Admin Panel

### 4. Database
- Stores:
  - User profiles
  - Membership plans
  - Digital card data
  - Coupons
  - Usage logs

---

## Data Flow Example

1. User enters Afterhours
2. Digital card is checked via UI
3. Backend validates active membership
4. Access is granted
5. Usage is logged in database

---

## Technology Principles
- Keep APIs simple and readable
- Prefer reliability over optimization
- Avoid unnecessary microservices
- Design for clarity and maintainability

---

## Future Extensions (Not in MVP)
- Mobile application
- Payment gateway integration
- AI-based personalization
- Analytics dashboard
- Multi-branch support
