Product Requirement Document (PRD)
Product Name: FlashCart
Document Version: 1.0
Author: Product Management Team
Status: Ready for Review
Target Launch: Q3 2024

1. Executive Summary
FlashCart is a hyper-local, 10-minute quick commerce (Q-commerce) platform designed to deliver groceries, fresh produce, and daily essentials to urban Indian households. Operating on a robust hub-and-spoke model powered by highly optimized, localized Dark Stores (micro-fulfillment centers), FlashCart eliminates the friction of traditional grocery shopping by promising lightning-fast delivery and absolute real-time inventory transparency.

Unlike traditional e-grocery platforms where deliveries are scheduled or take hours, FlashCart matches instant consumer demand with instant supply. Through deep integration of a consumer app, an automated Warehouse Management System (WMS), and a geo-fenced rider app, FlashCart guarantees order delivery in 10 minutes or less, while maintaining ultra-low-cost operational efficiency.

2. Problem Statement
In Tier-1 Indian cities, busy lifestyles, long commutes, and nuclear/single-member households have made traditional grocery shopping highly inconvenient.

Core Pain Points:
Inefficient Planning: Urban millennials struggle to plan meals days in advance, leading to urgent, last-minute ingredient needs.
The "Phantom Stock" Friction: Existing grocery platforms suffer from a high rate of post-order cancellations or item replacements because their inventory is synced with delay, frustrating users who expect what they paid for.
Inconvenient Offline Alternatives: Local Kirana stores lack comprehensive digital catalogs, do not guarantee instant home delivery, and rarely support real-time delivery tracking.
Operations vs. Speed: Most quick delivery models struggle to balance speed with profitability due to poor dark store picking layouts, high food waste, and inefficient dispatch routing.
Why It Matters:
Convenience is the new loyalty driver in urban Indian retail. A 10-minute delivery service with a 100% accurate live inventory system removes the cognitive load of shopping planning, creating an indispensable, habit-forming utility for the urban consumer.

3. Target Audience & User Personas
The primary target audience comprises tech-savvy, convenience-driven urban millennials and working professionals aged 22-40 in Tier-1 Indian cities (e.g., Bengaluru, Mumbai, Delhi-NCR, Pune, Hyderabad) who prioritize time over small delivery premiums.

User Personas
Persona Attribute	Persona 1: "The Busy Professional" (Riya, 28)	Persona 2: "The Young Parent" (Amit, 35)
Demographics	Single, Software Engineer, Bengaluru.	Married with a toddler, Finance Manager, Gurgaon.
Needs	Immediate ingredients for cooking after work; quick snacks for impromptu house parties; early-morning milk and coffee.	Urgent baby care products (diapers, wipes); fresh fruits for the toddler; last-minute party/guest hosting supplies.
Pain Points	Hates spending 45 minutes walking to/from a supermarket. Frustrated when items in her cart are replaced after she checks out on older delivery apps.	Cannot leave the house easily while managing work and a child. Scheduled delivery slots are often missed or too late.
Core Goal	Wants exact cooking ingredients delivered in under 10 minutes, with zero item mismatches.	Wants dependable, round-the-clock availability of domestic and baby essentials delivered instantly.
4. User Stories
ID	As a... [User Role]	I want to... [Goal]	So that... [Benefit]	Priority
US-01	Consumer	View a real-time count of available products in my nearest dark store.	I can purchase items with confidence that they won’t be cancelled after payment.	P0
US-02	Consumer	Complete checkout in under 3 taps using dynamic UPI/1-click payments.	I can place my order instantly without dealing with friction or inputting extensive details.	P0
US-03	Consumer	Track my delivery rider on a real-time map with an active countdown timer.	I know exactly when to expect them and can coordinate opening the door.	P1
US-04	Dark Store Picker	Receive an order picking list organized dynamically by the shortest physical path inside the dark store.	I can pick and pack the entire order in under 120 seconds.	P0
US-05	Delivery Partner	Receive instant, auto-assigned delivery routes on my app based on my proximity to the dark store exit.	I can pick up the bag and navigate safely to the customer using the most optimal path.	P0
US-06	Consumer	Raise an automated return/refund request within the app for damaged or incorrect items.	I can get instant wallet refunds without calling customer support.	P1
5. Functional Requirements
To enable a seamless 10-minute operation, the FlashCart ecosystem is divided into three core software modules: the Consumer Mobile App, the Dark Store/WMS Application, and the Rider Partner App.

