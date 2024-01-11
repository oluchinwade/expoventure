# ExpoVentures

## Overview

ExpoVentures is an e-commerce application that allows users to explore and purchase various products from different vendors.

## Table of Contents

1. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
2. [Django Project Structure](#django-project-structure)
3. [Database Models](#database-models)
4. [Django Views and Templates](#django-views-and-templates)
5. [Django URLs](#django-urls)
6. [Docker Setup](#docker-setup)
7. [AWS Integration](#aws-integration)
8. [Deployment](#deployment)
9. [Contributing](#contributing)
10. [License](#license)

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) (version 3.9)
- [Django](https://www.djangoproject.com/) (version 4.0 recommended)
- [Docker](https://www.docker.com/) (optional, for containerization)
- [AWS Account](https://aws.amazon.com/) (optional, for AWS integration)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/oluchinwade/expoventure.git
    ```

2. Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

## Django Project Structure

ExpoVentures follows the standard Django project structure. Key directories include:

- `expoventures/`: Main project directory.
- `expoventuresapp/`: Django app directory containing models, views, and templates.
- `templates/`: HTML templates for rendering views.
- `static/`: Static files such as CSS, JavaScript, and images.

## Database Models

ExpoVentures uses the following database models:

- `User`: Represents a user with a username, password, and email.
- `Vendor`: Represents a vendor with a name and email.
- `Order`: Represents an order with an amount, date, and associated user.
- `Product`: Represents a product with a name, category, description, amount, and associated vendor.
- `ProductOrder`: Represents the relationship between products and orders, including date and amount.

## Django Views and Templates

The application includes views for listing users, displaying user details, listing vendors, and more. Templates provide the HTML structure for rendering these views.

## Django URLs

URL patterns are defined in `expoventuresapp/urls.py` and include routes for user listing, user details, vendor listing, and more.

## Docker Setup

ExpoVentures can be containerized using Docker. The `Dockerfile` and `docker-compose.yml` files are provided for easy setup.

## AWS Integration

ExpoVentures can be integrated with AWS services for scalability and storage. Configure AWS RDS for the database and AWS S3 for static and media files.

## Deployment

To deploy ExpoVentures, follow these steps:

1. Build Docker image:

    ```bash
    docker-compose build
    ```

2. Run Docker container:

    ```bash
    docker-compose up
    ```

3. Access the application at `http://localhost:8000`.

## Contributing

Contributions are welcome! 

## License

This project is licensed under The Python Packaging Authority - see the [LICENSE.txt](LICENSE.txt) file for details.

