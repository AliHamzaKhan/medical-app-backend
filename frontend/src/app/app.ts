import { Component } from '@angular/core';
import { Router, RouterOutlet, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterModule, CommonModule],
  templateUrl: './app.html',
  styleUrls: ['./app.scss'],
})
export class App {
  title = 'frontend';

  constructor(private router: Router) {}

  isLandingPage(): boolean {
    const hiddenPaths = ['/login', '/signup', '/doctor/status'];
    return hiddenPaths.every(path => !this.router.url.startsWith(path));
  }
}
