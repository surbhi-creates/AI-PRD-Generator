# Product Requirement Document (PRD)
## Project: PhonePe Super-App (UPI, Bill Split, Utility Recharge, Financial Services)

---

# 1. Executive Summary

PhonePe is India’s leading digital payments super-app. This product initiative aims to consolidate and optimize PhonePe’s core offerings—including Unified Payments Interface (UPI) transfers, peer-to-merchant (P2M) payments, and bill splitting—while scaling high-margin financial services such as sachet-sized insurance and micro-investments.

The primary objective is to create a frictionless transaction environment for Indian consumers and merchants across Tier 1, 2, and 3 cities. By combining utility payments with peer-group financial interactions (bill splitting) and wealth management tools, PhonePe will drive daily user engagement, increase Average Revenue Per User (ARPU), and cement its position as the default financial operating system for Indian smartphone users.

---

# 2. Problem Statement

Despite the rapid growth of digital payments in India, users still face fragmented experiences across their daily financial workflows:

1. **Fragmented Daily Utilities:** Users switch between multiple apps to pay bills, split costs with friends, recharge mobile accounts, and manage micro-investments.
2. **Social Transaction Friction:** Splitting bills (for rent, dining, or trips) remains manual and socially awkward. No seamless pipeline directly converts a calculated split into a validated UPI transfer inside a group context.
3. **Complex Financial Products:** Insurance and investment options remain inaccessible or overly complex for the average Indian smartphone user, who prefers low-ticket-size, highly intuitive financial instruments (e.g., "sachet" insurance or micro-investing in digital gold).
4. **Merchant Verification Overhead:** Small merchants (Kirana owners) lose valuable business time manually checking phone screens or SMS notifications to verify incoming customer payments.

---

# 3. Target Audience & User Personas

Our target demographic covers Indian smartphone users aged 18–55. This spans digital-native college students to traditional local merchant owners.

### User Personas

```
+---------------------------------------------------------------------------------+
| Persona 1: Aarav Mehta (21) | College Student & Flatmate | Tier 1 City (Mumbai) |
+---------------------------------------------------------------------------------+
| • Tech Literacy: High (Mobile-first, heavy social media user)                   |
| • Behavioral Traits: Tight budget, frequently dines out/splits flat expenses.    |
| • Pain Points: Awkwardness in chasing friends for money; hates carrying cash.   |
| • Goal: Seamlessly split bills with flatmates and settle them via UPI instantly.|
+---------------------------------------------------------------------------------+

+---------------------------------------------------------------------------------+
| Persona 2: Rajesh Kumar (42) | Kirana Store Owner | Tier 2 City (Kanpur)        |
+---------------------------------------------------------------------------------+
| • Tech Literacy: Moderate (Uses WhatsApp, YouTube, and digital payment apps)    |
| • Behavioral Traits: Handles high volume of low-ticket transactions daily.      |
| • Pain Points: Hard to verify payments during peak hours; fears payment frauds.  |
| • Goal: Instant, reliable payment confirmation via voice and simple UI ledger.   |
+---------------------------------------------------------------------------------+

+---------------------------------------------------------------------------------+
| Persona 3: Priya Sharma (32) | Working Professional | Tier 1 City (Bengaluru)   |
+---------------------------------------------------------------------------------+
| • Tech Literacy: Very High (Corporate employee, values time over cost)          |
| • Behavioral Traits: Manages family utilities, prefers automated payments.      |
| • Pain Points: Forgets monthly recharge/bill dates; finds traditional insurance |
|   sign-ups tedious.                                                             |
| • Goal: Set-and-forget auto-bill payments, and purchase hassle-free travel/     |
|   health micro-insurance policies.                                              |
+---------------------------------------------------------------------------------+
```

---

# 4. User Stories

| ID | As a... | I want to... | So that I can... | Priority |
| :--- | :--- | :--- | :--- | :--- |
| **US-01** | App User | Scan any merchant UPI QR code and pay via my linked bank account using a 4/6 digit PIN | Complete transactions securely in under 5 seconds without physical cash. | P0 |
| **US-02** | Group Member | Select contacts, enter a custom amount, and split a bill equally or unequally | Avoid manual calculation errors and request money without awkward follow-ups. | P0 |
| **US-03** | Debtor Friend | Receive a bill-split request notification and pay my share with a single tap | Instantly settle my dues directly via UPI without searching for the requester's ID. | P0 |
| **US-04** | Merchant | Receive a real-time, localized voice broadcast of the received amount | Verify customer payments instantly without stopping my work to check my phone. | P1 |
| **US-05** | Mobile User | Enter a phone number, auto-detect the telecom operator/circle, and browse recharge plans | Quickly top up my or my family's mobile data balance in under three taps. | P1 |
| **US-06** | Retail Investor| Purchase fractional amounts of 24K Digital Gold starting as low as ₹10 | Build my savings portfolio incrementally and securely without visiting a jeweler. | P2 |
| **US-07** | Traveler | Buy single-trip domestic flight/train insurance directly during payment checkouts | Protect my journey against cancellations and delays with zero manual paperwork. | P2 |

