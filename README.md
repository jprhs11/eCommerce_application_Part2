🛒 Django eCommerce Ecosystem
A full-stack eCommerce application featuring a dual-user system for Vendors and Buyers. This project focuses on secure role-based access, session-based shopping experiences, automated post-purchase workflows, and third-party API integrations.

🚀 Key Features
👤 Role-Based User System
Vendors: Can create and manage unique stores. Full CRUD functionality (Create, Read, Update, Delete) for store listings and product inventories.
Buyers: Can browse products from various vendors, manage a persistent shopping cart, and complete checkouts.

🌐 RESTful Web API
Resource Representation: Fully serialised JSON resources for Stores, Products, and Reviews.
Vendor Endpoints: Vendors can manage their storefronts and inventories programmatically via a dedicated API.
Permissions & Security: Strict authentication guards ensure that only verified vendors can modify resources, while buyers retain read-only access.

🐦 X (Twitter) Integration
Automated Social Marketing: The system automatically broadcasts a tweet whenever a new store is launched or a new product is added to an inventory.
Dynamic Content: Tweets include store/product names and descriptions, keeping your social feed synchronised with your inventory in real-time.

💳 Shopping & Checkout
Session-Based Cart: Tracks user items locally without requiring a database entry for every update, ensuring a fast browsing experience.
Automated Invoicing: Upon checkout, the system clears the cart, generates a detailed invoice, and emails it directly to the buyer.

⭐ Verified Review System
Smart Logic: Reviews are automatically flagged as "Verified" if the system detects the user has previously purchased that specific product.
Transparency: Unverified users can still leave reviews, but they are clearly marked as "Unverified" to maintain community trust.

🔒 Security & Authentication
Double-Password Enforcment: Registration requires password confirmation to reduce user error and enhance account security.
Token-Based Recovery: Secure "Forgot Password" workflow using time-sensitive, expiring tokens sent via email.
Permission Guards: Custom decorators and DRF permission classes prevent role-jumping and unauthorized resource access.

🛠 Tech Stack
Backend: Django (Python)
API: Django REST Framework (DRF)
Database: MariaDB (Relational)
Third-Party APIs: X (Twitter) API v2 via Tweepy
Communication: SMTP for automated invoices and console-based email debugging.
Frontend: Django Templates with CSS and Bootstrap components.

⚙ Getting Started
Prerequisites
Python 3.x
MariaDB / MySQL
Virtual Environment (recommended)
X (Twitter) Developer Account (for social features)

Installation
Clone the repository:
bash
git clone https://github.com
cd eCommerce_application_Part2


Database Configuration:
Update your DATABASES settings in settings.py with your MariaDB credentials.

API Keys:
Add your X (Twitter) API credentials to settings.py or a .env file:
TWITTER_API_KEY
TWITTER_API_SECRET
TWITTER_ACCESS_TOKEN
TWITTER_ACCESS_SECRET

Apply Migrations:
bash
python manage.py migrate

Run the Server:
bash
python manage.py runserver
