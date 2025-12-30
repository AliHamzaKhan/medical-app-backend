import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './login.html',
  styleUrls: ['./login.scss']
})
export class LoginComponent {
  email = '';
  password = '';
  loading = false;
  error = '';

  constructor(private router: Router) {}

  handleLogin(): void {
    this.loading = true;
    this.error = '';
    console.log('Logging in with', { email: this.email, password: this.password });

    // Simulate API call
    setTimeout(() => {
      this.loading = false;
      // For now, we'll just log the data. 
      // In the future, this is where you would handle the authentication logic.
    }, 2000);
  }

  navigateToSignup(): void {
    this.router.navigate(['/signup']);
  }
}