---

# 5. Functional Requirements

## 5.1 Onboarding & UPI Infrastructure (P0)
*   **User Registration:** Secure OTP-based registration tied to the user's SIM card (Device Binding) to prevent spoofing.
*   **Multi-Bank Account Linking:** Integration with NPCI's PSP (Payment Service Provider) framework to discover and link bank accounts via registered mobile numbers.
*   **VPA Creation:** Auto-generation of a Virtual Payment Address (e.g., `mobilenumber@ybl`).

## 5.2 Core Payments & Scanning Engine (P0)
*   **Universal QR Scanner:** Capable of reading all BharatQR and UPI QR standards with auto-focus and low-light flashlight toggle.
*   **P2P Transfer:** Instant bank-to-bank transfer using Contact Search, UPI ID, or Bank Account + IFSC.
*   **Transaction Status Screens:** Clear, color-coded status screens (Success = Green, Pending/Processing = Orange, Failed = Red) with distinct sound cues.

## 5.3 Bill Splitting System (P1)
```
[Create Split Group] ──> [Add Contacts] ──> [Enter Amount & Method] ──> [Send Automated UPI Payment Requests]
```
*   **Group Creation & Management:** Users can create persistent groups (e.g., "Flatmates", "Trip") or quick one-time splits.
*   **Splitting Options:**
    *   *Equal Split:* Total divided by $N$ users.
    *   *Unequal Split:* Custom absolute amounts or percentages allocated per user.
*   **UPI Settlement Integration:** Integrated "Pay Now" CTA next to outstanding requests. Tapping it opens the pre-filled UPI PIN entry sheet directly.

## 5.4 Utility Payments & Mobile Recharge (P1)
*   **BBPS Integration:** Direct integration with the Bharat Bill Payment System (BBPS) to pull electricity, gas, water, broadband, and DTH bills.
*   **Mobile Recharge Engine:**
    *   Automatic operator and circle detection via mobile number lookup.
    *   Clean categorization of plans (e.g., Popular, Unlimited, Data Add-on).
*   **Auto-Pay (UPI Mandates):** Enable users to set up recurring payment mandates for recurring utility bills.

```
+------------------------------------------------------------------------+
|                      MOBILE RECHARGE FLOW                              |
+------------------------------------------------------------------------+
| 1. Enter Mobile Number -> 2. Auto-Detect Operator -> 3. Browse Plans   |
|                                                                        |
|  [ +91 98765 43210 ]        [ Jio - Maharashtra ]     [ Recommended ]  |
|                                                       [ Data Booster ] |
|                                                       [ Cricket Pack ] |
+------------------------------------------------------------------------+
| 4. Select Payment Method -> 5. Enter UPI PIN -> 6. Recharge Success    |
+------------------------------------------------------------------------+
```

## 5.5 Insurance & Micro-Investments (P2)
*   **Sachet Insurance:** Single-click, zero-medical-checkup insurance policies (e.g., Hospicash, dengue cover, domestic travel insurance) with premiums starting at ₹49.
*   **Digital Gold:** Users can buy, sell, or request physical delivery of 24K gold (99.9% purity) stored in secure, insured vaults (partnered with SafeGold or MMTC-PAMP).
*   **Mutual Funds / SIP:** Curated baskets of low-risk liquid funds and high-growth equity funds with paperless e-KYC integration.

## 5.6 Merchant Console & Audio confirmation (P1)
*   **In-app Business Switch:** Single-tap toggle between personal and merchant dashboards.
*   **Digital Ledger (Khata):** Real-time list of customer payments with filter options (by date, payment method, settlement status).
*   **Voice Notifications:** Direct integration with phone speakers to broadcast: *"Received Rs. 150 on PhonePe."* with multi-lingual support (Hindi, Tamil, Telugu, Kannada, Marathi, Bengali, English).

---

# 6. Non-Functional Requirements

### 6.1 Security & Compliance
*   **NPCI Compliance:** Strict adherence to UPI procedural guidelines, including secure MPIN input using a virtual keyboard.
*   **PCI-DSS Certification:** Ensure payment card data security if credit/debit cards are saved for utility bills.
*   **Device Binding:** Single active session per mobile device, locked with hardware-backed encryption (hardware keystore).
*   **Data Residency:** All Indian financial consumer data must reside exclusively on servers physically located within India (RBI directive).

### 6.2 Performance & Scalability
*   **Transaction Latency:** Core UPI payment status resolution must occur in $\le 2.5 \text{ seconds}$ from MPIN submission on a 3G/4G network.
*   **High Availability:** App backends must achieve $99.99\%$ uptime.
*   **Peak Load Handling:** Designed to scale dynamically to process up to $25,000 \text{ Transactions Per Second (TPS)}$ during national festivals and sales events (e.g., Diwali).

