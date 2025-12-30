import { Routes } from '@angular/router';
import { Landing } from './landing/landing';
import { Signup } from './signup/signup';
import { LoginComponent } from './login/login';
import { SignupSelectionComponent } from './signup-selection/signup-selection';
import { DoctorStatusComponent } from './doctor-status/doctor-status';

export const routes: Routes = [
  { path: '', component: Landing },
  { path: 'login', component: LoginComponent },
  { path: 'signup', component: SignupSelectionComponent },
  { path: 'signup/:type', component: Signup },
  { path: 'doctor/status', component: DoctorStatusComponent },
];
