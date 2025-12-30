import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router, RouterModule } from '@angular/router';

@Component({
  selector: 'app-signup',
  standalone: true,
  imports: [FormsModule, CommonModule, RouterModule],
  templateUrl: './signup.html',
  styleUrls: ['./signup.scss'],
})
export class Signup implements OnInit {
  userType: 'patient' | 'doctor' | null = null;

  // Basic Info
  firstName = '';
  lastName = '';
  email = '';
  password = '';
  phone = '';
  gender = '';
  dateOfBirth = '';

  // Patient Info
  bloodType = '';
  height = '';
  weight = '';
  emergencyContactName = '';
  emergencyContactPhone = '';
  allergies = '';
  medicalConditions = '';

  // Doctor Info
  specialization = '';
  licenseNumber = '';
  yearsOfExperience = '';
  consultationFee = '';
  education = '';
  bio = '';

  loading = false;
  error: string | null = null;

  constructor(private route: ActivatedRoute, private router: Router) {}

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      const type = params.get('type');
      if (type === 'patient' || type === 'doctor') {
        this.userType = type;
      } else {
        this.router.navigate(['/signup']);
      }
    });
  }

  handleSubmit(): void {
    this.loading = true;
    this.error = null;

    const userData = {
      userType: this.userType,
      firstName: this.firstName,
      lastName: this.lastName,
      email: this.email,
      phone: this.phone,
      gender: this.gender,
      dateOfBirth: this.dateOfBirth,
      ...(this.userType === 'patient' ? {
        bloodType: this.bloodType,
        height: this.height,
        weight: this.weight,
        emergencyContactName: this.emergencyContactName,
        emergencyContactPhone: this.emergencyContactPhone,
        allergies: this.allergies,
        medicalConditions: this.medicalConditions,
      } : {}),
      ...(this.userType === 'doctor' ? {
        specialization: this.specialization,
        licenseNumber: this.licenseNumber,
        yearsOfExperience: this.yearsOfExperience,
        consultationFee: this.consultationFee,
        education: this.education,
        bio: this.bio,
      } : {}),
    };

    console.log('Form Submitted:', userData);

    setTimeout(() => {
      this.loading = false;
      if (this.userType === 'doctor') {
        this.router.navigate(['/doctor/status']);
      }
    }, 2000);
  }
}
