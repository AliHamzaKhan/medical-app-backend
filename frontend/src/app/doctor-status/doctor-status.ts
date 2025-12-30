import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router, RouterModule } from '@angular/router';

@Component({
  selector: 'app-doctor-status',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './doctor-status.html',
  styleUrls: ['./doctor-status.scss']
})
export class DoctorStatusComponent implements OnInit {
  verificationStatus: 'pending' | 'rejected' | 'accepted' | null = null;
  rejectionReason = 'Invalid license number.'; // Example reason
  loading = false;
  error: string | null = null;

  selectedFiles: {
    license?: File;
    experience?: File;
    other?: FileList;
  } = {};

  constructor(private router: Router) {}

  ngOnInit(): void {
    // In a real app, you would fetch this status from the backend
    this.verificationStatus = 'rejected'; // Mock status
  }

  onFileChange(event: Event, fileType: 'license' | 'experience' | 'other'): void {
    const input = event.target as HTMLInputElement;
    if (input.files) {
      if (fileType === 'other') {
        this.selectedFiles[fileType] = input.files;
      } else {
        this.selectedFiles[fileType] = input.files[0];
      }
    }
  }

  handleSubmit(): void {
    this.loading = true;
    this.error = null;

    console.log('Submitting documents:', this.selectedFiles);

    // Simulate API call
    setTimeout(() => {
      this.loading = false;
      this.verificationStatus = 'pending';
    }, 2000);
  }
}