+------------------+       Order Details       +-------------------+
|                  | ------------------------> |                   |
|   Consumer App   |                           |  WMS (Dark Store) |
|                  | <------------------------ |                   |
+------------------+       Stock Sync (2s)     +-------------------+
         ^                                               |
         |                                               | Assigns
         | Live Location                                 v
+------------------+                           +-------------------+
|    Rider App     | <------------------------ |   Rider Dispatch  |
|                  |      Rider Selection      |      Service      |
+------------------+                           +-------------------+
5.1 Consumer Application (iOS & Android)
5.1.1 Location & Geofencing
System Action: The app must auto-detect the user's precise GPS lat-long coordinates upon launch.
Dark Store Mapping: The system must map the user’s coordinate to a geo-fenced boundary of the nearest active Dark Store (within a 2.5 km operational radius).
Serviceability Check: If the user is outside any active geo-fence, display a highly clear, non-serviceable screen with a "Notify Me when we launch here" capture form.
5.1.2 Catalog Search & Real-Time Inventory Integration
Dynamic Inventory Sync: The product catalog display must sync with the mapped Dark Store's local Warehouse Management System inventory database every 2 seconds.
Stock Threshold Handling:
If Stock > 5: Show normal active state.
If Stock 
≤
≤ 5 and > 0: Show "Only [X] left in stock" badge in red.
If Stock = 0: Instantly gray out the product item, disable the "Add to Cart" button, and label it "Out of Stock".
Search Engine: Power search via Elasticsearch with typo-tolerance, auto-suggest, and local language keyword synonyms (e.g., searching "Dahi" will surface "Curd / Yogurt").
5.1.3 Checkout & Payment Gateway Integration
Quick Checkout Engine: Implement an express checkout screen containing default delivery address and last-used payment instrument.
Payment Mix: Integrate UPI Deep Links (Google Pay, PhonePe, Paytm), Net Banking, Credit/Debit cards, and Corporate Sodexo meal cards.
No COD (Cash on Delivery): Cash on Delivery is disabled by default to keep transit times fast and reduce rider cash-handling liabilities.
5.1.4 Order Tracking and Map View
Visual States: The consumer order status page must dynamically transition between the following states:
Order Confirmed (0-30s)
Packing your items (30-120s)
Rider on the way (120s onwards - initiates real-time leaflet map tracking using rider GPS telemetry)
Delivered
Countdown Clock: A prominent countdown timer showing exact minutes and seconds remaining based on the initial ETA estimate.
5.2 Warehouse Management System (WMS) & Dark Store App
5.2.1 Real-Time Stock Reconciliation
Barcode-Driven Receipt & Pick: Every item received at the dark store must be scanned into a specific physical bin location using an RF handheld scanner.
Automatic Decrement: On successful payment completion by a customer, the system immediately reserves those items in the WMS, reducing the virtual inventory count in the consumer app before physical picking even begins.
5.2.2 Algorithmic Picking Routing
Picker App Sorting: Once an order is received, the WMS sorts items on the picker's screen by aisle number and bin shelf hierarchy (e.g., Aisle A 
→
→ Shelf 2 
→
→ Bin C).
Path Optimization: Pickers must be routed through the dark store in a continuous, non-overlapping loop to keep picking times below 90 seconds.
5.3 Rider Partner Application
5.3.1 Order Auto-Assignment
Proximity-Based Dispatch: The dispatch service automatically assigns ready orders to the rider parked in the dark store's designated waiting bay who has been idle the longest (FIFO approach).
One-Tap Accept: Riders have 15 seconds to accept an order inside the app. If unaccepted, the system auto-escalates to the next nearest idle rider.
5.3.2 Navigation & Delivery Completion
In-App Navigation: Integrates Google Maps SDK for Turn-by-Turn navigation directly inside the app, showing safe lane-by-lane routes.
No Contact Delivery: Features photo-verification upload to prove package drop-off at the customer's doorstep, prompting the consumer-facing status to transition to "Delivered."
6. Non-Functional Requirements (NFRs)
6.1 Performance & Latency
System Latency: The product catalog, pricing, and stock visibility must update across all active client apps within 
≤
≤ 2 seconds of a database update in the WMS.
API Response Time: Critical paths (Search, Cart Add, and Checkout initiation APIs) must return responses within 
≤
≤ 150ms at the 95th percentile (p95).
6.2 Scalability & Availability
High Availability: Core checkout services, payment routing microservices, and live location-tracking gateways must maintain 99.99% uptime (Four Nines) year-round.
Scalability Target: The infrastructure must support up to 50,000 concurrent active checkout sessions per city during peak demand windows (e.g., Friday evenings, heavy monsoons, and Sunday mornings).
6.3 Security & Regulatory Compliance
Data Security: All user location telemetry, PII (Personally Identifiable Information), and transaction history must be encrypted in transit using TLS 1.3 and at rest via AES-256.
Regulatory Frameworks: Adhere to RBI guidelines for tokenized online transactions, mandatory 2-Factor Authentication (2FA) for non-tokenized payment flows, and India's Digital Personal Data Protection (DPDP) Act.
6.4 Usability
Accessibility (a11y): The mobile application interface must support localized languages (Hindi, Kannada, Tamil, Telugu, Marathi, etc.) alongside English. It must adhere to WCAG 2.1 AA design contrast ratios.
Device Support: Ensure backward compatibility down to Android 7.0 (Nougat) and iOS 14.0, representing the baseline mobile hardware popular across Indian Tier-1 markets.
7. Success Metrics (KPIs)
To evaluate the product's market performance and technical efficacy, product management will track the following metrics on weekly/monthly dashboards:

                          ┌──────────────────────────┐
                          │    North Star Metric     │
                          │   Perfect Order Rate     │
                          │          (POR)           │
                          └────────────┬─────────────┘
                                       │
                ┌──────────────────────┴──────────────────────┐
                ▼                                             ▼
  ┌──────────────────────────┐                  ┌──────────────────────────┐
  │   Operational Metrics    │                  │     Business Metrics     │
  ├──────────────────────────┤                  ├──────────────────────────┤
  │ • Picker Packing < 90s   │                  │ • Average Order Value    │
  │ • Average Transit < 7m   │                  │   (AOV) >= ₹400          │
  │ • Out-of-Stock (OOS) < 1%│                  │ • Customer Retention     │
  └──────────────────────────┘                  └──────────────────────────┘
