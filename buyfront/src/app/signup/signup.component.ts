import { Component, OnInit } from '@angular/core';

import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
// import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { first } from 'rxjs/operators';

import { AlertService } from '../_services/alert.service';
import { AuthenticationService } from '../_services/authentication.service';
import { UserService } from '../_services/user.service';
import {User} from '../_models/user';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit 
{

  registerForm: FormGroup;
  loading = false;
  submitted = false;

  constructor
  ( 
    private formBuilder: FormBuilder,
    private router: Router,
    private authenticationService: AuthenticationService,
    private userService: UserService,
    private alertService: AlertService
  )
  {
    // if (this.authenticationService.currentUserValue)
    // {
    //   this.router.navigate(['/']);
    // }
  }


  ngOnInit(): void {
    this.registerForm = this.formBuilder.group({
      email: ['', Validators.required],
      name: ['', Validators.required],
      phone: ['', Validators.required],
      address: ['', Validators.required],
      shipaddress: ['', Validators.required],
      referralToken: ['', Validators.required],
      password: ['', Validators.required],
      cpassword: ['', Validators.required]
  });
}

  // convenience getter for easy access to form fields
  get f() { return this.registerForm.controls; }

  onSubmit() {
    this.submitted = true;

    //  this.alertService.clear();

    // stop here if form is invalid
    // if (this.registerForm.invalid) {
    //     return;
    // }

    this.loading = true;
    console.log('registerForm: ' + JSON.stringify(this.registerForm.value));
    this.userService.register(this.registerForm.value);
        // .pipe(first())
        // .subscribe(
        //     data => {
        //         this.alertService.success('Registration successful', true);
        //         // this.router.navigate(['/login']);
        //     },
        //     error => {
        //         this.alertService.error(error);
        //         this.loading = false;
        //     }
        // );
  }
}

