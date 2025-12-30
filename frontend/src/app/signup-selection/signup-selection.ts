import { Component } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-signup-selection',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './signup-selection.html',
  styleUrls: ['./signup-selection.scss']
})
export class SignupSelectionComponent {
  constructor(private router: Router) {}

  selectType(userType: string): void {
    this.router.navigate(['/signup', userType]);
  }
}