Metric Category	Metric Name	Target Value / KPI	Description
North Star	Perfect Order Rate (POR)	
≥
≥ 96.5%	Percentage of orders delivered in under 10 minutes with 100% item accuracy and zero transit damage.
Operational	Average Packing Time	
≤
≤ 90 Seconds	Total time elapsed from user payment success to order handoff at the dark store gate.
Operational	Average Rider Transit Time	
≤
≤ 7 Minutes	Transit duration from the moment the rider exits the store bay to the drop-off location.
Operational	Out-of-Stock (OOS) Rate at Cart	< 0.8%	Percentage of user sessions where a user clicks "Add to Cart" but is blocked due to sudden stock depletion.
Business	Average Order Value (AOV)	
≥
≥ ₹400	Average cart transaction value to ensure sustainable unit economics against delivery costs.
Business	Cohort Retention (Month-3)	
≥
≥ 45%	The percentage of newly acquired users who complete at least 2 orders in their third month.
8. Timeline & Milestones
The product development lifecyle is planned as a high-velocity 24-week rollout sequence:

[Month 1-2: Foundation] ────> [Month 3-4: Alpha MVP] ────> [Month 5: Beta Pilot] ────> [Month 6: Scale]
Month 1 & 2: Architectural Foundation & WMS Development
Finalize database structures, cloud service frameworks (AWS/GCP), and map boundary geofencing schemas.
Build the base layer Warehouse Management System (WMS) with scanning and storage system APIs.
Secure payment gateway contracts and aggregate UPI integration endpoints.
Month 3 & 4: Core Client Applications Development (Alpha MVP)
Develop the iOS and Android Consumer Client interfaces, search engine indexing pipelines, and checkout gateways.
Build first-release UI versions of the internal Dark Store Picker and Rider applications.
Complete internal mock-order dry runs within a test warehouse sandbox.
Month 5: Live Pilot (Beta Release)
Deploy FlashCart Beta across 3 select dark store locations in South Bengaluru (Indiranagar, HSR Layout, Koramangala).
Enlist a test cohort of 5,000 consumers to validate high-load edge situations (heavy evening order volume).
Verify live telemetry accuracy of rider apps and refine routing algorithms based on real-world transit times.
Month 6: General Availability (GA) & Market Scaling
Incorporate beta-stage bug resolutions.
Begin public rollout to full Tier-1 footprints (Bengaluru, Mumbai, Delhi NCR).
Unveil brand campaign marketing pushes to drive targeted user acquisition.
9. Risks & Mitigations
Risk ID	Identified Risk	Impact Level	Mitigation Action Strategy
RSK-01	Inventory Inaccuracy (Phantom Stock): System stock counts diverge from actual physical counts inside bins, leading to post-checkout order cancellations.	Critical (P0)	Introduce mandatory dynamic weight checks on packer scales during dispatch. Conduct daily automated cycle counts via WMS algorithms on high-volume SKU lines.
RSK-02	Rider Transit Accidents & Safety Violations: The strict "10-minute" promise could pressure riders to drive unsafely.	High	Strictly decouple rider incentives from individual delivery times. Frame the 10-minute delivery as a function of fast picking (under 90s) and close geographical dark store proximity (under 2 km), never rider speed.
RSK-03	Unpredictable Weather Events (e.g., Monsoon Delays): Heavy rain blocks transit lanes, making the 10-minute delivery SLA impossible to hit.	Medium	Implement an automated weather delay switch. During rain storms, the consumer app dynamically updates its Delivery SLA badge from "10 Min" to "20-30 Min" based on active localized weather data.
10. Appendix
10.1 Order Lifecycle States
[Draft Cart] 
     │
     ▼ (User payment success)
[Order Paid & Confirmed] (WMS reserves inventory immediately)
     │
     ▼ (Picker accepts order item task)
[Picking & Packing] (WMS Picker App optimal path sorting)
     │
     ▼ (Bag sealed & barcode scanned out)
[Dispatched / Out for Delivery] (Rider begins transit; live tracking begins)
     │
     ▼ (OTP validated/doorstep image upload)
[Delivered] (Transaction complete)
10.2 Glossary of Terms
Q-Commerce (Quick Commerce): Ultra-fast e-commerce delivery models focused on completing micro-orders (primarily groceries and household staples) in under 30 minutes.
Dark Store (Micro-Fulfillment Center): A highly dense, non-customer-facing neighborhood retail hub built exclusively to pick, pack, and ship online orders within a localized radius.
WMS (Warehouse Management System): Software engineered to direct, inventory-track, and optimize daily operations within dark stores.
SKU (Stock Keeping Unit): A unique identifier assigned to individual retail items to track inventory and stock parameters.
Phantom Stock: Discrepancies between system inventory balances and physical stock on store shelves, causing orders to be accepted for items that are not actually available.
