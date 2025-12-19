# Flask API Server Features

This document outlines the features of the Flask API server, separated by module.

## Core

### Authentication
- **JWT-Based Authentication:** Secure authentication using JSON Web Tokens (JWT).
- **Login Endpoints:** Endpoints for user login and token generation.

### Users
- **User Registration:** Endpoint for new user registration.
- **User Profile:** User profile management, including personal information and contact details.
- **Role-Based Access Control (RBAC):** Users are assigned roles (e.g., patient, doctor, admin) to control access to different parts of the API.

### Roles
- **Role Management:** CRUD operations for managing user roles.

## Medical Services

### Hospitals
- **Hospital Management:** CRUD operations for managing hospital information.

### Patients
- **Patient Profiles:** Management of patient-specific information, such as weight, height, and allergies.

### Doctors
- **Doctor Profiles:** Management of doctor profiles, including their specialities and associated documents.
- **Speciality Management:** CRUD operations for medical specialities.
- **Clinic Management:** Management of clinic information, including address, consultation fees, and timings.
- **Document Management:** Upload and manage doctor's documents.

### Availability & Appointments
- **Availability Management:** Doctors can set their availability for appointments.
- **Appointment Booking:** Patients can book appointments with doctors based on their availability.
- **Appointment Management:** CRUD operations for managing appointments.

## AI & Subscriptions

### AI Reports
- **AI Report Generation:** Generate AI-based medical reports.
- **Credit System:** Users have a limited number of credits for generating AI reports.

### Subscriptions & Plans
- **Subscription Plans:** Management of subscription plans for users.
- **Package & Credit Management:** Users can purchase packages to get more credits for AI reports and other features.

### Medicine Search
- **Medicine Information:** Search for medicines to get details like formula, side effects, and usage.
- **Doctor-Specific Information:** Doctors get access to additional information about medicines, such as alternatives and dose calculator information.
- **Credit System:** Medicine searches are a premium feature, and each search deducts a credit from the user's account.
- **Search History:** User's medicine search history is saved for their reference.
