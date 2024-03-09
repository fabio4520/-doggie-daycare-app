# Gr8 Dane Doggie Dude Ranch Booking System

Welcome to the Gr8 Dane Doggie Dude Ranch Booking System! This Django-based web application is designed to facilitate the booking of appointments for various dog services including grooming, walking, and more. Our system allows customers to easily manage their appointments and ensure their beloved pets receive the care they deserve.

## Deployment to Production

This application is currently deployed at [Doggie Daycare App](https://doggie-daycare-app.onrender.com). Follow the steps below to start app in localhost.

### Environment Variables

To run this project, you need to set up the following environment variables in your production environment. **Do not** hard-code these values in your source code or expose them in public repositories for security reasons.

- `DEBUG`: Set to `False` in production to turn off debug mode.
- `SECRET_KEY`: A secret key for a particular Django installation. Use a unique, unpredictable value.
- `DATABASE_URL`: The URL for your database connection. Use the format provided by your database service provider.

## Features

For all users:

- **Appointment Booking:** Schedule, update, and cancel appointments for dog services.
- **Email Confirmation:** Automated email confirmations sent to customers upon booking, leveraging Django signals to handle notifications (you can watch the email in django console).

Only for admin user:

- **Customer Management:** Register and manage customer information, including contact details and pet information.
- **Service Catalog:** A comprehensive list of services offered, such as grooming, walking, and training sessions.
- **Dog Management:** Register and manage dogs information.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.8 or later recommended)
- Django (version 3.2 or later)

### Installation

1.  **Clone the Repository**

    ```bash
    git clone git@github.com:fabio4520/doggie-daycare-app.git
    cd doggie-daycare-app
    ```

2.  **Set Up a Virtual Environment (Optional but recommended)**

    ```bash
      python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  Install Dependencies

    ```bash
      pip install -r requirements.txt
    ```

4.  Migrate the Database

    ```bash
      python manage.py migrate
    ```

5.  Create a Superuser (Optional). You can use de superuser already created

    username: fabio

    password: password

    ```bash
      python manage.py createsuperuser
    ```

6.  Run the Development Server

        ```bash
          python manage.py runserver
        ```

    Visit http://127.0.0.1:8000/ in your web browser to view the application.

## Running the Tests

Ensure the integrity of the application by running the included tests.

```bash
  python manage.py test
```

## Acknowledgments

- This is a challenge for a Technical interview, special thanks for Gener8tor team for inspiring this project.
- Django documentation and the Django community for their invaluable resources.

## Images

### All appointments

![all_appointments](/images/image.png)

### Detail of appointment

![detail_of_appointment](/images/image-1.png)

### Edit appointment

![edit_appointment](/images/image-2.png)

### Delete confirmation

![delete_appointment](/images/image-3.png)

### Admin view

![appointents admin](/images/image-4.png)

![customers admin](/images/image-5.png)

### Email confirmation

![email confirmation](/images/image-6.png)


### Tests
![tests image](/images/image-7.png)