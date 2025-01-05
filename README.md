# **Clinic Information Scraper**

This project is a Python-based tool for fetching clinic information (name, address, phone number, and rating) from the Google Places API and saving it in a CSV file. The tool allows users to input a query (e.g., "clinics in California") and fetch data dynamically.

---

## **Features**
- Fetches clinic details, including:
  - **Name**
  - **Address**
  - **Phone Number** (if available)
  - **Rating**
- Saves data in a CSV file for easy access.
- Handles pagination for large datasets.
- Implements rate limiting to avoid API quota issues.

---

## **Prerequisites**
1. **Python** 3.8 or higher
2. A valid **Google Places API key** with **Places API** enabled

---

## **Installation**

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/clinic-scraper.git
cd clinic-scraper
