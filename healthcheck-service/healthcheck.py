import requests
import schedule
import time
import logging
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/healthcheck.log'),
        logging.StreamHandler()
    ]
)

# Configuration from environment variables
BACKEND_URL = os.getenv('BACKEND_URL')
HEALTHCHECK_BASE_URL = os.getenv('HEALTHCHECK_BASE_URL', 'https://hc-ping.com')
HEALTHCHECK_UUID = os.getenv('HEALTHCHECK_UUID')

# Validate required environment variables
if not BACKEND_URL:
    raise ValueError("BACKEND_URL environment variable is required")
if not HEALTHCHECK_UUID:
    raise ValueError("HEALTHCHECK_UUID environment variable is required")

# Construct full healthcheck URL
HEALTHCHECK_URL = f"{HEALTHCHECK_BASE_URL}/{HEALTHCHECK_UUID}"

def perform_health_check():
    try:
        # Log the backend URL being checked
        logging.info(f"Checking backend health at: {BACKEND_URL}")
        
        # Check backend server
        response = requests.get(BACKEND_URL, timeout=10)
        response.raise_for_status()
        
        # Log the healthcheck ping
        logging.info(f"Sending ping to healthcheck service")
        
        # If backend check is successful, ping the health check service
        requests.get(HEALTHCHECK_URL, timeout=10)
        logging.info(f"Health check successful - Backend status: {response.status_code}")
        
    except requests.RequestException as e:
        logging.error(f"Health check failed for {BACKEND_URL}: {str(e)}")

def main():
    logging.info("Health check service started")
    logging.info(f"Monitoring backend: {BACKEND_URL}")
    logging.info(f"Reporting to healthcheck service: {HEALTHCHECK_BASE_URL}")
    
    # Schedule the health check to run every 30 minutes
    schedule.every(30).minutes.do(perform_health_check)
    
    # Run the first check immediately
    perform_health_check()
    
    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main() 