### 6.3 Usability & Localization
*   **Multilingual UI:** Support for English + 11 regional Indian languages (Hindi, Kannada, Tamil, Telugu, Malayalam, Marathi, Gujarati, Bengali, Odia, Punjabi, Assamese).
*   **Low Bandwidth Optimization:** App features must gracefully downgrade to handle unstable 2G/3G connections in rural areas.
*   **Lightweight App Footprint:** Keep the initial download size on Android under 35 MB to accommodate budget smartphones with limited storage.

---

# 7. Success Metrics (KPIs)

To evaluate the features defined in this PRD, we will track the following metrics:

| Metric Category | Key Performance Indicator (KPI) | Target Metric |
| :--- | :--- | :--- |
| **Acquisition** | New Registered Users | +20% Month-over-Month (MoM) |
| **Activation** | First-time Transaction Success | 85% of registered users perform a UPI transaction in Week 1 |
| **Engagement** | Monthly Active Users (MAU) / Daily Active Users (DAU) | Ratio of DAU/MAU $\ge 0.40$ |
| **Payment Performance**| Transaction Success Rate (TSR)| $\ge 99.5\%$ on Core UPI rails (excluding bank-side downtimes) |
| **Utility Adoption** | Bill Splitting Feature Adoption | 15% of active users creating or paying via a Split Bill group |
| **Cross-Sell** | Financial Services Conversion | 5% of transactional users purchasing Insurance or Digital Gold |
| **Merchant Retention** | Daily Merchant Active Status | 90% of active merchants using sound notifications daily |

---

# 8. Timeline & Milestones

The proposed execution timeline spans 24 weeks from kickoff to public rollout.

```
       Month 1-2              Month 3               Month 4-5               Month 6
  [   Phase 1   ]   ───>   [   Phase 2   ]   ───>   [   Phase 3   ]   ───>   [   Phase 4   ]
   Core Payment &           Bill Splitting         Recharges, BBPS,         Beta Testing &
   Onboarding Engine        & Merchant Audio        & Wealth Mgmt          Public Launch
```

*   **Phase 1: Core Payments Infrastructure (Week 1 - 8)**
    *   Deliverables: Device binding, UPI onboarding, Multi-bank linking, Universal QR Scanner, Contact Transfers.
*   **Phase 2: Merchant Console & Bill Split (Week 9 - 12)**
    *   Deliverables: Merchant ledger, Real-time voice confirmations, Group Split calculation, and immediate peer-to-peer collection flow.
*   **Phase 3: Ecosystem Expansion (Week 13 - 20)**
    *   Deliverables: BBPS utility integration, Mobile Recharge flows, Digital Gold buying, and Micro-insurance checkouts.
*   **Phase 4: Optimization, Beta & Rollout (Week 21 - 24)**
    *   Deliverables: Load testing (25,000 TPS), closed internal beta, security audit, translation checks, and staged rolling release (10% -> 50% -> 100%).

---

# 9. Risks & Mitigations

| Risk | Description | Impact | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| **Bank Sponsor Downtime** | Core UPI relies on sponsor banks (e.g., YES Bank, Axis Bank). If their APIs go down, payment success rates drop. | High | **Multi-bank UPI Model:** Route transactions dynamically across multiple partner bank PSPs (e.g., Axis, ICICI, Yes Bank) to ensure high redundancy. |
| **UPI Security Scams** | Fraudsters use the "Request Money" feature to trick less tech-savvy users into entering their UPI PIN to receive funds. | High | **Contextual Safety Flags:** Introduce clear, bright warning flags on incoming request sheets. Highlight red text stating: *"Entering your UPI PIN will DEBIT money from your account, not credit it."* |
| **Device Diversity Issues** | Budget Indian Android phones run out of storage quickly and have low RAM, leading to app crashes. | Medium | **Build Size Optimization:** Implement dynamic asset delivery. Compress core UI files and run regular automated test suites on devices with 2GB RAM or less. |

---

# 10. Appendix

### 10.1 Key Acronyms & Glossary
*   **UPI (Unified Payments Interface):** An instant real-time payment system developed by the National Payments Corporation of India (NPCI) facilitating inter-bank peer-to-peer (P2P) and person-to-merchant (P2M) transactions.
*   **PSP (Payment Service Provider):** The banking partner providing the infrastructure interface between PhonePe and the NPCI network.
*   **VPA (Virtual Payment Address):** A unique identifier used to make payments through UPI (e.g., `user@ybl`).
*   **BBPS (Bharat Bill Payment System):** An integrated bill payment system in India offering interoperable bill payment services to customers.
*   **Sachet Products:** Low-cost, small-sized commercial services customized for low-income demographics.

### 10.2 Core UPI Payment Flow Reference
```
[User Initiates Scan]
         │
         ▼
[Read UPI ID from QR] ──> [Query Name & VPA Verification via NPCI]
         │
         ▼
[Enter Transaction Amount] ──> [Prompt secure MPIN Screen]
         │
         ▼
[Debit Request to Payer Bank] ──> [Credit Request to Payee Bank]
         │
         ▼
[Push Real-time Transaction Success / Voice Notification to Merchant]
```